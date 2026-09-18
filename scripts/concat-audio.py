"""Ghép audio/Sxx.* thành MỘT file để thả vào CapCut, kèm bảng mốc.

Thả 84 file rời vào CapCut rồi tự căn là việc không nên làm tay. File này nối theo đúng
thứ tự mã shot và xuất luôn mốc vào của từng đoạn.

Chạy:
    python3 scripts/concat-audio.py series/TWB/C1/results
"""
import argparse, re, shutil, subprocess, sys
from pathlib import Path

AUDIO_EXT = (".mp3", ".wav", ".m4a", ".ogg", ".flac")


def dur(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def mmss(t: float) -> str:
    s = int(round(t))
    return f"{s // 60}:{s % 60:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("-o", "--out", type=Path)
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("thiếu ffmpeg → sudo apt install -y ffmpeg")
    adir = a.results / "audio"
    if not adir.is_dir():
        sys.exit(f"không thấy {adir}")
    files = sorted((f for f in adir.iterdir() if f.suffix.lower() in AUDIO_EXT
                    and re.fullmatch(r"S\d+", f.stem.upper())),
                   key=lambda f: int(f.stem[1:]))
    if not files:
        sys.exit(f"không thấy file Sxx trong {adir}")

    # Phát hiện thiếu đoạn giữa dãy — ghép thiếu thì lời kể nhảy mà không ai biết.
    nums = [int(f.stem[1:]) for f in files]
    gaps = [n for n in range(1, max(nums) + 1) if n not in nums]
    if gaps:
        print(f"(!) THIẾU {len(gaps)} đoạn: " +
              ", ".join(f"S{n:02d}" for n in gaps[:12]) +
              (" …" if len(gaps) > 12 else ""))
        print("    Ghép thiếu thì lời kể bị nhảy. Đọc nốt rồi chạy lại.")
        return 1

    dest = a.out or (a.results / "export" / "narration.mp3")
    dest.parent.mkdir(parents=True, exist_ok=True)
    lst = a.results / "_concat_audio.txt"
    lst.write_text("".join(f"file '{f.resolve()}'\n" for f in files), encoding="utf-8")

    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", str(lst), "-c:a", "libmp3lame",
                        "-b:a", "192k", str(dest)], capture_output=True, text=True)
    lst.unlink(missing_ok=True)
    if r.returncode != 0:
        print(r.stderr[-800:], file=sys.stderr)
        sys.exit("ffmpeg lỗi khi nối audio")

    rows, cursor = [], 0.0
    for f in files:
        d = dur(f)
        rows.append(f"| {f.stem} | {mmss(cursor)} | {d:.1f}s |")
        cursor += d
    (a.results / "audio-cues.md").write_text(
        "\n".join([f"# MỐC AUDIO — {len(files)} đoạn · tổng {mmss(cursor)}", "",
                   "Dùng khi cần nhảy tới một đoạn trong file ghép.", "",
                   "| Shot | Vào | Dài |", "|---|---|---|", *rows]) + "\n",
        encoding="utf-8")

    print(f"{len(files)} đoạn · tổng {mmss(cursor)} · {dest.stat().st_size/1e6:.1f} MB")
    print(f"→ {dest}")
    print(f"→ {a.results / 'audio-cues.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
