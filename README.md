# manga-narration — dây chuyền làm video kể manga

Từ **link chapter** → **lời kể**, **ảnh cắt theo từng đoạn**, **timeline khớp giọng đọc**.

Copy nguyên thư mục này đi đâu cũng chạy: chỉ cần Claude Code bản chuẩn + `python3` + `ffmpeg`.
Không phụ thuộc bộ truyện nào — `templates/` sinh ra file cấp bộ cho truyện bất kỳ.

## Bắt đầu một bộ mới

```bash
cd manga-narration
./scripts/new-chapter.sh <MÃ_BỘ> <số chapter>          # dựng thư mục + file cấp bộ
./scripts/pipeline.sh <MÃ_BỘ> <số chapter> '<url chapter>'
```

`pipeline.sh` chạy hết các bước **máy** và **dừng lại** ở mỗi bước cần AI, in tên skill phải gọi.
Chạy lại lệnh đó sau mỗi bước AI để đi tiếp.

## Phân vai: máy làm gì, AI làm gì

| Việc | Ai làm | Vì sao |
|---|---|---|
| Tải ảnh, bỏ banner quảng cáo | **máy** | phép đo, không phán đoán |
| Đọc hiểu chapter → beat sheet | **AI** | phải hiểu mới biết panel nào quan trọng |
| Viết lời kể | **AI** | ngôn ngữ |
| Tính mốc thời gian | **máy** | phép chia; sửa một chữ là mọi mốc sau đổi |
| Bắt lỗi đọc lên (tic, câu vụn, giật cục) | **máy** | phép đếm — tai nghe ra nhưng không chỉ được tên |
| Chấm hook, nhịp, giọng | **AI (subagent mắt mới)** | thẩm mỹ |
| Chọn khung cắt ảnh | **AI** | detector panel không đủ tin, xem dưới |
| Kiểm khung cắt đúng cảnh chưa | **AI (mắt)** | đo tỉ lệ không bắt được nội dung sai |
| Đo thời lượng audio thật | **máy** | ffprobe |

Nguyên tắc: **giao cho máy mọi thứ đếm được.** LLM đếm từ sai thường xuyên và hay báo PASS
cho thứ lệch 30%.

## Tám skill

| Skill | Việc | Dừng lại? |
|---|---|---|
| `/manga-crawl` | tải + làm sạch ảnh | kiểm mắt trang đầu/cuối |
| `/manga-bible` | Series Bible — **1 lần cho cả bộ** | — |
| `/manga-beat-sheet` | đọc HẾT ảnh → beat sheet | **có** — chờ user duyệt |
| `/manga-narration` | beat sheet → lời kể văn xuôi | tự chạy linter |
| `/manga-qc` | linter + subagent mắt mới | cập nhật voice-profile |
| `/manga-shots` | chọn khung cắt + kiểm mắt | **có** — đọc contact sheet |
| `/manga-voice` | TTS + re-time theo audio thật | chờ bạn đọc giọng |
| `/manga-package` | tiêu đề, mô tả, thumbnail | — |

## Bốn bài học đã trả giá — đừng làm lại

**1. Ngân sách từ là 3,5 từ/giây, không phải 2,6.**
Đo từ video kể truyện thật. Con số 2,6 chỉ đúng cho clip phân tích ngắn. Một chapter webtoon
~50 trang cho ra 7–8 phút; muốn 10–12 phút thì gom 2 chapter.

**2. Detector panel không dùng để tự cắt ảnh.**
Cùng bộ tham số: trang này ra 1 panel (thật có 3), trang kia ra 6 (thật có 3). Máng giữa
panel của webtoon không đủ tương phản. Nó chỉ để **đề xuất toạ độ biên**; chọn khung là người.

**3. Audit hình học pass ≠ nội dung đúng.**
Làm chapter đầu: đo tỉ lệ sạch 84/84, nhưng mắt vẫn bắt được 2 shot cắt ra sai hẳn cảnh so
với lời kể. **Bắt buộc đọc contact sheet.**

**4. "Chưa mượt" đo được.**
Tai nghe ra mà không chỉ được vì sao. `check-narration.py` chỉ đúng trong 5 giây: tic liên từ
mở 10% số câu, 27% câu cực ngắn, 4 câu vụn liên tiếp, đổi cách gọi nhân vật 72% số lần.

## Script

```bash
python3 scripts/crawl-chapter.py '<url>' --bo TWB      # tải ảnh, tự dựng scaffold
python3 scripts/clean-pages.py truyen/TWB/prepare/C1/pages     # bỏ banner quảng cáo
python3 scripts/build-narration.py .../results --wps 3.5
python3 scripts/check-narration.py .../prepare/C<n>/narration.tsv   # linter độ mượt
python3 scripts/build-shots.py .../results --sheet     # cắt ảnh + contact sheet
python3 scripts/build-shot-list.py .../results         # nối lời ↔ ảnh
python3 scripts/retime-from-audio.py .../results       # mốc theo audio thật
python3 scripts/detect-panels.py <ảnh> --preview       # đề xuất biên, KHÔNG tự cắt
python3 scripts/tts-loop.py .../results --exec scripts/tts-vbee.py  # đọc bằng Vbee
python3 scripts/concat-audio.py .../results            # ghép 84 file thành 1 mp3
```

## File nguồn sự thật — sửa ở đây, đừng sửa file sinh ra

| Nguồn | Sinh ra |
|---|---|
| `narration.tsv` | `narration.md`, `narration-tts.txt` |
| `shots.tsv` | `shots/Sxx.jpg` |
| `narration.tsv` + `audio/` | `timeline.md` |
| `narration.tsv` + `beat-sheet.md` | `shot-list.md` |

Mã `Sxx` dùng chung cho `shots/Sxx.jpg`, `audio/Sxx.wav` và dòng trong `timeline.md`.

## Cấu trúc

```
manga-narration/
├── .claude/skills/       8 skill (nhận khi cwd trong project)
├── scripts/              10 script + paths.py (một chỗ duy nhất biết thư mục nằm đâu)
├── templates/            file cấp bộ cho truyện mới
├── archive/              bộ đã cất kho — giữ phần chữ, ảnh bị .gitignore
└── truyen/<BỘ>/
    ├── series-bible.md   tên, thuật ngữ, giọng — 1 lần cho cả bộ
    ├── voice-profile.md  tích luỹ sau mỗi QC ← trái tim của việc giữ giọng
    ├── tts-pronounce.tsv map phát âm cho giọng máy
    ├── tracker.csv       chapter | crawl | beat_sheet | narration | qc | shots | audio | dung | ngay_dang
    │
    ├── prepare/C<n>/     NGUYÊN LIỆU — sửa tay, không sinh lại được
    │   ├── pages/        ảnh gốc
    │   ├── pages-clean/  đã bỏ banner ← ĐỌC CÁI NÀY
    │   └── beat-sheet.md   narration.tsv   shots.tsv    ← nguồn sự thật
    │
    └── results/C<n>/     THÀNH PHẨM — xoá đi chạy lại là có
        ├── narration.md    narration-tts.txt   narration-plain.txt
        ├── shot-list.md    timeline.md         qc-report.md
        ├── shots/          Sxx.jpg
        ├── audio/          Sxx.wav
        └── export/         narration.mp3  video-track.mp4
```

## Cần cài

```bash
sudo apt install -y ffmpeg
pip3 install --user --break-system-packages curl_cffi numpy pillow
```

**Máy không có `pip`** (một số bản Python 3.14 không kèm): dựng venv bằng `uv` rồi gọi
python trong đó, ĐỪNG gọi `python3` trần — `python3` hệ thống không có thư viện nào:

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python curl_cffi numpy pillow
.venv/bin/python scripts/crawl-chapter.py ...      # dùng đường dẫn này cho MỌI script
```

Ai (hoặc agent nào) chạy `python3 scripts/...` trên máy như vậy sẽ thấy `ModuleNotFoundError`
và dễ kết luận nhầm là máy thiếu PIL/numpy. Có đủ cả, chỉ nằm trong `.venv`.

`curl_cffi` không thay được bằng `requests`: CDN ảnh fingerprint **TLS handshake**, không
phải header. curl kèm header browser đầy đủ vẫn ăn 403.

## Giới hạn đã biết

- **`clean-pages.py` chỉ bỏ banner ở trang ĐẦU và trang CUỐI.** Banner giữa chapter không bắt
  được. Luật trang cuối đòi vùng bão hoà bắt đầu từ 60% chiều cao trở xuống — chapter nào có
  trang cuối kết bằng panel màu nằm dưới mốc đó sẽ bị cắt lố. **Kiểm mắt trang cuối.**
- **Watermark của site tổng hợp** nằm chồng lên tranh, script không xử được. Crop mép trên khi dựng.
- **Linter không phân biệt lời người kể với lời nhân vật được thuật lại** — mục "đổi cách gọi"
  chỉ là cảnh báo, người phải tự đọc và phán.
- `check-narration.py` tách từ bằng khoảng trắng. Đúng với tiếng Việt, sai với ngôn ngữ không
  tách từ bằng dấu cách.
- Ảnh nguồn hẹp (~580px) vẫn đọc được **nếu là webtoon chữ to**; manga nhiều panel nhỏ thì không.
- Manga có bản quyền, và bản scan trên site tổng hợp là bản không có license. Chính sách mỗi
  nền tảng mỗi khác — kiểm trước khi làm cả series.
