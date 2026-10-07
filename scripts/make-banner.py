#!/usr/bin/env python3
"""Dựng dải nhận diện kênh đặt cạnh ảnh truyện trong video.

    .venv/bin/python scripts/make-banner.py truyen/FRN/brand/dai-kenh.png \\
        --kenh "TỦ TRUYỆN NHỎ" --truyen "PHÁP SƯ TIỄN TÁNG" \\
        --phu "Sousou no Frieren" --the-loai "Phiêu lưu · Phép thuật · Cảm động"

Mặc định **360×1080** — hẹp có chủ ý. Khung video 1920×1080, hai dải 360 chiếm 37%
bề ngang, còn 1200px cho ảnh truyện. Dải 640px như bản vẽ tay đầu tiên thì hai bên
ăn hết 1280px, ảnh truyện còn 640 — trên điện thoại chữ trong bong bóng thoại
đọc không ra. Người xem YouTube phần lớn ở điện thoại, nên bề ngang ảnh truyện là
thứ phải giữ.

Không dùng ảnh ngoài: mọi thứ vẽ bằng hình khối, nên đổi tên bộ là chạy lại một lệnh.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# Bảng màu gáy sách — trầm, lệch tông nhau vừa đủ để thấy là nhiều cuốn.
SPINES = [(168, 76, 74), (183, 142, 56), (150, 70, 66), (62, 122, 116),
          (154, 150, 134), (70, 118, 112), (96, 122, 128), (74, 96, 140)]


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(draw, text: str, f, maxw: int) -> list[str]:
    """Ngắt dòng theo bề ngang thật của chữ, không đếm ký tự."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = f"{cur} {w}".strip()
        if draw.textlength(test, font=f) <= maxw or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y: int, text: str, f, fill, W: int, spacing: int = 0) -> int:
    """Vẽ một dòng căn giữa, trả về y của đáy dòng."""
    if spacing:
        total = sum(draw.textlength(c, font=f) for c in text) + spacing * (len(text) - 1)
        x = (W - total) / 2
        for c in text:
            draw.text((x, y), c, font=f, fill=fill)
            x += draw.textlength(c, font=f) + spacing
    else:
        draw.text(((W - draw.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)
    return y + f.size


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("out", type=Path)
    ap.add_argument("--size", default="360x1080")
    ap.add_argument("--kenh", required=True, help="tên kênh")
    ap.add_argument("--truyen", required=True, help="tên bộ đang kể")
    ap.add_argument("--phu", default="", help="tên gốc / tên phụ")
    ap.add_argument("--the-loai", default="", help="dòng thể loại, ngăn bằng ·")
    a = ap.parse_args()

    W, H = (int(x) for x in a.size.lower().split("x"))
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)

    # Nền chuyển sắc dọc: trên tím than, giữa ấm lên như ánh đèn, dưới trầm lại.
    for y in range(H):
        t = y / H
        warm = max(0.0, 1 - abs(t - 0.45) * 2.6)
        d.line([(0, y), (W, y)],
               fill=(int(32 + 26 * warm + 8 * t), int(26 + 16 * warm + 6 * t),
                     int(34 + 10 * warm + 6 * t)))

    # Vệt sáng mờ phía sau, gợi gáy sách xếp lộn xộn trong bóng tối.
    glow = Image.new("RGB", (W, H))
    gd = ImageDraw.Draw(glow)
    for i, (x, y, w, h) in enumerate([(18, 60, 70, 150), (250, 110, 64, 190),
                                      (70, 300, 92, 130), (272, 380, 58, 150),
                                      (24, 520, 76, 170), (236, 620, 84, 140),
                                      (110, 700, 64, 120), (286, 840, 52, 130)]):
        gd.rounded_rectangle([x, y, x + w, y + h], radius=10,
                             fill=(255, 236, 206) if i % 2 else (206, 216, 255))
    img = Image.blend(img, Image.blend(img, glow, 0.10), 1.0)
    d = ImageDraw.Draw(img)

    pad = 26
    inner = W - pad * 2

    # Dấu hiệu kênh: một ô sách xếp lưới, vẽ bằng hình khối nên không phụ thuộc file ngoài.
    mk = int(W * 0.30)
    mx, my = (W - mk) // 2, 62
    d.rounded_rectangle([mx, my, mx + mk, my + mk], radius=mk // 7,
                        fill=(58, 40, 34), outline=(150, 112, 74), width=3)
    cell, gap = mk // 5, mk // 22
    ox = mx + (mk - (cell * 3 + gap * 2)) // 2
    oy = my + (mk - (cell * 3 + gap * 2)) // 2
    for r in range(3):
        for c in range(3):
            d.rounded_rectangle(
                [ox + c * (cell + gap), oy + r * (cell + gap),
                 ox + c * (cell + gap) + cell, oy + r * (cell + gap) + cell],
                radius=3, fill=SPINES[(r * 3 + c) % len(SPINES)])

    y = my + mk + 36
    fk = font(FONT_B, 30)
    for ln in wrap(d, a.kenh.upper(), fk, inner):
        y = centered(d, y, ln, fk, (245, 240, 232), W) + 6

    y += 10
    d.line([(W / 2 - 42, y), (W / 2 + 42, y)], fill=(214, 158, 70), width=4)
    y += 74

    fdk = font(FONT_B, 15)
    y = centered(d, y, "ĐANG KỂ", fdk, (214, 158, 70), W, spacing=4) + 26

    ft = font(FONT_B, 34)
    for ln in wrap(d, a.truyen.upper(), ft, inner):
        y = centered(d, y, ln, ft, (250, 247, 240), W) + 8

    if a.phu:
        y += 16
        y = centered(d, y, a.phu, font(FONT_R, 20), (168, 164, 176), W)
    if a.the_loai:
        y += 20
        fg = font(FONT_R, 15)
        for ln in wrap(d, a.the_loai, fg, inner):
            y = centered(d, y, ln, fg, (150, 146, 158), W) + 4

    # Kệ sách ở chân dải: chiều cao gáy so le cho đỡ đều tăm tắp.
    shelf_y = H - 58
    heights = [128, 176, 104, 196, 146, 168, 118, 152]
    bw = (inner - 6 * (len(heights) - 1)) // len(heights)
    x = pad
    for i, hh in enumerate(heights):
        d.rounded_rectangle([x, shelf_y - hh, x + bw, shelf_y], radius=3,
                            fill=SPINES[i % len(SPINES)])
        x += bw + 6
    d.rounded_rectangle([pad - 4, shelf_y, W - pad + 4, shelf_y + 7], radius=3,
                        fill=(150, 112, 74))

    a.out.parent.mkdir(parents=True, exist_ok=True)
    img.save(a.out, quality=95)
    print(f"{W}×{H} → {a.out}")
    print(f"khung 1920×1080 · hai dải {W}px → còn {1920 - W * 2}px cho ảnh truyện")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
