"""QC kỹ thuật kịch bản — 6 mục, kiểm bằng máy chứ không hỏi LLM.

Vì sao là script: cả 6 mục đều là phép đếm và so sánh. LLM đếm từ sai thường
xuyên và có xu hướng báo PASS cho block lệch 30%. Việc này giao cho máy.

Chạy:
    python3 check-script.py series/BLK/C241/results/script.md
    python3 check-script.py .../script.md --target 180
"""
import argparse, re, sys
from pathlib import Path

WPS_DEFAULT = 2.6          # từ/giây, tốc độ đọc chuẩn trong Series Bible
MAX_BLOCK_SEC = 8
MAX_LINE_WORDS = 18
TOLERANCE = 0.10           # lệch tương đối số từ ÷ wps so với thời lượng ghi
# Slack tuyệt đối để hấp thụ việc làm tròn mốc về giây nguyên. Không có nó thì dung sai
# 10% là BẤT KHẢ THI ở block ngắn: block 2 giây, một giây làm tròn đã là 50%.
ROUND_SLACK = 0.6
EFFECTS = {"HOLD", "ZOOM-IN", "ZOOM-OUT", "PAN", "SHAKE", "FLASH-CUT"}

ROW = re.compile(r"^\|\s*(B\d+)\s*\|(.+)$")
TIME = re.compile(r"(\d{1,2}):(\d{2})\s*[–\-—]\s*(\d{1,2}):(\d{2})")
PANEL_REF = re.compile(r"P\d+-[a-z]|P\d+")


def secs(m: int, s: int) -> int:
    return m * 60 + s


def count_words(text: str) -> int:
    """Đếm từ theo cách giọng đọc phát âm: tách theo khoảng trắng.

    Bỏ dấu câu đứng riêng, bỏ nội dung trong ngoặc vuông (chú thích dựng).
    """
    text = re.sub(r"\[.*?\]", " ", text)
    toks = [t.strip(".,!?;:\"'…()-–—") for t in text.split()]
    return len([t for t in toks if t])


def parse(md: str) -> list[dict]:
    """Đọc bảng kịch bản. Cột: Mã | Mốc | Panel | Hiệu ứng | Lời đọc | Số từ."""
    blocks = []
    for line in md.splitlines():
        m = ROW.match(line.strip())
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 4:
            continue
        tm = TIME.search(cells[0])
        blocks.append({
            "id": m.group(1),
            "raw_time": cells[0],
            "start": secs(int(tm.group(1)), int(tm.group(2))) if tm else None,
            "end": secs(int(tm.group(3)), int(tm.group(4))) if tm else None,
            "panel": cells[1],
            "effect": cells[2],
            "line": cells[3],
            "stated_words": cells[4] if len(cells) > 4 else "",
        })
    return blocks


def real_panels(beat_sheet: Path | None) -> set[str] | None:
    """Danh sách panel có thật, lấy từ beat-sheet.md. None = bỏ qua mục 3."""
    if not beat_sheet or not beat_sheet.exists():
        return None
    return set(PANEL_REF.findall(beat_sheet.read_text(encoding="utf-8")))


def check(blocks: list[dict], panels: set[str] | None, wps: float) -> list[tuple]:
    fails = []
    add = lambda b, item, what, fix: fails.append((b["id"], item, what, fix))
    prev_end = 0

    for i, b in enumerate(blocks):
        # Mục 1 — mốc liên tục
        if b["start"] is None:
            add(b, "1 mốc", f"không đọc được mốc {b['raw_time']!r}", "viết dạng 00:00–00:04")
        else:
            if b["start"] != prev_end:
                gap = b["start"] - prev_end
                add(b, "1 mốc", f"{'hở' if gap > 0 else 'chồng/lùi'} {abs(gap)}s so với block trước",
                    f"đặt start = {prev_end // 60:02d}:{prev_end % 60:02d}")
            if b["end"] <= b["start"]:
                add(b, "1 mốc", "end <= start", "sửa mốc")
            prev_end = max(prev_end, b["end"])

        words = count_words(b["line"])
        b["words"] = words
        need = words / wps

        # Mục 2 — số từ ÷ wps khớp thời lượng ghi
        if b["start"] is not None and b["end"] > b["start"]:
            dur = b["end"] - b["start"]
            diff = abs(need - dur)
            if dur and diff > max(dur * TOLERANCE, ROUND_SLACK):
                add(b, "2 độ dài", f"{words} từ ÷ {wps} = {need:.1f}s nhưng mốc ghi {dur}s "
                                   f"(lệch {diff:.1f}s = {diff / dur * 100:.0f}%)",
                    f"đặt độ dài {round(need)}s, hoặc sửa lời còn {round(dur * wps)} từ")

            # Mục 4 — không giữ quá 8 giây
            if dur > MAX_BLOCK_SEC:
                add(b, "4 quá 8s", f"{dur}s", "tách thành 2 khung, khung 2 zoom vào chi tiết khác")

        # Mục 3 — panel có thật
        if panels is not None:
            refs = PANEL_REF.findall(b["panel"])
            if not refs:
                add(b, "3 panel", f"không thấy mã panel trong {b['panel']!r}", "ghi dạng P03-b")
            for r in refs:
                if r not in panels:
                    add(b, "3 panel", f"{r} không có trong beat sheet", "sửa về panel có thật")

        # Mục 5 — câu đọc tối đa 18 từ
        for sent in re.split(r"(?<=[.!?])\s+", b["line"]):
            n = count_words(sent)
            if n > MAX_LINE_WORDS:
                add(b, "5 câu dài", f"{n} từ: {sent[:50]}…", "tách câu, giọng đọc sẽ hụt hơi")

        # Mục 6 — hiệu ứng trong 6 loại
        tok = b["effect"].upper().split()
        if not tok or tok[0] not in EFFECTS:
            add(b, "6 hiệu ứng", f"{b['effect']!r} không thuộc 6 loại",
                "dùng " + " · ".join(sorted(EFFECTS)))

        # Phụ — cột Số từ do LLM tự ghi, hay sai. Báo nhưng không tính FAIL.
        if b["stated_words"].isdigit() and int(b["stated_words"]) != words:
            b["word_mismatch"] = f"cột ghi {b['stated_words']}, đếm thật {words}"

    return fails


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("script", type=Path)
    ap.add_argument("--beat-sheet", type=Path, help="mặc định beat-sheet.md cạnh script")
    ap.add_argument("--target", type=float, help="thời lượng mục tiêu (giây) để tính lệch")
    ap.add_argument("--wps", type=float, default=WPS_DEFAULT)
    a = ap.parse_args()

    blocks = parse(a.script.read_text(encoding="utf-8"))
    if not blocks:
        print("KHÔNG đọc được block nào. Bảng phải có dòng dạng | B01 | 00:00–00:04 | ...")
        return 1

    bs = a.beat_sheet or a.script.parent / "beat-sheet.md"
    panels = real_panels(bs)
    fails = check(blocks, panels, a.wps)

    total_words = sum(b["words"] for b in blocks)
    computed = total_words / a.wps
    end = max((b["end"] or 0) for b in blocks)

    print(f"Block: {len(blocks)} · từ: {total_words} · thời lượng tính: {computed:.0f}s "
          f"· mốc cuối: {end}s")
    if a.target:
        print(f"Mục tiêu {a.target:.0f}s · lệch {(computed - a.target) / a.target * 100:+.0f}%")
    if panels is None:
        print(f"(!) không thấy {bs.name} → BỎ QUA mục 3 (panel có thật)")

    mm = [(b["id"], b["word_mismatch"]) for b in blocks if b.get("word_mismatch")]
    if mm:
        print(f"\nCột 'Số từ' sai ở {len(mm)} block (không tính lỗi):")
        for bid, msg in mm[:8]:
            print(f"  {bid}: {msg}")

    if not fails:
        print("\nPASS toàn bộ 6 mục.")
        return 0

    print(f"\n### Bảng lỗi — {len(fails)} lỗi\n")
    print("| Mã block | Mục lỗi | Sai ở đâu | Cách sửa |")
    print("|---|---|---|---|")
    for bid, item, what, fix in fails:
        print(f"| {bid} | {item} | {what} | {fix} |")
    return 1


if __name__ == "__main__":
    sys.exit(main())
