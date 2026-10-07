"""Linter độ mượt khi ĐỌC LÊN cho kịch bản kể truyện.

Khác check-script.py (kiểm mốc thời gian của clip ngắn): file này kiểm những thứ làm
lời kể nghe giật cục hoặc khó theo khi phát bằng giọng đọc. Tất cả đều là phép đếm,
nên giao cho máy — tai người nghe ra "chưa mượt" nhưng không chỉ được vì sao.

Chạy:
    python3 scripts/check-narration.py truyen/TWB/prepare/C1/narration.tsv
"""
import argparse, re, sys
from collections import Counter
from pathlib import Path

# Hai tầng ngưỡng. Ngưỡng 5% duy nhất là SAI: đại từ chủ ngữ và tên nhân vật mở 10% số
# câu là bình thường trong tiếng Việt, còn liên từ mở 5% đã nghe thành tic. Tách ra.
CONNECTIVE_MAX = 0.04    # liên từ mở đầu câu — nghe thành tic rất nhanh
OPENER_MAX = 0.11        # từ khác (đại từ, tên riêng) — tự nhiên hơn nhiều
CONNECTIVES = {"rồi", "và", "thế", "nhưng", "vậy", "thì", "sau", "tiếp", "còn", "nên"}
FRAG_MAX = 0.20          # câu <=4 từ không nên quá 20%
FRAG_RUN_MAX = 2         # tối đa 2 câu cực ngắn liên tiếp
NUMWORD_MAX = 3          # số viết thành chữ trong một câu
FLIP_MAX = 0.50          # tỉ lệ đổi cách gọi nhân vật liên tiếp
NUMWORDS = {"một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín",
            "mười", "trăm", "nghìn", "mươi", "tỉ", "tỷ", "triệu"}


def load(path: Path) -> list[str]:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            out.append(parts[-1].strip())
    return out


def sentences(chunks: list[str]) -> list[tuple[int, str]]:
    out = []
    for i, t in enumerate(chunks, 1):
        for s in re.split(r"(?<=[.!?])\s+", t):
            if s.strip():
                out.append((i, s.strip()))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv", type=Path)
    ap.add_argument("--names", default="hắn,Yojin,chú,người đàn ông áo đen",
                    help="các cách gọi CÙNG một nhân vật, phân tách bằng dấu phẩy")
    a = ap.parse_args()

    chunks = load(a.tsv)
    if not chunks:
        sys.exit(f"không đọc được đoạn nào từ {a.tsv}")
    sents = sentences(chunks)
    fails, warns = [], []

    # 1 — từ mở đầu câu bị lặp thành tic
    openers = Counter(s.split()[0].lower() for _, s in sents)
    for w, n in openers.most_common():
        cap = CONNECTIVE_MAX if w in CONNECTIVES else OPENER_MAX
        if n / len(sents) > cap:
            kind = "tic liên từ" if w in CONNECTIVES else "tic mở câu"
            fails.append((kind, f"'{w}' mở {n}/{len(sents)} câu "
                                f"({n / len(sents) * 100:.0f}%)",
                          f"giảm còn dưới {int(len(sents) * cap) + 1} câu"))

    # 2 — tỉ lệ câu cực ngắn
    frags = [(i, s) for i, s in sents if len(s.split()) <= 4]
    if len(frags) / len(sents) > FRAG_MAX:
        fails.append(("câu vụn", f"{len(frags)}/{len(sents)} câu <=4 từ "
                                 f"({len(frags) / len(sents) * 100:.0f}%)",
                      f"gộp lại còn dưới {int(len(sents) * FRAG_MAX)} câu"))

    # 3 — chuỗi câu cực ngắn liên tiếp → đọc lên thành giật cục
    run, worst, at = 0, 0, None
    for idx, (i, s) in enumerate(sents):
        if len(s.split()) <= 4:
            run += 1
            if run > worst:
                worst, at = run, i
        else:
            run = 0
    if worst > FRAG_RUN_MAX:
        fails.append(("giật cục", f"{worst} câu cực ngắn liên tiếp (đoạn {at})",
                      f"chen một câu dài vào, tối đa {FRAG_RUN_MAX} câu ngắn liền nhau"))

    # 4 — số viết thành chữ quá dài chặn nhịp đọc
    for i, s in sents:
        n = sum(1 for w in s.split() if w.strip(".,").lower() in NUMWORDS)
        if n > NUMWORD_MAX:
            fails.append(("số dài", f"đoạn {i}: {n} từ số — {s[:55]}",
                          "làm tròn hoặc nói xấp xỉ"))

    # 5 — đổi cách gọi nhân vật liên tục → nghe khó theo ai là ai
    names = [n.strip() for n in a.names.split(",") if n.strip()]
    if names:
        pat = re.compile(r"\b(" + "|".join(re.escape(n) for n in
                                           sorted(names, key=len, reverse=True)) + r")\b")
        seq = [m.group(1) for t in chunks for m in pat.finditer(t)]
        if len(seq) > 2:
            flips = sum(1 for x, y in zip(seq, seq[1:]) if x != y)
            rate = flips / (len(seq) - 1)
            # Chỉ cảnh báo, không tính lỗi: máy không phân biệt được lời NGƯỜI KỂ với lời
            # nhân vật được thuật lại. "chú" trong câu Hikari nói là hợp lệ, nhưng vẫn bị
            # đếm là một lần đổi cách gọi. Người phải tự đọc và phán.
            if rate > FLIP_MAX:
                dist = " · ".join(f"{k}×{v}" for k, v in Counter(seq).most_common())
                warns.append(f"đổi cách gọi {flips}/{len(seq) - 1} lần ({rate * 100:.0f}%) — {dist}"
                             " · kiểm tay xem có phải lời thuật lại không")

    words = sum(len(t.split()) for t in chunks)
    print(f"{len(chunks)} đoạn · {len(sents)} câu · {words} từ "
          f"· {words / len(sents):.1f} từ/câu")
    for w in warns:
        print(f"(cảnh báo) {w}")
    if not fails:
        print("\nMƯỢT — không thấy lỗi đọc lên nào.")
        return 0
    print(f"\n### {len(fails)} lỗi\n")
    print("| Loại | Số đo | Cách sửa |")
    print("|---|---|---|")
    for kind, what, fix in fails:
        print(f"| {kind} | {what} | {fix} |")
    return 1


if __name__ == "__main__":
    sys.exit(main())
