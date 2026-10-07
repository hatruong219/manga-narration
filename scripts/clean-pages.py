"""Bỏ phần chrome của site (banner quảng cáo, dòng promo, credit nhóm dịch) khỏi trang.

Vì sao cần: crawler tải nguyên trang, trong đó có banner của site. Nếu không bỏ,
/manga-beat-sheet sẽ kể về quảng cáo và số panel lệch một nhịp.

Cách nhận — dùng LUẬT, không hardcode toạ độ, để chapter sau chạy được luôn:
  Luật A (mọi trang): bỏ dải MỎNG + SÁNG (chữ đen trên nền trắng) — đó là dòng promo
      "truy cập ngay…" và dòng credit "Dịch bởi:…". Đo trên chapter 1: đúng 3/3.
  Luật B (chỉ trang đầu): banner đồ hoạ nằm NGAY TRÊN dòng promo đầu tiên, nên bỏ luôn
      mọi thứ phía trên dải Luật A cao nhất nếu nó ở nửa trên trang.
      Không dùng độ bão hoà màu để nhận banner: đo thật cho thấy banner sat 0.483 còn
      panel lửa của truyện sat 0.449 — không tách được.

Chạy:
    python3 scripts/clean-pages.py truyen/TWB/prepare/C1/pages --dry-run
    python3 scripts/clean-pages.py truyen/TWB/prepare/C1/pages
"""
import argparse, re, sys
from pathlib import Path

import numpy as np
from PIL import Image

THIN_MAX_H = 30          # dải cao hơn mức này thì không coi là dòng text site
SAT_MIN = 0.20           # ngưỡng bão hoà coi một HÀNG là thuộc banner màu
BANNER_MIN_H = 100       # chuỗi ngắn hơn thì không phải banner
BANNER_MIN_POS = 0.60    # banner trang cuối phải bắt đầu dưới mốc này (tỉ lệ chiều cao)
BRIGHT_MIN = 200         # nền trắng của dòng text
UNI_STD = 6              # ngưỡng coi một hàng là đơn sắc (gutter)
MIN_RUN = 4              # số hàng đơn sắc liên tiếp để tính là ranh giới
MIN_BAND_H = 10


def find_bands(a: np.ndarray) -> list[tuple[int, int]]:
    """Tách trang thành dải ngang; ranh giới là chuỗi hàng gần đơn sắc."""
    uni = a.std(axis=(1, 2)) < UNI_STD
    out, start, run = [], None, 0
    for y, u in enumerate(uni):
        if u:
            run += 1
            if start is not None and run >= MIN_RUN:
                out.append((start, y - run + 1))
                start = None
        else:
            run = 0
            if start is None:
                start = y
    if start is not None:
        out.append((start, len(uni)))
    return [(s, e) for s, e in out if e - s >= MIN_BAND_H]


def row_saturation(a: np.ndarray) -> np.ndarray:
    """Bão hoà trung bình của TỪNG HÀNG.

    Phải đo theo hàng, không theo dải: banner ở trang cuối không có gutter đơn sắc tách
    khỏi tranh phía trên, nên nó bị gộp vào một dải lớn và lấy trung bình cả dải thì tín
    hiệu màu bị pha loãng (đo thật: dải gộp sat 0.205, riêng banner 0.32-0.56).
    """
    mx = a.max(axis=2)
    mn = a.min(axis=2)
    return ((mx - mn) / np.maximum(mx, 1)).mean(axis=1)


def longest_run(mask: np.ndarray) -> tuple[int, int]:
    best = (0, 0)
    start = None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        elif not v and start is not None:
            if i - start > best[1] - best[0]:
                best = (start, i)
            start = None
    if start is not None and len(mask) - start > best[1] - best[0]:
        best = (start, len(mask))
    return best


def bottom_banner(a: np.ndarray) -> tuple[int, int] | None:
    """Banner màu ở đáy trang cuối → bỏ từ đầu banner tới hết trang (kể cả lề dưới).

    BẮT BUỘC có chốt vị trí: đo thật trên chapter 1, chuỗi bão hoà dài nhất của trang
    cuối bắt đầu ở 73% chiều cao (banner), còn của trang đầu ở 35% (panel lửa CỦA TRUYỆN).
    Thiếu chốt này thì luật sẽ xoá mất cảnh truyện.
    """
    h = a.shape[0]
    s, e = longest_run(row_saturation(a) > SAT_MIN)
    if e - s >= BANNER_MIN_H and s >= h * BANNER_MIN_POS:
        return (s, h)
    return None


def chrome_ranges(a: np.ndarray, is_first: bool, is_last: bool) -> list[tuple[int, int]]:
    """Các khoảng y cần BỎ khỏi trang."""
    bands = find_bands(a)
    thin = [(s, e) for s, e in bands
            if (e - s) <= THIN_MAX_H and a[s:e].mean() >= BRIGHT_MIN]
    kill = list(thin)
    if is_first and thin:
        top = min(s for s, _ in thin)
        if top < a.shape[0] * 0.5:        # dòng promo ở nửa trên → banner nằm phía trên nó
            kill.append((0, top))
    if is_last and (b := bottom_banner(a)):
        kill.append(b)
    return sorted(kill)


def strip(a: np.ndarray, kill: list[tuple[int, int]]) -> np.ndarray:
    keep = np.ones(a.shape[0], dtype=bool)
    for s, e in kill:
        keep[s:e] = False
    return a[keep]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pages", type=Path, help="thư mục pages/ của một chapter")
    ap.add_argument("--out", type=Path, help="mặc định pages-clean/ cạnh pages/")
    ap.add_argument("--dry-run", action="store_true", help="chỉ in ra, không ghi file")
    a = ap.parse_args()

    files = sorted(a.pages.glob("*.[jp][pn]g"),
                   key=lambda p: int(m.group(1)) if (m := re.search(r"P(\d+)", p.name)) else 0)
    if not files:
        sys.exit(f"không thấy ảnh nào trong {a.pages}")

    out = a.out or a.pages.parent / "pages-clean"
    if not a.dry_run:
        out.mkdir(parents=True, exist_ok=True)

    total_removed = touched = 0
    for i, f in enumerate(files):
        arr = np.asarray(Image.open(f).convert("RGB"), dtype=np.uint8)
        kill = chrome_ranges(arr.astype(np.int16),
                             is_first=(i == 0), is_last=(i == len(files) - 1))
        removed = sum(e - s for s, e in kill)
        if removed:
            touched += 1
            total_removed += removed
            what = " ".join(f"y{s}-{e}" for s, e in kill)
            print(f"  {f.name}  bỏ {removed:>4}px / {arr.shape[0]}  [{what}]")
        if a.dry_run:
            continue
        res = strip(arr, kill) if removed else arr
        if res.shape[0] < 50:
            print(f"  (!) {f.name} còn {res.shape[0]}px sau khi bỏ — GIỮ NGUYÊN bản gốc")
            res = arr
        Image.fromarray(res).save(out / f.name, quality=95)

    print(f"\n{len(files)} trang · sửa {touched} · bỏ tổng {total_removed}px")
    if a.dry_run:
        print("(dry-run — chưa ghi file nào)")
    else:
        print(f"ảnh sạch → {out}")
        print("Dùng thư mục này cho /manga-beat-sheet, đừng dùng pages/ nữa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
