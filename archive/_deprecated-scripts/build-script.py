"""Dựng bảng kịch bản từ file lời đọc: máy tính mốc thời gian, AI viết chữ.

Vì sao cần: sửa một chữ là số từ đổi, là mốc của mọi block phía sau đổi theo. Sửa tay
29 mốc mỗi lần đổi câu thì sai là chắc chắn. Nguồn sự thật là blocks.tsv; script.md
là kết quả sinh ra, đừng sửa trực tiếp.

blocks.tsv — 3 cột, phân tách bằng TAB, dòng bắt đầu bằng # là ghi chú:
    panel <TAB> hiệu ứng <TAB> lời đọc

Chạy:
    python3 scripts/build-script.py series/TWB/C1/results
"""
import argparse, re, sys
from pathlib import Path

WPS = 2.6
DEFAULT_TARGET = 180


def count_words(text: str) -> int:
    """Đếm giống check-script.py để hai bên không lệch nhau."""
    text = re.sub(r"\[.*?\]", " ", text)
    return len([t for t in (w.strip(".,!?;:\"'…()-–—") for w in text.split()) if t])


def mmss(sec: float) -> str:
    s = int(round(sec))
    return f"{s // 60:02d}:{s % 60:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path, help="thư mục results/ của chapter")
    ap.add_argument("--target", type=float, default=DEFAULT_TARGET)
    ap.add_argument("--title", default="")
    a = ap.parse_args()

    src = a.results / "blocks.tsv"
    if not src.exists():
        sys.exit(f"không thấy {src}")

    blocks = []
    for ln, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            sys.exit(f"{src}:{ln} cần 3 cột phân tách bằng TAB, thấy {len(parts)}")
        blocks.append([p.strip() for p in parts[:3]])
    if not blocks:
        sys.exit("blocks.tsv rỗng")

    rows, cursor, total = [], 0, 0
    for i, (panel, fx, text) in enumerate(blocks, 1):
        w = count_words(text)
        d = max(1, round(w / WPS))
        rows.append(f"| B{i:02d} | {mmss(cursor)}–{mmss(cursor + d)} | {panel} | {fx} | {text} | {w} |")
        cursor += d
        total += w

    out = [f"# KỊCH BẢN — {a.title or a.results.parent.name}", "",
           "> Sinh ra từ `blocks.tsv` bằng `scripts/build-script.py`. Sửa lời thì sửa TSV rồi",
           "> chạy lại, đừng sửa bảng này bằng tay — mốc thời gian sẽ lệch.", "",
           "## Thông số",
           f"- Thời lượng mục tiêu: {a.target:.0f}s · Ngân sách từ: {int(a.target * WPS)}",
           f"- Tổng từ đã dùng: {total} · Thời lượng thực tính: {total / WPS:.0f}s "
           f"· Lệch: {(total / WPS - a.target) / a.target * 100:+.0f}%",
           f"- Mốc cuối: {mmss(cursor)} · {len(blocks)} block", "",
           "## Kịch bản",
           "| Mã | Mốc | Panel | Hiệu ứng | Lời đọc | Số từ |",
           "|---|---|---|---|---|---|"]
    out += rows

    notes = a.results / "build-notes.md"
    if notes.exists():
        out += ["", notes.read_text(encoding="utf-8").rstrip()]

    (a.results / "script.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(blocks)} block · {total} từ · {total / WPS:.0f}s → {a.results / 'script.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
