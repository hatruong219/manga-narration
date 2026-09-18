---
name: manga-voice
description: Hướng dẫn đọc giọng máy và chỉnh mốc hình theo audio thật bằng ffprobe. Dùng sau khi QC xong, hoặc khi user nói "TTS", "giọng đọc", "re-time", "audio xong rồi".
---

# Giọng đọc và re-time

**Audio thật là nguồn chân lý, không phải bảng mốc.** Mốc trong `narration.md` chỉ là dự
toán từ số từ. Có giọng rồi thì chỉnh timeline **hình** theo audio — đừng cắt chữ cho vừa mốc.

## 1. Bản đọc

`results/narration-tts.txt` do `build-narration.py` sinh ra, mỗi dòng `[Sxx] <lời>`.

Trước khi đọc cả chapter, **đọc thử 1 đoạn có tên riêng** để nghe máy phát âm. Sai thì sửa
`series/<BỘ>/tts-pronounce.tsv` (2 cột TAB: từ gốc → cách viết cho TTS) rồi chạy lại.

Script chỉ **báo** chứ không tự đổi số thành chữ: `16.820 yên`, `chương 1`, `trang 3` đọc
khác nhau hoàn toàn, máy đoán sai còn tệ hơn người sửa tay.

## 2. User đọc ra file

Từng đoạn một file: `results/audio/S01.wav`, `S02.wav`… Một file chung thì không re-time được.

## 3. Re-time

```bash
python3 scripts/retime-from-audio.py series/<BỘ>/C<n>/results
python3 scripts/retime-from-audio.py series/<BỘ>/C<n>/results --durations S01=4.2 S02=9.8
```

Xuất `timeline.md`: mốc thật, ảnh `shots/Sxx.jpg`, lời kể. Còn báo shot dài quá 14 giây —
một hình đứng yên lâu vậy sẽ chán, thêm zoom chậm hoặc tách khung.

Cần `ffmpeg`: `sudo apt install -y ffmpeg`

## 4. Thứ tự dựng

1. Thả **toàn bộ audio** lên timeline trước
2. Thả `shots/Sxx.jpg` theo mốc trong `timeline.md`
3. Zoom chậm cho shot dài
4. SFX và nhạc nền
5. Phụ đề

| Mục | Giá trị |
|---|---|
| Khung | 1080×1920 dọc |
| FPS | 30 |
| Giọng đọc | đỉnh −3 dB |
| Nhạc nền | −18 đến −22 dB |

Nhạc vào/ra là một nửa phần cảm xúc và không nằm trong chữ. Đỉnh cảm xúc thì nhạc dâng;
cú lật lạnh thì **tắt hẳn về im lặng**.
