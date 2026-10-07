# Đọc chương bằng giọng Vbee — các lệnh

Giọng đang chọn: `hn_female_ngochuyen_full_48k-fhg` (HN - Ngọc Huyền).

## 1. Lấy token (làm 1 lần)

https://studio.vbee.vn/apps → **Tích hợp API** → **Tạo ứng dụng** → đặt tên →
chọn thời hạn token → **Tạo**. Trang đó cho ra **App ID** và **Token**.

## 2. Khai báo

```bash
export VBEE_TOKEN='<token vừa tạo>'
export VBEE_APP_ID='<app id vừa tạo>'
```

Thử một đoạn trước khi chạy cả chương:

```bash
cd ~/my-project/manga-narration
./scripts/tts-vbee.py truyen/TWB/results/C1/tts-lines/S01.txt /tmp/s01.mp3
ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/s01.mp3
```

Nghe thấy được thì đi tiếp. Không được thì dừng ở đây — lỗi Vbee in ra kèm mã.

## 3. Đọc cả chương

```bash
python3 scripts/tts-loop.py truyen/TWB/results/C1 --exec scripts/tts-vbee.py
```

- Đoạn nào đã có file trong `audio/` thì **bỏ qua**, không đọc lại, không tốn quota.
- Hết quota giữa chừng → script dừng, báo đoạn hỏng. Hôm sau chạy **y nguyên lệnh
  trên**, nó đọc tiếp đúng chỗ còn thiếu.
- `--dry-run` để xem nó định đọc những đoạn nào mà chưa gọi API.

Quota tiêu tới đâu xem ở `truyen/TWB/results/C1/vbee-usage.tsv`.

## 4. Ghép lại + khớp mốc thời gian

```bash
python3 scripts/concat-audio.py truyen/TWB/results/C1
python3 scripts/retime-from-audio.py truyen/TWB/results/C1
python3 scripts/build-video.py truyen/TWB/results/C1
```

`concat-audio.py` **từ chối ghép nếu thiếu đoạn** — không có chuyện ra file câm giữa chừng.

## Số liệu chương 1

| | |
|---|---|
| Số đoạn | 84 |
| Tổng ký tự | 7.342 |
| Đoạn dài nhất | S27 — 176 ký tự |
| Quota free | 3.000 ký tự/ngày → **3 ngày/chương** |

50 chương ≈ 367.000 ký tự ≈ 122 ngày quota free. Bản free không kham nổi cả bộ —
tính trước để khỏi làm nửa chừng rồi kẹt.

## Hai cái bẫy của API Vbee (đã xử trong script)

1. **Lỗi trả kèm HTTP 200.** Mã lỗi nằm trong thân JSON (`error_code`,
   `error_message`). Tin `%{http_code}` là tưởng thành công trong khi hỏng.
2. **POST không trả audio.** Nó trả `request_id` + `IN_PROGRESS`. Phải gọi
   `GET /api/v1/tts/<request_id>` tới khi `SUCCESS` mới có `audio_link`.
   **Link chỉ sống 3 phút** — script tải ngay, không hoãn.

Tài liệu bắt buộc `callback_url`, nhưng máy này không có webhook công khai nên
script gửi URL placeholder rồi tự poll. Có webhook thật thì:
`export VBEE_CALLBACK='https://...'`.

## Hết quota API giữa chừng — lối thoát: tự dán lên web Vbee (dùng point-pool lớn hơn)

Quota API là một **sub-cap riêng** bên trong tổng điểm đã mua, nhỏ hơn hẳn point-pool
dùng trên `studio.vbee.vn`. Khi API báo hết, vẫn còn điểm dùng được qua web — đây là
tài khoản trả phí của chính mình, không phải lách luật gì cả. Quy trình (user làm tay
phần dán/xuất, mình chỉ tự động hoá phần đổi tên/ghép):

1. Lấy nội dung cần đọc: `truyen/FRN/results/C<n>/narration-plain.txt` (đã tách đoạn
   bằng dòng trống, đúng thứ tự `tts-lines/Sxx.txt`).
2. User dán nguyên văn vào studio.vbee.vn — web tự tách khối theo dòng trống, khối thứ
   N tương ứng đúng `S0N`. Chọn giọng/tốc độ y hệt (`hn_female_ngochuyen_full_48k-fhg`,
   tốc độ 1.0), xuất **từng khối riêng** (không gộp) → tải về 1 file zip.
3. Giải nén, file trả về tên dạng `{số thứ tự}_{slug}_{uuid}.mp3.mp3`. Đổi tên về
   `S{NN}.mp3` (2 chữ số, khớp `tts-lines/`) rồi copy vào `truyen/FRN/results/C<n>/audio/`:

```bash
mkdir -p truyen/FRN/results/C<n>/audio
for f in /path/to/giai-nen/*.mp3; do
  n=$(basename "$f" | grep -oE '^[0-9]+')
  cp "$f" "truyen/FRN/results/C<n>/audio/S$(printf '%02d' "$n").mp3"
done
```

4. Kiểm nhanh số file khớp số đoạn, nghe thử 1-2 file đối chiếu với `narration-plain.txt`
   cùng số thứ tự (phòng lệch khối do dòng trống thừa/thiếu khi paste).
5. Chạy tiếp pipeline bình thường từ bước ghép: `concat-audio.py` → `retime-from-audio.py`
   → `build-video.py --with-audio` → `mix-bgm.py --gain -12` → `release.sh`.

Đã chạy thành công toàn chương C20 (70 đoạn) bằng cách này khi quota API cạn.

## Chỉnh giọng

```bash
export VBEE_VOICE='<mã giọng khác>'   # mặc định hn_female_ngochuyen_full_48k-fhg
export VBEE_SPEED='1.1'               # 0.1–1.9, một chữ số thập phân
export VBEE_BITRATE='128'             # 8|16|32|64|128
```

Danh sách giọng: `GET https://vbee.vn/api/public/v1/voices`, header `app-id: <APP_ID>`.
