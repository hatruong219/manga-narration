"""Một chỗ duy nhất biết thư mục nằm ở đâu.

Cấu trúc:
    truyen/<BỘ>/
        series-bible.md · voice-profile.md · tracker.csv · tts-pronounce.tsv
        prepare/C<n>/    ảnh + các đoạn văn NGUỒN  (pages, pages-clean,
                         beat-sheet.md, narration.tsv, shots.tsv)
        results/C<n>/    thành phẩm  (narration-tts.txt, timeline.md,
                         audio/, shots/, video-track.mp4)

Vì sao tách: nguyên liệu và thành phẩm lẫn vào nhau thì không biết xoá gì được khi
làm lại một chương. `prepare/` sửa tay, `results/` sinh lại được hết.

Script nhận đường dẫn `results/C<n>` làm tham số như cũ; `sources()` lần ngược ra
`prepare/C<n>` tương ứng. Bộ cũ nằm phẳng trong `archive/` vẫn chạy được: không
thấy `prepare/` thì lấy chính thư mục results.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRUYEN = ROOT / "truyen"


def series_dir(bo: str) -> Path:
    return TRUYEN / bo


def prepare_dir(bo: str, ch: str | int) -> Path:
    return TRUYEN / bo / "prepare" / f"C{ch}"


def results_dir(bo: str, ch: str | int) -> Path:
    return TRUYEN / bo / "results" / f"C{ch}"


def sources(results: Path) -> Path:
    """prepare/C<n> ứng với một results/C<n>. Bố cục cũ thì trả về chính nó."""
    results = Path(results)
    cand = results.parent.parent / "prepare" / results.name
    return cand if cand.is_dir() else results


def pages_clean(results: Path) -> Path:
    return sources(results) / "pages-clean"


def bo_ch(results: Path) -> tuple[str, str]:
    """Suy mã bộ và số chương từ đường dẫn results/C<n> hoặc bố cục cũ."""
    results = Path(results).resolve()
    ch = results.name.lstrip("C")
    parent = results.parent
    bo = parent.parent.name if parent.name in ("results", "prepare") else parent.name
    return bo, ch
