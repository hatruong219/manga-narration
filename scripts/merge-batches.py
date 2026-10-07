"""Nhặt audio từ các lô về audio/Sxx.* theo đúng mã shot, rồi báo còn thiếu gì.

Công cụ TTS đặt tên file theo ý nó (audio_1.mp3, output(2).wav, tts-download…), nên
script khớp theo THỨ TỰ trong lô thay vì tin vào tên file. Nếu tên file đã đúng mã Sxx
thì dùng luôn mã đó.

Chạy:
    python3 scripts/merge-batches.py truyen/TWB/results/C1
    python3 scripts/merge-batches.py truyen/TWB/results/C1 --dry-run
"""
import argparse, json, re, shutil, subprocess, sys
from pathlib import Path

AUDIO_EXT = (".mp3", ".wav", ".m4a", ".ogg", ".flac")


def dur(p: Path) -> float:
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of", "csv=p=0", str(p)],
                             capture_output=True, text=True, check=True)
        return float(out.stdout.strip())
    except Exception:
        return 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    man = a.results / "batches" / "manifest.json"
    if not man.exists():
        sys.exit(f"không thấy {man} — chạy split-by-quota.py trước")
    manifest = json.loads(man.read_text(encoding="utf-8"))
    out = a.results / "audio"
    if not a.dry_run:
        out.mkdir(parents=True, exist_ok=True)

    moved, missing, extra = [], [], []
    for b in manifest["batches"]:
        d = a.results / "batches" / f"batch-{b['batch']:02d}"
        shots = b["shots"]
        auds = sorted(f for f in d.iterdir()
                      if f.suffix.lower() in AUDIO_EXT and f.is_file())
        if not auds:
            missing += shots
            print(f"lô {b['batch']:02d}: chưa có audio ({len(shots)} đoạn: {shots[0]}–{shots[-1]})")
            continue

        # Nếu tên file đã là Sxx thì tin tên; không thì khớp theo thứ tự.
        named = {f.stem.upper(): f for f in auds if re.fullmatch(r"S\d+", f.stem.upper())}
        if len(named) >= len(shots):
            pairs = [(s, named[s]) for s in shots if s in named]
        else:
            if len(auds) != len(shots):
                print(f"lô {b['batch']:02d}: có {len(auds)} file audio nhưng {len(shots)} đoạn "
                      f"— KHÔNG khớp được theo thứ tự, đặt tên file thành Sxx rồi chạy lại")
                extra.append(b["batch"])
                continue
            pairs = list(zip(shots, auds))

        for sid, src in pairs:
            dest = out / f"{sid}{src.suffix.lower()}"
            if a.dry_run:
                print(f"  {src.name} → {dest.name}")
            else:
                shutil.copy2(src, dest)
            moved.append(sid)
        print(f"lô {b['batch']:02d}: {len(pairs)} file → audio/")

    have = {re.match(r"S\d+", f.stem.upper()).group()
            for f in out.iterdir() if f.suffix.lower() in AUDIO_EXT
            and re.match(r"S\d+", f.stem.upper())} if out.is_dir() else set()
    want = [s for b in manifest["batches"] for s in b["shots"]]
    still = [s for s in want if s not in have]

    # File có sẵn từ lần chạy backend KHÁC (vd edge-tts) cũng nằm trong audio/.
    # Báo "đủ cả" mà không phân biệt thì người dùng tưởng luồng lô đã xong.
    pre = sorted(have - set(moved))
    print(f"\nghép từ lô: {len(moved)} · có sẵn từ trước: {len(pre)} · tổng {len(have)}/{len(want)}")
    if pre and not moved:
        print(f"(!) KHÔNG file nào đến từ các lô. {len(pre)} file trong audio/ là của lần")
        print("    chạy backend khác trước đó, không phải audio bạn vừa tạo.")
        print("    Muốn thay bằng audio mới: xoá audio/ rồi đọc lại các lô.")
        return 1
    if pre:
        print(f"(!) {len(pre)} file không đến từ lô này: {', '.join(pre[:8])}"
              + (" …" if len(pre) > 8 else "") + " — kiểm xem có phải giọng bạn muốn")
    if still:
        print(f"(!) còn thiếu {len(still)}: {', '.join(still[:12])}"
              + (" …" if len(still) > 12 else ""))
        print("    Đọc nốt các lô còn lại rồi chạy lại — file đã có không bị ghi đè sai.")
        return 1

    # Kiểm file rỗng hoặc quá ngắn — công cụ TTS đôi khi trả file lỗi mà vẫn có đuôi đúng.
    bad = [f.name for f in sorted(out.iterdir())
           if f.suffix.lower() in AUDIO_EXT and dur(f) < 0.4]
    if bad:
        print(f"(!) {len(bad)} file ngắn bất thường (<0,4s), nghi lỗi: {', '.join(bad[:8])}")
        return 1

    print("\nĐỦ CẢ. Tiếp:")
    print(f"   python3 scripts/retime-from-audio.py {a.results}")
    print(f"   python3 scripts/build-video.py {a.results}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
