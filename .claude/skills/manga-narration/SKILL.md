---
name: manga-narration
description: Viết lời kể dạng văn xuôi liền mạch cho video kể truyện, giọng kịch tính, mốc thời gian máy tự tính. Dùng sau khi user duyệt beat sheet, hoặc khi user nói "viết lời kể", "viết kịch bản".
---

# Viết lời kể

Chỉ chạy **sau khi user duyệt** `beat-sheet.md`.

## Đọc trước khi viết — đủ 4 tầng

1. `series/<BỘ>/series-bible.md` — tên, thuật ngữ, giọng, cụm CẤM dùng
2. `series/<BỘ>/voice-profile.md` — cách diễn đạt đã ăn, cụm đã bị gạch, nhịp đang chạy
3. **Lời kể của 2 chapter gần nhất** (`results/narration.tsv`) — bắt nhịp thật
4. `results/beat-sheet.md` của chapter đang làm

Nhiều hơn 2 chapter thì dùng `voice-profile.md` — nó là bản đúc kết. Đọc cả 50 chapter sẽ
vỡ context mà không giúp thêm.

## Ngân sách

Tốc độ đọc **3,5 từ/giây** cho giọng kể truyện (đo từ video mẫu thật; con số 2,6 chỉ đúng
cho clip phân tích ngắn). Một chapter webtoon ~50 trang cho ra **7–8 phút**. Muốn 10–12 phút
thì gom 2 chapter vào một video.

## Viết vào `results/narration.tsv` — 2 cột TAB

```
gợi ý trang<TAB>lời kể
P01	Lửa kín cả khung hình, không thấy trời cũng không thấy đất.
P07-P08	Tivi báo chiều tối có mưa, tiếp đó tới bản tin về...
```

Mỗi dòng là một đoạn ~5–12 giây. Cột trang là gợi ý ảnh, **không đọc lên**.

## Năm kỹ thuật làm lời có cảm xúc

1. **Phá vỡ độ dài câu** — câu ngắn nhất đặt đúng chỗ đau nhất, không rải đều.
2. **Hình ảnh vật lý thay nhãn cảm xúc** — đừng viết "cậu bé thấy tệ", cho thấy cái làm
   nên điều đó. Câu hay nhất thường là một chi tiết cụ thể, không phải tính từ.
3. **Chậm ở đỉnh, nén ở đoạn nối** — cảnh mua sắm một nhịp là đủ; đỉnh cảm xúc thì giãn ra.
4. **Nội tâm thay hành động** — nhân vật đang nghĩ gì, không chỉ làm gì.
5. **Đừng giải thích hộ người xem** — thay vì "cảnh này đổi nghĩa", liệt kê lại ba chi tiết
   để họ tự nối.

## Ba lỗi làm lời đọc lên nghe cứng

- **Tic liên từ** — "Rồi…", "Và…" mở quá 4% số câu là nghe thành nhịp máy.
- **Câu vụn dồn cục** — quá 2 câu cực ngắn liên tiếp là giật cục, không phải kịch tính.
- **Đổi cách gọi nhân vật liên tục** — chốt **một tên + một đại từ** cho người kể; các cách
  gọi khác chỉ dùng khi thuật lời nhân vật.

## Dựng bảng và kiểm

```bash
python3 scripts/build-narration.py series/<BỘ>/C<n>/results --wps 3.5
python3 scripts/check-narration.py series/<BỘ>/C<n>/results/narration.tsv
```

Linter phải **MƯỢT** mới sang bước sau. Nó bắt được thứ tai nghe ra mà không chỉ được tên.
Sửa lời thì sửa `narration.tsv` rồi chạy lại — **không sửa `narration.md`**, nó là file sinh ra.
