"""Nối nhiều chapter thành MỘT video: track hình + bản đọc + bảng mốc.

Không đổi cấu trúc thư mục: mỗi chapter vẫn tự sinh video-track.mp4 và audio/ riêng.
File này chỉ nối lại, nên thêm chapter chỉ là chạy lại pipeline cho chapter đó.

Chạy:
    python3 scripts/merge-chapters.py TWB 1 2                 # C1 + C2
    python3 scripts/merge-chapters.py TWB 1 2 3 --name V01
"""
import argparse, shutil, subprocess, sys
from pathlib import Path

AUDIO_EXT = (".wav", ".mp3", ".m4a", ".flac", ".ogg")
WPS = 3.5


def probe(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def mmss(t: float) -> str:
    s = int(round(t))
    return f"{s // 60}:{s % 60:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("bo")
    ap.add_argument("chapters", nargs="+")
    ap.add_argument("--name", default="V01", help="tên video gộp")
    ap.add_argument("--wps", type=float, default=WPS)
    a = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    series = root / "truyen" / a.bo
    dest = series / "videos" / a.name
    dest.mkdir(parents=True, exist_ok=True)

    tracks, lines, rows, cursor, total_words = [], [], [], 0.0, 0
    for ch in a.chapters:
        R = series / "results" / f"C{ch}"
        tsv = R / "narration.tsv"
        if not tsv.exists():
            sys.exit(f"C{ch} chưa có narration.tsv — chạy pipeline cho chapter đó trước")
        track = R / "export" / "video-track.mp4"
        if not track.exists():
            sys.exit(f"C{ch} chưa có video-track.mp4 — chạy build-video.py cho chapter đó")
        tracks.append(track)

        adir = R / "audio"
        real = {}
        if adir.is_dir():
            real = {f.stem.upper(): probe(f) for f in sorted(adir.iterdir())
                    if f.suffix.lower() in AUDIO_EXT and f.stem.upper().startswith("S")}

        texts = []
        for line in tsv.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            c = line.split("\t")
            if len(c) >= 2:
                texts.append((c[0].strip(), c[-1].strip()))

        rows.append(f"| **C{ch}** | {mmss(cursor)} | {len(texts)} shot | |")
        for i, (pages, text) in enumerate(texts, 1):
            sid = f"S{i:02d}"
            d = real.get(sid, len(text.split()) / a.wps)
            rows.append(f"| C{ch}·{sid} | {mmss(cursor)} | {d:.1f}s "
                        f"| `C{ch}/results/shots/{sid}.jpg` |")
            lines.append(text)
            cursor += d
            total_words += len(text.split())

    if not shutil.which("ffmpeg"):
        sys.exit("thiếu ffmpeg")
    lst = dest / "_concat.txt"
    lst.write_text("".join(f"file '{t.resolve()}'\n" for t in tracks), encoding="utf-8")
    out_mp4 = dest / "video-track.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c", "copy", str(out_mp4)], capture_output=True, text=True)
    lst.unlink(missing_ok=True)
    if r.returncode != 0:
        print(r.stderr[-1200:], file=sys.stderr)
        sys.exit("ffmpeg lỗi khi nối track")

    (dest / "narration-plain.txt").write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    (dest / "timeline.md").write_text(
        "\n".join([f"# TIMELINE GỘP — {a.bo} {a.name}", "",
                   f"Chapter: {', '.join('C' + c for c in a.chapters)}",
                   f"**Tổng {mmss(cursor)}** · {len(lines)} shot · {total_words} từ", "",
                   "| Shot | Vào | Dài | Ảnh |", "|---|---|---|---|", *rows]) + "\n",
        encoding="utf-8")

    print(f"{len(a.chapters)} chapter · {len(lines)} shot · {total_words} từ · {mmss(cursor)}")
    print(f"→ {out_mp4}")
    print(f"→ {dest / 'timeline.md'}")
    print(f"→ {dest / 'narration-plain.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
