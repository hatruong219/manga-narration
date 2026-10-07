"""Dựng TRACK HÌNH 1080x1920 từ shots/ + độ dài từng shot, có thể ghép sẵn giọng đọc.

Vì sao cần: thả 84 ảnh vào CapCut rồi sửa tay 84 độ dài là việc không ai muốn làm.
File này ghép sẵn thành một video câm đúng mốc; CapCut chỉ còn việc thả video + audio
+ nhạc + phụ đề.

Độ dài lấy từ audio/Sxx.wav nếu có (chính xác), không có thì dự toán từ số từ.

Chạy:
    python3 scripts/build-video.py truyen/TWB/results/C1
    python3 scripts/build-video.py truyen/TWB/results/C1 --fps 30 --wps 3.5
    python3 scripts/build-video.py truyen/TWB/results/C1 --with-audio   # kèm giọng đọc

`video-track.mp4` cố ý CÂM: đó là bản để thả vào CapCut, nơi bạn còn chồng nhạc nền,
phụ đề, hiệu ứng — có sẵn tiếng trong đó chỉ vướng.

`--with-audio` xuất thêm `video-preview.mp4` đã ghép giọng, để XEM THỬ. Đây mới là
cách duy nhất kiểm được hình có khớp tiếng không; nhìn bảng mốc không thay thế được.
Ảnh cuối đứng thêm vài giây so với tiếng là bình thường — concat demuxer cắt mất file
cuối nếu không lặp nó lại, nên script lặp có chủ ý.
"""
import argparse, shutil, subprocess, sys
from pathlib import Path

from PIL import Image

from paths import sources

W, H = 1080, 1920          # mặc định dọc 9:16; đổi bằng --size
AUDIO_EXT = (".wav", ".mp3", ".m4a", ".flac", ".ogg")


def probe(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("results", type=Path)
    ap.add_argument("--size", default="1080x1920",
                    help="khung hình. 1080x1920 = dọc 9:16 (Shorts/TikTok, phải dưới 3 phút). "
                         "1920x1080 = ngang 16:9 (video YouTube dài)")
    ap.add_argument("--fill", choices=["blur", "black"], default="blur",
                    help="lấp chỗ trống quanh ảnh: nền mờ phóng to (mặc định) hay đen")
    ap.add_argument("--brand", type=Path,
                    help="ảnh nhận diện kênh đặt thành dải bên; ghi đè --fill. "
                         "Ảnh nên cao đúng bằng khung (vd 640x1080 cho khung 1920x1080)")
    ap.add_argument("--brand-side", choices=["left", "right", "both"], default="left")
    ap.add_argument("--bg-color", default="0x2c242d",
                    help="màu lấp phần trống quanh ảnh truyện khi dùng --brand")
    ap.add_argument("--with-audio", action="store_true",
                    help="xuất thêm video-preview.mp4 đã ghép giọng đọc, để xem thử")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--wps", type=float, default=3.5)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("thiếu ffmpeg → sudo apt install -y ffmpeg")

    src = sources(a.results) / "narration.tsv"
    shots = a.results / "shots"
    if not src.exists():
        sys.exit(f"không thấy {src}")
    if not shots.is_dir():
        sys.exit(f"không thấy {shots} — chạy build-shots.py trước")

    texts = []
    for line in src.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        c = line.split("\t")
        if len(c) >= 2:
            texts.append(c[-1].strip())

    adir = a.results / "audio"
    real = {}
    if adir.is_dir():
        real = {f.stem.upper(): probe(f) for f in sorted(adir.iterdir())
                if f.suffix.lower() in AUDIO_EXT and f.stem.upper().startswith("S")}
    src_label = "audio thật" if real else "dự toán từ số từ"

    items, missing_img, total = [], [], 0.0
    for i, t in enumerate(texts, 1):
        sid = f"S{i:02d}"
        img = shots / f"{sid}.jpg"
        if not img.exists():
            missing_img.append(sid)
            continue
        d = real.get(sid, len(t.split()) / a.wps)
        items.append((img, d))
        total += d

    if not items:
        sys.exit("không có shot nào để ghép")

    # Concat demuxer: file cuối phải lặp lại một lần nữa, nếu không nó bị cắt mất.
    lst = a.results / "_concat.txt"
    with lst.open("w", encoding="utf-8") as f:
        for img, d in items:
            f.write(f"file '{img.resolve()}'\nduration {d:.3f}\n")
        f.write(f"file '{items[-1][0].resolve()}'\n")

    dest = a.out or (a.results / "export" / "video-track.mp4")
    dest.parent.mkdir(parents=True, exist_ok=True)
    w, h = (int(x) for x in a.size.lower().split("x"))
    if a.brand:
        if not a.brand.exists():
            sys.exit(f"không thấy ảnh nhận diện {a.brand}")
        bi = Image.open(a.brand).size
        bw = bi[0] * h // bi[1]
        sides = 2 if a.brand_side == "both" else 1
        cw = w - bw * sides              # bề ngang còn lại cho ảnh truyện
        if cw < 400:
            sys.exit(f"dải kênh {bw}px x{sides} chỉ chừa {cw}px cho ảnh truyện — quá hẹp")
        # Ảnh truyện co vừa vùng còn lại rồi pad ra đủ khung, sau đó dán dải kênh đè lên.
        # Làm theo thứ tự này thì không cần nguồn màu vô hạn của lavfi, khỏi lo video
        # bị kéo dài vô tận vì overlay chờ nguồn nền.
        offx = f"({cw}-iw)/2" if a.brand_side == "right" else f"{bw}+({cw}-iw)/2"
        vf = (f"[0:v]scale={cw}:{h}:force_original_aspect_ratio=decrease,"
              f"pad={w}:{h}:{offx}:(oh-ih)/2:{a.bg_color}[base];"
              f"[1:v]scale={bw}:{h}[br]")
        if a.brand_side == "both":
            # Dán cùng một ảnh hai bên: tách làm hai nhánh rồi chồng lần lượt.
            vf += (f";[br]split=2[brL][brR];"
                   f"[base][brL]overlay=0:0[one];"
                   f"[one][brR]overlay={w - bw}:0,format=yuv420p")
        else:
            brx = 0 if a.brand_side == "left" else w - bw
            vf += f";[base][br]overlay={brx}:0,format=yuv420p"
    elif a.fill == "black":
        vf = (f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
              f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p")
    else:
        # Trang manga là ảnh DỌC. Nhét vào khung ngang mà lấp đen thì hai bên trống
        # gần nửa màn hình. Lấy chính ảnh đó phóng to tràn khung rồi làm mờ làm nền,
        # ảnh gốc đặt nét ở giữa — cách các kênh kể truyện dài vẫn dùng.
        vf = (f"split=2[bg][fg];"
              f"[bg]scale={w}:{h}:force_original_aspect_ratio=increase,"
              f"crop={w}:{h},gblur=sigma=24,eq=brightness=-0.12[b];"
              f"[fg]scale={w}:{h}:force_original_aspect_ratio=decrease[f];"
              f"[b][f]overlay=(W-w)/2:(H-h)/2,format=yuv420p")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst)]
    if a.brand:
        cmd += ["-loop", "1", "-i", str(a.brand)]
    cmd += ["-filter_complex" if (a.brand or a.fill == "blur") else "-vf", vf,
            "-r", str(a.fps), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20"]
    if a.brand:
        cmd += ["-shortest"]             # ảnh kênh là nguồn lặp vô hạn, phải chặn lại
    cmd += [str(dest)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    lst.unlink(missing_ok=True)
    if r.returncode != 0:
        print(r.stderr[-1500:], file=sys.stderr)
        sys.exit("ffmpeg lỗi")

    mm = f"{int(total)//60}:{int(total)%60:02d}"
    size = dest.stat().st_size / 1e6
    print(f"{len(items)} shot · {mm} · {size:.1f} MB · độ dài lấy từ {src_label}")
    print(f"→ {dest}")
    if missing_img:
        print(f"(!) thiếu ảnh cho {len(missing_img)} shot: {', '.join(missing_img[:8])}")

    if a.with_audio:
        voice = a.results / "export" / "narration.mp3"
        if not voice.exists():
            print("(!) chưa có export/narration.mp3 — chạy concat-audio.py trước, "
                  "bỏ qua bước ghép tiếng")
            return 0
        prev = dest.with_name("video-preview.mp4")
        # copy luồng hình, không encode lại: nhanh và không mất chất lượng lần hai.
        mux = ["ffmpeg", "-y", "-i", str(dest), "-i", str(voice),
               "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
               "-map", "0:v:0", "-map", "1:a:0", str(prev)]
        r = subprocess.run(mux, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-1000:], file=sys.stderr)
            sys.exit("ffmpeg ghép tiếng lỗi")
        print(f"→ {prev}  (bản xem thử, đã có giọng đọc)")
    if not real:
        print("(!) chưa có audio — mốc là DỰ TOÁN. Đọc giọng rồi chạy lại để khớp thật.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
