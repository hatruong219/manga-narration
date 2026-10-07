#!/usr/bin/env bash
# Tải ảnh một chapter về đúng thư mục + đúng tên theo quy ước của project.
#
# Chạy:
#   ./scripts/fetch-pages.sh TWB 1 'https://cdn1.zetimage.com/twilight-blade/1/{n}.jpg' \
#       --from 0 --to 20 --referer https://www.zettruyen.work/
#
# {n} trong URL được thay bằng số trang gốc của site. File lưu ra luôn đánh số từ 01.
set -euo pipefail
cd "$(dirname "$0")/.."

usage() {
    # Không dùng ${1:?...} cho URL mẫu: dấu } trong "{n}" sẽ đóng sớm phần mở ngoặc
    # và thông báo lỗi bị nối thẳng vào giá trị biến.
    cat >&2 <<USAGE
Dùng: $(basename "$0") {BO} {CHAPTER} {URL_MAU} --to N [--from N] [--referer URL] [--ext jpg]
URL mẫu phải chứa {n} — chỗ sẽ thay bằng số trang gốc của site.
Ví dụ: $(basename "$0") TWB 1 'https://host/path/{n}.jpg' --from 0 --to 20 --referer https://site/
USAGE
    exit 2
}
[ $# -ge 3 ] || usage
BO="$1"; CH="$2"; TPL="$3"; shift 3
case "$TPL" in *"{n}"*) ;; *) echo "URL mẫu thiếu {n}" >&2; usage ;; esac

FROM=0; TO=""; REFERER=""; EXT=""
while [ $# -gt 0 ]; do
    case "$1" in
        --from) FROM="$2"; shift 2 ;;
        --to) TO="$2"; shift 2 ;;
        --referer) REFERER="$2"; shift 2 ;;
        --ext) EXT="$2"; shift 2 ;;
        *) echo "tham số lạ: $1" >&2; exit 2 ;;
    esac
done
[ -n "$TO" ] || { echo "thiếu --to (trang cuối)" >&2; usage; }
[ -n "$EXT" ] || EXT="${TPL##*.}"

UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
DIR="series/$BO/C$CH/pages"
mkdir -p "$DIR"

ok=0; fail=0; page=1
for n in $(seq "$FROM" "$TO"); do
    url="${TPL//\{n\}/$n}"
    out=$(printf '%s/%s_C%s_P%02d.%s' "$DIR" "$BO" "$CH" "$page" "$EXT")

    args=(-sS --fail --retry 2 --retry-delay 1 -H "User-Agent: $UA")
    [ -n "$REFERER" ] && args+=(-H "Referer: $REFERER")

    if curl "${args[@]}" -o "$out" "$url"; then
        # Firewall/CDN hay trả trang HTML kèm HTTP 200. Ảnh thật thì `file` phải nhận ra.
        kind=$(file -b --mime-type "$out")
        case "$kind" in
            image/*) printf 'P%02d  %-9s %s\n' "$page" "$(du -h "$out"|cut -f1)" "$(basename "$out")"; ok=$((ok+1)) ;;
            *) echo "P$(printf '%02d' $page)  KHÔNG PHẢI ẢNH ($kind) — xem $out"; fail=$((fail+1)) ;;
        esac
    else
        echo "P$(printf '%02d' $page)  tải lỗi: $url"; rm -f "$out"; fail=$((fail+1))
    fi
    page=$((page+1))
    sleep 0.4          # đừng dập CDN
done

echo
echo "xong: $ok ảnh · $fail lỗi → $DIR"
[ "$fail" -eq 0 ] || echo "(!) có lỗi — kiểm lại URL mẫu / --referer / mạng có bị lọc không"
[ "$ok" -gt 0 ] && echo "kiểm chiều rộng ảnh (cần >= 1200px để đọc được bong bóng thoại):" \
    && echo "  identify -format '%f %wx%h\\n' $DIR/*.$EXT 2>/dev/null || python3 -c \"
from PIL import Image; import glob
for f in sorted(glob.glob('$DIR/*.$EXT')):
    w,h=Image.open(f).size; print(f.split('/')[-1], f'{w}x{h}', '' if w>=1200 else '  <-- HẸP')\""
