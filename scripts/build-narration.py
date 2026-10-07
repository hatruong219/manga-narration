"""Dựng kịch bản kể truyện dạng văn xuôi liền mạch từ narration.tsv.

Khác build-script.py (bảng 6 cột cho clip ngắn): format này bám theo kênh kể truyện —
mốc thời gian chạy liên tục, lời kể là văn xuôi, không có cột hiệu ứng. Cột gợi ý trang
chỉ để người dựng biết thả ảnh nào, và bị lược khi xuất bản TTS.

narration.tsv — 2 cột, TAB, dòng # là ghi chú:
    gợi ý trang <TAB> lời kể

Chạy:
    python3 scripts/build-narration.py truyen/TWB/results/C1 --wps 3.5
"""
import argparse, re, sys
from pathlib import Path

from paths import bo_ch, sources


def count_words(text: str) -> int:
    text = re.sub(r"\[.*?\]", " ", text)
    return len([t for t in (w.strip(".,!?;:\"'…()-–—") for w in text.split()) if t])


def mmss(sec: float) -> str:
    s = int(sec)
    return f"{s // 60}:{s % 60:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    # Đo thật trên edge-tts giọng vi-VN: mỗi đoạn có ~1,1s lặng đầu/cuối cố định,
    # phần chữ chạy ~3,8 từ/giây. Chia đều theo một con số wps sẽ ước lượng sai đoạn ngắn
    # tới 40% (đoạn 5 từ thực tế 2,4s, chia đều cho ra 1,4s).
    ap.add_argument("--wps", type=float, default=3.8, help="từ/giây phần chữ")
    ap.add_argument("--overhead", type=float, default=1.1, help="giây lặng cố định mỗi đoạn")
    ap.add_argument("--title", default="")
    a = ap.parse_args()

    src = sources(a.results) / "narration.tsv"
    if not src.exists():
        sys.exit(f"không thấy {src}")

    chunks = []
    for ln, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            sys.exit(f"{src}:{ln} cần 2 cột phân tách bằng TAB")
        chunks.append((parts[0].strip(), parts[1].strip()))
    if not chunks:
        sys.exit("narration.tsv rỗng")

    body, tts, cursor, total, long_chunks = [], [], 0.0, 0, []
    for i, (pages, text) in enumerate(chunks, 1):
        w = count_words(text)
        d = a.overhead + w / a.wps
        sid = f"S{i:02d}"
        body.append(f"**{sid}** · {mmss(cursor)} · `{pages}` — {text}")
        # Mã [Sxx] trùng tên file ảnh shots/Sxx.jpg và file audio audio/Sxx.wav.
        # Một mã duy nhất cho cả ba thứ, nên re-time và dựng không lệch nhau.
        tts.append(f"[{sid}] {text}")
        if d > 12:
            long_chunks.append((i, mmss(cursor), round(d)))
        cursor += d
        total += w

    head = [f"# KỊCH BẢN KỂ — {a.title or a.results.parent.name}", "",
            "> Sinh từ `narration.tsv` bằng `scripts/build-narration.py`. Sửa lời thì sửa TSV",
            "> rồi chạy lại — mốc thời gian tự tính lại.", "",
            f"- Tốc độ đọc: **{a.wps} từ/giây** (đo từ video mẫu, không dùng 2,6 của clip ngắn)",
            f"- Tổng từ: **{total}** · Thời lượng: **{mmss(cursor)}** · {len(chunks)} đoạn",
            f"- Trung bình {total / len(chunks):.0f} từ/đoạn · {cursor / len(chunks):.1f}s/đoạn", "",
            "Mã `Sxx` khớp `shots/Sxx.jpg` và `audio/Sxx.wav`. Cột `` `trang` `` không đọc lên.",
            "", "---", ""]
    (a.results / "narration.md").write_text("\n".join(head + body) + "\n", encoding="utf-8")
    (a.results / "narration-tts.txt").write_text("\n\n".join(tts) + "\n", encoding="utf-8")

    # Bản KHÔNG có mã Sxx: dán vào TTS đọc một lượt thì máy không đọc "ét không một".
    plain = [t.split("] ", 1)[1] for t in tts]
    (a.results / "narration-plain.txt").write_text("\n\n".join(plain) + "\n", encoding="utf-8")

    # Mỗi đoạn một file: đọc lần lượt rồi lưu thành audio/Sxx.wav, khỏi phải tự cắt.
    lines_dir = a.results / "tts-lines"
    lines_dir.mkdir(exist_ok=True)
    for old in lines_dir.glob("S*.txt"):
        old.unlink()
    for i, t in enumerate(plain, 1):
        (lines_dir / f"S{i:02d}.txt").write_text(t + "\n", encoding="utf-8")

    print(f"{len(chunks)} đoạn · {total} từ · {mmss(cursor)} → {a.results / 'narration.md'}")
    print(f"bản đọc TTS → {a.results / 'narration-tts.txt'}  (có mã Sxx, để tra cứu)")
    print(f"bản đọc SẠCH → {a.results / 'narration-plain.txt'}  (không mã — dán vào TTS)")
    print(f"từng đoạn    → {a.results / 'tts-lines'}/Sxx.txt  ({len(plain)} file)")
    if long_chunks:
        print(f"(!) {len(long_chunks)} đoạn dài hơn 12s, nên tách:")
        for i, t, d in long_chunks[:6]:
            print(f"   đoạn {i} tại {t} — {d}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
