#!/usr/bin/env bash
# Gom video cuối của một chương vào release/<BỘ>/ (thư mục PHẲNG, dùng chung
# cho cả bộ) dưới tên C<n>-video-final.mp4, đồng thời ghi/cập nhật đúng 1 mục
# cho chương đó trong release/<BỘ>/note.md (tiêu đề + mô tả + tag lấy từ
# Phương án 1 của package.md) — note.md là nơi DUY NHẤT cần mở khi lên YouTube.
#
#   ./scripts/release.sh FRN 1
#   ./scripts/release.sh FRN 1 2 3 4 5      # nhiều chương một lượt
set -euo pipefail
cd "$(dirname "$0")/.."

BO="${1:?thiếu mã bộ, vd FRN}"; shift
[ $# -ge 1 ] || { echo "thiếu số chapter, vd: $0 $BO 1 2 3"; exit 1; }

DEST="release/$BO"
NOTE="$DEST/note.md"
mkdir -p "$DEST"
touch "$NOTE"

for CH in "$@"; do
    SRC="truyen/$BO/results/C$CH"

    [ -f "$SRC/export/video-final.mp4" ] || { echo "C$CH: chưa có $SRC/export/video-final.mp4 — dựng video trước"; continue; }
    [ -f "$SRC/package.md" ] || { echo "C$CH: chưa có $SRC/package.md — chạy /manga-package trước"; continue; }

    INFO="$(python3 scripts/extract-package-info.py "$SRC/package.md")" || { echo "C$CH: lỗi trích tiêu đề/mô tả/tag từ package.md, kiểm tra thủ công"; continue; }
    TITLE="$(sed -n '1p' <<<"$INFO")"
    DESC="$(sed -n '2p' <<<"$INFO")"
    TAGS="$(sed -n '3p' <<<"$INFO")"

    cp "$SRC/export/video-final.mp4" "$DEST/C$CH-video-final.mp4"

    # xoá mục cũ của chương này trong note.md (nếu release lại) rồi thêm mục mới cuối file
    python3 - "$NOTE" "$CH" <<'PYEOF'
import re, sys
path, ch = sys.argv[1], sys.argv[2]
with open(path, encoding="utf-8") as f:
    content = f.read()
content = re.sub(rf"(?m)^{re.escape(ch)},.*?(?=\n\d+,|\Z)", "", content, flags=re.S).strip()
with open(path, "w", encoding="utf-8") as f:
    f.write(content + ("\n\n" if content else ""))
PYEOF
    printf '%s, %s\n%s\n%s\n\n' "$CH" "$TITLE" "$DESC" "$TAGS" >> "$NOTE"

    echo "C$CH → $DEST/C$CH-video-final.mp4  ($(du -h "$DEST/C$CH-video-final.mp4" | cut -f1))  + note.md"
done
