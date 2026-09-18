---
name: manga-qc
description: QC lời kể hai vòng — vòng máy chạy linter độ mượt, vòng nội dung chạy bằng subagent mắt mới. Cập nhật voice-profile sau khi xong. Dùng khi user nói "QC", "kiểm lời kể", "review".
---

# QC hai vòng

## Vòng 1 — máy

```bash
python3 scripts/check-narration.py series/<BỘ>/C<n>/results/narration.tsv
```

Bắt: tic liên từ · câu vụn · giật cục · số viết thành chữ quá dài · đổi cách gọi nhân vật.
**Đừng tự kiểm mấy mục này bằng cách đọc** — chúng là phép đếm. Phải **MƯỢT** mới sang vòng 2.

## Vòng 2 — subagent mắt mới

Spawn **một subagent `general-purpose`**, đưa **CHỈ**:
- toàn văn `narration.md`
- mục Giọng kể của `series-bible.md`
- mục "Đã bị QC gạch" của `voice-profile.md`

Không đưa beat sheet, không đưa lịch sử hội thoại, không nói ai viết. Nó phải xem lần đầu —
đó là toàn bộ giá trị của vòng này.

Yêu cầu nó chấm 1-5 và tìm lỗi ở: **hook 15 giây đầu · nhịp lên đỉnh · giọng có đúng quy ước ·
người chưa đọc truyện có theo được không · đọc thành tiếng có trẹo không · có suy diễn hay
thổi phồng không**. Kết thúc bằng một bản đã sửa.

### Đừng nuốt trọn kết quả subagent

Nó **không được xem ảnh**. Mọi câu thoại nó "trích" đều là nó tự dựng lại — **phải đối chiếu
trang thật** trước khi đưa vào. Nhận xét về giọng và mạch thì tin được; sự thật với nguồn thì không.

## Sau khi có kết quả

1. Ghi nhận xét + điểm vào `results/qc-report.md`
2. Sửa lời trong `narration.tsv`, chạy lại `build-narration.py` rồi `check-narration.py`
3. **Cập nhật `series/<BỘ>/voice-profile.md`** — bước dễ bỏ nhất và là lý do file đó tồn tại:
   - hook đã dùng + mô-típ, để chapter sau không lặp
   - cụm bị gạch kèm lý do
   - cách diễn đạt được chấm cao
   - nhịp đang chạy (từ/câu, giây/đoạn, phân bố hiệu ứng)
4. Đánh `x` cột `qc` trong `tracker.csv`

Bỏ bước 3 thì chapter sau mắc đúng lỗi cũ. Cả cơ chế "giọng ngày càng xịn" nằm ở đó.
