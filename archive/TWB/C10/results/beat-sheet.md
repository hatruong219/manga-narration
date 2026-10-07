# BEAT SHEET — Twilight Blade C10

Nguồn ảnh: `series/TWB/C10/pages-clean/`
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **🚫 DỪNG — BẢN CRAWL KHÔNG CÓ NỘI DUNG TRUYỆN. 0/12 trang dùng được.**

---

### A. Kiểm tra đầu vào

**⚠ CẢNH BÁO NẶNG: chapter này chưa hề được tải về. Không có một panel truyện nào.**

Đã nhận đủ 12 file `TWB_C10_P01`–`P12`, số trang liên tục, không đứt quãng tên file.
Nhưng **nội dung bên trong cả 12 file đều không phải truyện**. Đã mở và đọc từng ảnh một
theo đúng thứ tự P01 → P12, không nhảy cóc. Kết quả:

| Trang | Kích thước | Nội dung THẤY trong ảnh | Kết luận |
|---|---|---|---|
| P01 | 1080×1500 | Banner quảng cáo TRUYENQQQ.COM (hồng) + dòng promo + nửa trên khung placeholder | **BỎ** |
| P02 | 1080×1028 | Đuôi chữ "TẢI LÊN", "Vui lòng chờ 1-2p nữa vào đọc lại sẽ có ảnh", NetTruyen.Link / .Party | **BỎ** |
| P03 | 1080×1500 | Nguyên khung "NetTruyen13s.com — CHAPTER ĐANG ĐƯỢC TẢI LÊN" | **BỎ** |
| P04 | 1080×420 | Dải trống, chỉ có nền xanh lá nhạt, không chữ không hình | **BỎ** |
| P05 | 1080×1500 | **Trùng khít P03** | **BỎ** |
| P06 | 1080×420 | **Trùng khít P04** | **BỎ** |
| P07 | 1080×1500 | **Trùng khít P03** | **BỎ** |
| P08 | 1080×420 | **Trùng khít P04** | **BỎ** |
| P09 | 1080×1500 | **Trùng khít P03** | **BỎ** |
| P10 | 1080×420 | **Trùng khít P04** | **BỎ** |
| P11 | 1080×1500 | Khung placeholder như P03 (khác P03 vài byte do nén lại) | **BỎ** |
| P12 | 1080×1028 | Đuôi khung placeholder + banner quảng cáo TRUYENQQQ.COM (xanh) ở ĐÁY | **BỎ** |

**Bằng chứng trùng lặp — kiểm bằng md5, không phải nhìn bằng mắt:**

```
4a013012bd2edd73c820c6b03ba6ae3b  P03 = P05 = P07 = P09
5b42cc2a3fcc46f957831a8de60a16e1  P04 = P06 = P08 = P10
```

Bốn cặp trang giữa là **cùng một file lặp lại 4 lần**, giống nhau đến từng byte.
Thực chất cả chapter chỉ là **một ảnh placeholder duy nhất của site NetTruyen được lặp
6 lần rồi cắt đôi**, kẹp giữa hai banner quảng cáo ở P01 và P12.

**Nguyên nhân: lỗi ở khâu crawl, không phải khâu clean.**
Đã so `pages/` (ảnh thô) với `pages-clean/`: hai cặp md5 trùng lặp **đã có sẵn trong
`pages/`**. Tức là lúc `crawl-chapter.py` chạy, site đang trả về trang chờ
"CHAPTER ĐANG ĐƯỢC TẢI LÊN" — chapter 10 khi đó **chưa upload xong**, crawler vẫn tải
và lưu lại đúng cái trang chờ đó.

**Lỗi phụ — `clean-pages.py` cắt 0 px trên toàn bộ 12 trang.**
Kích thước `pages/` và `pages-clean/` **giống hệt nhau từng trang** (P01 1080×1500 →
1080×1500, P12 1080×1028 → 1080×1028, …). Banner quảng cáo ở P01 và P12 **vẫn còn nguyên**
trong `pages-clean/`. Luật A/B của script dò dải mỏng-sáng chữ đen trên nền trắng; ảnh
chapter này nền xanh lá nhạt và banner không có dải promo trắng phía dưới theo đúng
khuôn mẫu C1, nên không luật nào khớp. **Cần sửa/chạy lại sau khi có ảnh thật** — nhưng
đây là vấn đề thứ yếu, chữa xong cũng không đẻ ra nội dung.

**So với các chapter đã làm:** C1 = 53 trang, C3 = 58 trang. C10 "12 trang" không phải
chapter ngắn bất thường — nó **không phải chapter**. Con số 12 chỉ là số lát cắt của ảnh
báo lỗi.

**→ VIỆC CẦN LÀM TRƯỚC KHI ĐI TIẾP:** chạy lại `scripts/crawl-chapter.py` cho C10 khi
site đã upload xong, rồi chạy `clean-pages.py`, rồi mới làm lại beat sheet. Nên thêm
một bước kiểm tra vào crawler: **phát hiện trang trùng md5 và phát hiện chữ "ĐANG ĐƯỢC
TẢI LÊN" thì báo lỗi ngay thay vì lưu**.

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| — | — | **KHÔNG CÓ PANEL TRUYỆN NÀO ĐỂ GHI.** Cả 12 trang đều là trang chờ của site + quảng cáo, đã đánh dấu BỎ toàn bộ ở mục A. | — | — | — |

**Tổng số panel truyện đọc được: 0.**

Không ghi beat suy đoán. Không có nhân vật nào của Twilight Blade (Yojin, Hikari, Kenta)
xuất hiện trong bất kỳ trang nào. Các nhân vật thấy trên banner quảng cáo ở P01 và P12 là
**nhân vật của bộ khác** (banner tổng hợp của site) — **không được tính là nội dung chapter**.

---

### C. Điểm cao trào

**Không xác định được.** Không có sự kiện nào trong ảnh để xếp đỉnh.

Yêu cầu ban đầu có nói cú lật thường nằm ở trang cuối và đổi nghĩa toàn bộ phần đầu —
đã kiểm riêng **P12** với giả định đó. **P12 không có cú lật**: nửa trên là phần đuôi của
khung placeholder, nửa dưới là banner quảng cáo TRUYENQQQ.COM nền xanh. Không có khung
truyện, không có thoại, không có "CÒN TIẾP…".

---

### D. Chưa rõ

Ở bản crawl này **mọi thứ về nội dung C10 đều chưa rõ** — dưới đây là những câu hỏi đang
để ngỏ, ghi lại để lần crawl sau biết cần trả lời gì. **Không đoán bừa bất cứ mục nào.**

- **Toàn bộ nội dung C10** — cốt truyện, số panel thật, có bao nhiêu trang thật: chưa rõ.
- **Tên chương C10**: chưa rõ. Trang tiêu đề chưa tải về được.
- **C10 có bao nhiêu trang thật**: chưa rõ. Suy từ C1 (53) và C3 (58) thì con số thật
  nhiều khả năng lớn hơn 12 rất nhiều, nhưng **đây là suy đoán, không phải dữ liệu** —
  không được dùng làm căn cứ.
- Các mốc còn treo từ series bible, chưa biết C10 có động tới hay không:
  - Yojin làm cho tổ chức nào, ai ra chỉ thị nhiệm vụ.
  - Vì sao Hikari có **thể chất đặc biệt** thu hút **oán hồn**.
  - Hikari đã biết mình bị **giám sát như nhân tố có nguy cơ gây thảm hoạ** chưa.
  - Mắt Yojin đỏ ở C1 P01 là hiệu ứng màu hay một trạng thái khi dùng thuật.
- Không rõ site có bản C10 đầy đủ ở thời điểm hiện tại hay không, hay chapter thật sự
  chưa đăng. Cần mở link chapter kiểm tra bằng mắt trước khi crawl lại.

---

## DỪNG Ở ĐÂY

Không sang `/manga-narration`. Không viết lời kể. Với bản crawl này thì **không có gì để kể** —
viết tiếp là bịa nguyên một chapter.

**Ba câu hỏi duyệt:**

1. **Panel có thật không?** — Không. 0/12 trang có nội dung truyện; 4 cặp trang trùng nhau
   đến từng byte. Anh xác nhận giúp là bản crawl này hỏng chứ không phải em đọc sót ảnh?
2. **Tên nhân vật đúng chưa?** — Không có nhân vật nào để đối chiếu. Tên trong series bible
   (Yojin Odaki, Hikari Fujino, Kenta) vẫn giữ nguyên, chưa có gì trong C10 để bổ sung hay sửa.
3. **Trọng số hợp lý chưa?** — Chưa chấm được trọng số nào vì chưa có beat. Anh muốn em
   crawl lại C10 ngay bây giờ, hay chờ site upload xong rồi mới chạy?
