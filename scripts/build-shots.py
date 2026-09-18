"""Cắt ảnh cho từng shot theo shots.tsv → shots/S01.jpg …

shots.tsv — 6 cột TAB: shot, trang, x0, y0, x1, y1.  Dùng -1 cho "hết cỡ".
Toạ độ tính trên ảnh trong pages-clean/.

Chạy:
    python3 scripts/build-shots.py series/TWB/C1/results
    python3 scripts/build-shots.py series/TWB/C1/results --sheet   # thêm contact sheet để kiểm
"""
import argparse, sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

MIN_SIDE = 80


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--pages", default="pages-clean")
    ap.add_argument("--sheet", action="store_true", help="ghi contact sheet ra /tmp để kiểm mắt")
    ap.add_argument("--sheet-cols", type=int, default=6)
    a = ap.parse_args()

    src = a.results / "shots.tsv"
    if not src.exists():
        sys.exit(f"không thấy {src}")
    chapter = a.results.parent
    bo, ch = chapter.parent.name, chapter.name.lstrip("C")
    pdir = chapter / a.pages
    out = a.results / "shots"
    out.mkdir(parents=True, exist_ok=True)

    made, bad, thumbs = [], [], []
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        c = line.split("\t")
        if len(c) < 6:
            bad.append(f"{line[:40]} — thiếu cột")
            continue
        sid, page = c[0].strip(), int(c[1].strip().lstrip("P"))
        x0, y0, x1, y1 = (int(v) for v in c[2:6])
        f = pdir / f"{bo}_C{ch}_P{page:02d}.jpg"
        if not f.exists():
            bad.append(f"{sid} — không thấy {f.name}")
            continue
        im = Image.open(f)
        W, H = im.size
        x1 = W if x1 < 0 else min(x1, W)
        y1 = H if y1 < 0 else min(y1, H)
        x0, y0 = max(0, x0), max(0, y0)
        if x1 - x0 < MIN_SIDE or y1 - y0 < MIN_SIDE:
            bad.append(f"{sid} — khung quá nhỏ {x1-x0}x{y1-y0}")
            continue
        crop = im.crop((x0, y0, x1, y1))
        crop.save(out / f"{sid}.jpg", quality=95)
        made.append(sid)
        thumbs.append((sid, crop))

    print(f"cắt {len(made)} shot → {out}")
    if bad:
        print(f"(!) {len(bad)} lỗi:")
        for b in bad[:10]:
            print("   " + b)

    if a.sheet and thumbs:
        TH = 260
        cols = a.sheet_cols
        try:
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        except Exception:
            fnt = ImageFont.load_default()
        for page_i in range(0, len(thumbs), cols * 3):
            batch = thumbs[page_i:page_i + cols * 3]
            scaled = [(s, im.resize((max(1, int(im.width * TH / im.height)), TH)))
                      for s, im in batch]
            rows = [scaled[i:i + cols] for i in range(0, len(scaled), cols)]
            wid = max(sum(im.width + 8 for _, im in r) for r in rows)
            sheet = Image.new("RGB", (wid, (TH + 30) * len(rows)), (40, 40, 46))
            d = ImageDraw.Draw(sheet)
            y = 0
            for r in rows:
                x = 0
                for s, im in r:
                    sheet.paste(im, (x, y + 26))
                    d.text((x + 4, y + 2), s, font=fnt, fill=(255, 220, 90))
                    x += im.width + 8
                y += TH + 30
            p = Path(f"/tmp/shots-sheet-{page_i // (cols * 3) + 1}.png")
            sheet.save(p)
            print("sheet:", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
