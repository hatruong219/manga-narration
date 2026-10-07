#!/usr/bin/env python3
"""Trộn nhạc nền vào giọng đọc, rồi ghép thành video hoàn chỉnh.

    .venv/bin/python scripts/mix-bgm.py truyen/FRN/results/C1
    .venv/bin/python scripts/mix-bgm.py truyen/FRN/results/C1 --gain -18 --no-duck
    .venv/bin/python scripts/mix-bgm.py truyen/FRN/results/C1 --audio-only

Nhạc lấy từ `truyen/<BỘ>/bgm/` (file đầu tiên, hoặc chỉ định bằng `--bgm`), **lặp lại**
cho đủ độ dài giọng đọc rồi cắt đúng bằng.

Ra:
    export/narration-bgm.mp3   giọng đọc đã trộn nhạc
    export/video-final.mp4     track hình + tiếng đó   (bỏ qua nếu --audio-only)

## Hai thứ quyết định nghe có ra kênh kể truyện hay không

**1. Âm lượng nhạc.** Mặc định **-22 dB** so với giọng. Nhạc phải ở dưới xa: người xem
tới để nghe kể, nhạc chỉ để lấp khoảng lặng cho đỡ trống. Muốn to hơn thì `--gain -18`;
quá -14 là bắt đầu nuốt lời.

**2. Ducking (mặc định BẬT).** Nhạc tự hạ xuống khi có tiếng nói, tự dâng lên ở khoảng
lặng, bằng `sidechaincompress` lấy chính giọng đọc làm tín hiệu điều khiển. Đây là thứ
khiến lời nghe rõ mà nhạc vẫn còn mặt — chỉnh âm lượng cố định không làm được việc đó:
để đủ nhỏ cho lời rõ thì lúc im lặng nhạc gần như biến mất.

Có `afade` 3 giây cuối để nhạc tắt dần thay vì đứt phựt.
"""
import argparse
import subprocess
import sys
from pathlib import Path

AUDIO_EXT = (".mp3", ".wav", ".m4a", ".flac", ".ogg")


def probe(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(out.stdout.strip() or 0)


def run(cmd: list[str], what: str) -> None:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1200:], file=sys.stderr)
        sys.exit(f"ffmpeg lỗi khi {what}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path, help="vd truyen/FRN/results/C1")
    ap.add_argument("--bgm", type=Path, help="file nhạc; mặc định lấy trong truyen/<BỘ>/bgm/")
    ap.add_argument("--gain", type=float, default=-22.0,
                    help="âm lượng nhạc so với giọng, dB (mặc định -22)")
    ap.add_argument("--no-duck", action="store_true",
                    help="tắt ducking (nhạc giữ một mức, không né lời)")
    ap.add_argument("--fade", type=float, default=3.0, help="giây tắt dần cuối bài")
    ap.add_argument("--audio-only", action="store_true", help="chỉ trộn tiếng, không dựng video")
    a = ap.parse_args()

    voice = a.results / "export" / "narration.mp3"
    if not voice.exists():
        sys.exit(f"không thấy {voice} — chạy concat-audio.py trước")

    bgm = a.bgm
    if bgm is None:
        # truyen/<BỘ>/results/C<n> → truyen/<BỘ>/bgm
        bdir = a.results.parent.parent / "bgm"
        found = sorted(f for f in bdir.glob("*") if f.suffix.lower() in AUDIO_EXT) \
            if bdir.is_dir() else []
        if not found:
            sys.exit(f"không thấy file nhạc nào trong {bdir} — bỏ nhạc vào đó hoặc dùng --bgm")
        bgm = found[0]

    vdur, bdur = probe(voice), probe(bgm)
    loops = int(vdur // bdur) + 1
    print(f"giọng đọc {vdur / 60:.1f} phút · nhạc {bdur:.0f}s → lặp {loops} lần")
    print(f"nhạc ở {a.gain:+.0f} dB · ducking {'TẮT' if a.no_duck else 'BẬT'}")

    fade_at = max(0.0, vdur - a.fade)
    if a.no_duck:
        fc = (f"[1:a]volume={a.gain}dB,afade=t=out:st={fade_at:.2f}:d={a.fade}[bg];"
              f"[0:a][bg]amix=inputs=2:duration=first:normalize=0[out]")
    else:
        # Giọng tách đôi: một nhánh ra loa, một nhánh làm tín hiệu điều khiển cho nhạc.
        fc = (f"[0:a]asplit=2[voice][key];"
              f"[1:a]volume={a.gain}dB,afade=t=out:st={fade_at:.2f}:d={a.fade}[bg];"
              f"[bg][key]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=400[duck];"
              f"[voice][duck]amix=inputs=2:duration=first:normalize=0[out]")

    mixed = a.results / "export" / "narration-bgm.mp3"
    run(["ffmpeg", "-y", "-i", str(voice), "-stream_loop", str(loops), "-i", str(bgm),
         "-filter_complex", fc, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k",
         str(mixed)], "trộn nhạc")
    print(f"→ {mixed}  ({probe(mixed) / 60:.1f} phút)")

    if a.audio_only:
        return 0

    track = a.results / "export" / "video-track.mp4"
    if not track.exists():
        print(f"(!) chưa có {track} — chạy build-video.py trước, bỏ qua bước dựng video")
        return 0
    final = a.results / "export" / "video-final.mp4"
    run(["ffmpeg", "-y", "-i", str(track), "-i", str(mixed),
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
         "-map", "0:v:0", "-map", "1:a:0", str(final)], "ghép vào video")
    print(f"→ {final}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
