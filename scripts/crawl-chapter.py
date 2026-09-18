"""Tải ảnh một chapter từ URL trang đọc truyện → đúng thư mục, đúng tên quy ước.

Chạy:
    python3 scripts/crawl-chapter.py https://site/twilight-blade/chapter-1 --bo TWB
    python3 scripts/crawl-chapter.py <url> --bo TWB --chapter 241 --force

Cách tìm ảnh: trang đọc truyện lazy-load ảnh qua data-src, còn src là logo và ảnh
quảng cáo. Script lấy data-src, rồi giữ lại host XUẤT HIỆN NHIỀU NHẤT — đó là CDN ảnh
trang. Không hardcode tên host nào nên chạy được với nhiều site.
"""
import argparse, collections, re, subprocess, sys, time
from io import BytesIO
from pathlib import Path

from curl_cffi import requests as cr
from PIL import Image

MIN_WIDTH = 1200          # dưới ngưỡng này AI đọc không ra chữ trong bong bóng thoại
DELAY = 0.4               # giây giữa 2 request, đừng dập CDN
IMG_EXT = re.compile(r"\.(jpe?g|png|webp)(?:\?|$)", re.I)


def session() -> cr.Session:
    # impersonate chrome: nhiều CDN ảnh fingerprint TLS, curl/requests trơn sẽ ăn 403
    return cr.Session(impersonate="chrome", timeout=40)


def find_images(html: str) -> list[str]:
    """data-src theo đúng thứ tự trang, lọc còn host chiếm đa số."""
    cands = [u for u in re.findall(r'data-src\s*=\s*["\']([^"\']+)["\']', html)
             if IMG_EXT.search(u) and u.startswith("http")]
    if not cands:
        return []
    host = re.compile(r"https?://([^/]+)/")
    top, _ = collections.Counter(
        m.group(1) for u in cands if (m := host.match(u))).most_common(1)[0]
    return [u for u in cands if f"//{top}/" in u]


def derive(url: str, bo: str | None, chapter: str | None) -> tuple[str, str, str]:
    """Suy mã bộ + số chapter từ URL nếu không được truyền vào."""
    parts = [p for p in url.split("?")[0].rstrip("/").split("/") if p]
    slug = next((p for p in reversed(parts) if not p.lower().startswith("chapter")), "series")
    ch = chapter or (m.group(1) if (m := re.search(r"chapter[-_]?([\d.]+)", url, re.I)) else "0")
    code = bo or "".join(w[0] for w in slug.split("-") if w)[:4].upper() or "SER"
    return code, ch, slug


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--bo", help="mã bộ cho tên file (mặc định suy từ slug)")
    ap.add_argument("--chapter", help="số chapter (mặc định suy từ URL)")
    ap.add_argument("--force", action="store_true", help="tải lại cả file đã có")
    ap.add_argument("--limit", type=int, help="chỉ tải N trang đầu (để thử)")
    a = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    bo, ch, slug = derive(a.url, a.bo, a.chapter)

    # Dựng scaffold cấp bộ qua new-chapter.sh thay vì mkdir trần: vào project bằng crawler
    # thì trước đây thiếu series-bible.md / voice-profile.md / tracker.csv, và /manga-script
    # sẽ không có gì để đọc. new-chapter.sh idempotent, không ghi đè file đã có.
    scaffold = root / "scripts" / "new-chapter.sh"
    if scaffold.exists():
        subprocess.run([str(scaffold), bo, ch], cwd=root,
                       stdout=subprocess.DEVNULL, check=False)

    out = root / "series" / bo / f"C{ch}" / "pages"
    out.mkdir(parents=True, exist_ok=True)

    s = session()
    ref = "/".join(a.url.split("/")[:3]) + "/"
    hdr = {"Referer": ref}

    # Site throttle sau một loạt request và trả 500 tạm thời — thử lại vài lần.
    r = None
    for attempt in range(3):
        r = s.get(a.url, headers=hdr)
        if r.status_code == 200:
            break
        print(f"trang chapter HTTP {r.status_code}, thử lại ({attempt + 1}/3)…", file=sys.stderr)
        time.sleep(3 * (attempt + 1))
    if r.status_code != 200:
        sys.exit(f"trang chapter trả HTTP {r.status_code} sau 3 lần thử")
    if re.search(r"fortiguard|web filter violation", r.text, re.I):
        sys.exit("mạng đang chặn host này (FortiGuard web filter) — đổi mạng")

    urls = find_images(r.text)
    if not urls:
        sys.exit("không tìm được ảnh nào qua data-src. Trang có thể nạp ảnh bằng JS "
                 "→ mở DevTools, xem request ảnh thật rồi dùng scripts/fetch-pages.sh")
    if a.limit:
        urls = urls[:a.limit]

    print(f"bộ {bo} · chapter {ch} · slug {slug}")
    print(f"tìm được {len(urls)} ảnh → {out.relative_to(root)}\n")

    ok = skip = fail = 0
    widths = []
    for i, u in enumerate(urls, 1):
        ext = (m.group(1).lower() if (m := IMG_EXT.search(u)) else "jpg").replace("jpeg", "jpg")
        dest = out / f"{bo}_C{ch}_P{i:02d}.{ext}"
        if dest.exists() and not a.force:
            skip += 1
            continue
        try:
            g = s.get(u, headers=hdr)
            ct = g.headers.get("content-type", "")
            # CDN và firewall hay trả HTML kèm HTTP 200 — phải mở bằng PIL mới chắc là ảnh
            if g.status_code != 200 or not ct.startswith("image"):
                print(f"  P{i:02d} HTTP {g.status_code} ct={ct or '?'} → bỏ")
                fail += 1
                continue
            im = Image.open(BytesIO(g.content))
            w, h = im.size
            widths.append(w)
            dest.write_bytes(g.content)
            flag = "" if w >= MIN_WIDTH else "  HẸP"
            print(f"  P{i:02d} {w}x{h} {len(g.content)//1024}KB{flag}")
            ok += 1
        except Exception as e:
            print(f"  P{i:02d} lỗi {type(e).__name__}: {str(e)[:70]}")
            fail += 1
        time.sleep(DELAY)

    print(f"\ntải {ok} · có sẵn {skip} · lỗi {fail}")
    if widths:
        mn, mx = min(widths), max(widths)
        print(f"chiều rộng: {mn}–{mx}px")
        if mn < MIN_WIDTH:
            print(f"(!) dưới ngưỡng {MIN_WIDTH}px. Đọc được hay không tuỳ KIỂU TRANG:")
            print("    - webtoon/manhwa (cuộn dọc, 1 panel lớn, chữ to): ~580px vẫn đọc rõ")
            print("    - manga truyền thống (nhiều panel nhỏ, chữ nhỏ): sẽ đọc không ra")
            print("    Mở thử 1 ảnh xem chữ trong bong bóng có rõ không trước khi chạy "
                  "/manga-beat-sheet cho cả chapter.")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
