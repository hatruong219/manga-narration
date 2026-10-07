# BEAT SHEET — Twilight Blade (TWB) · Chapter 11

> Trạng thái: **KHÔNG LÀM ĐƯỢC — DỪNG.** Bản đăng của chapter 11 không có nội dung truyện.
> Đã đọc đủ 12/12 ảnh trong `pages-clean/` theo thứ tự P01→P12, không nhảy cóc.

---

### A. Kiểm tra đầu vào

**CẢNH BÁO NẶNG: chapter chưa được đăng. Toàn bộ 12 trang là trang chờ của site, không có một panel truyện nào.**

Thư mục đọc: `series/TWB/C11/pages-clean/` — nhận đủ 12 file, đúng dải P01…P12, **không đứt số**.
Nhưng số trang liên tục không có nghĩa là nội dung đủ: cả 12 trang đều là **chrome của site**, không phải trang manga.

| Trang | Kích thước | Nội dung thật sự nhìn thấy | Kết luận |
|---|---|---|---|
| P01 | 1080×1500 | Banner quảng cáo TruyenQQQ (dàn nhân vật Naruto/Deku/Jujutsu…) + dòng promo + mở đầu khung "NetTruyen13s.com / CHAPTER ĐANG ĐƯỢC TẢI LÊN" | **BỎ** |
| P02 | 1080×1028 | Phần đuôi khung chờ: "…TẢI LÊN / Vui lòng chờ 1-2p nữa vào đọc lại sẽ có ảnh, xin cảm ơn! / NetTruyen.Link / NetTruyen.Party" | **BỎ** |
| P03 | 1080×1500 | Trọn khung chờ "CHAPTER ĐANG ĐƯỢC TẢI LÊN" trên nền xanh lá nhạt | **BỎ** |
| P04 | 1080×420 | Dải nền xanh lá trống trơn, không chữ, không hình | **BỎ** (trang trắng) |
| P05 | 1080×1500 | **Trùng khít P03** | **BỎ** |
| P06 | 1080×420 | **Trùng khít P04** | **BỎ** |
| P07 | 1080×1500 | **Trùng khít P03** | **BỎ** |
| P08 | 1080×420 | **Trùng khít P04** | **BỎ** |
| P09 | 1080×1500 | **Trùng khít P03** | **BỎ** |
| P10 | 1080×420 | **Trùng khít P04** | **BỎ** |
| P11 | 1080×1500 | Khung chờ như P03 (lệch vài px khi nén, nội dung y hệt) | **BỎ** |
| P12 | 1080×1028 | Đuôi khung chờ + banner quảng cáo TruyenQQQ nền xanh + dòng promo cuối | **BỎ** |

**Bằng chứng trùng lặp (md5, `pages-clean/`):**

- `P03 = P05 = P07 = P09` → `4a013012bd2edd73c820c6b03ba6ae3b`
- `P04 = P06 = P08 = P10` → `5b42cc2a3fcc46f957831a8de60a16e1`

Nghĩa là 8 trang giữa chỉ là **2 ảnh được lặp lại 4 lần**. Kiểm tra chéo trong `pages/` (bản gốc chưa clean) cho đúng cùng một kiểu trùng (`e5fe88bf…` ×4 và `560f20b4…` ×4), nên **đây là lỗi từ nguồn/crawl, không phải lỗi của `clean-pages.py`**.

**Về `clean-pages.py`: đã chạy nhưng CẮT 0 px trên cả 12 trang.**
Kích thước `pages/` và `pages-clean/` giống hệt nhau từng trang (1080×1500, 1080×1028, 1080×420…); chỉ khác md5 do ảnh bị mã hoá lại. Hệ quả: **banner quảng cáo ở P01 và P12 vẫn còn nguyên** trong bản "clean". Luật B của script (bỏ mọi thứ phía trên dải promo ở trang đầu) không bắt được layout này. Khi có bản đăng thật thì cần kiểm lại script trên chapter mới, đừng tin là nó đã sạch.

**Vì sao chapter "chỉ có 12 trang" so với C1 (53) và C3 (58):** không phải chapter ngắn. Là vì chương chưa lên ảnh — site trả về trang placeholder thay cho mọi trang truyện. 12 là số ảnh placeholder, không phải số trang truyện.

**Việc cần làm trước khi làm lại beat sheet:**

1. Crawl lại `C11` sau khi site đăng xong (`scripts/crawl-chapter.py`), hoặc đổi nguồn khác.
2. Kiểm nhanh: nếu `pages/` còn trang trùng md5, hoặc còn chữ "CHAPTER ĐANG ĐƯỢC TẢI LÊN", là bản đăng vẫn hỏng — đừng chạy tiếp.
3. Chạy lại `clean-pages.py` và **xác nhận nó thật sự cắt px** (so kích thước trước/sau), đừng chỉ chạy cho có.
4. Rồi mới chạy lại `/manga-beat-sheet` cho C11.

**Không viết lời kể cho chapter này.** Không có gì để kể, và mọi nội dung viết ra ở trạng thái này đều là bịa.

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| — | — | *(trống — không có panel truyện nào trong 12 trang nhận được)* | — | — | — |

**Tổng số panel truyện: 0.**
Cả 12 trang đều đánh dấu **BỎ** theo quy tắc "trang tiêu đề, trang trắng, trang quảng cáo sót lại" của skill. Không panel nào được đánh số `P{trang}-a/b` vì không có khung truyện để đánh.

---

### C. Điểm cao trào

**Không có.**
Không có cao trào cảm xúc, không có cao trào hành động, và **không có cú lật cuối** — trang cuối (P12) là banner quảng cáo của site, không phải trang truyện. Mọi nhận định về "cú lật ở trang cuối đổi nghĩa phần đầu" đều không kiểm chứng được với bản đăng hiện tại.

---

### D. Chưa rõ

Toàn bộ nội dung chapter 11 hiện **chưa rõ**. Liệt kê để lần đọc sau đối chiếu, **không đoán trước**:

- **Chapter 11 kể chuyện gì** — chưa biết một chi tiết nào.
- **Yojin và Hikari có xuất hiện không**, ai là người dẫn cảnh — chưa thấy mặt nhân vật nào.
- **Cú lật cuối chương** — chưa biết có hay không.
- **Chuỗi sự kiện nối từ C10 sang** — chưa đọc được, và trong repo `C2`–`C10` đều chưa có beat sheet (`tracker.csv` chỉ đánh dấu `C1` đã xong). Nghĩa là **đang thiếu mạch C2→C10**; nếu làm C11 trước, sẽ không biết mốc cốt truyện nào đã tiết lộ rồi.
- **Mốc cốt truyện mới** — không cập nhật được gì vào mục 4 của `series-bible.md`.

**Không suy đoán** dựa trên tên chapter, số thứ tự, hay nội dung C1. Các điểm "chưa tiết lộ" đã chốt trong series bible (Yojin làm cho tổ chức nào · ai ra chỉ thị · vì sao Hikari có thể chất đó · mắt Yojin đỏ ở C1-P01) **vẫn giữ nguyên là chưa tiết lộ** — chapter này không bổ sung được gì.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** — Beat sheet đang **0 panel**, và đó là kết quả đúng: 12/12 trang là trang chờ + quảng cáo của site, 8 trang giữa chỉ là 2 ảnh lặp 4 lần. Anh xác nhận C11 trên site lúc crawl đúng là chưa lên ảnh chứ?
2. **Tên nhân vật đúng chưa?** — Chưa có nhân vật nào để gọi tên. Cách gọi chốt trong series bible (**Yojin** + đại từ *anh*, **Hikari**, **oán hồn**, **pháp sư trừ tà**) giữ nguyên, chưa dùng tới. Anh có muốn bổ sung tên mới nào trước khi crawl lại không?
3. **Trọng số hợp lý chưa?** — Chưa chấm trọng số nào. Câu hỏi thay thế: nên **crawl lại C11** trước, hay **làm C2–C10 cho liền mạch** rồi quay lại C11?
