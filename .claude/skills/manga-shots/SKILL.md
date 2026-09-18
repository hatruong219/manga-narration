---
name: manga-shots
description: Cắt ảnh cho từng đoạn lời kể và kiểm bằng mắt. Dùng sau khi lời kể chốt, hoặc khi user nói "cắt ảnh", "shot", "ảnh theo đoạn".
---

# Cắt ảnh theo từng đoạn kể

Mỗi đoạn trong `narration.tsv` cần một hình. Mã `Sxx` dùng chung cho `shots/Sxx.jpg`,
`audio/Sxx.wav` và dòng trong `timeline.md`.

## KHÔNG tin detector panel

`detect-panels.py` chỉ để **đề xuất toạ độ biên**, không dùng để tự cắt. Đo thực tế trên
webtoon: cùng một bộ tham số cho trang này ra 1 panel (thật có 3), trang kia ra 6 (thật có 3).
Máng giữa panel không đủ tương phản. **Cắt tự động sai thì video sai khung mà không ai biết.**

## Quy trình

**1. Lấy biên đề xuất** cho các trang được dùng:
```bash
python3 scripts/detect-panels.py series/<BỘ>/C<n>/pages-clean/<file>.jpg
```

**2. Viết `results/shots.tsv`** — 6 cột TAB: `shot, trang, x0, y0, x1, y1` (`-1` = hết cỡ).
Chọn khung từ biên đề xuất + nội dung trang. Với webtoon cuộn dọc, hầu hết là **full width,
chỉ chọn dải y**.

**3. Cắt và kiểm:**
```bash
python3 scripts/build-shots.py series/<BỘ>/C<n>/results --sheet
```

**4. Đọc contact sheet ở `/tmp/shots-sheet-*.png` bằng tool Read.** Bắt buộc, không bỏ.

## Hai tầng kiểm, cả hai đều cần

| Tầng | Bắt được | Không bắt được |
|---|---|---|
| **Máy** — tỉ lệ khung | khung quá dẹt (>3.0) hoặc quá hẹp (<0.35) | nội dung sai |
| **Mắt** — contact sheet | khung ra sai cảnh so với lời kể | — |

Đo tỉ lệ pass **không có nghĩa là nội dung đúng**. Lần làm chapter đầu, audit hình học sạch
mà mắt vẫn bắt được 2 shot cắt ra sai hẳn cảnh.

Ngưỡng cho khung dọc 9:16: tỉ lệ **0.35–3.0** là dùng được. Dưới 0.35 là sliver; trên 3.0 là
dải ngang mỏng, nong thêm chiều cao cho đến khi tỉ lệ ≤ 2.0.

## Lệch một dải thường KHÔNG phải lỗi

Câu dẫn không có panel riêng ("người đó dừng lại giữa đường") dùng chung khung với câu kế
tiếp. Đó là bản chất format kể truyện, đừng churn.

## Xong thì
```bash
python3 scripts/build-shot-list.py series/<BỘ>/C<n>/results
```
Nó còn báo: shot liên tiếp trùng trang (phải đổi khung) và trang tải về mà không dùng
(có thể đã bỏ sót nội dung).
