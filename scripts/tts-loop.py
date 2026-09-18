"""Loop 1..n qua các lô, gọi một script TTS bên ngoài cho từng đoạn.

Khâu gọi nhà cung cấp để CẮM NGOÀI vì mỗi nơi mỗi API. Bạn viết một script nhận
2 tham số và loop lo phần còn lại:

    my-tts.sh <file-text-vào> <file-audio-ra>

Loop này KHÔNG xử lý quota — hết token thì lệnh bên ngoài fail, nó ghi nhận rồi đi tiếp,
chạy lại là tiếp đúng chỗ dừng vì file đã có được bỏ qua.

Chạy:
    python3 scripts/tts-loop.py series/TWB/C1/results --exec ./my-tts.sh --quota 1000
    python3 scripts/tts-loop.py series/TWB/C1/results --exec ./my-tts.sh --dry-run
"""
import argparse, subprocess, sys
from pathlib import Path

AUDIO_EXT = ".mp3"


def batches_of(files: list[Path], quota: int) -> list[list[Path]]:
    """Gom đoạn thành lô ≤ quota ký tự. Không bao giờ cắt giữa một đoạn."""
    out, cur, n = [], [], 0
    for f in files:
        c = len(f.read_text(encoding="utf-8").strip())
        if cur and n + c > quota:
            out.append(cur)
            cur, n = [], 0
        cur.append(f)
        n += c
    if cur:
        out.append(cur)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--exec", dest="cmd", required=True,
                    help="script nhận <textfile> <outfile>")
    ap.add_argument("--quota", type=int, default=1000, help="ký tự mỗi lô")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="đọc lại cả file đã có")
    ap.add_argument("--stop-on-fail", action="store_true")
    a = ap.parse_args()

    src = a.results / "tts-lines"
    if not src.is_dir():
        sys.exit(f"không thấy {src} — chạy build-narration.py trước")
    files = sorted(src.glob("S*.txt"))
    if not files:
        sys.exit(f"{src} rỗng")
    out = a.results / "audio"
    out.mkdir(parents=True, exist_ok=True)

    lots = batches_of(files, a.quota)
    tot_chars = sum(len(f.read_text(encoding="utf-8").strip()) for f in files)
    print(f"{len(files)} đoạn · {tot_chars} ký tự → {len(lots)} lô "
          f"(hạn mức {a.quota}/lô)\n")

    done = skip = fail = 0
    for i, lot in enumerate(lots, 1):
        n = sum(len(f.read_text(encoding="utf-8").strip()) for f in lot)
        print(f"── lô {i}/{len(lots)}: {lot[0].stem}–{lot[-1].stem} · {n} ký tự")
        for f in lot:
            dest = out / f"{f.stem}{AUDIO_EXT}"
            if dest.exists() and dest.stat().st_size > 1000 and not a.force:
                skip += 1
                continue
            if a.dry_run:
                print(f"   {a.cmd} {f} {dest}")
                done += 1
                continue
            r = subprocess.run([a.cmd, str(f), str(dest)],
                               capture_output=True, text=True)
            if r.returncode != 0 or not dest.exists() or dest.stat().st_size < 1000:
                print(f"   LỖI {f.stem}: {(r.stderr or r.stdout).strip()[:100]}")
                dest.unlink(missing_ok=True)
                fail += 1
                if a.stop_on_fail:
                    print("\n(!) dừng theo --stop-on-fail")
                    print(f"đọc {done} · có sẵn {skip} · lỗi {fail}")
                    return 1
            else:
                done += 1
        print(f"   xong lô {i}: {done} tổng đọc được")

    print(f"\nđọc {done} · có sẵn {skip} · lỗi {fail} → {out}")
    if fail:
        print("(!) chạy lại để đọc tiếp phần lỗi — file đã có sẽ bỏ qua")
        return 1
    print("→ tiếp:")
    print(f"   python3 scripts/concat-audio.py {a.results}")
    print(f"   python3 scripts/retime-from-audio.py {a.results}")
    print(f"   python3 scripts/build-video.py {a.results}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
