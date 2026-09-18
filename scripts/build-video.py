"""Dựng sẵn TRACK HÌNH 1080x1920 từ shots/ + độ dài từng shot.

Vì sao cần: thả 84 ảnh vào CapCut rồi sửa tay 84 độ dài là việc không ai muốn làm.
File này ghép sẵn thành một video câm đúng mốc; CapCut chỉ còn việc thả video + audio
+ nhạc + phụ đề.

Độ dài lấy từ audio/Sxx.wav nếu có (chính xác), không có thì dự toán từ số từ.

Chạy:
    python3 scripts/build-video.py series/TWB/C1/results
    python3 scripts/build-video.py series/TWB/C1/results --fps 30 --wps 3.5
"""
import argparse, shutil, subprocess, sys
from pathlib import Path

W, H = 1080, 1920
AUDIO_EXT = (".wav", ".mp3", ".m4a", ".flac", ".ogg")


def probe(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--wps", type=float, default=3.5)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("thiếu ffmpeg → sudo apt install -y ffmpeg")

    src = a.results / "narration.tsv"
    shots = a.results / "shots"
    if not src.exists():
        sys.exit(f"không thấy {src}")
    if not shots.is_dir():
        sys.exit(f"không thấy {shots} — chạy build-shots.py trước")

    texts = []
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        c = line.split("\t")
        if len(c) >= 2:
            texts.append(c[-1].strip())

    adir = a.results / "audio"
    real = {}
    if adir.is_dir():
        real = {f.stem.upper(): probe(f) for f in sorted(adir.iterdir())
                if f.suffix.lower() in AUDIO_EXT and f.stem.upper().startswith("S")}
    src_label = "audio thật" if real else "dự toán từ số từ"

    items, missing_img, total = [], [], 0.0
    for i, t in enumerate(texts, 1):
        sid = f"S{i:02d}"
        img = shots / f"{sid}.jpg"
        if not img.exists():
            missing_img.append(sid)
            continue
        d = real.get(sid, len(t.split()) / a.wps)
        items.append((img, d))
        total += d

    if not items:
        sys.exit("không có shot nào để ghép")

    # Concat demuxer: file cuối phải lặp lại một lần nữa, nếu không nó bị cắt mất.
    lst = a.results / "_concat.txt"
    with lst.open("w", encoding="utf-8") as f:
        for img, d in items:
            f.write(f"file '{img.resolve()}'\nduration {d:.3f}\n")
        f.write(f"file '{items[-1][0].resolve()}'\n")

    dest = a.out or (a.results / "export" / "video-track.mp4")
    dest.parent.mkdir(parents=True, exist_ok=True)
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
          f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
           "-vf", vf, "-r", str(a.fps), "-c:v", "libx264", "-preset", "veryfast",
           "-crf", "20", str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    lst.unlink(missing_ok=True)
    if r.returncode != 0:
        print(r.stderr[-1500:], file=sys.stderr)
        sys.exit("ffmpeg lỗi")

    mm = f"{int(total)//60}:{int(total)%60:02d}"
    size = dest.stat().st_size / 1e6
    print(f"{len(items)} shot · {mm} · {size:.1f} MB · độ dài lấy từ {src_label}")
    print(f"→ {dest}")
    if missing_img:
        print(f"(!) thiếu ảnh cho {len(missing_img)} shot: {', '.join(missing_img[:8])}")
    if not real:
        print("(!) chưa có audio — mốc là DỰ TOÁN. Đọc giọng rồi chạy lại để khớp thật.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
