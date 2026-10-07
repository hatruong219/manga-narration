"""Nối từng đoạn kể với file ảnh thật → shot list cho người dựng.

Đọc narration.tsv (format kể truyện). Cột gợi ý trang có thể là một trang "P07" hoặc
một dải "P07-P08"; dải sẽ được liệt kê thành nhiều file.

Còn báo hai thứ máy thấy được mà mắt hay bỏ sót:
  - đoạn liên tiếp dùng CÙNG một trang → người dựng phải đổi khung, không thả trùng ảnh
  - trang đã tải về nhưng không đoạn nào dùng → hoặc bỏ sót nội dung, hoặc trang thừa

Chạy:
    python3 scripts/build-shot-list.py truyen/TWB/results/C1
"""
import argparse, re, sys
from pathlib import Path

from paths import bo_ch, sources

WPS = 3.5


def mmss(sec: float) -> str:
    s = int(sec)
    return f"{s // 60}:{s % 60:02d}"


def pages_of(hint: str) -> list[str]:
    """'P07-P08' → ['P07','P08'] · 'P07' → ['P07']"""
    return [p for p in re.findall(r"P\d+", hint)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--pages", default="pages-clean")
    ap.add_argument("--wps", type=float, default=WPS)
    a = ap.parse_args()

    prep = sources(a.results)
    src = prep / "narration.tsv"
    if not src.exists():
        sys.exit(f"không thấy {src}")

    bo, ch = bo_ch(a.results)
    pdir = prep / a.pages

    chunks = []
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            chunks.append((parts[0].strip(), parts[-1].strip()))

    rows, cursor, used, missing, repeats = [], 0.0, [], set(), []
    prev_pages = None
    for i, (hint, text) in enumerate(chunks, 1):
        ps = pages_of(hint)
        files = []
        for p in ps:
            n = int(p[1:])
            f = f"{bo}_C{ch}_P{n:02d}.jpg"
            files.append(f)
            used.append(p)
            if not (pdir / f).exists():
                missing.add(f)
        if ps and ps == prev_pages:
            repeats.append(i)
        prev_pages = ps

        w = len(text.split())
        d = w / a.wps
        rows.append(f"| S{i:02d} | {mmss(cursor)} | {int(round(d))}s "
                    f"| {' + '.join(f'`{f}`' for f in files) or '—'} | {text} |")
        cursor += d

    all_pages = sorted(p.name for p in pdir.glob("*.jpg"))
    used_files = {f"{bo}_C{ch}_P{int(p[1:]):02d}.jpg" for p in used}
    unused = [f for f in all_pages if f not in used_files]

    out = [f"# SHOT LIST — {bo} chapter {ch}", "",
           "> Sinh từ `narration.tsv` bằng `scripts/build-shot-list.py`.",
           f"> Ảnh dựng ở `{pdir}`", "",
           "**Mốc là DỰ TOÁN** ở {:.1f} từ/giây. Có giọng đọc thật rồi thì dựng theo".format(a.wps),
           "`timeline.md` do `retime-from-audio.py` sinh ra.", "",
           f"- {len(rows)} shot · {len(used_files)}/{len(all_pages)} trang được dùng "
           f"· tổng {mmss(cursor)}", "",
           "| Shot | Vào | Dài | File ảnh | Lời kể |",
           "|---|---|---|---|---|"]
    out += rows

    if repeats:
        out += ["", "### Shot liên tiếp dùng cùng một trang",
                "Đổi khung hình (zoom vào chi tiết khác), đừng thả trùng ảnh:",
                "- " + ", ".join(f"S{i:02d}" for i in repeats)]
    if unused:
        out += ["", f"### {len(unused)} trang đã tải nhưng không đoạn nào dùng",
                "Kiểm xem có bỏ sót nội dung không:",
                "- " + ", ".join(f"`{f}`" for f in unused)]
    if missing:
        out += ["", "### (!) Thiếu file ảnh", *(f"- `{m}`" for m in sorted(missing))]

    (a.results / "shot-list.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} shot · {len(used_files)}/{len(all_pages)} trang dùng → {a.results / 'shot-list.md'}")
    if repeats:
        print(f"(!) {len(repeats)} shot liên tiếp trùng trang: " +
              ", ".join(f"S{i:02d}" for i in repeats[:10]))
    if unused:
        print(f"(!) {len(unused)} trang không dùng: " + ", ".join(unused[:6]))
    if missing:
        print(f"(!) thiếu {len(missing)} file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
