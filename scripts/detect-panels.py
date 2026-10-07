"""Tách một trang thành từng panel, đánh số theo thứ tự đọc.

Vì sao cần: kịch bản trỏ tới panel dạng P05-b, nhưng trên đĩa chỉ có ảnh cả trang.
Nhãn a/b/c trong beat sheet đặt theo THỨ TỰ ĐỌC, nên a = panel 1, b = panel 2...
Script này tìm ranh giới panel bằng máng trắng (gutter) rồi trả về hộp theo đúng thứ tự đó.

Cắt 2 tầng: trước tiên tách dải ngang, rồi trong mỗi dải tách cột. Thứ tự đọc mặc định
là trên→dưới, trong mỗi dải thì phải→trái (manga Nhật); webtoon một panel mỗi dải thì
thứ tự cột không ảnh hưởng.

Chạy:
    python3 scripts/detect-panels.py truyen/TWB/prepare/C1/pages-clean/TWB_C1_P05.jpg --preview
    python3 scripts/detect-panels.py <ảnh> --json
"""
import argparse, json, sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Hiệu chỉnh bằng cách quét tham số trên các trang đã biết số panel (2026-08-31).
# Ngưỡng std cũ 12 quá ngặt: máng của webtoon này có nhiễu nén JPEG nên std thật ~20-30.
GUTTER_STD = 35          # hàng/cột gần đơn sắc thì coi là máng
GUTTER_BRIGHT = 150      # máng của truyện này là trắng
MIN_RUN = 2              # số hàng/cột liên tiếp để tính là máng
MIN_H, MIN_W = 60, 60    # hộp nhỏ hơn thì bỏ, là nhiễu
LTR = False              # trong một dải: True = trái→phải, False = phải→trái


def _split(a: np.ndarray, axis: int) -> list[tuple[int, int]]:
    """Tách theo trục: trả về các đoạn KHÔNG phải máng."""
    other = tuple(i for i in range(a.ndim) if i != axis)
    std = a.std(axis=other)
    mean = a.mean(axis=other)
    gut = (std < GUTTER_STD) & (mean > GUTTER_BRIGHT)

    segs, start, run = [], None, 0
    for i, g in enumerate(gut):
        if g:
            run += 1
            if start is not None and run >= MIN_RUN:
                segs.append((start, i - run + 1))
                start = None
        else:
            run = 0
            if start is None:
                start = i
    if start is not None:
        segs.append((start, len(gut)))
    return segs


def panels(img: Image.Image) -> list[tuple[int, int, int, int]]:
    """Danh sách hộp (x0, y0, x1, y1) theo thứ tự đọc."""
    a = np.asarray(img.convert("L"), dtype=np.int16)
    out = []
    for y0, y1 in _split(a, axis=0):
        if y1 - y0 < MIN_H:
            continue
        band = a[y0:y1]
        cols = [c for c in _split(band, axis=1) if c[1] - c[0] >= MIN_W]
        if not cols:
            cols = [(0, a.shape[1])]
        cols.sort(key=lambda c: c[0], reverse=not LTR)
        for x0, x1 in cols:
            out.append((x0, y0, x1, y1))
    return out


def preview(img: Image.Image, boxes: list, dest: Path) -> Path:
    """Vẽ hộp + số thứ tự lên ảnh để người kiểm bằng mắt."""
    canvas = img.convert("RGB").copy()
    d = ImageDraw.Draw(canvas)
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
    except Exception:
        f = ImageFont.load_default()
    for i, (x0, y0, x1, y1) in enumerate(boxes):
        label = chr(ord("a") + i) if i < 26 else str(i + 1)
        d.rectangle([x0, y0, x1 - 1, y1 - 1], outline=(255, 0, 255), width=4)
        d.rectangle([x0, y0, x0 + 46, y0 + 46], fill=(255, 0, 255))
        d.text((x0 + 10, y0 + 2), label, font=f, fill=(255, 255, 255))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest)
    return dest


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("image", type=Path)
    ap.add_argument("--preview", action="store_true", help="ghi ảnh có đánh số ra /tmp")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    img = Image.open(a.image)
    boxes = panels(img)
    if a.json:
        print(json.dumps({"image": str(a.image), "size": img.size,
                          "panels": [{"label": chr(ord('a') + i), "box": list(b)}
                                     for i, b in enumerate(boxes)]}, indent=1))
    else:
        print(f"{a.image.name}  {img.size[0]}x{img.size[1]}  → {len(boxes)} panel")
        for i, (x0, y0, x1, y1) in enumerate(boxes):
            print(f"   {chr(ord('a') + i)}  x{x0}-{x1} y{y0}-{y1}  ({x1-x0}x{y1-y0})")
    if a.preview:
        print("preview:", preview(img, boxes, Path("/tmp/panels") / a.image.name.replace(".jpg", ".png")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
