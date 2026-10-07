#!/usr/bin/env python3
"""Đọc cả chương bằng Vbee (tài khoản trả phí) — gọi thẳng, không qua tts-loop.

    .venv/bin/python scripts/vbee-tts.py truyen/FRN/results/C1            # xem kế hoạch
    .venv/bin/python scripts/vbee-tts.py truyen/FRN/results/C1 --yes      # gọi thật
    .venv/bin/python scripts/vbee-tts.py truyen/FRN/results/C1 --redo S07 S12 --yes

Đọc `tts-lines/Sxx.txt` → ghi `audio/Sxx.mp3`.

## Audio đã lấy về là thứ KHÔNG tái tạo miễn phí — script ràng bằng bốn luật

1. **Đoạn nào đã có `audio/Sxx.mp3` thì bỏ qua, không hỏi lại Vbee.** Không có cờ
   `--force` để lỡ tay gọi lại cả chương; muốn làm lại thì phải gõ đích danh
   `--redo S07 S12`, tức phải cố ý cho từng đoạn một.
2. **Mặc định chỉ in kế hoạch.** Không có `--yes` thì không một request nào được gửi.
3. **Ghi file tạm rồi mới đổi tên.** Tải về `Sxx.mp3.part`, dùng ffprobe xác nhận đúng
   là audio có độ dài > 0, xong mới `rename` sang `Sxx.mp3`. Đứt mạng giữa chừng để lại
   file cụt bị tưởng là "đã xong" thì lần sau sẽ skip nhầm và chương thiếu tiếng —
   đổi tên nguyên tử chặn đúng chỗ đó.
4. **Mọi lần gọi ghi vào `vbee-usage.tsv`** (đoạn, ký tự, request_id, độ dài, thời điểm)
   để đối chiếu với bảng cước bên Vbee.

## Hai cái bẫy của API Vbee (đã xử)

- **Lỗi trả kèm HTTP 200.** Mã lỗi nằm trong thân JSON (`error_code`, `error_message`),
  tin `http_code` là tưởng thành công trong khi hỏng.
- **POST không trả audio**, nó trả `request_id` + `IN_PROGRESS`; phải GET tới khi
  `SUCCESS` mới có `audio_link`, và **link chỉ sống 3 phút** nên tải ngay.

## Khai báo — đặt trong `.env` ở gốc repo (file này đã bị .gitignore)

    VBEE_TOKEN=...      bắt buộc   JWT của App
    VBEE_APP_ID=...     bắt buộc   ID App, sinh cùng lúc với token
    VBEE_VOICE=...      tuỳ        mặc định hn_female_ngochuyen_full_48k-fhg
    VBEE_SPEED=1.0      tuỳ        0.1–1.9, một chữ số thập phân
    VBEE_BITRATE=128    tuỳ        8|16|32|64|128
    VBEE_CALLBACK=...   tuỳ        webhook thật, nếu có
    VBEE_TIMEOUT=180    tuỳ        giây chờ tối đa cho một đoạn
"""
import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://vbee.vn/api/v1/tts"
DEFAULT_VOICE = "hn_female_ngochuyen_full_48k-fhg"
# Vbee bắt buộc trường callback_url. Không có webhook thì vẫn phải gửi một URL hợp lệ;
# callback fail không chặn việc tổng hợp, ta lấy kết quả bằng poll.
DEFAULT_CALLBACK = "https://example.com/vbee-callback"
ROOT = Path(__file__).resolve().parent.parent


def die(msg, code=1):
    print(f"[vbee] {msg}", file=sys.stderr)
    sys.exit(code)


def load_env() -> None:
    """Nạp .env ở gốc repo. Biến đã có sẵn trong môi trường thì giữ nguyên."""
    f = ROOT / ".env"
    if not f.is_file():
        return
    for line in f.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


# Lỗi cổng (nginx 502/503/504) là sự cố thoáng qua phía Vbee, không phải lỗi request.
# Chỉ thử lại đúng nhóm mã này: chúng gần như chắc chắn chưa tới được backend nên
# không sợ bị tính tiền hai lần. Lỗi nghiệp vụ (hết hạn mức, token sai) KHÔNG thử lại.
GATEWAY_ERRORS = (502, 503, 504)
RETRIES = 4


def call(url, token, body=None):
    """Gọi API, trả (dict json, http_code). Lỗi HTTP vẫn đọc được body."""
    data = json.dumps(body).encode() if body is not None else None
    for attempt in range(1, RETRIES + 1):
        req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode()), r.status
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors="replace")
            if e.code in GATEWAY_ERRORS and attempt < RETRIES:
                wait = 5 * attempt
                print(f"[vbee] HTTP {e.code} từ máy chủ — chờ {wait}s rồi thử lại "
                      f"({attempt}/{RETRIES - 1})", file=sys.stderr)
                time.sleep(wait)
                continue
            try:
                return json.loads(raw), e.code
            except json.JSONDecodeError:
                return {"_raw": raw[:300]}, e.code
        except urllib.error.URLError as e:
            if attempt < RETRIES:
                wait = 5 * attempt
                print(f"[vbee] mạng trục trặc ({e.reason}) — chờ {wait}s rồi thử lại "
                      f"({attempt}/{RETRIES - 1})", file=sys.stderr)
                time.sleep(wait)
                continue
            die(f"không nối được tới Vbee sau {RETRIES} lần: {e.reason}")


def explain(payload) -> str:
    """Vbee báo lỗi trong thân JSON chứ không chỉ ở mã HTTP."""
    if "_raw" in payload:
        return payload["_raw"]
    parts = [str(payload.get(k)) for k in ("error_code", "error_message") if payload.get(k)]
    return " | ".join(parts) or json.dumps(payload)[:300]


def duration(path: Path) -> float:
    """Độ dài audio theo ffprobe. 0.0 nghĩa là file không dùng được."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(path)],
            capture_output=True, text=True, timeout=30)
        return float(out.stdout.strip() or 0)
    except Exception:
        return 0.0


def synth(text: str, dest: Path, cfg: dict) -> tuple[str, float, int]:
    """Một đoạn → một file mp3. Trả (request_id, độ dài giây, số ký tự)."""
    body = {
        "app_id": cfg["app_id"],
        "response_type": "indirect",
        "callback_url": cfg["callback"],
        "input_text": text,
        "voice_code": cfg["voice"],
        "audio_type": "mp3",
        "bitrate": int(cfg["bitrate"]),
        "speed_rate": cfg["speed"],
    }
    res, code = call(API, cfg["token"], body)
    if res.get("status") != 1:
        die(f"POST /tts hỏng (HTTP {code}): {explain(res)}")
    result = res.get("result", {})
    req_id = result.get("request_id")
    chars = result.get("characters", len(text))
    if not req_id:
        die(f"không có request_id: {json.dumps(res)[:300]}")

    deadline = time.time() + cfg["timeout"]
    link, state = None, "?"
    while time.time() < deadline:
        time.sleep(2)
        got, code = call(f"{API}/{req_id}", cfg["token"])
        if got.get("status") != 1:
            die(f"GET /tts/{req_id} hỏng (HTTP {code}): {explain(got)}")
        r = got.get("result", {})
        state = r.get("status")
        if state == "SUCCESS":
            link = r.get("audio_link")
            break
        if state in ("FAILURE", "FAILED", "ERROR"):
            die(f"Vbee xử lý hỏng: {explain(got)}")
    if not link:
        die(f"quá hạn chờ request {req_id} (trạng thái cuối: {state})")

    # Link sống 3 phút — tải ngay. Ghi .part rồi mới đổi tên, để đứt mạng giữa chừng
    # không để lại file cụt mà lần chạy sau tưởng là đã xong rồi bỏ qua.
    part = dest.with_suffix(dest.suffix + ".part")
    try:
        with urllib.request.urlopen(link, timeout=120) as r, open(part, "wb") as f:
            f.write(r.read())
    except Exception as e:
        part.unlink(missing_ok=True)
        die(f"tải audio hỏng ({req_id}): {e}")

    secs = duration(part)
    if part.stat().st_size < 1000 or secs <= 0:
        size = part.stat().st_size
        part.unlink(missing_ok=True)
        die(f"file tải về không dùng được ({size} byte, {secs:.1f}s) — request {req_id}")
    part.rename(dest)
    return req_id, secs, chars


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path, help="vd truyen/FRN/results/C1")
    ap.add_argument("--yes", action="store_true",
                    help="thật sự gọi API (không có cờ này thì chỉ in kế hoạch)")
    ap.add_argument("--redo", nargs="*", default=[], metavar="Sxx",
                    help="đọc lại ĐÍCH DANH vài đoạn đã có audio — cố ý từng cái một")
    ap.add_argument("--limit", type=int, help="chỉ làm N đoạn đầu (để thử giọng)")
    ap.add_argument("--workers", type=int, default=1,
                    help="số đoạn đọc song song (mặc định 1). Vbee trả phí chịu được "
                         "vài luồng; gặp lỗi hạn mức thì hạ xuống 1.")
    a = ap.parse_args()

    load_env()
    cfg = {
        "token": os.environ.get("VBEE_TOKEN"),
        "app_id": os.environ.get("VBEE_APP_ID"),
        "voice": os.environ.get("VBEE_VOICE", DEFAULT_VOICE),
        "speed": os.environ.get("VBEE_SPEED", "1.0"),
        "bitrate": os.environ.get("VBEE_BITRATE", "128"),
        "callback": os.environ.get("VBEE_CALLBACK", DEFAULT_CALLBACK),
        "timeout": int(os.environ.get("VBEE_TIMEOUT", "180")),
    }

    src = a.results / "tts-lines"
    if not src.is_dir():
        die(f"không thấy {src} — chạy build-narration.py trước")
    lines = sorted(src.glob("S*.txt"))
    if not lines:
        die(f"{src} rỗng")

    adir = a.results / "audio"
    adir.mkdir(parents=True, exist_ok=True)
    redo = {s.upper() for s in a.redo}

    todo, done = [], []
    for f in lines:
        sid = f.stem
        dest = adir / f"{sid}.mp3"
        if dest.exists() and sid.upper() not in redo:
            done.append(sid)
            continue
        text = f.read_text(encoding="utf-8").strip()
        if text:
            todo.append((sid, text, dest))
    if a.limit:
        todo = todo[: a.limit]

    chars = sum(len(t) for _, t, _ in todo)
    print(f"{len(lines)} đoạn · đã có audio {len(done)} · sẽ gọi Vbee {len(todo)} "
          f"· {chars} ký tự")
    if redo:
        print(f"  đọc lại đích danh: {', '.join(sorted(redo))} — ĐÈ LÊN audio cũ")
    if not todo:
        print("không còn đoạn nào cần đọc.")
        return 0
    if not a.yes:
        print("\n→ đây mới là KẾ HOẠCH, chưa gửi request nào.")
        print(f"   gọi thật:  .venv/bin/python {sys.argv[0]} {a.results} --yes")
        return 0
    if not cfg["token"] or not cfg["app_id"]:
        die("thiếu VBEE_TOKEN hoặc VBEE_APP_ID — điền vào .env ở gốc repo")

    log = a.results / "vbee-usage.tsv"
    if not log.exists():
        log.write_text("thời điểm\tđoạn\tký tự\tgiây\trequest_id\tgiọng\n", encoding="utf-8")

    # Ghi nhật ký từ nhiều luồng → khoá lại, không để hai dòng chèn vào nhau.
    lock = threading.Lock()
    counter = {"n": 0}

    def one(job):
        sid, text, dest = job
        req_id, secs, billed = synth(text, dest, cfg)
        with lock:
            counter["n"] += 1
            i = counter["n"]
            with log.open("a", encoding="utf-8") as fh:
                fh.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}\t{sid}\t{billed}\t"
                         f"{secs:.2f}\t{req_id}\t{cfg['voice']}\n")
            print(f"[{i}/{len(todo)}] {sid} · {len(text)} ký tự · {secs:.1f}s → {dest.name}")
        return sid

    w = max(1, a.workers)
    print(f"đọc {len(todo)} đoạn bằng {w} luồng…\n")
    if w == 1:
        for job in todo:
            one(job)
    else:
        with ThreadPoolExecutor(max_workers=w) as ex:
            list(ex.map(one, todo))
    ok = counter["n"]

    total = sum(duration(adir / f"{sid}.mp3") for sid, _, _ in todo)
    print(f"\nxong {ok} đoạn · tổng {total / 60:.1f} phút audio mới")
    print(f"nhật ký cước → {log}")
    print("\nbước tiếp:")
    print(f"  .venv/bin/python scripts/concat-audio.py {a.results}")
    print(f"  .venv/bin/python scripts/retime-from-audio.py {a.results}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
