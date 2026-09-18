#!/usr/bin/env python3
"""Gọi Vbee TTS API cho MỘT đoạn text -> MỘT file mp3.

Đúng giao kèo mà tts-loop.py mong đợi:
    tts-vbee.py <file text vào> <file audio ra>
    exit 0 + file audio có thật  = thành công

Cấu trúc API lấy từ Postman collection chính thức của Vbee
(documenter.getpostman.com/view/12951168/Uz5FHbSd), không phải suy đoán:

  POST https://vbee.vn/api/v1/tts   -> trả request_id, status IN_PROGRESS
  GET  https://vbee.vn/api/v1/tts/<request_id> -> poll tới SUCCESS, lấy audio_link

Vbee KHÔNG trả audio ngay trong response. Nó nhận việc rồi trả mã request;
audio sinh xong mới có link. Tài liệu ghi callback_url là bắt buộc, nhưng máy
này không có webhook công khai nên ta đi đường poll: gửi callback_url placeholder
rồi tự hỏi lại bằng Get Request. Link audio chỉ sống 3 phút -> tải ngay.

Biến môi trường:
  VBEE_TOKEN     bắt buộc  JWT của App (Authorization: Bearer ...)
  VBEE_APP_ID    bắt buộc  ID App, sinh cùng lúc với token
  VBEE_VOICE     tuỳ       mặc định hn_female_ngochuyen_full_48k-fhg (HN - Ngọc Huyền)
  VBEE_SPEED     tuỳ       mặc định "1.0", khoảng 0.1-1.9, một chữ số thập phân
  VBEE_BITRATE   tuỳ       mặc định 128 (8|16|32|64|128)
  VBEE_CALLBACK  tuỳ       URL webhook; để mặc định nếu không có
  VBEE_TIMEOUT   tuỳ       giây chờ tối đa cho một đoạn, mặc định 180
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://vbee.vn/api/v1/tts"
DEFAULT_VOICE = "hn_female_ngochuyen_full_48k-fhg"
# Vbee bắt buộc trường callback_url. Không có webhook thì vẫn phải gửi một URL
# hợp lệ; callback fail không chặn việc tổng hợp, ta lấy kết quả bằng poll.
DEFAULT_CALLBACK = "https://example.com/vbee-callback"


def die(msg, code=1):
    print(f"[vbee] {msg}", file=sys.stderr)
    sys.exit(code)


def call(url, token, body=None):
    """Gọi API, trả (dict json, http_code). Lỗi HTTP vẫn đọc được body."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode()), r.status
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors="replace")
        try:
            return json.loads(raw), e.code
        except json.JSONDecodeError:
            return {"_raw": raw[:300]}, e.code
    except urllib.error.URLError as e:
        die(f"không nối được tới Vbee: {e.reason}")


def explain(payload):
    """Vbee báo lỗi trong thân JSON chứ không chỉ ở mã HTTP."""
    if "_raw" in payload:
        return payload["_raw"]
    parts = [str(payload.get(k)) for k in ("error_code", "error_message") if payload.get(k)]
    return " | ".join(parts) or json.dumps(payload)[:300]


def main():
    if len(sys.argv) != 3:
        die(f"dùng: {Path(sys.argv[0]).name} <file text> <file mp3 ra>", 2)
    src, dest = Path(sys.argv[1]), Path(sys.argv[2])

    token = os.environ.get("VBEE_TOKEN")
    app_id = os.environ.get("VBEE_APP_ID")
    if not token or not app_id:
        die("thiếu VBEE_TOKEN hoặc VBEE_APP_ID. Tạo App tại studio.vbee.vn -> API,\n"
            "       rồi: export VBEE_TOKEN='...'  export VBEE_APP_ID='...'")

    text = src.read_text(encoding="utf-8").strip()
    if not text:
        die(f"{src} rỗng")

    body = {
        "app_id": app_id,
        "response_type": "indirect",
        "callback_url": os.environ.get("VBEE_CALLBACK", DEFAULT_CALLBACK),
        "input_text": text,
        "voice_code": os.environ.get("VBEE_VOICE", DEFAULT_VOICE),
        "audio_type": "mp3",
        "bitrate": int(os.environ.get("VBEE_BITRATE", "128")),
        "speed_rate": os.environ.get("VBEE_SPEED", "1.0"),
    }

    res, code = call(API, token, body)
    if res.get("status") != 1:
        die(f"POST /tts thất bại (HTTP {code}): {explain(res)}")

    req_id = res.get("result", {}).get("request_id")
    chars = res.get("result", {}).get("characters", len(text))
    if not req_id:
        die(f"không có request_id trong phản hồi: {json.dumps(res)[:300]}")
    print(f"[vbee] {src.name}: {chars} ký tự -> request {req_id}")

    # Poll. Đoạn ~1000 ký tự thường xong trong vài giây; để rộng cho chắc.
    deadline = time.time() + int(os.environ.get("VBEE_TIMEOUT", "180"))
    link = None
    while time.time() < deadline:
        time.sleep(3)
        got, code = call(f"{API}/{req_id}", token)
        if got.get("status") != 1:
            die(f"GET /tts/{req_id} thất bại (HTTP {code}): {explain(got)}")
        r = got.get("result", {})
        state = r.get("status")
        if state == "SUCCESS":
            link = r.get("audio_link")
            break
        if state in ("FAILURE", "FAILED", "ERROR"):
            die(f"Vbee xử lý hỏng: {explain(got)}")
    if not link:
        die(f"quá hạn chờ request {req_id} (trạng thái cuối: {state})")

    # Link chỉ sống 3 phút -> tải ngay, không hoãn.
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(link, timeout=120) as r, open(dest, "wb") as f:
            f.write(r.read())
    except Exception as e:
        die(f"tải audio hỏng: {e}")

    size = dest.stat().st_size
    if size < 1000:
        dest.unlink(missing_ok=True)
        die(f"file tải về chỉ {size} byte, không phải audio dùng được")

    # Ghi sổ ký tự đã tiêu — quota tính theo ký tự, cần biết còn bao nhiêu.
    ledger = dest.parent.parent / "vbee-usage.tsv"
    with open(ledger, "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{src.name}\t{chars}\t{size}\n")

    print(f"[vbee] {dest.name}: {size:,} byte")


if __name__ == "__main__":
    main()
