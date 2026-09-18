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
./scripts/tts-vbee.py series/TWB/C1/results/tts-lines/S01.txt /tmp/s01.mp3
ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/s01.mp3
```

Nghe thấy được thì đi tiếp. Không được thì dừng ở đây — lỗi Vbee in ra kèm mã.

## 3. Đọc cả chương

```bash
python3 scripts/tts-loop.py series/TWB/C1/results --exec scripts/tts-vbee.py
```

- Đoạn nào đã có file trong `audio/` thì **bỏ qua**, không đọc lại, không tốn quota.
- Hết quota giữa chừng → script dừng, báo đoạn hỏng. Hôm sau chạy **y nguyên lệnh
  trên**, nó đọc tiếp đúng chỗ còn thiếu.
- `--dry-run` để xem nó định đọc những đoạn nào mà chưa gọi API.

Quota tiêu tới đâu xem ở `series/TWB/C1/results/vbee-usage.tsv`.

## 4. Ghép lại + khớp mốc thời gian

```bash
python3 scripts/concat-audio.py series/TWB/C1/results
python3 scripts/retime-from-audio.py series/TWB/C1/results
python3 scripts/build-video.py series/TWB/C1/results
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

## Chỉnh giọng

```bash
export VBEE_VOICE='<mã giọng khác>'   # mặc định hn_female_ngochuyen_full_48k-fhg
export VBEE_SPEED='1.1'               # 0.1–1.9, một chữ số thập phân
export VBEE_BITRATE='128'             # 8|16|32|64|128
```

Danh sách giọng: `GET https://vbee.vn/api/public/v1/voices`, header `app-id: <APP_ID>`.
