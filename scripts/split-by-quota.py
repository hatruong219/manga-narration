"""Chia tts-lines/ thành các lô vừa hạn mức ký tự của nhà cung cấp.

Cắt đúng ranh giới đoạn — không bao giờ cắt giữa câu, vì mỗi đoạn phải khớp một file
audio Sxx.mp3 và một ảnh Sxx.jpg.

Chạy:
    python3 scripts/split-by-quota.py series/TWB/C1/results --quota 3000
"""
import argparse, json, sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--quota", type=int, default=3000, help="ký tự tối đa mỗi lô")
    a = ap.parse_args()

    src = a.results / "tts-lines"
    if not src.is_dir():
        sys.exit(f"không thấy {src} — chạy build-narration.py trước")
    files = sorted(src.glob("S*.txt"))
    if not files:
        sys.exit(f"{src} rỗng")

    batches, cur, cur_n = [], [], 0
    for f in files:
        n = len(f.read_text(encoding="utf-8").strip())
        if n > a.quota:
            print(f"(!) {f.stem} dài {n} ký tự, vượt hạn mức {a.quota} — để riêng một lô")
        if cur and cur_n + n > a.quota:
            batches.append((cur, cur_n))
            cur, cur_n = [], 0
        cur.append(f)
        cur_n += n
    if cur:
        batches.append((cur, cur_n))

    out = a.results / "batches"
    manifest = {"quota": a.quota, "batches": []}
    print(f"{len(files)} đoạn → {len(batches)} lô (hạn mức {a.quota} ký tự)\n")
    for i, (group, total) in enumerate(batches, 1):
        d = out / f"batch-{i:02d}"
        d.mkdir(parents=True, exist_ok=True)
        # Một file gộp để DÁN vào web UI, và các file lẻ để đối chiếu.
        joined = "\n\n".join(f.read_text(encoding="utf-8").strip() for f in group)
        (d / "paste-me.txt").write_text(joined + "\n", encoding="utf-8")
        for f in group:
            (d / f.name).write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        ids = [f.stem for f in group]
        manifest["batches"].append({"batch": i, "chars": total, "shots": ids})
        print(f"  lô {i:02d}: {ids[0]}–{ids[-1]}  ·  {len(group)} đoạn  ·  {total} ký tự")

    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                       encoding="utf-8")
    print(f"\n→ {out}")
    print("Mỗi lô: dán paste-me.txt vào công cụ TTS, tải audio về, đặt vào chính thư mục lô đó.")
    print("Xong hết thì:  python3 scripts/merge-batches.py " + str(a.results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
