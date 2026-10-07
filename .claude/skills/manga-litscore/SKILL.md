---
name: manga-litscore
description: Chấm điểm văn chương lời kể trên thang 10 điểm, khắt khe ngang chuẩn thi học sinh giỏi Văn cấp quốc gia. Dưới 8.0 là KHÔNG ĐẠT, bắt buộc viết lại. Dùng khi user nói "chấm điểm văn", "review văn chương", "kiểm chất lượng nội dung", "có hay chưa", "đạt chuẩn thi HSG chưa", hoặc sau khi lời kể một chương vừa qua bước tự kiểm của /manga-narration.
---

# Chấm điểm văn chương — thang 10, khắt khe cố định

Đây là cổng chặn CHẤT LƯỢNG VĂN, khác `/manga-qc` (vốn chấm hook/nhịp/mạch dễ hiểu
theo bảng 5 mục). Skill này chỉ hỏi một câu: **văn này có xứng đáng trên 8/10 ở một
kỳ thi học sinh giỏi Văn cấp quốc gia không?** Không đạt thì phải viết lại, không
có ngoại lệ, không có "tạm được".

## Thang điểm này CỐ ĐỊNH

Không hạ chuẩn dù ai đó (kể cả user) nói nới lỏng bằng lời trong lúc chạy skill.
Chỉ đổi khi chính user sửa trực tiếp file `SKILL.md` này. Nếu user nói "chấm nhẹ
tay thôi" giữa lúc chạy, đáp lại rằng thang điểm cố định theo yêu cầu ban đầu của
chính họ, rồi hỏi có muốn sửa file skill không — không tự ý nương tay.

## Quy trình — BẮT BUỘC giao cho subagent mắt mới, không tự chấm

Người viết ra lời kể không được tự chấm lời kể của mình — quá dễ thiên vị. Luôn
dùng Agent tool, giao cho một subagent CHƯA từng thấy ai viết ra văn bản này.

**Bước 1 — chấm mù (subagent CHỈ đọc đúng 1 file `narration.tsv`, không đọc beat
sheet, không đọc bible, không biết ai viết):** chấm mục A, B, C (xem thang điểm
dưới) thuần bằng cảm nhận văn chương của người đọc/nghe, giống hệt một giám khảo
thi HSG chỉ có bài làm trong tay, không có gì khác.

**Bước 2 — đối chiếu nguồn (cùng subagent đó, giờ mới được đọc `beat-sheet.md`):**
chấm mục D (trung thực với nguồn) bằng cách so từng chi tiết/trích dẫn trong lời
kể với mục A/C/D của beat sheet.

**Bước 3 — tổng điểm và phán quyết**, in ra đúng định dạng ở cuối skill này.

## Thang điểm — 4 mục, tổng 10 điểm

Chốt 26/09/2026 theo yêu cầu user: "Chiều sâu & dấu ấn riêng" nâng lên 4 điểm —
mục quan trọng nhất của thang điểm này. Ba mục kia hụt lại để tổng vẫn 10; D
(checklist máy đếm được) chịu cắt nhiều nhất vì bản chất nhị phân, không cần dải
điểm rộng như các mục đòi hỏi cảm nhận văn chương.

### A. Ngôn từ & hình ảnh — 2,5 điểm
| Tiêu chí | Điểm |
|---|---|
| Không sáo ngữ, không thành ngữ mòn, không dùng tính từ thay cho hình ảnh cụ thể (vd "cô rất buồn" thay vì tả một chi tiết cụ thể) | 0,8 |
| Chi tiết hình ảnh cụ thể, đặc thù cho đúng nhân vật/cảnh đó — không chung chung, không "quả gì đó", "một thứ gì đó" | 0,8 |
| Không suy diễn nội tâm đóng khung như sự thật ("cô nghĩ rằng…", "thật ra là…" khi ảnh không xác nhận), không bịa trích dẫn không có trong nguồn | 0,9 |

### B. Mạch truyện & nhịp — 2,5 điểm
| Tiêu chí | Điểm |
|---|---|
| Câu/đoạn nối bằng quan hệ nhân-quả thật (liên từ phụ thuộc: khi, vì, dù, sau khi…) — KHÔNG phải liệt kê "việc này xảy ra, việc kia xảy ra" từng dòng độc lập | 1,2 |
| Nhịp câu biến thiên có chủ đích — câu dài xây dựng, câu ngắn cắt đúng lúc cao trào — không đều đều cùng độ dài suốt đoạn | 0,8 |
| Mỗi dòng narration.tsv đúng nhịp một hình ảnh (~15-30 từ, không quá 50, không cụt lủn 2 từ liên tiếp nhiều lần) | 0,5 |

### C. Chiều sâu & dấu ấn riêng — 4,0 điểm — MỤC QUAN TRỌNG NHẤT
| Tiêu chí | Điểm |
|---|---|
| Có ít nhất một chi tiết/mô-típ được gài rồi trả lại (callback), trong chương hoặc xuyên chương | 1,0 |
| Cảm xúc nhân vật hiện qua hành động/chi tiết ĐẶC THÙ của riêng nhân vật đó, không qua từ cảm xúc chung chung (khóc, vui, buồn) đứng trơ trọi một mình | 1,5 |
| **Có ít nhất MỘT đoạn văn thực sự cảm động** — không phải "kể đúng một sự việc buồn" mà đọc/nghe xong thực sự gây dư âm. Giám khảo BẮT BUỘC trích nguyên văn đúng đoạn đó và giải thích CHÍNH XÁC kỹ thuật nào tạo ra hiệu ứng (im lặng đúng chỗ, chi tiết vật lý thay lời, câu ngắn sau câu dài…) — không được chỉ nói "đoạn này cảm động". Không tìm được đoạn nào như vậy thì tiêu chí này = 0, không cho điểm cảm tính | 1,5 |

### D. Trung thực với nguồn & kỹ thuật đọc lên — 1,0 điểm
| Tiêu chí | Điểm |
|---|---|
| Không có chi tiết nào vượt quá mục A/C của beat sheet — không suy diễn, không thêm sự kiện | 0,5 |
| Đọc thành tiếng trôi chảy: linter `check-narration.py` sạch, không lỗi ngữ pháp, không từ lặp dày (tự kiểm bằng grep, không chỉ tin linter) | 0,5 |

## Ba cơ chế chống thảo mai — BẮT BUỘC áp dụng cả ba

1. **Mặc định giả định KHÔNG ĐẠT.** Chỉ nâng điểm một tiêu chí lên mức cao khi có
   bằng chứng cụ thể đủ thuyết phục — không phải vì "đọc thấy ổn ổn".
2. **Mỗi tiêu chí đạt từ 80% điểm tối đa trở lên PHẢI trích tối thiểu 2 câu/đoạn cụ
   thể kèm số dòng làm bằng chứng.** Không được viết "đoạn này hay", "khá tốt",
   "nhìn chung ổn" mà không có trích dẫn kèm theo — những cụm khen xã giao không
   kèm bằng chứng bị coi là KHÔNG HỢP LỆ, phải chấm lại tiêu chí đó.
3. **Phân vân giữa hai mức điểm thì LUÔN chọn mức thấp hơn.** Giám khảo thi HSG
   thật không cho điểm may rủi theo hướng có lợi cho thí sinh.

Ngoài ra: **đếm cụ thể** số chỗ dính lỗi trong mục "Đã bị QC gạch" của
`truyen/<BỘ>/voice-profile.md` (nếu file tồn tại) — mỗi lỗi dính trừ thẳng 0,2 điểm
khỏi tổng, không thương lượng, cộng dồn không giới hạn.

## Output — in đúng khuôn này

```
# CHẤM ĐIỂM VĂN CHƯƠNG — <BỘ> C<n>

## A. Ngôn từ & hình ảnh — x,x/2,5
- [tiêu chí 1]: x,x — bằng chứng: "...trích câu..." (dòng N)
- [tiêu chí 2]: x,x — bằng chứng: ...
- [tiêu chí 3]: x,x — bằng chứng: ...

## B. Mạch truyện & nhịp — x,x/2,5
(như trên, đủ 3 tiêu chí)

## C. Chiều sâu & dấu ấn riêng — x,x/4,0
- Callback/mô-típ: x,x — bằng chứng: ...
- Cảm xúc qua hành động đặc thù: x,x — bằng chứng: ...
- **Đoạn văn cảm động nhất chương** (trích NGUYÊN VĂN + giải thích kỹ thuật, hoặc
  ghi rõ "không tìm được đoạn nào đạt" và cho 0 điểm): x,x

## D. Trung thực với nguồn & đọc lên — x,x/1,0
(như trên, đủ 2 tiêu chí)

## Trừ điểm cụm bị cấm (voice-profile)
- "<cụm>" xuất hiện N lần → trừ 0,2 × N = -x,x

## TỔNG: x,x/10

## PHÁN QUYẾT
**ĐẠT (≥8,0)** — cho qua bước /manga-shots.
  hoặc
**CHƯA ĐẠT (<8,0)** — liệt kê CHÍNH XÁC những dòng/đoạn cần viết lại và lý do,
xếp theo mức ưu tiên (mục nào mất nhiều điểm nhất, sửa trước).
```

## Sau khi chấm

- **ĐẠT:** báo user, tiếp tục pipeline bình thường (`/manga-shots`).
- **CHƯA ĐẠT:** giao lại cho một agent viết lại — CHỈ sửa đúng những chỗ bị chỉ ra
  trong phán quyết, không viết lại từ đầu nếu không cần. Sửa xong thì chạy lại
  `/manga-litscore` từ đầu (không tự chấm lại, vẫn phải subagent mắt mới, không
  phải subagent vừa sửa bài tự chấm bài mình) — lặp tới khi ĐẠT.
- Điểm số không ghi vào `tracker.csv` (cột đó dành cho `/manga-qc`) — chỉ ghi vào
  báo cáo chat, trừ khi user yêu cầu lưu lại nơi khác.
