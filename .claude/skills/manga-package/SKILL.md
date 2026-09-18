---
name: manga-package
description: Xuất 3 phương án đóng gói cho video đã dựng — tiêu đề, mô tả, brief thumbnail, từ khoá. Dùng khi user nói "đóng gói", "tiêu đề", "thumbnail", "đăng video".
---

# Đóng gói và đăng

## Đọc trước

- `results/script.md` (bản đã QC)
- `series/{BỘ}/voice-profile.md` — mục "Hook đã dùng": tiêu đề **không lặp mô-típ** đã dùng
- Tiêu đề 3–5 chapter gần nhất (grep `results/package.md` của chúng) — tránh ra một loạt
  tiêu đề giống nhau, người xem sẽ tưởng video trùng

## Output → `results/package.md`

3 phương án, mỗi phương án gồm:

- **Tiêu đề** tối đa 60 ký tự, gây tò mò nhưng **KHÔNG nói sai nội dung**
- **3 dòng mô tả đầu** (phần hiện trước nút "xem thêm")
- **Brief thumbnail**: dùng panel nào · chữ trên ảnh tối đa 5 từ · biểu cảm nhân vật
- **5 từ khoá**

Sắp theo thứ tự bạn cho là hiệu quả nhất, nói lý do trong 1 câu.

## Xong thì

Đánh `x` cột `dung`, điền ngày vào cột `ngay_dang` trong `series/{BỘ}/tracker.csv`.
Xem chỗ tắc: `column -s, -t series/{BỘ}/tracker.csv`

## Lưu ý bản quyền

Manga có bản quyền. Video an toàn hơn khi nội dung **thêm giá trị** — phân tích chiến thuật,
bình luận tâm lý nhân vật, so sánh với arc trước — chứ không phải đọc lại nguyên chapter trên
nền ảnh gốc. Nếu kịch bản đang nghiêng về kể lại thô, nói thẳng với user ở bước này.
Chính sách mỗi nền tảng mỗi khác — kiểm trước khi làm cả series.
