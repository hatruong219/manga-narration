"""Đọc toàn bộ tts-lines/Sxx.txt thành audio/Sxx.mp3 bằng edge-tts.

edge-tts KHÔNG phải model mã nguồn mở. Nó là wrapper không chính thức gọi endpoint
đọc-thành-tiếng của Microsoft Edge: miễn phí, không cần API key, giọng Việt tự nhiên,
NHƯNG là endpoint không có tài liệu công khai và KHÔNG kèm giấy phép dùng thương mại.
Kênh có doanh thu thì nên cân nhắc dịch vụ có license rõ ràng (Vbee, FPT.AI, Zalo AI,
Viettel AI) hoặc model tự host có license cho phép (Piper, F5-TTS — đọc license từng model).

Chạy:
    python3 scripts/tts-edge.py series/TWB/C1/results
    python3 scripts/tts-edge.py series/TWB/C1/results --voice vi-VN-HoaiMyNeural --rate -5%
    python3 scripts/tts-edge.py series/TWB/C1/results --only S03      # thử một đoạn
"""
import argparse, subprocess, sys, time
from pathlib import Path

VOICES = {"nam": "vi-VN-NamMinhNeural", "nu": "vi-VN-HoaiMyNeural"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--voice", default="vi-VN-NamMinhNeural",
                    help="vi-VN-NamMinhNeural (nam) hoặc vi-VN-HoaiMyNeural (nữ)")
    ap.add_argument("--rate", default="+0%", help="tốc độ, vd -10%% cho chậm lại")
    ap.add_argument("--only", help="chỉ đọc một shot, vd S03")
    ap.add_argument("--force", action="store_true", help="đọc lại cả file đã có")
    ap.add_argument("--delay", type=float, default=0.3, help="giây nghỉ giữa 2 request")
    a = ap.parse_args()

    lines = a.results / "tts-lines"
    if not lines.is_dir():
        sys.exit(f"không thấy {lines} — chạy build-narration.py trước")
    out = a.results / "audio"
    out.mkdir(parents=True, exist_ok=True)

    files = sorted(lines.glob("S*.txt"))
    if a.only:
        files = [f for f in files if f.stem.upper() == a.only.upper()]
        if not files:
            sys.exit(f"không thấy {a.only}.txt")

    done = skipped = failed = 0
    for f in files:
        dest = out / f"{f.stem}.mp3"
        if dest.exists() and not a.force:
            skipped += 1
            continue
        r = subprocess.run(["python3", "-m", "edge_tts", "--voice", a.voice,
                            "--rate", a.rate, "--file", str(f),
                            "--write-media", str(dest)],
                           capture_output=True, text=True)
        if r.returncode != 0 or not dest.exists() or dest.stat().st_size < 1000:
            print(f"  {f.stem} LỖI: {r.stderr.strip()[:90]}")
            dest.unlink(missing_ok=True)
            failed += 1
        else:
            done += 1
            if done % 10 == 0:
                print(f"  … {done} đoạn")
        time.sleep(a.delay)

    print(f"\nđọc {done} · có sẵn {skipped} · lỗi {failed} → {out}")
    if failed:
        print("(!) chạy lại để đọc tiếp các đoạn lỗi — file đã có sẽ được bỏ qua")
    if done or skipped:
        print("→ tiếp: python3 scripts/build-video.py " + str(a.results))
        print("→ và:   python3 scripts/retime-from-audio.py " + str(a.results))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
