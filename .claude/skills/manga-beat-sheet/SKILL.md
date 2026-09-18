---
name: manga-beat-sheet
description: Đọc hiểu toàn bộ ảnh chapter thành Beat Sheet — sự việc từng panel, cảm xúc, trọng số. CHƯA viết lời kể. Dừng chờ user duyệt. Dùng sau khi crawl xong, hoặc khi user nói "beat sheet", "đọc chapter".
---

# Beat Sheet — bước đọc hiểu

Bước này tồn tại **chỉ để chống lỗi**: nếu vừa đọc ảnh vừa viết lời trong một lượt, sẽ bịa
panel và hiểu sai vai nhân vật. **Việc ở đây là ĐỌC HIỂU, chưa viết lời kể.**

## Đọc từ đâu

`series/<BỘ>/C<n>/pages-clean/` — **không đọc `pages/`** (còn banner quảng cáo).
`clean-pages.py` chưa chạy thì chạy trước.

## Quy tắc đọc

- Đọc **hết mọi trang**, không nhảy cóc. Cú lật thường nằm ở trang cuối và nó **đổi nghĩa
  toàn bộ phần đầu** — đọc thiếu là hiểu sai vai nhân vật.
- Mỗi trang đánh số panel `P{trang}-a`, `P{trang}-b`… theo thứ tự đọc.
- Chỉ ghi những gì **THẤY trong ảnh**. Không suy diễn ngoài khung.
- Chữ mờ không đọc được: ghi `KHÔNG ĐỌC ĐƯỢC`, đừng đoán.
- Trang tiêu đề, trang trắng, trang quảng cáo sót lại: đánh dấu **BỎ**.

## Output → `results/beat-sheet.md`

```markdown
### A. Kiểm tra đầu vào
Liệt kê ảnh đã nhận. Thiếu trang liên tiếp → CẢNH BÁO và DỪNG.
Ghi rõ trang nào đã bị clean-pages cắt bao nhiêu px.

### B. Beat Sheet
| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |

Cột `Sự việc` viết bằng lời của mình — tóm tắt, không chép lại.
Cột thoại chỉ trích câu **đắt nhất** của panel, vài từ, và chỉ khi cần cho việc viết lời kể.
Trọng số 3 = khoảnh khắc quyết định · 1 = panel chuyển tiếp.

### C. Điểm cao trào
Có thể có NHIỀU đỉnh (một cảm xúc, một hành động). Ghi cả cú lật cuối nếu có.

### D. Chưa rõ
Tên chưa xuất hiện, quan hệ chưa rõ, chi tiết mơ hồ. **Không đoán bừa.**
```

## DỪNG Ở ĐÂY

In 3 câu hỏi duyệt: panel có thật không · tên nhân vật đúng chưa · trọng số hợp lý chưa.
**Không tự sang `/manga-narration`.**
