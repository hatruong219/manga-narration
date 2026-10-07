"""Xuất bản sạch cho giọng đọc máy từ blocks.tsv.

Mỗi block một dòng, mở đầu bằng mã [Bxx] để sau này khớp lại với file audio Bxx.wav.
Bỏ hết mốc thời gian, panel, hiệu ứng, markdown — TTS chỉ cần chữ để đọc.

Map phát âm nằm ở series/{BO}/tts-pronounce.tsv (2 cột, TAB: từ gốc → cách viết cho TTS).
Để ở file dữ liệu chứ không hardcode: cách viết nào đọc đúng còn tuỳ engine TTS, phải
thử rồi chỉnh, và mỗi bộ có tên riêng khác nhau.

Chạy:
    python3 scripts/build-tts.py series/TWB/C1/results
"""
import argparse, re, sys
from pathlib import Path

# TTS biến các ký tự này thành khoảng lặng dài không kiểm soát được, hoặc đọc trôi.
RISKY = {
    "…": "dấu ba chấm → khoảng lặng dài",
    "—": "gạch ngang dài → khoảng lặng dài",
    "–": "gạch ngang → khoảng lặng dài",
    ":": "hai chấm → đọc liền, mất nhịp",
    ";": "chấm phẩy → nhịp không đoán được",
}


def load_map(series_dir: Path) -> list[tuple[str, str]]:
    f = series_dir / "tts-pronounce.tsv"
    if not f.exists():
        return []
    out = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            out.append((parts[0].strip(), parts[1].strip()))
    # thay từ dài trước, tránh "Yojin Odaki" bị cắt lẻ sai
    return sorted(out, key=lambda p: -len(p[0]))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path, help="thư mục results/ của chapter")
    ap.add_argument("--no-map", action="store_true", help="giữ nguyên tên riêng, không thay")
    a = ap.parse_args()

    src = a.results / "blocks.tsv"
    if not src.exists():
        sys.exit(f"không thấy {src}")
    series_dir = a.results.parent.parent
    pmap = [] if a.no_map else load_map(series_dir)

    lines, warnings, replaced = [], [], {}
    idx = 0
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        idx += 1
        text = parts[2].strip()

        for ch, why in RISKY.items():
            if ch in text:
                warnings.append(f"B{idx:02d} còn {ch!r} — {why}")
        for m in re.findall(r"\d[\d.,]*", text):
            # Không tự đổi số thành chữ: "16.820 yên", "chương 1", "trang 3" đọc khác nhau,
            # máy đoán sai còn tệ hơn người sửa tay. Chỉ báo để người viết lại.
            warnings.append(f"B{idx:02d} còn số {m!r} — viết thành chữ bằng tay")

        for a_, b_ in pmap:
            if a_ in text:
                text = text.replace(a_, b_)
                replaced[a_] = replaced.get(a_, 0) + 1
        lines.append(f"[B{idx:02d}] {text}")

    out = a.results / "tts.txt"
    body = "\n".join(lines)
    if pmap:
        body += "\n\n# --- map phát âm đã áp (sửa ở series/{BO}/tts-pronounce.tsv) ---\n"
        for a_, b_ in pmap:
            n = replaced.get(a_, 0)
            body += f"# {a_} → {b_}  ({n} lần)\n"
    out.write_text(body + "\n", encoding="utf-8")

    print(f"{len(lines)} dòng → {out}")
    if replaced:
        print("thay phát âm: " + " · ".join(f"{k}×{v}" for k, v in replaced.items()))
    if warnings:
        print(f"\n(!) {len(warnings)} chỗ cần xem lại:")
        for w in warnings[:12]:
            print("   " + w)
    else:
        print("không còn ký tự nào TTS đọc sai.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
