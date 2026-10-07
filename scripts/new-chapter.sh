#!/usr/bin/env bash
# Dựng thư mục cho một chapter. Bộ mới thì dựng luôn file cấp bộ từ templates/.
#   ./scripts/new-chapter.sh TWB 1
set -euo pipefail
cd "$(dirname "$0")/.."

BO="${1:?thiếu mã bộ, vd TWB}"
CH="${2:?thiếu số chapter, vd 1}"
SER="truyen/$BO"
PREP="$SER/prepare/C$CH"      # nguyên liệu: sửa tay
RES="$SER/results/C$CH"       # thành phẩm: sinh lại được hết
TPL="templates"

mkdir -p "$PREP/pages" "$RES/audio" "$RES/export"

# Nội dung template nằm ở templates/, không nhúng vào script — sửa một chỗ, mọi bộ mới đổi theo.
[ -f "$SER/series-bible.md" ]  || sed "s/{TÊN BỘ}/$BO/g" "$TPL/series-bible.md"  > "$SER/series-bible.md"
[ -f "$SER/voice-profile.md" ] || sed "s/{MÃ BỘ}/$BO/g"  "$TPL/voice-profile.md" > "$SER/voice-profile.md"
[ -f "$SER/tts-pronounce.tsv" ] || printf '# từ gốc\tcách viết cho TTS  — thử 1 đoạn rồi chỉnh\n' > "$SER/tts-pronounce.tsv"
[ -f "$SER/tracker.csv" ] || echo "chapter,crawl,beat_sheet,narration,qc,shots,audio,dung,ngay_dang" > "$SER/tracker.csv"
grep -q "^C$CH," "$SER/tracker.csv" || echo "C$CH,,,,,,,," >> "$SER/tracker.csv"

echo "Đã dựng $PREP (nguyên liệu) và $RES (thành phẩm)"
echo "  → crawl:  python3 scripts/crawl-chapter.py '<url>' --bo $BO"
echo "  → hoặc thả ảnh vào $PREP/pages/ rồi: ./scripts/pipeline.sh $BO $CH"
