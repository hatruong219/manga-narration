---
name: manga-bible
description: Lập Series Bible cho một bộ manga — cách gọi tên, thuật ngữ, giọng kể, mốc cốt truyện đã tiết lộ. Làm MỘT LẦN cho cả bộ, trước khi làm chapter đầu tiên. Dùng khi user nói "lập bible", "bộ mới", "series mới", hoặc gửi ảnh một bộ chưa có series-bible.md.
---

# Series Bible

Chạy một lần cho mỗi bộ. Output là file tham chiếu cho MỌI chapter sau.

## Đầu vào

`series/{BỘ}/C*/pages/` của 1–2 chapter đầu. Không có ảnh thì hỏi user thả vào đâu, đừng đoán.

## Vai trò

Story Editor của kênh video kể manga.

## Nguyên tắc cứng

Chỉ ghi những gì **có bằng chứng trong ảnh**. Chỗ không chắc ghi `CHƯA RÕ`.
Tuyệt đối không suy đoán rồi ghi như thật — file này sẽ được dùng lại 50 chapter,
một cái tên sai ở đây là 50 video sai.

## Việc cần làm

1. Đọc hết ảnh trong `pages/` bằng tool Read (đọc **phải → trái, trên → dưới**).
2. Ghi ra `series/{BỘ}/series-bible.md` theo đúng cấu trúc dưới.
3. In ra 3 điểm `CHƯA RÕ` quan trọng nhất để user bổ sung.

## Cấu trúc output

```markdown
# SERIES BIBLE — {TÊN BỘ}

## 1. Cách gọi tên
| Tên gốc | Cách đọc trong video | Ghi chú (giới tính, vai vế, nhân vật khác gọi là gì) |

## 2. Thuật ngữ
| Thuật ngữ | Giữ nguyên / dịch | Bản dịch chốt | Giải thích 1 câu |

## 3. Giọng kể
- 3 tính từ mô tả văn phong
- 5 từ/cụm NÊN dùng
- 5 từ/cụm CẤM dùng (sáo rỗng, lệch tông)

## 4. Mốc cốt truyện đã tiết lộ
(để chapter sau không spoil sớm)

## 5. Thông số sản xuất
- Thời lượng video mục tiêu: {…} giây
- Tốc độ đọc chuẩn: 2,6 từ/giây
- Tỉ lệ khung: {9:16 dọc / 16:9 ngang}
```

## Xong thì

Nhắc user: `series/{BỘ}/voice-profile.md` bắt đầu rỗng và sẽ tự dày lên sau mỗi vòng
`/manga-qc`. Không cần điền tay.
