#!/usr/bin/env bash
# Chạy các bước MÁY của một chapter theo đúng thứ tự. Các bước cần AI đọc/viết
# thì script dừng lại và in tên skill phải gọi.
#
#   ./scripts/pipeline.sh TWB 1 'https://site/truyen/chapter-1'
set -euo pipefail
cd "$(dirname "$0")/.."

BO="${1:?thiếu mã bộ}"; CH="${2:?thiếu số chapter}"; URL="${3:-}"
P="truyen/$BO/prepare/C$CH"     # nguyên liệu: ảnh + các đoạn văn nguồn
R="truyen/$BO/results/C$CH"     # thành phẩm: text chuẩn, audio, video
step(){ printf '\n\033[1m── %s\033[0m\n' "$1"; }
need_ai(){ printf '\n\033[33m⏸  CẦN AI: %s\033[0m\n   %s\n' "$1" "$2"; exit 0; }

mkdir -p "$P/pages" "$R"

step "1. Tải và làm sạch ảnh"
if [ -n "$URL" ] && [ -z "$(ls -A "$P/pages" 2>/dev/null)" ]; then
    python3 scripts/crawl-chapter.py "$URL" --bo "$BO" --chapter "$CH"
fi
[ -n "$(ls -A "$P/pages" 2>/dev/null)" ] || { echo "chưa có ảnh — đưa URL hoặc thả ảnh vào $P/pages/"; exit 1; }
python3 scripts/clean-pages.py "$P/pages"

[ -f "$P/beat-sheet.md" ] || need_ai "/manga-beat-sheet" \
  "Đọc HẾT $P/pages-clean/ → $P/beat-sheet.md, rồi chờ user duyệt."

[ -f "$P/narration.tsv" ] || need_ai "/manga-narration" \
  "Viết lời kể vào $P/narration.tsv (2 cột TAB: gợi ý trang, lời kể)."

step "2. Dựng bảng lời kể + kiểm độ mượt"
python3 scripts/build-narration.py "$R" --wps 3.5 --title "$BO chapter $CH"
python3 scripts/check-narration.py "$P/narration.tsv" || {
    echo; echo "→ sửa narration.tsv rồi chạy lại. Phải MƯỢT mới đi tiếp."; exit 1; }

[ -f "$P/shots.tsv" ] || need_ai "/manga-shots" \
  "Chọn khung cắt cho từng đoạn → $P/shots.tsv (shot, trang, x0, y0, x1, y1)."

step "3. Cắt ảnh theo shot"
python3 scripts/build-shots.py "$R" --sheet
echo "→ ĐỌC contact sheet ở /tmp/shots-sheet-*.png bằng mắt. Tỉ lệ đúng KHÔNG có nghĩa nội dung đúng."

step "4. Shot list"
python3 scripts/build-shot-list.py "$R"

if [ -n "$(ls -A "$R/audio" 2>/dev/null)" ]; then
    step "5. Re-time theo audio thật"
    python3 scripts/retime-from-audio.py "$R"
else
    printf '\n\033[33m⏸  CẦN BẠN: đọc %s ra %s/audio/S01.wav …\033[0m\n' "$R/narration-tts.txt" "$R"
    printf '   rồi chạy lại lệnh này để re-time.\n'
fi
