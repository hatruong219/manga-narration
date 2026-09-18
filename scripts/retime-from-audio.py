"""Chỉnh mốc hình theo thời lượng audio THẬT (nguyên tắc: audio là nguồn chân lý).

Mốc trong narration.md chỉ là dự toán từ số từ. Sau khi đọc ra giọng, file này đo từng
audio/Sxx.wav bằng ffprobe, cộng dồn từ 00:00, và xuất timeline.md để dựng.
LỜI KỂ giữ nguyên tuyệt đối — chỉ mốc đổi.

Chạy:
    python3 scripts/retime-from-audio.py series/TWB/C1/results
    python3 scripts/retime-from-audio.py series/TWB/C1/results --durations S01=4.2 S02=9.8
"""
import argparse, shutil, subprocess, sys
from pathlib import Path

AUDIO_EXT = (".wav", ".mp3", ".m4a", ".flac", ".ogg")


def probe(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def mmss(t: float) -> str:
    s = int(round(t))
    return f"{s // 60}:{s % 60:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--durations", nargs="*", help="đo tay: S01=4.2 S02=9.8")
    ap.add_argument("-o", "--out", type=Path)
    a = ap.parse_args()

    src = a.results / "narration.tsv"
    if not src.exists():
        sys.exit(f"không thấy {src}")

    chunks = []
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        c = line.split("\t")
        if len(c) >= 2:
            chunks.append((c[0].strip(), c[-1].strip()))

    if a.durations:
        real = {}
        for kv in a.durations:
            k, _, v = kv.partition("=")
            real[k.strip().upper()] = float(v)
    else:
        adir = a.results / "audio"
        if not shutil.which("ffprobe"):
            sys.exit("thiếu ffprobe → sudo apt install -y ffmpeg")
        if not adir.is_dir():
            sys.exit(f"không thấy {adir}")
        real = {f.stem.upper(): probe(f) for f in sorted(adir.iterdir())
                if f.suffix.lower() in AUDIO_EXT and f.stem.upper().startswith("S")}
        if not real:
            sys.exit(f"không thấy file audio Sxx.* nào trong {adir}")

    missing = [f"S{i:02d}" for i in range(1, len(chunks) + 1)
               if f"S{i:02d}" not in real]
    if missing:
        print(f"(!) chưa có audio cho {len(missing)} shot: {', '.join(missing[:8])}"
              " — giữ mốc dự toán cho các shot đó\n", file=sys.stderr)

    rows, cursor, long = [], 0.0, []
    for i, (pages, text) in enumerate(chunks, 1):
        sid = f"S{i:02d}"
        d = real.get(sid, len(text.split()) / 3.5)
        rows.append(f"| {sid} | {mmss(cursor)}–{mmss(cursor + d)} | {d:.1f}s "
                    f"| `shots/{sid}.jpg` | `{pages}` | {text} |")
        if d > 14:
            long.append((sid, round(d)))
        cursor += d

    out = ["# TIMELINE — theo audio thật", "",
           f"**Tổng {mmss(cursor)}** · {len(rows)} shot", "",
           "| Shot | Mốc | Dài | Ảnh | Trang gốc | Lời kể |",
           "|---|---|---|---|---|---|", *rows]
    if long:
        out += ["", "### Shot dài hơn 14 giây",
                "Một hình đứng yên quá lâu sẽ chán — thêm zoom chậm hoặc tách khung:",
                *(f"- {s} ({d}s)" for s, d in long)]
    out += ["", "> Lời kể giữ nguyên từ narration.tsv. Bảng này chỉ đổi mốc hình."]

    dest = a.out or (a.results / "timeline.md")
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} shot · tổng {mmss(cursor)} → {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
