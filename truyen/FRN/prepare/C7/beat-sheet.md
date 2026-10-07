# BEAT SHEET — FRN Chương 7

> Tên chương in trên trang màu P03: **"Chương 7 · Vùng đất linh hồn yên nghỉ"**.
> Nguồn ảnh: nettruyen13s (rộng 1000px) — **khác nguồn C1–C5, C8–C12 (truyenqq, 900px)**.
> Trạng thái: **CHƯA viết lời kể.** Dừng chờ duyệt.

---

## A. Kiểm tra đầu vào

### A.1 — Đã nhận đủ 25 file, không thiếu số

`truyen/FRN/prepare/C7/pages-clean/` — `FRN_C7_P01.jpg` … `FRN_C7_P25.jpg`, liên tiếp, không đứt số.

| File | Kích thước (pages-clean) | Kích thước gốc (pages) | clean-pages cắt |
|---|---|---|---|
| P01 | 1000×632 | 1000×632 | 0 px |
| P02 | 1000×800 | 1000×800 | 0 px |
| P03 | 1000×1435 | 1000×1435 | 0 px |
| P04 | 1000×1452 | 1000×1452 | 0 px |
| P05–P08 | 1000×1435 | 1000×1435 | 0 px |
| **P09** | **1000×1424** | 1000×1435 | **−11 px** |
| P10–P12 | 1000×1435 | 1000×1435 | 0 px |
| **P13** | **1000×1424** | 1000×1435 | **−11 px** |
| P14–P21 | 1000×1435 | 1000×1435 | 0 px |
| P22 | 1000×718 | 1000×718 | 0 px |
| P23 | 1000×1525 | 1000×1525 | 0 px |
| P24 | 1000×625 | 1000×625 | 0 px |
| P25 | 1000×522 | 1000×522 | 0 px |

`clean-pages.py` **chỉ đụng vào P09 và P13**, mỗi trang 11 px ở mép dưới. Hệ quả: **số trang in
ở góc dưới của P09 và P13 đã bị cắt mất** (các trang khác đều còn đọc được số). Không mất panel
nào — mép dưới hai trang đó là viền trắng.

### A.2 — Trang BỎ / GIỮ: đã MỞ RA XEM TỪNG TRANG, không suy theo khuôn

Bốn trang bị nghi theo số đo (P01 632, P02 800, P24 625, P25 522) đều đã mở ra xem. Kết luận:

| File | Quyết định | **Nhìn thấy gì** |
|---|---|---|
| **P01** (632) | **BỎ** | Ảnh ghép quảng cáo các bộ khác của nhóm dịch: *Sukinako ga Megane wo Wasureta*, *Hatsukoi Zombie*, *Shinigami Bocchan to Kuro Maid*, *Yofukashi no Uta*, *Komi-san ha Komyusho Desu*, *Murenase! Shiiton Gakuen* + hộp đỏ "**7 FINGERS TEAM**" + link facebook.com/sevenfingersteam. **Không có một nét nào của FRN.** |
| **P02** (800) | **BỎ** | Trang credit: TRANSLATOR Credemoe · EDITOR Yahari! · PROOFREADER Credemoe · QUALITY CHECKER Credemoe, "Tất cả các sản phẩm đều phi lợi nhuận", logo 7 FINGERS TEAM "Khi 5 ngón là chưa đủ", link facebook + blogtruyen. **Nền là ảnh bìa tankōbon ghép lại, và góc trái in "2話 僧侶の嘘" (= tên chương 2, "Lời nói dối của tư tế") — đây là trang credit DÙNG LẠI, không phải trang nội dung C7.** |
| **P03** (1435) | **GIỮ — quan trọng** | **Trang màu tên chương.** In "Chương 7 · **Vùng đất linh hồn yên nghỉ**", tên gốc 葬送のフリーレン, tác giả 山田鐘人 / アベツカサ, và tranh Frieren bé đứng ở khung cửa đá cùng một phụ nữ tóc bím dài. Trang này **mở ra toàn bộ nghĩa của chương** — mất là mất tên chương. *(Đúng tiền lệ C9-P02.)* |
| **P22** (718) | **GIỮ — là TRANG ĐÔI, không phải rác** | Một khung tràn toàn trang: **lâu đài Quỷ Vương** trong đêm, thoại "Hiện giờ chính là tòa lâu đài của Quỷ Vương đấy." Ảnh ngang → đúng dấu hiệu trang đôi mà bible mô tả. Xem A.3 để biết vì sao chắc chắn. |
| **P24** (625) | **BỎ** | Banner "**THÔNG BÁO** — 7 Fingers Team xin phép: KHÔNG nhận thêm nhân sự / KHÔNG liên quan đến các WEB dịch truyện / KHÔNG nhận donate từ độc giả", ký "Trưởng nhóm Credemoe", nền là tranh một cô hầu gái không thuộc FRN. |
| **P25** (522) | **BỎ** | Banner "**12 FINGERS TEAM**" + "Let's start over from the beginning, from that misunderstanding filled day one more time. (4/5/2020)" + tranh Komi-san và chữ viết tay linh tinh. Không thuộc FRN. |

→ **Nội dung truyện = P03 → P23, tổng 21 trang file.**
→ **Bỏ 4 trang: P01, P02, P24, P25.**

**Khác luật C1/C2 ở chỗ nào:** C1/C2 bỏ P01+P02 ở đầu và **một** trang cuối. C7 bỏ P01+P02 ở
đầu và **hai** trang cuối (P24 **và** P25) — đúng như bible đã cảnh báo cho cụm C6/C7. Nhưng
**P03 ở đây là trang màu tên chương, không phải trang bìa bỏ đi**, và **P22 nhỏ bất thường lại
là trang nội dung**. Hai điểm này không suy ra được từ số đo, chỉ mở ảnh mới thấy.

### A.3 — Đối chiếu số trang IN trên ảnh: không mất trang nào

| File | Số in trên ảnh | Lệch (file − in) |
|---|---|---|
| P04 | 2 | −2 |
| P05 | 3 | −2 |
| P06 | 4 | −2 |
| P07 | 5 | −2 |
| P08 | 6 | −2 |
| P09 | *(bị clean-pages cắt)* | (suy ra 7) |
| P10 | 8 | −2 |
| P11 | 9 | −2 |
| P12 | 10 | −2 |
| P13 | *(bị clean-pages cắt)* | (suy ra 11) |
| P14 | 12 | −2 |
| P15 | 13 | −2 |
| P16 | 14 | −2 |
| P17 | 15 | −2 |
| P18 | 16 | −2 |
| P19 | 17 | −2 |
| P20 | 18 | −2 |
| P21 | 19 | −2 |
| **P22** | **không in số** | — |
| **P23** | **22** | **−1** |

Độ lệch nhảy từ −2 sang −1 **đúng ngay sau P22**. Đây là bằng chứng cứng rằng **P22 là một
file chứa HAI trang in (20 và 21) — một trang đôi**, khớp với việc nó là ảnh ngang 1000×718 và
chứa một khung tràn trang. Không có trang nội dung nào bị thiếu. *(Cùng cơ chế bible đã ghi
cho C1-P04 và C1-P26.)*

**Lưu ý sản xuất:** P22 là trang đôi → khi lên khung 9:16 phải **PAN ngang hoặc cắt panel**,
không thả nguyên.

### A.4 — Chiều đọc: PHẢI → TRÁI, đã xác minh bằng chứng cứ TRONG CHÍNH ẢNH C7

Không suy theo "manga Nhật thì phải thế". Bốn chỗ trong chương này tự chứng minh:

1. **P18, hàng 2 (hồi tưởng với sư phụ)** — bốn bóng thoại chỉ ghép thành câu chuyện khi đọc từ
   phải sang: Frieren bé hỏi (trang trước, khung trái) *"Nhưng đến lúc đấy thì sư phụ đã mất rồi
   mà?"* → khung **phải nhất** sư phụ cười đáp *"Đúng vậy, còn em thì không."* → khung giữa *"Chắc
   chắn một ngày nào đó em sẽ phạm phải một sai lầm nghiêm trọng…"* → khung **trái nhất** Frieren
   bé hỏi lại *"Sư phụ muốn em hiểu thêm về họ sao ạ?"* / *"Không không."*
   Đọc ngược lại thì câu trả lời đứng trước câu hỏi.
2. **P10, hàng cuối** — chuỗi trêu chọc chỉ có nghĩa theo hướng phải→trái: *"'Từ xưa' ư… chẳng
   biết là bao lâu rồi nhỉ?"* (phải) → *"Có lẽ là thời đại nguyên thủy không chừng ạ?"* (giữa) →
   *"Tôi chưa có già đến thế đâu."* (trái, Frieren đáp trả).
3. **P21, hàng cuối** — câu hỏi *"Vậy rốt cuộc là nó ở đâu vậy ạ?"* nằm ở khung **phải**, câu đáp
   *"'Ende' ấy ạ…" / "Đúng vậy."* nằm ở khung **trái**.
4. **P04 hàng 3 → P05 hàng 1** — khung phải: Eisen *"Mọi người đều tan biến thành cát bụi sau khi
   chết mà."* → khung trái: Heiter *"Họ lên thiên đường đó."* → sang P05 Frieren bình: *"Người lùn
   tôn kính truyền thống của mình thật đấy."* Câu bình này khớp đúng với việc **người lùn (Eisen)
   nói câu 'cát bụi'**, tức khung phải phải đọc trước.

Mọi mã panel `P{trang}-a/b/c…` bên dưới đều đánh theo thứ tự **phải → trái, trên → dưới**.

### A.5 — Ghi chú chính tả tên gọi

Bible chốt: Frieren · Himmel · Heiter · Eisen · Fern · Stark. Đại từ người kể: Frieren → **cô**,
Himmel → **anh**, Heiter → **ông**, Eisen → **ông**, Fern → **cô bé**. Thuật ngữ thống nhất
**Quỷ Vương** và **ma lực**.
C7 in nguyên văn "quỷ vương" (P22) → lời kể dùng **Quỷ Vương**.
Các tên riêng MỚI xuất hiện trong C7 (Flamme, Aureole, Ende, lưu vực Voll, khu vực Bredt) đều là
**chữ in trên trang**, không phải mình đặt — xem mục D.

---

## B. Beat Sheet

**Bố cục chương:** P03 trang màu · **P04–P07 hồi tưởng thời còn đi cùng tổ đội** · P08–P16 hiện
tại ở khu vực Bredt · **P17–P18 hồi tưởng 1000 năm trước với sư phụ** · P19–P23 phế tích và
quyết định.

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang màu tên chương. Frieren bé và một phụ nữ tóc bím dài đứng ở khung cửa đá dẫn xuống bậc thang. Chữ in: "Chương 7 · Vùng đất linh hồn yên nghỉ". | *(tên chương)* | trang trọng, mở | 3 |
| 2 | P04-a | **Hồi tưởng.** Bốn người tổ đội đứng trước một căn nhà gỗ giữa rừng. Chữ dọc bên lề: "thời còn đi cùng các anh hùng… về 'lời cầu nguyện' của kẻ đưa tang". | — | tĩnh, mở đoạn | 2 |
| 3 | P04-b | Trước mấy nấm mộ đá, Heiter hỏi Eisen về nơi này; Eisen nói làng mình từng bị quỷ dữ tấn công. | "Làng của tôi đã bị quỷ dữ tấn công ấy mà." | trầm | 2 |
| 4 | P04-c | Heiter quỳ xuống chắp tay. Có người hỏi ông đang làm gì. | "Cầu nguyện đấy." | lặng | 2 |
| 5 | P04-d | Eisen phản bác: chết là tan thành cát bụi. | "Mọi người đều tan biến thành cát bụi sau khi chết mà." | khô khan | 2 |
| 6 | P04-e | Heiter đáp gọn. | "Họ lên thiên đường đó." | điềm nhiên | 2 |
| 7 | P05-a | Frieren nhận xét: vài ngàn năm trước, tin "chết là tan thành cát bụi" mới là lẽ thường; người lùn giữ truyền thống rất kỹ. | "Người lùn tôn kính truyền thống của mình thật đấy." | quan sát lạnh | 2 |
| 8 | P05-b | Frieren nói thẳng: phép thuật hiện tại không quan sát được linh hồn người chết, nên **không thể chứng minh "thiên đường" tồn tại**. Cô hoài nghi. | "…để chứng minh 'thiên đường' có tồn tại là điều bất khả thi." | thẳng, lạnh | 3 |
| 9 | P05-c | Himmel gạt đi, không quan tâm bên nào đúng. | "Đối với tôi thì cái nào cũng được hết." | nhẹ nhõm | 1 |
| 10 | P05-d | Heiter cười, đồng tình rằng chuyện có hay không cũng chẳng thành vấn đề. | "Có tồn tại hay không thì cũng chẳng có vấn đề gì hết ha." | ung dung | 2 |
| 11 | P05-e | Frieren vặn lại: một tư tế mà nói thế thì có ổn không. | "Một tư tế nói ra điều đó liệu có ổn không vậy?" | châm | 2 |
| 12 | P06-a | Heiter cười, nói kể cả khi thiên đường không tồn tại thì ông vẫn cho rằng **nên** nghĩ là có. | "Mà kể cả khi nó không có tồn tại, thì tôi vẫn nghĩ là nên như vậy." | ấm, cứng cỏi | 3 |
| 13 | P06-b | Frieren không hiểu. | "Là sao chứ?" | ngơ | 1 |
| 14 | P06-c | Heiter: chẳng ai chịu sống một đời tuyệt vọng mà không có đích đến cả — **tin thế thì tốt hơn**. | "Bởi vì làm vậy thì sẽ tốt hơn mà." | dịu, nặng | 3 |
| 15 | P06-d | Heiter quỳ cầu nguyện, nói thêm: nghĩ rằng mọi người đang sống sung túc trên thiên đường chẳng phải tốt hơn sao. | "…chẳng phải là sẽ tốt hơn… hay sao?" | lặng, ấm | 3 |
| 16 | P07-a | Eisen cận mặt, im lặng nghe. | — | nén | 1 |
| 17 | P07-b | Eisen quay lưng, đứng cạnh vách nhà gỗ. | — | tĩnh | 1 |
| 18 | P07-c | Himmel chắp tay, bật cười khẽ, thấy cách nghĩ đó đúng là tốt hơn thật. | "Quả là tốt hơn thật." / "Fu fu." | ấm | 2 |
| 19 | P07-d | Himmel rủ Frieren cùng cầu nguyện. | "Chúng ta cùng cầu nguyện cho họ nhé?" | mềm | 3 |
| 20 | P07-e | Cả bốn người cùng chắp tay trước mộ. | — | trang nghiêm | 3 |
| 21 | P07-f | Cận cảnh đôi bàn tay chắp lại; một tiếng ừ. | "Ừm." | lặng | 2 |
| 22 | P08-a | Đôi tay chắp còn giữ nguyên — **kết hồi tưởng**. | — | lặng | 2 |
| 23 | P08-b | **Hiện tại.** Chữ trong khung: "**28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời**" · "**Các vùng trung tâm, khu vực Bredt**". Vẫn căn nhà gỗ ấy, giờ có hoa; một bóng người lùn đang quỳ bên mấy nấm mộ. Frieren và Fern đi tới. | "28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời." | thời gian đè | 3 |
| 24 | P08-c | Frieren cất tiếng gọi. | "Eisen, tôi tới chơi nè." | nhẹ | 2 |
| 25 | P08-d | Eisen: khó tin là đã trôi qua 30 năm. | "Thật khó để tin rằng là đã trôi qua 30 năm rồi đấy nhỉ." | bùi ngùi | 2 |
| 26 | P08-e | Frieren thấy 30 năm chẳng là bao; Eisen ừ theo. | "Mới chỉ 30 năm thôi mà?" | lệch nhịp thời gian | 3 |
| 27 | P09-a | Trong nhà gỗ: Eisen ngồi một bên bàn dài, Frieren và Fern bên kia. | — | chuyển | 1 |
| 28 | P09-b | Eisen ngạc nhiên vì Frieren lại nhận học trò. | "Không ngờ cô lại nhận học trò đấy." | ngỡ ngàng | 2 |
| 29 | P09-c | Frieren hỏi thẳng: có chuyện gì cần giúp không. | "Eisen này. Chúng tôi có thể giúp cậu chuyện gì không?" | thẳng | 2 |
| 30 | P09-d | Hai người nhìn nhau qua bàn. | — | chờ | 1 |
| 31 | P09-e | Eisen đoán trúng rằng Heiter cũng từng nhờ cô một việc tương tự; và nói **chặng đường của ông chưa kết thúc**. | "Vẫn còn quá sớm để chặng đường của tôi kết thúc ha." | rắn rỏi | 3 |
| 32 | P09-f | Frieren hỏi sao ông biết cô sẽ tới. Ảnh cắt song song: Eisen và Heiter, mỗi người ngồi viết ở bàn của mình. | "Bởi vì tụi tôi thường hay trao đổi qua thư mà." | ấm, hé lộ | 3 |
| 33 | P09-g | Frieren: ông thành thật hơn vẻ ngoài; Eisen đáp lại rằng cô thì quá lạnh lùng. | "Còn cô thì lại quá đỗi lạnh lùng đấy." | trêu nhau | 2 |
| 34 | P10-a | Frieren hỏi lại lần nữa ông muốn nhờ gì. | "Thế cậu có muốn chúng tôi giúp gì không nào?" | thúc | 2 |
| 35 | P10-b | Eisen im, nhìn đi chỗ khác. | — | ngập ngừng | 2 |
| 36 | P10-c | Khung rộng: dãy núi và rừng — họ lên đường. | — | mở | 1 |
| 37 | P10-d | Bên cỗ xe ngựa: nhắc tên **lưu vực Voll**, Frieren thấy hoài niệm; có người hỏi cô từng tới chưa. | "Lưu vực Voll à. Hoài niệm thật đấy." | hoài niệm | 2 |
| 38 | P10-e | Frieren đáp gọn. | "Từ xưa rồi." | phẳng | 1 |
| 39 | P10-f | Eisen và Fern trêu "từ xưa" là bao lâu, có khi là thời đại nguyên thủy; Frieren phản đối. | "Tôi chưa có già đến thế đâu." | hài nhẹ | 2 |
| 40 | P11-a | Eisen nói rõ thứ cần tìm: **quyển ghi chú của pháp sư vĩ đại Flamme**. Một cuốn sách hiện lên trong khung. | "Quyển ghi chú của pháp sư vĩ đại Flamme." | hé mở | 3 |
| 41 | P11-b | Frieren sững lại. | "Hở…?" | bất ngờ | 2 |
| 42 | P11-c | Frieren nhận lời nhưng cảnh báo: gần như mọi cuốn sách mang tên Flamme đều là hàng giả. | "…các quyển sách của Flamme đều là hàng giả cả thôi." | hoài nghi | 2 |
| 43 | P11-d | Eisen kể có một nơi **Heiter tìm ra nhờ phiên dịch các ghi chép còn sót lại của Flamme trong thánh thành**. Ảnh: thư phòng trong thánh thành. | "…Heiter khám phá ra bằng việc phiên dịch các ghi chép còn sót lại của Flamme…" | hé lộ | 3 |
| 44 | P11-e | Quyển ghi chú thật nằm đâu đó trong lưu vực Voll. | "…đang nằm đâu đó ở lưu vực Voll này." | hướng đi | 2 |
| 45 | P11-f | Eisen quả quyết Frieren biết chỗ. | "Và tôi chắc chắn rằng Frieren biết nơi đó." | chắc nịch | 3 |
| 46 | P11-g | Frieren lẩm bẩm về Heiter. | "Cái đồ tư tế thúi đó… nghiên cứu đến thế này rồi cơ à?" | vừa cay vừa mềm | 3 |
| 47 | P12-a | Ba người vào rừng; Frieren bảo tìm "cây lớn" trước. Có người bật cười vì quanh đây cây lớn nhan nhản. | "Hãy tìm cái cây lớn trước nào." | chớm hài | 2 |
| 48 | P12-b | Frieren bảo dù sao cũng thừa thời gian. | "…chúng ta cũng có quá trời thời gian cơ mà." | thong dong | 2 |
| 49 | P12-c | Fern cận mặt, cười rất khẽ. | — | lạnh êm | 2 |
| 50 | P12-d | Eisen(?) nhắc rằng Fern ghét phung phí thời gian nên nên làm nhanh. | "…Fern ghét việc phung phí thời gian lắm…" | cảnh giác vui | 2 |
| 51 | P12-e | Fern chốt lại một câu gọn lỏn. | "Hãy cố gắng hết sức để tìm đi ạ." | lạnh, dứt | 3 |
| 52 | P13-a | Ba người đi sâu vào rừng cổ thụ. | — | chuyển | 1 |
| 53 | P13-b | Eisen nhận xét Frieren đã thay đổi — trước kia cô có bao giờ đoái hoài đến thời gian của người khác. | "Cô đã thay đổi rồi." | dịu, nặng | 3 |
| 54 | P13-c | Frieren gạt đi bằng lý do khác. | "Bởi vì Fern rất đáng sợ một khi mà em ấy tức lên đấy." | né tránh | 3 |
| 55 | P13-d | Eisen cận mặt, không nói thêm. | — | hiểu ngầm | 2 |
| 56 | P13-e | Eisen chỉ dặn cẩn thận. | "Vậy à. Thế thì hãy cẩn thận nhé." | ấm | 2 |
| 57 | P13-f | Khung trời nhìn qua tán lá. | — | khoảng lặng | 1 |
| 58 | P14-a | **Chuỗi khung không thoại — nhiều ngày tìm kiếm.** Eisen nâng bổng một tảng đá khổng lồ chắn đường. | — | sức vóc | 2 |
| 59 | P14-b | Cả ba dựng bếp nấu ăn trong rừng. | — | đời thường | 1 |
| 60 | P14-c | Frieren vác Fern đang ngủ (ZZZ) bay đi. | — | ấm, hài | 2 |
| 61 | P14-d | Ba người đứng dưới một gốc cổ thụ to. | — | tìm kiếm | 1 |
| 62 | P14-e | Frieren đứng một mình trong rừng, Eisen và Fern ngủ lăn lóc. | — | cô độc | 2 |
| 63 | P14-f | Frieren và Fern bay trên dãy núi, mỗi người cưỡi một cây gậy. | — | rộng | 2 |
| 64 | P14-g | Ba người lại đi trên lối mòn. | — | lặp, mỏi | 1 |
| 65 | P15-a | Fern bay cao trên nền trời và núi. | — | mở | 2 |
| 66 | P15-b | Fern báo về: phía tây có **một cây lớn đang bao bọc vài tàn tích**. Frieren nhận tin. | "…một cái cây lớn ở phía đằng tây đang bao bọc một vài tàn tích đấy ạ." | tìm thấy | 3 |
| 67 | P15-c | Frieren quay sang hỏi Eisen vì sao ông đi tìm sổ ghi chú của Flamme. | "Này, sao cậu lại tìm kiếm sổ ghi chú của Flamme vậy?" | dò hỏi | 3 |
| 68 | P15-d | Eisen im một nhịp rồi trả lời. | "Chỉ vì tôi thấy thật là đáng thương." | nghẹn | 3 |
| 69 | P15-e | Eisen cận mặt: **cả Frieren lẫn Himmel đều đáng thương**. | "Cả cô và Himmel thật là đáng thương ấy mà." | xót | 3 |
| 70 | P15-f | Hồi tưởng cảnh 30 năm trước: Frieren từng hỏi vì sao mình đã không cố thân thiết với Himmel hơn. | "…vì sao mình lại không cố gắng thân thiết với Himmel hơn." | vết thương cũ | 3 |
| 71 | P15-g | Eisen: ông đã nghĩ cô nên nói thẳng những lời ấy với chính Himmel. | "…cô nên bày tỏ trực tiếp những lời nói ấy đến với Himmel mà thôi." | quyết | 3 |
| 72 | P16-a | Eisen nói ra lý do thật: **nghe nói ghi chú của Flamme có chép lại đoạn hội thoại của bà với người chết**. | "…ghi chép lại đoạn hội thoại của cô ấy với người chết đấy." | mấu chốt | 3 |
| 73 | P16-b | Frieren gạt: chỉ là chuyện cổ tích. | "Chỉ là chuyện cổ tích mà thôi." | phòng thủ | 2 |
| 74 | P16-c | Frieren nói thêm — và cô cũng không hẳn muốn nói chuyện với anh thêm lần nào nữa. | "…cũng không hẳn là tôi muốn nói chuyện với cậu ấy thêm lần nào nữa." | chối, đau | 3 |
| 75 | P16-d | Eisen đáp lại: mọi phép thuật đều sinh ra từ chuyện cổ tích — và ông **cũng muốn hiểu thêm về Himmel**. | "Tất cả phép thuật đều được sinh ra từ chuyện cổ tích cả mà." | cứng | 3 |
| 76 | P16-e | Eisen và Fern đứng trong rừng. | — | chuyển | 1 |
| 77 | P16-f | Eisen thú nhận đã hỏi ý Heiter, và ông tin Frieren đang ăn năn với Himmel nên muốn giúp. | "Chính vì thế nên tôi đã tham khảo Heiter." | thương | 3 |
| 78 | P16-g | Khung lớn: **một cây cổ thụ khổng lồ mọc trùm lên cả một cụm phế tích đá**. Fern bay lơ lửng, hai người kia nhỏ xíu dưới gốc. | — | choáng ngợp | 3 |
| 79 | P17-a | Fern báo: cả cây lẫn tàn tích đều nằm trong **một rào chắn đầy uy lực**. | "…được bao bọc bởi một rào chắn đầy uy lực đấy ạ." | cảnh giác | 3 |
| 80 | P17-b | Fern chạm tay vào thân cây bên một cột đá. | — | dò | 1 |
| 81 | P17-c | Frieren nghiêng mặt, nhận ra: **qua cả ngàn năm mình vẫn nằm trong lòng bàn tay sư phụ**. | "…mình vẫn lại nằm trong lòng bàn tay của sư phụ à." | sững, cay | 3 |
| 82 | P17-d | Phế tích nhà đá lộ ra dưới tán rừng. | — | mở | 1 |
| 83 | P17-e | **Hồi tưởng ~1000 năm trước.** Hai bàn tay vun đất quanh một mầm cây con. | — | xa xăm | 2 |
| 84 | P17-f | Frieren bé và người phụ nữ tóc bím dài ngồi bên mầm cây; Frieren chê cây giám hộ này trông chẳng đáng tin. | "Trông cây giám hộ này không đáng tin cậy lắm nhỉ." | trẻ con | 2 |
| 85 | P18-a | Sư phụ: khi cái cây bé này lớn lên, nó sẽ còn bảo vệ nơi này kể cả sau một ngàn năm nữa. | "…kể cả sau một ngàn năm nữa đấy." | trù tính xa | 3 |
| 86 | P18-b | Hai người bước xuống bậc thang đá; Frieren bé vặn lại rằng đến lúc đó thì sư phụ đã mất rồi. | "Nhưng đến lúc đấy thì sư phụ đã mất rồi mà?" | hồn nhiên, tàn nhẫn | 3 |
| 87 | P18-c | Sư phụ cười, đáp gọn. | "Đúng vậy, còn em thì không." | điềm nhiên | 3 |
| 88 | P18-d | Sư phụ đoán trước: **một ngày nào đó Frieren sẽ phạm một sai lầm nghiêm trọng, rồi bắt đầu muốn hiểu thêm về mọi người**. | "…em sẽ phạm phải một sai lầm nghiêm trọng…" | tiên tri | 3 |
| 89 | P18-e | Frieren bé hiểu sai ý; sư phụ gạt đi. | "Sư phụ muốn em hiểu thêm về họ sao ạ?" / "Không không." | lệch nhịp | 2 |
| 90 | P18-f | Sư phụ xoa đầu Frieren bé trước khung cửa đá: sẽ dặn em quay lại đây đúng vào lúc đó. | "Ta sẽ nói cho em để trở lại đây vào thời điểm đó." | ấm, nặng | 3 |
| 91 | P19-a | **Hiện tại.** Frieren bước qua đúng khung cửa ấy. Bóng thoại nối tiếp từ hồi tưởng: "Ma pháp sư vĩ đại Flamme này…" | "Ma pháp sư vĩ đại Flamme này" | rùng mình | 3 |
| 92 | P19-b | Căn phòng đá trống, **một cuốn sách mở lơ lửng trên bệ đá**. Vế sau của câu: "…sẽ chỉ dẫn em." | "…sẽ chỉ dẫn em." | **đỉnh** | 3 |
| 93 | P19-c | Fern đi vào phòng, tiến về phía bệ. | — | nín thở | 2 |
| 94 | P19-d | Fern và Frieren cầm cuốn sách phát sáng; Fern hỏi có phải hàng thật, Frieren khẳng định. | "Là thật đấy." | chắc | 3 |
| 95 | P19-e | Fern hỏi sao ngài biết; Eisen trả lời thay. | "Frieren là học trò xuất sắc nhất của Flamme mà." | **hé lộ lớn** | 3 |
| 96 | P20-a | Fern ngỡ ngàng: Flamme là một anh hùng cổ đại trong lịch sử phép thuật, vậy là bà thật sự đã sống ở thời đại nguyên thủy. Eisen giục hỏi phần quan trọng. | "Trong đó có ghi chép gì về hội thoại với người chết không?" | dồn | 3 |
| 97 | P20-b | Fern đọc: các trang sách đang **tự từ từ mở ra**. | "Các trang sách đang từ từ mở ra mà thôi." | huyền bí | 3 |
| 98 | P20-c | Frieren tự hỏi liệu sư phụ đã biết trước mình sẽ quay lại sau một ngàn năm; rồi lẩm bẩm ghét. | "Vẫn khó chịu như thường nhỉ…" | nể mà cay | 3 |
| 99 | P20-d | **Nội dung ghi chú của Flamme** (khung lớn: Flamme đi giữa những bóng linh hồn trong một thành phố mái vòm trắng): xa về **phía bắc lục địa**, bà đã tới **nơi thế gian gọi là thiên đường, nơi các linh hồn yên nghỉ**; ở đó bà **đã tiếp xúc với những người bạn cũ**. | "…một nơi mà những linh hồn đang yên nghỉ." | **đỉnh** | 3 |
| 100 | P21-a | Fern hỏi vậy là thật sao; Frieren nói không chắc vì Flamme hay phóng đại. | "Ngài ấy là một người hay phóng đại quá mức mà." | ngờ vực | 2 |
| 101 | P21-b | Eisen đứng ngoài, nói gọn một câu khẳng định. | "Thiên đường có tồn tại." | dứt khoát | 3 |
| 102 | P21-c | Eisen dùng đúng lý lẽ của Heiter năm xưa. | "Bởi vì như thế sẽ tốt hơn mà." | **vòng lặp đóng lại** | 3 |
| 103 | P21-d | Frieren nghiêng mặt, im. | — | lay động | 2 |
| 104 | P21-e | Frieren nhượng bộ: đôi khi cũng nên thử tin một lần. | "Đôi khi tôi nên tin thử một lần vậy." | mềm ra | 3 |
| 105 | P21-f | Fern hỏi rốt cuộc nơi đó ở đâu; Frieren dò sách rồi đọc: **lục địa phía bắc, Ende**. | "…Lục địa phía bắc, Ende." | hé lộ | 3 |
| 106 | P21-g | Fern nhắc lại cái tên; Frieren xác nhận. | "'Ende' ấy ạ…" | gợn | 2 |
| 107 | P22-a | **Trang đôi, khung tràn trang:** toà lâu đài Quỷ Vương sừng sững trong đêm. | "Hiện giờ chính là tòa lâu đài của Quỷ Vương đấy." | **đỉnh — sốc** | 3 |
| 108 | P23-a | Frieren buột miệng: sao lại đúng nơi đó. | "Tại sao lại là nơi đó cơ chứ…" | ngán ngẩm | 3 |
| 109 | P23-b | Eisen nói thẳng điều ông muốn nhờ: **hãy đi tìm Aureole — vùng đất yên nghỉ của các linh hồn — rồi nói chuyện với Himmel**. | "Frieren. Hãy tìm kiếm vùng đất yên nghỉ của các linh hồn, Aureole, rồi nói chuyện với Himmel nhé." | **đỉnh — lời nhờ cậy** | 3 |
| 110 | P23-c | Eisen cận mặt, nói thêm một câu *(xem mục D — chưa rõ chỉ ai)*. | "Cậu ta sẽ có ích với tôi đấy." | **CHƯA RÕ** | 3 |
| 111 | P23-d | Frieren nghiêng mặt, không đáp ngay. | — | cân nhắc | 2 |
| 112 | P23-e | Frieren nói Eisen ngày càng xảo quyệt; ông đáp là học từ Heiter. | "Nhờ Heiter cả thôi." | **vòng lặp đóng lại** | 3 |
| 113 | P23-f | Frieren nhận lời: dù sao chuyến đi của họ cũng vô định. | "…Tôi hiểu rồi." | **nhận nhiệm vụ** | 3 |
| 114 | P23-g | Frieren lập tức than: quanh lâu đài Quỷ Vương lúc nào chả lạnh cóng, cô chẳng muốn đi. Fern than thầm rằng ngài ấy lại nản. | "Tôi chẳng muốn đi tí tẹo nào cả…" | hài, hạ nhiệt | 2 |

**Tổng: 114 panel / 21 trang nội dung (P03–P23).** Trang đôi P22 tính là 1 khung tràn trang.

---

## C. Điểm cao trào

C7 có **bốn đỉnh** và **một cú lật cuối**. Sắp theo thứ tự trên trang:

**Đỉnh 1 — Lý do thật của Eisen (P15-e → P16-f, panel 69–77).**
Ông không tìm sách vì sách. *"Cả cô và Himmel thật là đáng thương ấy mà."* Ông nhớ câu Frieren
đã hỏi ở tang lễ 30 năm trước, và muốn cô nói thẳng những lời ấy với chính Himmel. Ông còn hỏi ý
Heiter để làm việc này. Đây là đoạn nặng nhất về tình cảm trong chương.

**Đỉnh 2 — Câu nói của sư phụ khớp lại sau một ngàn năm (P18-d → P19-b, panel 88–92).**
Cấu trúc hai vế bắc qua hai trang: hồi tưởng khép bằng *"Ta sẽ nói cho em để trở lại đây vào thời
điểm đó."*, rồi Frieren hiện tại bước qua đúng khung cửa ấy, và câu nói chảy tiếp sang cuốn sách
lơ lửng: *"Ma pháp sư vĩ đại Flamme này… sẽ chỉ dẫn em."*
Đúng kiểu cú lật thời gian mà bible mô tả cho bộ này: một câu vu vơ ngàn năm trước thành cú đánh
ở hiện tại. **Khung P19-b là khung để HOLD.**

**Đỉnh 3 — Nội dung ghi chú Flamme (P20-d, panel 99).**
Khung lớn Flamme đi giữa những bóng linh hồn: phía bắc lục địa có nơi *"những linh hồn đang yên
nghỉ"*, và ở đó bà *"đã tiếp xúc với những người bạn cũ"*. Đây là lần đầu bộ truyện xác nhận
chuyện nói chuyện với người chết không chỉ là cổ tích.

**Đỉnh 4 — Lời nhờ cậy có tên (P23-b, panel 109).**
*"Frieren. Hãy tìm kiếm vùng đất yên nghỉ của các linh hồn, **Aureole**, rồi nói chuyện với
Himmel nhé."* Và Frieren nhận lời ở panel 113.

**Cú lật cuối — trang đôi P22 (panel 107).**
Ende, nơi có Aureole, **chính là chỗ toà lâu đài Quỷ Vương đứng**. Cú lật này đổi nghĩa cả chương:
chuyến đi "vô định" của Frieren và Fern bỗng có đích, và cái đích ấy lại là nơi họ đã đánh xong
từ đầu C1. Đặt ngay sau khi Frieren vừa mềm lòng đồng ý tin — rồi trang sau cô than lạnh, hạ
nhiệt để không bi quá.

**Vòng lặp đóng lại (dùng cho lời kể, không phải đỉnh riêng).**
Hồi tưởng P06-c Heiter nói *"Bởi vì làm vậy thì sẽ tốt hơn mà."* → 28 năm sau, P21-c, Eisen lặp
lại **nguyên văn** câu đó để thuyết phục Frieren, và ở P23-e ông nhận là học từ Heiter. Đây đúng
loại "nhắc lại nguyên văn một câu đã nói ở đoạn trước, ở ngữ cảnh mới, không bình luận thêm" mà
bible liệt là cụm NÊN dùng.

### C.1 — C7 nối C5 → C8 được không? **ĐƯỢC, và nối trọn cả ba mắt xích.**

| Mắt xích hụt giữa C5 và C8 | C7 trả lời |
|---|---|
| **Aureole là gì, ở đâu, từ đâu ra** | **Trả lời trọn.** Tên chương P03: "Vùng đất linh hồn yên nghỉ". Tên riêng in rõ ở P23-b: **Aureole**. Vị trí: **Ende, lục địa phía bắc** (P21-f), **chính là nơi toà lâu đài Quỷ Vương đứng** (P22). Nguồn gốc thông tin: **ghi chú của pháp sư vĩ đại Flamme**, tìm thấy trong phế tích ở **lưu vực Voll** (P19-b, P20-d). |
| **Vì sao lại là "nơi nói chuyện được với Himmel"** | **Trả lời trọn.** P20-d: Flamme chép rằng ở đó bà "đã tiếp xúc với những người bạn cũ". P23-b: Eisen nói thẳng mục đích — "rồi nói chuyện với Himmel nhé". Động cơ có từ P15-f: câu Frieren hỏi ở tang lễ 30 năm trước. |
| **Vì sao C8 mở ra đã thấy Eisen đi cùng đoàn, trái với C1 nơi ông từ chối vì quá già** | **Trả lời một phần — đủ để nối, nhưng KHÔNG có khung nào cho thấy ông nhập đoàn.** C7 dựng lại toàn bộ lý do: ông vẫn thấy **"còn quá sớm để chặng đường của tôi kết thúc"** (P09-e), ông đã chủ động chuẩn bị việc này bằng thư từ với Heiter (P09-f), ông vẫn đủ sức nâng bổng tảng đá khổng lồ (P14-a), và ông đi bộ suốt chuyến tìm kiếm cùng Frieren và Fern. Nhưng **chương kết thúc khi cả ba vẫn còn ở chỗ phế tích, không có cảnh lên đường chung.** Xem D.3. |
| **Câu "Cậu ta sẽ có ích với tôi đấy" trong C8** | **Câu này CÓ MẶT TRONG C7, ở P23-c**, Eisen nói ngay sau khi giao nhiệm vụ Aureole. Nhưng **trong C7 cũng không rõ "cậu ta" chỉ ai** — không có nhân vật nam thứ ba nào lên hình trong cả chương. Xem D.2. |

**Kết luận:** C7 là **bản lề trực tiếp** giữa C5 và C8. Mọi thứ C8 coi là đã biết (Aureole, mục
tiêu nói chuyện với Himmel, việc Eisen là người khởi xướng) đều được C7 dựng lên. Không còn chỗ
đứt mạch nào cần bịa.

---

## D. Chưa rõ — KHÔNG đoán

### D.1 — Nhân vật mới, chưa có trong series-bible

| Ghi trên trang | Thấy gì | CHƯA RÕ |
|---|---|---|
| **Flamme** — "pháp sư vĩ đại Flamme", "Ma pháp sư vĩ đại Flamme" (P11-a, P16-a, P19-a, P20-a) | **Nữ** (bản dịch gọi "cô ấy" ở P11-e, P16-a; cũng có chỗ gọi "ngài ấy" ở P20-c, P21-a). **Là sư phụ của Frieren** — suy ra từ chữ trên trang, không phải suy diễn: P17-c Frieren nói "vẫn lại nằm trong lòng bàn tay của **sư phụ**", P18–P19 hồi tưởng với người phụ nữ ấy khép lại đúng bằng câu "**Ma pháp sư vĩ đại Flamme này sẽ chỉ dẫn em**", và P19-e Eisen nói "**Frieren là học trò xuất sắc nhất của Flamme mà**". Ngoại hình: tóc dài bím một bên, áo trắng, quần rộng. Sống ở **thời đại nguyên thủy**, cách hiện tại **hơn một ngàn năm** (P17-c, P18-a, P20-a). Fern gọi bà là "**một anh hùng cổ đại trong lịch sử phép thuật**". | Họ · tuổi · chết ra sao · vì sao nhận Frieren làm học trò · quan hệ với Quỷ Vương · vì sao sách của bà bị làm giả nhiều · "những người bạn cũ" bà gặp ở Aureole là ai. **Trang màu P03 vẽ bà cùng Frieren bé — nhưng trên trang không in tên bà, nên đừng chú thích tên vào ảnh đó.** |
| Người phụ nữ tóc bím trong hồi tưởng P17-f → P18 và trên trang màu P03 | Chính là Flamme (nối bằng câu thoại P18-f → P19-a như trên). | Nếu QC thấy mắt xích này chưa đủ chắc thì gọi là "**sư phụ của Frieren**" — **đừng đặt tên khác**. |

### D.2 — Câu thoại không rõ chủ ngữ (P23-c, panel 110) — **ĐIỂM CẦN DUYỆT NHẤT**

Nguyên văn bản dịch: **"Cậu ta sẽ có ích với tôi đấy."**
Khung: Eisen cận mặt, ngay sau khi ông giao nhiệm vụ Aureole cho Frieren.

- **"Cậu ta" là ai — CHƯA RÕ.** Suốt 21 trang nội dung của C7 **không có nhân vật nam thứ ba nào
  lên hình hay được nêu tên** ngoài Himmel (đã mất, chỉ trong hồi tưởng) và Heiter (đã mất).
- **Câu y hệt cũng xuất hiện trong C8** theo ghi chú bàn giao. Hai khả năng, **không được chọn bừa
  cái nào**: (a) bản dịch nhóm này dịch lệch ngôi một câu kiểu "như vậy thì cũng giúp được cho
  tôi"; (b) đây đúng là một lời bóng gió về một người chưa lên hình.
- **Tuyệt đối không viết lời kể gán câu này cho Stark.** Bible đã chốt "cậu" của người kể chỉ
  Stark, nên đọc lướt rất dễ tưởng nhầm. Trong C7 **không có một chữ nào tên Stark**.

### D.3 — Eisen có nhập đoàn trong C7 không: KHÔNG THẤY CẢNH ĐÓ

Chương khép lại khi cả ba còn đứng ở chỗ phế tích, Frieren vừa nhận lời và đang than lạnh. **Không
có khung nào vẽ cảnh ba người lên đường cùng nhau, cũng không có câu thoại nào Eisen nói ông sẽ đi
theo.** Việc C8 mở ra đã thấy ông trong đoàn là **khoảng trống giữa hai chương** — lời kể C7 chỉ
được dừng ở "Frieren nhận lời", không được nói trước rằng Eisen đi cùng.

### D.4 — Hai con số thời gian không khớp nhau (P08)

- Chữ trong khung: **"28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời."**
- Thoại Eisen ngay sau đó: **"…đã trôi qua 30 năm rồi đấy nhỉ."**
- Thoại Eisen ở P15-f: **"vào cái ngày định mệnh từ 30 năm về trước"** (chỉ ngày tang lễ Himmel).

**CHƯA RÕ hai mốc này đo từ đâu.** Có thể 28 năm tính từ ngày Himmel mất còn 30 năm tính từ lần
cuối Eisen gặp Frieren, nhưng **trang không nói**. Lời kể nên **dùng đúng con số 28 năm của khung
chữ** và nếu cần trích 30 năm thì trích **nguyên văn thoại**, không gộp hai con số làm một.
*(Đối chiếu: C2 xảy ra "20 năm sau khi Himmel qua đời" → C7 cách C2 khoảng 8 năm. Đây là phép trừ
của mình, không phải chữ trên trang.)*

### D.5 — Địa danh mới, chưa có trong bible

| Tên in trên trang | Ở đâu | CHƯA RÕ |
|---|---|---|
| **Khu vực Bredt**, thuộc **các vùng trung tâm** (P08-b) | Nơi Eisen sống hiện tại — chính là chỗ căn nhà gỗ và mấy nấm mộ trong hồi tưởng P04. | Bredt là làng, vùng hay lãnh địa · có phải làng cũ của Eisen không (P04-b chỉ nói "làng của tôi đã bị quỷ dữ tấn công", **không in tên làng**). |
| **Lưu vực Voll** (P10-d, P11-e) | Nơi có cây cổ thụ trùm phế tích và cuốn ghi chú thật của Flamme. Frieren từng tới "từ xưa". | Thuộc vùng nào · vì sao Flamme chọn nơi này. |
| **Ende**, **lục địa phía bắc** (P21-f) | Nơi có Aureole; **cũng là nơi toà lâu đài Quỷ Vương đứng** (P22). | Đường đi mất bao lâu · Ende là tên lục địa, vùng hay thành phố · quan hệ giữa Aureole và lâu đài Quỷ Vương (gần nhau? trùng chỗ? trang không nói). |
| **Aureole** — "vùng đất yên nghỉ của các linh hồn" (P23-b) | Tên riêng, chỉ in **đúng một lần** trong cả chương. | Có thật hay không (chính Frieren còn nghi) · vào bằng cách nào · có phải cùng cái "thiên đường" tôn giáo của Heiter hay không — P05-b Frieren nói không thể chứng minh, P21-b Eisen nói "Thiên đường có tồn tại", hai câu này **không được gộp làm một khẳng định**. |

### D.6 — Chi tiết mơ hồ khác

- **Mấy nấm mộ ở P04:** Heiter hỏi "Đây là gia đình cậu à…?" và Eisen đáp "Làng của tôi đã bị quỷ
  dữ tấn công ấy mà." → **CHƯA RÕ đó là mộ gia đình Eisen hay mộ dân làng**, và **chưa rõ ai chôn**.
  Trang không nói tên ai.
- **"Rào chắn đầy uy lực" quanh cây và phế tích (P17-a):** **chưa rõ ai dựng** (rất có thể là
  Flamme, nhưng trang không viết) và **chưa rõ nhóm đã phá hay đi vòng** — không có khung nào vẽ
  cảnh phá rào.
- **Cuốn ghi chú "tự từ từ mở ra" (P20-b):** cơ chế là gì, còn bao nhiêu trang chưa mở, **trang
  không nói**. Đừng viết là "cuốn sách chỉ mở dần theo thời gian" như một luật.
- **Ai nói câu nào ở vài chỗ hồi tưởng P04–P07:** một số bóng thoại không có đuôi chỉ rõ người nói
  (nhất là "Cậu đang làm gì vậy?" ở P04-c và "Ừm." ở P07-f). Đã gán theo mạch hội thoại và theo
  câu đối chứng ở P05-a, nhưng **nếu QC không chắc thì viết lời kể không nêu tên người nói**.
- **Từ "ma lực" không xuất hiện trong C7.** Chương này dùng "phép thuật", "rào chắn đầy uy lực".
  Đừng chèn "ma lực" vào chỗ trang không có.
- **Trang P03 (màu) và P16-g, P19-b, P22** là bốn khung đẹp nhất chương → ưu tiên làm hook /
  thumbnail. **P22 là trang đôi, phải PAN ngang.**

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** — 114 panel trên 21 trang nội dung (P03–P23). Xin soi kỹ ba chỗ:
   panel 92 (`P19-b`, cuốn sách lơ lửng và vế "…sẽ chỉ dẫn em"), panel 99 (`P20-d`, Flamme giữa
   các linh hồn), panel 107 (`P22-a`, trang đôi lâu đài Quỷ Vương). Ba khung này gánh cả chương.
2. **Tên nhân vật đúng chưa?** — Đã dùng đúng Frieren · Himmel · Heiter · Eisen · Fern theo bible.
   Cần duyệt hai điểm: (a) **Flamme là sư phụ của Frieren** — mình suy từ ba chỗ chữ in
   (P17-c "sư phụ" + P18-f→P19-a "Ma pháp sư vĩ đại Flamme này sẽ chỉ dẫn em" + P19-e "học trò xuất
   sắc nhất của Flamme"), nếu anh thấy chưa đủ chắc thì gọi là "sư phụ của Frieren"; (b) **"Cậu ta"
   ở P23-c chưa xác định được là ai — mình KHÔNG gán cho Stark** (mục D.2).
3. **Trọng số hợp lý chưa?** — Mình để **bốn đỉnh TS 3** (lý do của Eisen · câu sư phụ khớp sau
   ngàn năm · ghi chú Flamme · lời nhờ cậy Aureole) cộng **cú lật trang đôi P22**. Chương này thoại
   dày và hai lớp hồi tưởng, nên số panel TS 3 nhiều hơn mức thường — anh xem có cần hạ bớt cụm
   P04–P07 (hồi tưởng cầu nguyện) xuống không, vì đoạn đó đẹp nhưng chỉ là nền cho câu "Bởi vì làm
   vậy thì sẽ tốt hơn mà" quay lại ở P21-c.

**Chưa sang `/manga-narration`.**
