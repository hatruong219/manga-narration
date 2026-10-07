# BEAT SHEET — FRN Chapter 2 · "Lời nói dối của tư tế"

Nguồn ảnh: `truyen/FRN/prepare/C2/pages-clean/` · Bible: `truyen/FRN/series-bible.md`
Trạng thái: **ĐỌC HIỂU XONG — chưa viết lời kể.** Chờ user duyệt.

---

## A. Kiểm tra đầu vào

### A.1 — Ảnh đã nhận

Nhận **37 file**, `FRN_C2_P01.jpg` → `FRN_C2_P37.jpg`, đánh số liên tục, **không thiếu trang nào**.
Đã đọc **hết 37 trang theo đúng thứ tự P01→P37**, không nhảy cóc (đọc theo 10 lô nhỏ vì Read tool
giới hạn số ảnh mỗi lượt; kiểm lại cuối cùng: 37/37).

### A.2 — Trang BỎ (không phải nội dung truyện)

| File | Là gì | Xử lý |
|---|---|---|
| `FRN_C2_P01` | Banner quảng cáo bộ khác + logo **7 FINGERS TEAM** + link facebook | **BỎ** |
| `FRN_C2_P02` | Trang credit nhóm dịch (TRANSLATOR Credemoe · EDITOR Yahari · PROOFREADER/QC Credemoe) | **BỎ** |
| `FRN_C2_P37` | Banner **12 FINGERS TEAM** + quảng cáo `truyenqqq.com` | **BỎ** |

→ Nội dung thật = **34 trang giữa, P03–P36** (khớp mục 5 của bible).
`FRN_C2_P03` là **trang tên chương màu** ("Chương 2 · Lời nói dối của tư tế") — không có sự việc,
không tính vào beat truyện, nhưng **giữ lại làm hook/thumbnail** (bible mục 5).

→ **Beat truyện đếm từ P04 đến P36 = 33 trang, 163 khung.**

### A.3 — clean-pages.py đã cắt bao nhiêu px

Đối chiếu `pages/` với `pages-clean/`:

| File | Gốc | Sau clean | Cắt |
|---|---|---|---|
| `FRN_C2_P01` | 900×1075 | 900×585 | **−490 px** (cắt banner) |
| `FRN_C2_P36` | 900×1291 | 900×1277 | **−14 px** |
| `FRN_C2_P37` | 900×976 | 900×946 | **−30 px** |
| 34 file còn lại (P02–P35) | 900×1291 (P02: 900×720) | y nguyên | **0 px** |

Lưu ý: P36 bị cắt 14 px ở đáy, nhưng khung cuối của P36 là **khoảng trời trống** (chỉ có bong bóng
"Vậy giờ chúng ta đi chứ?" nằm cao hơn) → **không mất nội dung**. P01 và P37 dù sao cũng BỎ.
Bản scan **không có watermark site đè lên tranh** — khớp bible.

### A.4 — Chiều đọc: PHẢI → TRÁI (manga Nhật nhiều panel/trang)

Đây **không phải webtoon**. Panel trong beat sheet dưới đây được đánh số theo **tier (hàng ngang)
từ trên xuống, trong mỗi tier đi từ khung PHẢI sang khung TRÁI**; bong bóng trong cùng một khung
cũng đọc phải→trái. **Bằng chứng đã xác minh trong ảnh:**

1. **P04-a** — hai hộp dẫn truyện trong cùng một khung: hộp *bên phải* là "20 năm đã trôi qua kể từ
   lúc Anh hùng Himmel qua đời.", hộp *bên trái* là "Các vùng trung tâm, ngoại ô của Thánh Thành,
   Strahl." Mốc thời gian phải đọc trước địa danh → trái→phải là vô nghĩa.
2. **P04, tier 2** — khung *phải*: Frieren đi một mình, "Mình lúc nào cũng bị lạc ở trong khu rừng
   này thì phải...?"; khung *trái*: Fern xuất hiện sau lưng, "Chị đang tìm gì sao ạ?" Người lạ chỉ
   có thể xuất hiện **sau** khi Frieren đã lạc.
3. **Câu bị cắt đôi qua hai bong bóng, vế đầu luôn nằm bên phải** — P12-e: "Cô bé đã phải khổ luyện
   đến nhường nào..." (phải) / "khi còn trẻ thế này vậy?" (trái). P34-a: "Vậy thì mình cũng," (phải)
   / "Nghĩ là sẽ làm vậy." (trái).
4. **Câu bị cắt đôi qua hai KHUNG, vế đầu ở khung phải** — P36: khung phải "Ta chỉ đơn thuần là bị
   lừa." → khung trái "Bởi cái đồ tư tế thúi này mà thôi."
5. **Số trang in trên ảnh đổi mép trái/phải xen kẽ** (P04 in "2" ở mép trái, P05 in "3" ở mép phải,
   P06 "4" trái, P07 "5" phải…) = trang in hai mặt của sách giấy, không phải dải cuộn dọc.
   Đồng thời xác nhận công thức của bible: **số in trên ảnh = số thứ tự file − 2**.

→ Hệ quả sản xuất: **bắt buộc cắt theo panel + zoom**, không thả nguyên trang lên khung 9:16.

### A.5 — Thuật ngữ chốt (theo bible)

Cột "Sự việc" dùng **Quỷ Vương** và **ma lực**. Bản dịch trong ảnh có dùng "mana" ở **P14-d** —
giữ nguyên trong cột trích thoại vì đó là nguyên văn, nhưng **lời kể phải quy về "ma lực"**.
Hậu tố `-sama` chỉ giữ khi trích nguyên thoại của Fern.

---

## B. Beat Sheet

**Quy ước:** `P{số file}-{a,b,c…}` · TS 3 = khoảnh khắc quyết định · 2 = trung bình · 1 = chuyển tiếp.
Panel đánh theo chiều đọc phải→trái (xem A.4). Trang P03 là trang tên chương — không tính beat.

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| — | P03 | **Trang tên chương** (màu): Frieren ngồi dựa gốc cây trong rừng, giở tấm bản đồ. Không có sự việc. | "Chương 2 · Lời nói dối của tư tế" | tĩnh, mở màn | — |
| 1 | P04-a | Toàn cảnh thung lũng, Thánh Thành Strahl ở xa. Hai hộp dẫn đặt mốc thời gian và địa điểm. | "20 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời." | trầm, đặt mốc | 3 |
| 2 | P04-b | Frieren xách vali đi một mình trong rừng, không biết mình đang ở đâu. | "Mình lúc nào cũng bị lạc ở trong khu rừng này thì phải...?" | lơ đãng | 1 |
| 3 | P04-c | Một cô bé tóc tím áo choàng đen bắt chuyện từ phía sau. | "Chị đang tìm gì sao ạ?" | bất ngờ nhẹ | 2 |
| 4 | P04-d | Frieren đứng lặng, chưa trả lời ngay. | "..." | ngập ngừng | 1 |
| 5 | P04-e | Cô bé hỏi lại; Frieren nói mình đang tìm nhà Heiter. Tên Heiter xuất hiện lần đầu. | "...tôi đang tìm nhà của một người tên là Heiter ấy mà." | bình thản | 2 |
| 6 | P05-a | Cô bé đoán ra Frieren là khách của nhà mình. | "Vậy thì chắc hẳn chị là khách rồi nhỉ." | thân thiện | 1 |
| 7 | P05-b | Căn nhà gỗ giữa rừng hiện ra; hai người đi lên lối mòn, có bóng người đứng ở hiên. | — | mong chờ | 1 |
| 8 | P05-c | Frieren nhìn thấy Heiter còn sống, chào bằng câu chửi yêu quen thuộc. | "Vậy ra cậu còn sống à, tư tế thúi." | mừng, giấu sau câu đùa | 3 |
| 9 | P05-d | Heiter già nua, chống gậy, đeo kính, cười đáp. | "Có vẻ như là khó có thể chết ở trong độ tuổi trẻ đẹp mắt rồi." | tự giễu | 2 |
| 10 | P06-a | Frieren khoe đã mua rượu để rót lên mộ ông, rủ uống luôn; Heiter nói đã bỏ rượu. | "Tôi đã không còn uống rượu nữa rồi." | đùa cợt → hụt | 2 |
| 11 | P06-b | Vào trong nhà. Frieren trêu chuyện nữ thần tha thứ. | "Tôi không nghĩ là nữ thần sẽ tha thứ cho cậu..." | châm chọc | 1 |
| 12 | P06-c | Cô bé bưng đồ ra bàn, im lặng phục vụ. | — | lặng lẽ | 1 |
| 13 | P06-d | Frieren hỏi về cô bé; Heiter cho biết tên **Fern**, trẻ mồ côi vì chiến tranh ở vùng phía nam. | "Đó là Fern. Cô bé là một nạn nhân bị mồ côi do chiến tranh từ vùng phía nam đấy." | thông tin nền | 3 |
| 14 | P06-e | Frieren không tin Heiter nhận nuôi vì lòng tốt — và nói thẳng ông không phải Himmel. | "Cậu đâu phải là Himmel." | sắc, vô tình đâm trúng | 3 |
| 15 | P06-f | Cận mặt Heiter, chỉ cười, không cãi. | — | giấu | 2 |
| 16 | P07-a | Heiter hỏi vì sao Frieren tới; cô nói tiện đường, và từ giờ muốn gần gũi người khác nhiều hơn. | "Từ giờ thì tôi sẽ cố gần gũi với những người mà mình bắt gặp trong chuyến đi càng nhiều càng tốt." | nối tiếp C1 | 3 |
| 17 | P07-b | Frieren nói mình nợ Heiter nhiều, tới để trả trước khi ông mất. | "...nên tôi cũng tới đây để đền đáp lại trước khi mà cậu mất nữa." | thẳng đến tàn nhẫn | 3 |
| 18 | P07-c | Heiter cúi mắt, không đáp. | — | nặng | 2 |
| 19 | P07-d | Heiter nêu thỉnh cầu: nhận Fern làm học trò, dẫn theo trên hành trình. | "Xin cậu hãy nuôi dạy học trò của tôi nhé?" | đặt vấn đề | 3 |
| 20 | P08-a | Frieren từ chối thẳng. | "Cô bé sẽ chỉ là gánh nặng mà thôi." | dứt khoát, lạnh | 3 |
| 21 | P08-b | Lý do: tỉ lệ chết của pháp sư tập sự quá cao, cô không muốn đẩy đứa trẻ bạn gửi gắm vào chỗ chết. | "Tôi không hề có ý định để một đứa trẻ... đi vào chỗ chết đâu." | bảo vệ | 3 |
| 22 | P08-c | Cận mặt Heiter, vẫn cười. | — | đã đoán trước | 2 |
| 23 | P08-d | Heiter mở cửa hầm, nói còn một thỉnh cầu khác. | "Nếu là thế thì tôi cũng còn có một thỉnh cầu khác nữa đây." | chuyển hướng | 2 |
| 24 | P08-e | Hai người xuống cầu thang tối. | — | dẫn dắt | 1 |
| 25 | P08-f | Mở ra một thư khố khổng lồ đầy kệ sách. | — | choáng ngợp | 2 |
| 26 | P09-a | Cuốn sách bìa đen có vòng phép đặt trên bàn; Heiter nói đào được từ mộ pháp sư Ewig. | "Tôi đã đào thứ này từ mộ của pháp sư Ewig đấy." | bí ẩn | 3 |
| 27 | P09-b | Heiter nói trong **sách ma thuật** có ghi chép về **phép phục sinh và bất tử**. | "...những ghi chép về phép phục sinh và bất tử đó." | mồi câu | 3 |
| 28 | P09-c | Frieren kinh ngạc; Heiter nhờ giải mã và hỏi cô làm được không. | "Cậu làm được chứ?" | thách thức | 2 |
| 29 | P09-d | Frieren lật sách, nhận ra là mật mã bằng hình ảnh, ước chừng 5–6 năm là xong. | "Mà, nếu tôi dành ra 5 hoặc 6 năm, thì chắc là sẽ được thôi." | thản nhiên (thời gian elf) | 3 |
| 30 | P09-e | Frieren hỏi ngược: giải mã xong ông định làm gì, chẳng phải ông không sợ chết sao. | "Chẳng phải là cậu không sợ cái chết đó hay sao?" | dò hỏi | 2 |
| 31 | P10-a | Heiter thú nhận **hai lý do**: trước mặt Frieren ông chỉ đang ra vẻ; và giờ ông sợ chết hơn xưa. | "Thứ hai là giờ tôi lại sợ hãi cái chết hơn cả trước kia nữa." | thú nhận trần trụi | 3 |
| 32 | P10-b | Cận mặt Heiter: ông không đòi bất tử, chỉ xin thêm chút thời gian. | "Tất cả những gì tôi muốn chỉ là có thêm chút thời gian nữa mà thôi." | tha thiết | 3 |
| 33 | P10-c | Heiter viện Kinh Thánh để bào chữa; Frieren chửi yêu. | "Đồ tư tế thúi." | đùa che đậy | 2 |
| 34 | P10-d | Heiter cài thêm điều kiện thật: rảnh thì dạy Fern chút phép thuật. | "Cậu dạy Fern chút phép thuật với nhé?" | cài cắm (mấu chốt cú lật) | 3 |
| 35 | P11-a | Frieren ngẫm rồi chấp nhận nửa vời. | "Mà, nếu chỉ có thể, thì..." | nhượng bộ | 2 |
| 36 | P11-b | Khung lớn: vách đá dựng đứng, một tảng đá khổng lồ nằm trên mỏm — nơi Fern luyện tập. | — | rộng, lặng | 2 |
| 37 | P11-c | Frieren rẽ bụi rậm tìm thấy Fern. | "Ra là ở đây à." | tìm kiếm | 1 |
| 38 | P11-d | Frieren than tìm mãi mới ra, hỏi Fern lúc nào cũng tập trong rừng à. | "Tìm em khổ sở thật đấy." | bắt đầu gần gũi | 2 |
| 39 | P12-a | Fern hỏi lại, kể Heiter cũng bảo sự hiện diện của em rất yếu. | "Heiter-sama cũng thường nói rằng sự hiện diện của em quả thực là rất yếu." | thật thà | 2 |
| 40 | P12-b | Fern cho rằng đó là điều tốt. | "Nhưng chẳng phải đó là một điều tốt sao ạ?" | điềm tĩnh | 2 |
| 41 | P12-c | Frieren đồng ý. | "Đúng vậy nhỉ." | công nhận | 1 |
| 42 | P12-d | Nội tâm Frieren: hầu như không dò được **ma lực** của Fern, và cô bé đã nắm hết nền tảng pháp sư. | "Quả nhiên là hầu như không thể phát hiện được ma lực." | đánh giá | 3 |
| 43 | P12-e | Frieren tự hỏi Fern đã khổ luyện đến mức nào khi còn nhỏ thế này. | "Cô bé đã phải khổ luyện đến nhường nào... khi còn trẻ thế này vậy?" | chớm xót | 3 |
| 44 | P13-a | Fern chỉ tảng đá trên vách: Heiter bảo xuyên thủng được nó thì em tự lo được cho bản thân. | "...em có thể tự lo cho bản thân một khi mà xuyên thủng được tảng đá đằng kia." | **đặt điều kiện — hạt giống của cả chương** | 3 |
| 45 | P13-b | Frieren hiểu ra Heiter đã tính cả chuyện này. | "Vậy ra Heiter cũng biết... Về mấy thứ đấy à-..." | thoáng nghi | 2 |
| 46 | P13-c | Khung lớn: một luồng phép bắn đi về phía vách đá (Fern thi triển — xác định qua thoại P14-d). | — | căng | 2 |
| 47 | P13-d | Luồng phép băng ngang trời về phía tảng đá. | — | chờ đợi | 1 |
| 48 | P14-a | Người thi triển hạ tay, che mắt nhìn theo. | — | theo dõi | 1 |
| 49 | P14-b | Vệt phép tan dần thành bụi. | — | hụt | 1 |
| 50 | P14-c | Toàn cảnh: luồng phép tan giữa không trung, không chạm tới vách đá bên kia. | — | thất bại | 2 |
| 51 | P14-d | Fern giải thích **mana** của em phân rã trước khi tới nơi; Frieren xác nhận. | "Mana của em đã phân rã và không thể chạm tới được..." *(lời kể dùng "ma lực")* | bình tĩnh nhận khuyết | 3 |
| 52 | P14-e | Fern hỏi vậy phải luyện thế nào. | "Vậy giờ em phải luyện tập như thế nào đây ạ?" | cầu thị | 2 |
| 53 | P15-a | Frieren hỏi ngược một câu trước: em có thích phép thuật không. | "Em thích phép thuật chứ?" | dò lòng | 3 |
| 54 | P15-b | Fern đáp dè dặt. | "Cũng có phần nào ạ." | kín | 2 |
| 55 | P15-c | Frieren mỉm cười, nhận là cùng hội cùng thuyền. | "Vậy là chúng ta cùng hội cùng thuyền rồi." | ấm lên | 3 |
| 56 | P15-d | Frieren lên mỏm đá, bắt đầu dạy: phép thuật tầm xa có **3 yếu tố** phải kết hợp. | "...có tới 3 yếu tố cần thiết phải kết hợp đối với pháp sư đấy." | vào việc | 2 |
| 57 | P15-e | Khung trời trống ở đáy trang, cắt ngang lời giảng (truyện không liệt kê 3 yếu tố). | — | ngắt | 1 |
| 58 | P16-a | Montage: Frieren ngồi trong thư khố, vẽ vòng phép bên chồng sách — việc giải mã bắt đầu. | — | miệt mài | 2 |
| 59 | P16-b | Rừng đầy nắng, Frieren ngồi trên đá đọc sách, Fern lội dưới suối. | — | êm | 1 |
| 60 | P16-c | Mùa đông, hai người đi trong tuyết cạnh một người tuyết. | — | thời gian trôi | 2 |
| 61 | P16-d | Dưới gốc cây lớn, Fern tạo ra ngọn lửa nhỏ trong lòng bàn tay, Frieren ngồi trên đá nhìn. | — | tiến bộ | 2 |
| 62 | P16-e | Hai thầy trò hơ tay bên chậu lửa giữa tuyết. | — | gần gũi | 1 |
| 63 | P16-f | Heiter và Fern bên kệ sách trong thư khố. | — | đời thường | 1 |
| 64 | P16-g | Bên suối, Frieren ngồi xổm vẽ vòng phép dưới đất cho Fern xem. | — | dạy dỗ | 1 |
| 65 | P17-a | Montage tiếp: Frieren cặm cụi ở bàn giữa thư khố. | — | bền bỉ | 1 |
| 66 | P17-b | Heiter và Fern ngồi ăn cơm trong nhà. | — | ấm | 1 |
| 67 | P17-c | Frieren nằm gục giữa đống giấy tờ dưới chân kệ sách. | — | kiệt sức | 2 |
| 68 | P17-d | Tuyết rơi; Fern giơ gậy tập bắn, Frieren đứng xem. | — | kiên trì | 2 |
| 69 | P17-e | Heiter đưa ngón tay lên môi ra hiệu im lặng với Fern: Frieren đang ngủ gục trên chồng sách. | — | trìu mến | 3 |
| 70 | P17-f | Frieren chìm trong hồ nước giữa rừng. | — | lạ, tếu | 1 |
| 71 | P17-g | Thư khố, tường đã dán kín ghi chú giải mã. | — | thời gian tích lại | 2 |
| 72 | P18-a | Nhìn từ trên xuống: thư khố ngập sách vở. Heiter hỏi việc huấn luyện Fern có suôn sẻ. | "Việc huấn luyện Fern vẫn diễn ra suôn sẻ cả chứ?" | thăm dò | 2 |
| 73 | P18-b | Frieren: **4 năm** mà Fern đã chạm ngưỡng người thường mất **10 năm**; và cô bé dốc sức quá mức. | "Chỉ trong có 4 năm, mà cô bé đã chạm tới ngưỡng... 10 năm lận." | vừa khen vừa lo | 3 |
| 74 | P18-c | Heiter gạt đi, nói đó là vì cô bé yêu phép thuật. | "...tình yêu phép thuật của đứa trẻ ấy nhiều đến nhường nào đấy nhỉ?" | lảng | 2 |
| 75 | P18-d | Cận mặt Frieren, không tin lời đó. | — | nghi | 2 |
| 76 | P18-e | Frieren: dù vậy vẫn còn xa mới tới lúc Fern tự lo được cho bản thân. | "...vẫn còn cả một chặng đường dài trước khi cô bé có thể tự lo cho bản thân mình đấy." | chưa biết mình vừa nói gì | 3 |
| 77 | P19-a | Cận mặt Heiter, im lặng. | — | ngầm tính | 2 |
| 78 | P19-b | Frieren nói mình cũng sắp giải mã xong sách ma thuật; Heiter chỉ "Vậy à." | "Vậy à." | nhạt một cách bất thường | 2 |
| 79 | P19-c | Cận mắt Frieren. | — | chột dạ | 2 |
| 80 | P19-d | Frieren quay lại định nói về cuốn sách — thì nghe tiếng đổ. | "Nè, Heiter, cái cuốn sách ma thuật này... có lẽ..." *(SFX: ドサッ)* | cắt ngang | 3 |
| 81 | P19-e | Heiter đổ gục xuống sàn thư khố. | "Heiter?" | **hẫng** | 3 |
| 82 | P20-a | Mưa xối xuống căn nhà gỗ. | *(SFX: ザアアア)* | u ám | 2 |
| 83 | P20-b | Trong phòng: Heiter nằm liệt giường, Fern ngồi trên ghế đẩu cạnh giường, quay lưng. | — | nặng nề | 3 |
| 84 | P20-c | Heiter bảo Frieren đừng làm mặt như thế; ông sống được tới giờ đã là phép màu. | "...Tôi còn sống được bình thường cho đến tận bây giờ đã là một phép màu rồi đấy." | buông xuôi | 3 |
| 85 | P20-d | Frieren hứa sẽ mau chóng giải mã xong; Heiter nhờ vậy. | "...Xin hãy làm vậy nhé." | hai người cùng nói dối nhau | 3 |
| 86 | P21-a | Mưa trắng trên vách đá. | — | lạnh | 1 |
| 87 | P21-b | Fern vẫn đứng luyện tập dưới mưa; Frieren đứng phía sau. | — | bướng | 2 |
| 88 | P21-c | Frieren bảo Fern nghỉ tập, Heiter đổ bệnh, mau về với ông. | "Heiter đổ bệnh rồi." | giục | 3 |
| 89 | P21-d | Fern từ chối: phải xuyên thủng được tảng đá đã. | "Em cần phải xuyên thủng được tảng đá cao đằng kia đã." | cố chấp | 3 |
| 90 | P21-e | Frieren bảo chuyện đó để sau cũng được. | "Cái đó em để sau rồi làm cũng được mà." | dỗ | 2 |
| 91 | P22-a | Fern giơ gậy, không quay lại. | "Không có cái 'sau' đó đâu ạ." | **đỉnh cảm xúc 1** | 3 |
| 92 | P22-b | Cận mặt Fern trong mưa: vì sau đó Heiter sẽ mất. | "Bởi vì 'sau' đó... Heiter-sama sẽ qua đời mất..." | vỡ ra, ghìm | 3 |
| 93 | P22-c | Frieren lặng người. | — | bị đâm trúng | 3 |
| 94 | P22-d | Toàn cảnh hai người dưới mưa; Fern nói em từng được Heiter cứu. | "Em đã được ngài ấy cứu đấy ạ." | mở hồi tưởng | 3 |
| 95 | P22-e | **HỒI TƯỞNG**: Fern lúc nhỏ, váy trắng, đứng trên đồi nhìn xuống thị trấn. | — | trống rỗng | 2 |
| 96 | P23-a | Cận đôi giày của Fern nhỏ ngay mép vực. | — | nguy hiểm | 3 |
| 97 | P23-b | Fern nhỏ đứng một mình ở mép vực đá. | — | cận kề | 3 |
| 98 | P23-c | Mặt dây chuyền mở ra: ảnh cha, mẹ và Fern lúc bé. | — | mất mát | 3 |
| 99 | P23-d | Fern nhỏ nắm mặt dây chuyền, mặt trống. | — | tê dại | 3 |
| 100 | P23-e | Có giọng người lạ phía sau: chết bây giờ thì tiếc lắm. | "Ta thấy nếu giờ mà cháu chết đi thì hẳn là sẽ tiếc lắm đó." | can thiệp | 3 |
| 101 | P23-f | Fern nhỏ quay lại; phía xa Heiter ngồi trên gốc cây. | — | ngơ ngác | 2 |
| 102 | P23-g | Fern nhỏ hỏi lại chữ "tiếc". | "...'Tiếc' ấy ạ...?" | không hiểu | 2 |
| 103 | P23-h | Heiter kể ông từng mất một ông bạn già. | "...nhưng ta cũng đã mất đi một ông bạn già đấy." | mở lòng | 3 |
| 104 | P24-a | Heiter tả người bạn đó: ngay thẳng, hướng thiện, không bao giờ bỏ rơi ai khi hoạn nạn. | "Cậu ấy luôn ngay thẳng và hướng thiện," | tôn kính | 3 |
| 105 | P24-b | Nếu người đó sống thay ông thì đã cứu được rất nhiều người. | "Thì hẳn là sẽ cứu được rất nhiều người rồi." | tự ti | 3 |
| 106 | P24-c | Heiter ngồi ôm chai rượu: khác bạn mình, ông chỉ muốn sống một đời tĩnh lặng — cho tới một ngày. | "Nhưng rồi một ngày, ta chợt nhận ra rằng..." | day dứt | 3 |
| 107 | P24-d | Khung ký ức lớn: bóng **Quỷ Vương** đội sọ ngồi trên ngai ở giữa, quanh là cảnh tổ đội ngày xưa. Nếu ông chết đi thì can đảm, ý chí, tình bạn học được từ bạn cũng mất theo. | "Nếu như mình cứ thế mà chết đi như vậy..." | hoang mang | 3 |
| 108 | P25-a | Ký ức: bốn người tổ đội đi khuất vào rừng. Chúng sẽ biến mất cùng những ký ức quý giá. | "Chẳng phải là sẽ biến mất khỏi thế giới này cùng với những ký ức quý giá đó hay sao?" | **cốt lõi bộ truyện** | 3 |
| 109 | P25-b | Fern nhỏ đứng nghe, im. | — | lắng | 2 |
| 110 | P25-c | Cận bàn tay Fern nhỏ siết mặt dây chuyền. | — | níu lại | 3 |
| 111 | P25-d | Heiter: nếu cháu còn giữ những kỉ niệm quý báu thì lúc chết chắc chắn sẽ thấy tiếc. | "Thì chắc chắn lúc chết đi sẽ thấy tiếc lắm đấy." | cứu người bằng lời | 3 |
| 112 | P26-a | **Về hiện tại**, trong mưa: Fern nói Heiter luôn sợ chết và sợ bỏ em lại một mình. | "Heiter-sama lúc nào cũng e sợ cái chết và việc phải bỏ mặc em lại một mình." | thấu | 3 |
| 113 | P26-b | Fern: ông đã làm điều đúng đắn, em không muốn ông hối tiếc vì đã cứu mình. | "Vậy nên em không muốn ngài ấy phải cảm thấy hối tiếc vì đã cứu mình." | quyết | 3 |
| 114 | P26-c | Fern: làm pháp sư hay không không quan trọng — tự lực cánh sinh mới là cách em đền ơn. | "Học được cách để tự lực cánh sinh mới chính là lòng biết ơn mà em muốn đền đáp..." | **đỉnh cảm xúc 2** | 3 |
| 115 | P26-d | Fern muốn ông nghĩ: "May mà ta đã cứu cháu", "Giờ thì mọi thứ ổn cả rồi". | "'May mà ta đã cứu cháu...', 'Giờ thì mọi thứ ổn cả rồi...'" | dịu mà nặng | 3 |
| 116 | P26-e | Cận mặt Frieren nghe xong. | — | đổi ý | 3 |
| 117 | P26-f | Frieren hỏi Fern còn nhớ những gì mình dạy không; Fern đáp còn. | "...Em vẫn còn nhớ những gì mà ta đã dạy cho chứ?" — "Dạ còn ạ." | đồng thuận | 3 |
| 118 | P27-a | Hồi tưởng khép lại: Heiter ngồi nhìn Fern nhỏ bước đi. | "Vậy thì hãy làm những gì mà mình muốn đi." | buông tay | 3 |
| 119 | P27-b | Fern hiện tại mỉm cười dưới mưa. | — | nhẹ đi | 3 |
| 120 | P27-c | Montage: Fern với tay lấy sách trên kệ cao. | — | học | 1 |
| 121 | P27-d | Fern ngồi tĩnh tâm trên tảng đá trong rừng. | — | tập trung | 2 |
| 122 | P27-e | Frieren cặm cụi giải mã trong thư khố. | — | song song | 1 |
| 123 | P27-f | Fern bay lên trong đêm cùng cây gậy. | — | tiến bộ vọt | 2 |
| 124 | P27-g | Hai thầy trò bên ngọn đèn trong thư khố. | — | đồng hành | 1 |
| 125 | P27-h | Tảng đá vẫn nằm nguyên trên đỉnh vách. | — | chưa xong | 2 |
| 126 | P28-a | Frieren ngả người trên ghế giữa núi sách, tường dán kín giấy — việc giải mã đã tới cuối. | — | cạn sức, sắp xong | 2 |
| 127 | P28-b | **Khung lớn tràn trang**: Fern vươn tay, một vòng phép khổng lồ lao đi. (Để HOLD, đừng cắt nhỏ.) | — | **đỉnh hành động** | 3 |
| 128 | P29-a | Mái nhà gỗ, chong chóng gió hình gà trống. | — | chuyển cảnh | 1 |
| 129 | P29-b | Frieren đặt cuốn sách ma thuật xuống cạnh giường Heiter. | *(SFX: パサッ)* | dứt khoát | 2 |
| 130 | P29-c | **CÚ LẬT**: Frieren tuyên bố cả phép phục sinh lẫn bất tử đều không hề được ghi chép; Heiter chỉ đáp "Hẳn là vậy nhỉ". | "Cả phép phục sinh lẫn bất tử... đều không được ghi chép lại đâu." | **lật toàn chương** | 3 |
| 131 | P29-d | Frieren hỏi ông biết à; lập luận: nếu có thật thì Ewig đã dùng rồi. | "Nếu mà có một thứ như vậy thì hẳn là Ewig đã sử dụng nó rồi, phải không nào?" | vỡ lẽ | 3 |
| 132 | P29-e | Frieren định hỏi vì sao thì Heiter cắt ngang, hỏi về Fern. | "Vậy thì tại sao cậu lại..." — "Thế Fern ra sao rồi?" | né | 3 |
| 133 | P30-a | Frieren báo cáo: còn hơi thô nhưng Fern đã ngang trình một người trưởng thành. | "...nhìn chung cũng đã cùng đẳng cấp với một người trưởng thành rồi." | công nhận | 3 |
| 134 | P30-b | Heiter cười: vậy là cô bé kịp rồi — và không còn là "gánh nặng" nữa, đúng không Frieren? | "Thế tức là không còn là gánh nặng nữa rồi, đúng không nào Frieren?" | **chốt bẫy chữ** | 3 |
| 135 | P30-c | Khung hồi tưởng lồng vào: chính câu từ chối của Frieren ở P08 được ném ngược lại. | "Cô bé sẽ chỉ là gánh nặng mà thôi." | bị dồn | 3 |
| 136 | P30-d | Frieren hiểu ra ông đã tính hết từ đầu; Heiter chỉ cười. | "...Cậu đã tính hết trước rồi à, Heiter?" — "Hahaha." | cay đắng pha nể | 3 |
| 137 | P30-e | Heiter trả công giải mã để trong ngăn kéo, xin hai người rời đi ngay trong đêm. | "Xin hãy rời khỏi nơi này cùng với cô bé trong đêm nay nhé." | dồn dập | 3 |
| 138 | P30-f | Lý do: ông không còn nhiều thời gian, không muốn Fern chứng kiến cảnh mất người thân thêm lần nữa. | "...tôi không muốn cô bé phải chứng kiến cảnh mất người thân thêm một lần nào nữa." | **đỉnh cảm xúc 3** | 3 |
| 139 | P31-a | Heiter chính thức giao Fern lại cho Frieren. | "Frieren. Tôi giao lại Fern cho cậu tiếp quản đấy." | trao gửi | 3 |
| 140 | P31-b | Frieren trách ông lại ra vẻ ta đây. | "Cậu lại tính ra vẻ ta đây nữa đấy à, Heiter?" | giận dỗi | 3 |
| 141 | P31-c | Heiter: Fern đã sẵn lòng rời đi từ lâu rồi. | "Fern đã sẵn lòng rời khỏi đây từ lâu rồi." | đã sắp xếp cả | 3 |
| 142 | P31-d | Frieren khuyên ngược: việc ông nên làm là từ biệt cô bé thật lòng và tạo thêm kỉ niệm chừng nào hay chừng ấy. | "Và hãy cố tạo nên nhiều kỉ niệm cùng với nhau được chừng nào hay chừng ấy đi nhé." | **Frieren đã học được bài học C1** | 3 |
| 143 | P32-a | Heiter nói Frieren thật là người tốt bụng. | "Frieren à, cậu quả thật là rất tốt bụng mà." | dịu | 3 |
| 144 | P32-b | Cận mặt Frieren: nước mắt chảy. | — | **đỉnh cảm xúc 4** | 3 |
| 145 | P32-c | Rừng cây; Fern đi trong nắng. | — | khoảng lặng | 1 |
| 146 | P32-d | Frieren hỏi vì sao ông lại cứu Fern. | "Sao cậu lại cứu Fern vậy?" | câu hỏi then chốt | 3 |
| 147 | P32-e | Cận cánh tay Heiter tựa mép giường, chưa đáp. | — | khựng lại | 2 |
| 148 | P33-a | Heiter trả lời. | "Nếu là Anh hùng Himmel, thì cậu ấy cũng sẽ làm vậy thôi." | **câu chốt chủ đề** | 3 |
| 149 | P33-b | Frieren, trong bóng tối, đồng ý. | "Đúng thế nhỉ." | thấm | 3 |
| 150 | P33-c | Khung lớn không thoại: Heiter và Fern cùng mỉm cười bên giường — lời từ biệt. | — | **lặng mà đau** | 3 |
| 151 | P33-d | Frieren đi trong rừng, rẽ lá. | *(SFX: ガサッ)* | rời đi | 2 |
| 152 | P34-a | Frieren đứng ở bãi đá, tự nhủ mình cũng sẽ làm như Himmel. | "Vậy thì mình cũng, nghĩ là sẽ làm vậy." | nối gót | 3 |
| 153 | P34-b | Fern đứng nhìn lên đỉnh vách — trên đó còn vệt khói. | — | hồi hộp | 2 |
| 154 | P34-c | Tảng đá khổng lồ bị xuyên thủng một lỗ lớn; chim bay quanh. | — | **điều kiện của Heiter đã hoàn thành** | 3 |
| 155 | P34-d | Cận mặt Frieren, mỉm cười. | — | tự hào | 3 |
| 156 | P35-a | Toàn cảnh mái nhà và nhà thờ mái vòm của Thánh Thành Strahl. | — | chuyển cảnh, thời gian đã qua | 2 |
| 157 | P35-b | Ba vòm cổng lớn của thánh đường, người qua lại. | — | trang nghiêm | 1 |
| 158 | P35-c | Nghĩa trang trong rừng; Frieren và Fern đứng giữa những bia mộ. | — | **Heiter đã mất** | 3 |
| 159 | P36-a | Rót rượu lên bia mộ — lời hứa từ C1 được thực hiện. | — | giữ lời | 3 |
| 160 | P36-b | Fern cảm ơn Frieren: nhờ cô mà em đã đền đáp được cho Heiter. | "Nhờ có ngài, mà em đã đền đáp được cho Heiter-sama rồi." | biết ơn | 3 |
| 161 | P36-c | Frieren mỉm cười, phủi công. | "Ta chỉ đơn thuần là bị lừa." | **cú lật cuối, nói bằng đùa** | 3 |
| 162 | P36-d | Bia mộ khắc chữ **HEITER**; vế sau của câu. | "Bởi cái đồ tư tế thúi này mà thôi." | thương tiếc giấu trong câu chửi yêu | 3 |
| 163 | P36-e | Khoảng trời trống; Frieren rủ đi tiếp. | "Vậy giờ chúng ta đi chứ?" | khép chương, mở hành trình | 3 |

**Tổng: 163 khung nội dung** (P04–P36) + 1 trang tên chương (P03).

---

## C. Điểm cao trào

Chương này có **nhiều đỉnh**, không dồn về một chỗ. Xếp theo thứ tự xuất hiện:

1. **Đỉnh cảm xúc 1 — P22-a/b:** Fern từ chối nghỉ tập. "Không có cái 'sau' đó đâu ạ. / Bởi vì 'sau'
   đó... Heiter-sama sẽ qua đời mất..." Đây là lần đầu chương này gọi thẳng cái chết ra.
2. **Đỉnh cảm xúc 2 — P26-c/d:** Fern nói lý do khổ luyện: không phải vì thích phép thuật, mà vì
   muốn Heiter nghĩ "May mà ta đã cứu cháu". Đổi nghĩa toàn bộ phần luyện tập P11–P21.
3. **Đỉnh hành động — P28-b:** khung lớn tràn trang, Fern bắn vòng phép khổng lồ. Kết quả trả ở
   **P34-c** (tảng đá thủng một lỗ). Hai khung này là một cặp, đừng tách xa nhau khi dựng.
4. **CÚ LẬT CHÍNH — P29-c → P30-f:** cả phép phục sinh lẫn bất tử **không hề được ghi chép**. Toàn
   bộ lời nhờ giải mã ở P09–P10 là cái cớ để giữ Frieren ở lại dạy Fern. Bẫy chữ đóng lại ở **P30-b**
   khi Heiter ném ngược chính câu "gánh nặng" của Frieren ở P08.
5. **Đỉnh cảm xúc 3 — P30-f:** "tôi không muốn cô bé phải chứng kiến cảnh mất người thân thêm một
   lần nào nữa."
6. **Đỉnh cảm xúc 4 — P32-b:** Frieren khóc. Đối chiếu C1-P31 (cô chỉ biết khóc **sau khi** Himmel
   chết); lần này cô khóc **trước khi** người kia mất.
7. **Câu chốt chủ đề — P33-a:** "Nếu là Anh hùng Himmel, thì cậu ấy cũng sẽ làm vậy thôi." Trả lời
   ngược cho P06-e ("Cậu đâu phải là Himmel") — cùng một câu, hai nghĩa trái nhau. Cặp P06-e ↔ P33-a
   là trục của cả chương.
8. **CÚ LẬT CUỐI — P36-c/d:** ở mộ, Frieren tổng kết bốn năm bằng "Ta chỉ đơn thuần là bị lừa. /
   Bởi cái đồ tư tế thúi này mà thôi." Và **P36-e** mở ra hành trình mới: "Vậy giờ chúng ta đi chứ?"

**Nhịp cần giữ khi dựng:** P16–P17 và P27 là montage **không thoại** — đây là chỗ để khoảng lặng,
không nhét lời. P33-c (Heiter và Fern cùng cười, không một chữ) là khung im lặng đắt nhất chương.

---

## D. Chưa rõ — KHÔNG ĐOÁN

**Do ảnh không nói rõ:**

1. **P13-c — ai là người bắn luồng phép.** Trong khung có hai người chồng lấp, người giơ tay bị các
   đường tốc độ che; ảnh 900px không phân biệt được y phục. Bản beat sheet ghi là **Fern** — căn cứ
   **thoại P14-d** ("Mana của em đã phân rã... như ngài đã thấy đấy ạ"), không phải căn cứ hình ảnh.
   Nếu dựng cần cắt cận, phải kiểm lại bằng ảnh gốc độ phân giải cao hơn.
2. **P14-a — người hạ tay che mắt nhìn theo** là Frieren hay Fern: chưa phân biệt chắc.
3. **P32-d — khung minh hoạ đi kèm câu "Sao cậu lại cứu Fern vậy?"**: trong khung là Heiter ngồi
   trong phòng và Fern đứng ở khung cửa. Chưa rõ đây là **cảnh đang diễn ra** hay **khung hồi tưởng
   lúc Fern mới tới nhà**. Đuôi bong bóng không chỉ rõ người nói trong khung.
4. **P36-a — người rót rượu lên bia** quay lưng, tóc buộc gọn, không thấy mặt và không thấy tai.
   Beat sheet ghi trung tính "rót rượu lên bia mộ". Suy đoán hợp lý nhất là **Frieren** (chai rượu
   nằm trong tay cô ở khung kế bên, và C1-P32/33 là Heiter dặn riêng cô) — **nhưng ảnh chưa xác nhận.**
5. **Chữ nhỏ trên bia mộ P36-d** dưới chữ "HEITER": **KHÔNG ĐỌC ĐƯỢC** (quá nhỏ/mờ).
6. **SFX tiếng Nhật** chỉ đọc được một phần: P19-d ドサッ (tiếng đổ), P20-a ザアアア (mưa),
   P29-b パサッ (tiếng giấy), P11-c / P33-d ガサ・ガサッ (rẽ lá). Các SFX nhỏ khác trong montage
   **KHÔNG ĐỌC ĐƯỢC**.

**Truyện cố tình chưa nói (bible mục "Chưa tiết lộ" — không được suy đoán trong video):**

7. **Ba yếu tố của phép thuật tầm xa** (P15-d) — nêu "có tới 3 yếu tố" rồi cắt sang khung trời trống,
   không liệt kê yếu tố nào.
8. **Ewig là ai** — chưa lên hình, chưa rõ nam/nữ, sống thời nào, chết ra sao, có liên quan gì tới
   Frieren không. Bible chốt gọi trung tính "pháp sư Ewig".
9. **Tuổi Fern, họ của Fern, tên cuộc chiến tranh ở vùng phía nam, cha mẹ em chết thế nào** — P23-c
   chỉ cho thấy tấm ảnh trong mặt dây chuyền, không có tên, không có lời giải thích.
10. **Quỷ Vương** — P24-d chỉ là một bóng đội sọ ngồi trên ngai trong khung ký ức tối, không thoại,
    không tên. Không được mô tả thêm gì ngoài chừng đó.
11. **Khoảng cách thời gian từ P34 tới P35** (Fern phá đá → hai người viếng mộ): chương **không nói
    Heiter mất khi nào**, cũng không cho thấy cảnh ông mất. Lời kể không được tự điền con số.
12. **Eisen** — C2 không nhắc tới ông một lần nào. Không được kéo ông vào.
13. **Frieren có định hồi sinh Himmel hay không** — P09/P10 không hề nói. Không ám chỉ.
14. **Cụm "Mà, nếu chỉ có thể, thì..." (P11-a)** — bản dịch mơ hồ (có thể là "nếu chỉ có thế").
    Không tự sửa lời dịch; nếu cần cho nghe thoại gốc thì trích đúng chữ trong ảnh.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** — 163 khung ở mục B có khớp với ảnh không, nhất là 4 chỗ đã đánh dấu
   ở mục D (P13-c, P14-a, P32-d, P36-a)?
2. **Tên nhân vật đúng chưa?** — Frieren · Himmel · Heiter · Eisen · Fern · Ewig; đại từ riêng từng
   người (Frieren "cô", Himmel "anh", Heiter/Eisen "ông", Fern "cô bé"); **Quỷ Vương** (không "Ma
   Vương") và **ma lực** (không "mana") đã thống nhất chưa?
3. **Trọng số hợp lý chưa?** — 8 điểm cao trào ở mục C có đúng là 8 điểm cần HOLD không, hay cần
   gộp bớt để vừa ngân sách 1.470–1.680 từ / 7–8 phút?

**Chưa sang `/manga-narration`.**
