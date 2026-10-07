#!/usr/bin/env python3
"""Rút tiêu đề/mô tả/tag của Phương án 1 (hoặc bản đơn) từ package.md,
in ra 3 dòng: tiêu đề | mô tả (1 dòng, đã nối) | tag. Dùng cho release.sh
để ghi vào note.md.
"""
import re
import sys


def extract(text: str):
    # Tiêu đề: dòng in đậm đầu tiên sau heading "Tiêu đề"
    m = re.search(r"#{2,3}\s*Tiêu đề.*?\n+\*\*(.+?)\*\*", text, re.S)
    title = m.group(1).strip() if m else None

    # Mô tả: đoạn văn bản sau heading "3 dòng mô tả đầu" hoặc "Mô tả", tới heading/--- kế tiếp
    m = re.search(
        r"#{2,3}\s*(?:3 dòng mô tả đầu|Mô tả)[^\n]*\n+(.+?)(?=\n#{2,3}\s|\n---|\Z)",
        text,
        re.S,
    )
    desc = m.group(1).strip() if m else None
    if desc:
        desc = " ".join(line.strip() for line in desc.splitlines() if line.strip())

    # Tag: dòng sau heading "Từ khoá" / "5 từ khoá" đầu tiên
    m = re.search(r"#{2,3}\s*(?:\d+\s*)?[Tt]ừ khoá[^\n]*\n+(.+?)(?=\n#{2,3}\s|\n---|\Z)", text, re.S)
    tags = m.group(1).strip().splitlines()[0].strip() if m else None

    return title, desc, tags


def main():
    if len(sys.argv) != 2:
        print("usage: extract-package-info.py <package.md>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()
    title, desc, tags = extract(text)
    missing = [n for n, v in (("tiêu đề", title), ("mô tả", desc), ("tag", tags)) if not v]
    if missing:
        print(f"LỖI: không trích được {', '.join(missing)} từ {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
    print(title)
    print(desc)
    print(tags)


if __name__ == "__main__":
    main()
