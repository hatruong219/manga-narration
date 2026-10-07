# BEAT SHEET — FRN Chapter 3 · "Anh thảo lam"

> Bước ĐỌC HIỂU. **Chưa viết lời kể.** Đọc theo `.claude/skills/manga-beat-sheet/SKILL.md`,
> đối chiếu `truyen/FRN/series-bible.md` (lập từ C1+C2).
> Nguồn ảnh: `truyen/FRN/prepare/C3/pages-clean/` — 37 file, đã đọc hết P01→P37, không nhảy cóc.

---

## A. Kiểm tra đầu vào

### A.1 Danh sách ảnh đã nhận — 37/37, liên tục, KHÔNG thiếu trang

`FRN_C3_P01.jpg` → `FRN_C3_P37.jpg`, đánh số liên tục 01…37, không đứt quãng. Không có CẢNH BÁO.

| File | Kích thước (pages-clean) | Kích thước gốc (pages) | clean-pages.py đã cắt | Trạng thái |
|---|---|---|---|---|
| P01 | 900×585 | 900×1075 | **cắt 490 px** (phần dưới) | **BỎ** — banner quảng cáo |
| P02 | 900×720 | 900×720 | 0 px | **BỎ** — trang credit |
| P03 | 900×1291 | 900×1291 | 0 px | Trang tên chương |
| P04–P35 | 900×1291 | 900×1291 | 0 px | Nội dung |
| P36 | 900×1372 | 900×1372 | 0 px | Nội dung (trang cao hơn chuẩn) |
| P37 | 900×946 | 900×976 | **cắt 30 px** | **BỎ** — banner + credit |

### A.2 Ba trang BỎ — đã mở ảnh kiểm tận nơi, không suy từ kích thước

- **P01 (900×585)** — collage bìa các bộ khác (`HATSUKOI ZOMBIE`, `SHINIGAMI BOCCHAN TO KURO MAID`,
  `KOMI-SAN HA KOMYUSHO DESU`, `YOFUKASHI NO UTA`, `MURENASE! SHIITON GAKUEN`,
  `SUKINAKO GA MEGANE WO WASURETA`) + logo **7 FINGERS TEAM** + link facebook. **Không có nội dung truyện.** → BỎ
- **P02 (900×720)** — trang credit: bìa `Sousou no Frieren`, chữ Nhật 葬送のフリーレン,
  `TRANSLATOR: Credemoe · EDITOR: Yahari · PROOFREADER: Credemoe · QUALITY CHECKER: Credemoe`,
  "Tất cả các sản phẩm đều phi lợi nhuận / Giữ nguyên credit khi reup", logo 7 Fingers Team. → BỎ
- **P37 (900×946)** — bảng đen **12 FINGERS TEAM** (4/5/2020) + dải quảng cáo
  "CẬP NHẬT CHƯƠNG MỚI SỚM NHẤT TẠI WEBSITE **TRUYENQQQ.COM**". → BỎ

→ Khớp đúng khuôn lặp mỗi chương đã ghi trong bible (C1: P01/P02/P38 · C2: P01/P02/P37).
**C3 còn 34 trang nội dung: P03–P36.**

### A.3 Chiều đọc — ĐÃ XÁC MINH: **PHẢI → TRÁI** (manga Nhật)

Không suy từ "vì là manga Nhật". Bốn bằng chứng nội tại trong chính ảnh C3:

1. **P05, hàng dưới, TRONG CÙNG MỘT PANEL** — bong bóng bên **PHẢI** là câu hỏi của Fern
   ("Chúng ta chỉ làm những việc đơn giản này thôi ạ?"), bong bóng bên **TRÁI** là câu Frieren đáp
   ("Thì mạo hiểm giả là thế mà."). Hỏi trước – đáp sau ⇒ phải đọc phải→trái.
2. **P06, hàng 2** — panel phải: Fern hỏi "Chúng ta chỉ toàn tiếp thu những phép thuật kì lạ thôi ạ?"
   → panel trái: Fern nói tiếp "Frieren-sama quả thật là rất thích phép thuật nhỉ?"
   → panel dưới: Frieren đáp "Cũng có phần nào như Fern mà thôi." Chuỗi hỏi-đáp chỉ khớp theo chiều phải→trái.
3. **P11, hàng 1** — panel phải: "Quả là một câu chuyện lạ kỳ ha." → panel trái mở đầu bằng
   **"Mà ngẫm lại thì…"**. Cụm nối tiếp này về ngữ pháp chỉ có thể đứng SAU ⇒ panel trái đọc sau.
4. **P24, hàng 3** — câu **bị cắt ngang** "Ngài quả thực là hết sức bướng bỉnh đ-…" nằm ở panel
   **TRÁI CÙNG** của trang, tức là câu cuối trang. Mọi câu bị ngắt của C3 (P13 "Vậy thì tại sao ng-…",
   P14 "…thì phép thuật sẽ không th-…", P23 "…thay vì đi t-…", P33 "…đi chăng n-…") đều rơi vào
   panel trái nhất / cuối trang — đúng quy luật của chiều phải→trái.

Bổ sung: số trang in trên ảnh **đổi bên theo trang chẵn/lẻ** (P04 số "2" góc dưới-trái,
P05 số "3" mép phải, P06 số "4" góc dưới-trái, P07 số "5" mép phải…) — đúng kiểu sách đóng gáy phải.

### A.4 Đối chiếu đánh số trang

Quy tắc bible ("số trang in trên ảnh = số thứ tự file − 2") **vẫn đúng ở C3**:
file `P04` in số "2", file `P36` in số "34". Trong beat sheet này dùng **số FILE** (P04…P36).
Ba số trang tập in trong ngoặc cũng xuất hiện: `(128)` ở P12, `(139)` ở P23, `(151)` ở P35.

### A.5 Số panel

**185 panel nội dung** trên 33 trang (P04–P36), cộng 1 trang tranh tên chương (P03) = **186 khung**.

---

## B. Beat Sheet

Ký hiệu: TS = trọng số (3 = khoảnh khắc quyết định · 2 = có sức nặng · 1 = panel chuyển tiếp).
Panel đánh `a, b, c…` **theo thứ tự đọc phải→trái, trên→dưới**.

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03 (cả trang) | **TRANG TÊN CHƯƠNG.** Nhìn qua khung cửa sổ vào trong quán: Frieren cắn một quả tròn, Fern ngồi đọc bên cạnh. Ngoài cửa sổ tuyết/bụi rơi. Không có sự việc. | "Chương 3 — Anh thảo lam" | tĩnh, ấm | 1 |
| 2 | P04-a | Toàn cảnh thung lũng ruộng bậc thang, núi tuyết, một căn nhà mái ngói. Hai ô chú thích đặt mốc. | "26 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời." / "Các vùng trung tâm, khu vực Turk." | mở màn, trầm | **3** |
| 3 | P04-b | Nhìn từ trên xuống cánh đồng: một xe kéo chất đầy nông sản, ba bóng người nhỏ đang làm việc. | — | lao động thường nhật | 1 |
| 4 | P04-c | Frieren cầm một cây gậy/cán dài, dùng phép cho hàng loạt quả bí bay lơ lửng quanh mình. | — | nhẹ, hơi buồn cười | 2 |
| 5 | P04-d | Khung rộng: xe bí đã chất đầy, Fern cầm cán xẻng ở tiền cảnh, hai người khác phía xa, núi nền sau. | — | kết thúc buổi làm | 1 |
| 6 | P05-a | Frieren tuyên bố hết việc, bên cạnh là người đàn ông thấp đậm và chiếc xe bí. | "Làm đến thế thôi, Fern. Chúng ta xong việc rồi." | thoải mái | 1 |
| 7 | P05-b | Ba người đi về phía căn nhà mái ngói. | — | chuyển cảnh | 1 |
| 8 | P05-c | Trong rừng, người thuê việc cảm ơn và đưa thù lao cho Frieren và Fern. | "Cảm ơn các vị đã giúp đỡ tôi nhé." | tử tế | 1 |
| 9 | P05-d | Cận cảnh bàn tay chìa ra một cuộn giấy/cuộn vật phẩm. | "Đây là thù lao như đã hứa này." | — | 2 |
| 10 | P05-e | Hai thầy trò đi khuất vào rừng. | — | chuyển cảnh | 1 |
| 11 | P05-f | Frieren vừa đi vừa đọc tờ giấy; Fern thắc mắc công việc quá tầm thường. | Fern: "Chúng ta chỉ làm những việc đơn giản này thôi ạ?" / Frieren: "Thì mạo hiểm giả là thế mà." | tò mò / hờ hững | 2 |
| 12 | P06-a | Fern hỏi thù lao là gì; Frieren giải thích đó là phép thuật thường. | "Là loại phép thuật có thể sản xuất trà ấm à." / "Tí nữa hãy thử qua nhé." | bình thản | 2 |
| 13 | P06-b | Hồi tưởng những "thù lao" trước: phép tẩy sạch rỉ sét khỏi tượng đồng, phép biến nho ngọt thành nho chua. Fern cận cảnh mặt đơ. | "Và cả trước đó cũng là một phép thuật biến nho ngọt thành nho chua nữa ha." | khôi hài khô | 2 |
| 14 | P06-c | Fern hỏi lại, giọng hơi ngán; Frieren nhận đó là sở thích. | Fern: "Chúng ta chỉ toàn tiếp thu những phép thuật kì lạ thôi ạ?" / Frieren: "Sở thích của ta ấy mà." | ngán / thản nhiên | 2 |
| 15 | P06-d | Cận Fern — nhận xét về Frieren. | "Frieren-sama quả thật là rất thích phép thuật nhỉ?" | quan sát | 2 |
| 16 | P06-e | Hai người đi giữa rừng cây. | — | chuyển cảnh | 1 |
| 17 | P06-f | Frieren tựa gốc cây, đáp lại bằng một câu đặt Fern ngang hàng với mình. | "Cũng có phần nào như Fern mà thôi." | ấm, kín đáo | **3** |
| 18 | P07-a | Fern phản bác nhẹ. | "Hình như là có hơi khác thì phải ạ?" | không phục | 1 |
| 19 | P07-b | Frieren quay lưng đi giữa ruộng ngô, gạt đi. | "Như nhau cả thôi." | dứt khoát | 2 |
| 20 | P07-c | Khung rộng: ngôi làng trên sườn đồi, nhà cổ, núi xa. | — | mở không gian mới | 1 |
| 21 | P07-d | Một bà lão ngập ngừng nhờ việc, tự nhận không có phép thuật gì để trả công. | "Tôi là một nhà thảo dược học, nên cũng không có bất kì loại phép thuật nào có thể dạy được đâu, nhưng mà…" | ngại ngùng | 2 |
| 22 | P07-e | Frieren nhận lời, chỉ xin được dạy về rau củ vùng này. | "Cứ dạy cho chúng tôi về rau củ ở khu vực này là hữu ích lắm rồi." | rộng rãi | 2 |
| 23 | P08-a | Ba người tới một khoảnh rừng; trong rừng có một pho tượng đứng trên bệ đá khắc chữ **HIMMEL**. | "Chúng ta tới nơi rồi." | mở nút | **3** |
| 24 | P08-b | Cận mặt tượng: gương mặt Himmel mỉm cười, phủ rêu mốc. | — | hoài niệm | **3** |
| 25 | P08-c | Cận Frieren ngước nhìn tượng, mặt không đổi. | — | lặng | 2 |
| 26 | P08-d | Fern hỏi xác nhận danh tính pho tượng. | "Là tượng của Anh hùng Himmel sao?" | xác nhận | 2 |
| 27 | P08-e | Toàn thân tượng phủ rêu, cỏ mọc um; bà lão đứng dưới, than rằng mình già rồi không dọn nổi và dân làng cũng quên. | "Trông thật là thảm tệ nhỉ?" / "Và dân làng cũng chẳng có ai thèm đoái hoài đến nữa." | tủi, xót | **3** |
| 28 | P09-a | **HỒI TƯỞNG của bà lão:** một con quái vật lao xuống bậc đá, dân làng bỏ chạy. | — | kinh hoàng | 2 |
| 29 | P09-b | Một bé gái tóc tết ngã ngồi giữa gạch vỡ, giỏ đồ đổ bên cạnh — chính là bà lão thuở nhỏ. | — | tuyệt vọng | **3** |
| 30 | P09-c | Himmel (thấy từ sau lưng) đứng chắn giữa con quái vật và đứa bé, tay cầm kiếm. | "Himmel-sama đã đặt cả sinh mạng của mình để chiến đấu vì chúng tôi" / "Khi có một con quái vật đến phá làng, và rồi…" | biết ơn, nghẹn | **3** |
| 31 | P09-d | Trở lại hiện tại: bà lão nhìn pho tượng, nói lý do muốn dọn dẹp. | "Cứ để kệ thế này quả thực là quá đỗi thương tâm mà." | thương tiếc | **3** |
| 32 | P09-e | Fern quay đầu nhìn Frieren. | — | dò xét | 1 |
| 33 | P09-f | Cận nghiêng Frieren, im lặng. | — | không biểu cảm | 2 |
| 34 | P10-a | Frieren phủ nhận, gọi cảnh tượng đó là nhân quả. | "Không, đây chắc hẳn là nhân quả." / "Là lỗi của Himmel vì đã quá khoe mẽ mà thôi." | cợt nhả che giấu | **3** |
| 35 | P10-b | Pho tượng trong rừng, hai bóng người đứng nhìn. | "Khi dân làng nói rằng họ muốn tạc tượng cho cậu ta, thì đáng lẽ ra cậu ta nên từ chối mới phải." | trách yêu | 2 |
| 36 | P10-c | **HỒI TƯỞNG của Frieren:** xưởng tạc tượng. Himmel ngồi làm mẫu, loay hoay chỉnh dáng; nghệ nhân trung niên cáu; Frieren, Heiter, Eisen đứng chờ phát chán. Chữ viết tay nhỏ: "Thế này đã được chưa nhỉ? Mà tư thế này có hơi đẹp trai quá không ta?" / "Tôi đói~" / "Đủ rồi đấy, quyết nhanh lên đi!" | "Đằng này cậu ta lại mải chú tâm tới tư thế của mình những 18 tiếng lận…" | hài, ấm | **3** |
| 37 | P10-d | Trở lại: pho tượng với tư thế chống kiếm rất đơn giản, bà lão đứng cạnh. | "Và rồi cuối cùng cậu ta lại chọn cái tư thế hết sức đơn giản này." | chùng xuống | **3** |
| 38 | P10-e | Cận đôi mắt Frieren và Fern đứng cạnh nhau. | — | lặng | 2 |
| 39 | P11-a | Bà lão cười hiền, gọi chuyện tổ đội anh hùng là chuyện lạ. | "Quả là một câu chuyện lạ kỳ ha." | thích thú | 1 |
| 40 | P11-b | Bà lão sực nhớ trong nhóm anh hùng có một pháp sư elf — **nhưng không nhận ra người đang đứng trước mặt chính là cô**. | "Mà ngẫm lại thì, hình như là cũng có một pháp sư elf nữa ở trong nhóm anh hùng thì phải?" | trớ trêu | **3** |
| 41 | P11-c | Cận Frieren, thoáng cười. | — | không đính chính | 2 |
| 42 | P11-d | Frieren cầm chổi/cán dài, rủ bắt tay vào dọn. | "Giờ thì, chúng ta sửa sang lại thôi nhỉ?" | bắt việc | 2 |
| 43 | P11-e | Khung rộng núi rừng. | — | chuyển thời gian | 1 |
| 44 | P12-a | Sau khi dọn: khoảnh rừng quang, tượng Himmel sạch sẽ, ba người đứng nhìn. | — | nhẹ nhõm | 2 |
| 45 | P12-b | Bà lão cảm ơn, khen phép thuật. | "Cảm ơn các vị đã giúp bà già này nhé. Phép thuật quả thực là tuyệt diệu nhỉ." | biết ơn | 2 |
| 46 | P12-c | Khung ngang: Fern, Frieren chống gậy phép, bà lão — bà trầm trồ pho tượng sạch bong không còn vết han. | "Đặc biệt là bức tượng. Không hề có chút han gì nào luôn." | vui | 2 |
| 47 | P12-d | Bà lão đi lại quanh bệ tượng. | — | chuyển tiếp | 1 |
| 48 | P12-e | Bà lão nheo mắt, ao ước có thêm màu sắc quanh chỗ này. | "Tôi muốn có chút sắc màu quanh đây nữa." / "Có lẽ tôi nên trồng thêm ít hoa vậy." | mơ mộng | **3** |
| 49 | P13-a | Fern gợi ý Frieren dùng phép tạo luống hoa; Frieren gật, với điều kiện có loài hoa phù hợp. | Fern: "…ngài có thể sử dụng phép thuật tạo ra luống hoa mà nhỉ?" / Frieren: "Dĩ nhiên rồi." | đề xuất | 2 |
| 50 | P13-b | Hai người đứng trong rừng. | — | chuyển tiếp | 1 |
| 51 | P13-c | Frieren khựng lại giữa câu, nghĩ ra một loài hoa. | "…ấy mà khoan, có lẽ hoa **anh thảo lam** sẽ hợp nhất đấy." | chợt nhớ | **3** |
| 52 | P13-d | Fern hỏi hoa ấy trông thế nào; Frieren thú nhận chính mình cũng chưa từng thấy. | "…loại hoa đó trông như thế nào vậy ạ?" / "Ai biết. Ta cũng đã thấy bao giờ đâu." | hụt | **3** |
| 53 | P13-e | Fern bắt đầu hỏi lý do, bị cắt ngang. | "Vậy thì tại sao ng-…" | ngờ vực | 2 |
| 54 | P13-f | Pho tượng Himmel đứng giữa rừng; lời Frieren đè lên. | "Đó là loại hoa quê nhà của Himmel." | nặng, lặng | **3** |
| 55 | P14-a | Ba người trong rừng. | — | chuyển tiếp | 1 |
| 56 | P14-b | Fern vạch ra vấn đề kỹ thuật: chưa thấy hoa thì không thể dựng phép. | "Nhưng mà nếu đó là loài hoa mà ngài chưa từng nhìn thấy, thì phép thuật sẽ không th-…" | lý trí | 2 |
| 57 | P14-c | Khung ngang: bà lão mỉm cười, mắt rưng rưng — bà nhận ra cái tên. | — | xúc động | **3** |
| 58 | P14-d | Căn nhà đá phủ dây leo — nhà bà lão. | — | chuyển cảnh | 1 |
| 59 | P14-e | Cuốn sách thảo dược mở ra, trong đó ép một bông hoa khô có tên **anh thảo lam**. | "Anh thảo lam à." | reo nhẹ | **3** |
| 60 | P14-f | Trong nhà, bà lão nói tên hoa gợi lại ký ức. | "Quả là một cái tên hoài niệm nhỉ." | hoài niệm | 2 |
| 61 | P15-a | Fern đứng trong phòng, mặt căng thẳng khác thường. | — | giấu chuyện | 2 |
| 62 | P15-b | Cận hai con vật nhỏ lông xù đang gặm thức ăn trên nóc tủ. | — | ngộ nghĩnh | 1 |
| 63 | P15-c | Cận mặt Fern — cố làm mặt thản nhiên. | — | lúng túng | 2 |
| 64 | P15-d | Bà lão bên cửa sổ, kể về quá khứ khu rừng. | "Đã từ rất lâu về trước, khu rừng đó đã ngạt ngào các cánh đồng hoa đấy." | hồi tưởng | **3** |
| 65 | P15-e | Frieren hỏi tình hình hiện nay. | "Vậy giờ xung quanh đây thì sao?" | dò | 2 |
| 66 | P15-f | Bà lão nghiêng mặt, nền tối lại — loài hoa đã tuyệt diệt, hàng chục năm bà không còn thấy trên lục địa này. | "…tất cả đều đã bị tuyệt diệt." / "…trong nhiều thập kỷ rồi." | tuyệt vọng lặng lẽ | **3** |
| 67 | P16-a | Frieren tiếp nhận tin, không phản ứng. | "Ra là vậy à." | phẳng | 2 |
| 68 | P16-b | Frieren đứng ở cửa gọi Fern; Fern đang ngồi thụp, giấu tay sau lưng. | "Fern, đi thôi." | bắt quả tang | 2 |
| 69 | P16-c | Frieren đi ra, Fern đáp khẽ. | "…Vâng." | chột dạ | 1 |
| 70 | P16-d | Cận nghiêng Frieren — đã biết. | — | sắc | 2 |
| 71 | P16-e | Frieren tóm lấy Fern, ôm nhấc lên, hứa không giận. | "Em vừa giấu gì đó có đúng không nào?" / "Ta sẽ không giận đâu, nên hãy cho ta xem qua nhé." | dỗ, nghiêm | **3** |
| 72 | P16-f | Cận bàn tay hứng hai con **chuột hạt giống** mũm mĩm. | — | dễ thương | 2 |
| 73 | P16-g | Frieren gọi tên và dán nhãn "loài vật gây hại"; Fern hứa mang trả về rừng. Có chú thích của nhóm dịch: "*Không nhầm đâu, là 'Chuột hạt giống' thật đó." | "Chuột hạt giống à. Đây là loài vật gây hại vì nó ăn hạt giống đấy." / "Em sẽ mang nó về rừng ạ." | tiếc nuối trẻ con | **3** |
| 74 | P17-a | Núi rừng nhìn từ xa. | — | chuyển tiếp | 1 |
| 75 | P17-b | Hai người đi trong rừng lá rụng. | — | chuyển tiếp | 1 |
| 76 | P17-c | Frieren rủ Fern đi **tìm anh thảo lam** — dù vừa nghe nói nó đã tuyệt diệt. | "Giờ thì, Fern này, chúng ta đi tìm anh thảo lam nhé?" | ngang bướng | **3** |
| 77 | P17-d | Fern hỏi lại cho chắc. | "Ngài nghiêm túc thật đấy ạ?" | ngỡ ngàng | 2 |
| 78 | P17-e | Frieren biện hộ "mới gần đây thôi"; Fern chỉnh lại đó là hàng chục năm. | "Chỉ mới dạo gần đây thôi…" / "Đó là cả hàng dài thập kỷ rồi đấy ạ." | lệch cảm nhận thời gian | **3** |
| 79 | P17-f | Khung tối, một bông anh thảo lam vẽ nổi — Frieren nêu logic: tìm được mẫu vật sống thì tiếp thu được phép tạo ra nó. | "…thì sẽ tiếp thu được phép thuật tạo ra anh thảo lam đấy." / "Nhưng đáng để tìm kiếm mà." | quyết | **3** |
| 80 | P18-a | Fern hỏi thẳng động cơ. | "Ngài làm chuyện này vì Himmel-sama sao ạ?" | dò thật lòng | **3** |
| 81 | P18-b | Frieren phủ nhận dứt khoát, nhận là vì chính mình. | "Không, chắc như đinh đóng cột là vì ta mà thôi." | chối, mơ hồ | **3** |
| 82 | P18-c | Đi tìm: gặp một con rùa lớn giữa bụi hoa trắng. | — | lặn lội | 1 |
| 83 | P18-d | Ba người chụm đầu tra cuốn sách thảo dược trong nhà bà lão, có lọ mẫu trên bàn. | — | nghiên cứu | 2 |
| 84 | P18-e | Frieren ngồi xổm soi một bông hoa lạ, Fern ghi chép. | — | kiên nhẫn | 1 |
| 85 | P18-f | Trong phòng trọ, Frieren nằm vật ra sàn; Fern đứng ở cửa nhìn. | — | mệt, buồn cười | 2 |
| 86 | P19-a→g | **MONTAGE KHÔNG LỜI (7 panel).** Hai người đi trên phố làng; hai bóng áo trắng lùng sục trong rừng; trong phòng; Frieren đổ nguyên liệu vào vạc lớn cùng bà lão, Fern ló ở cửa; toàn cảnh làng đổi mùa; Frieren ngồi bệt dưới gốc cây, Fern đứng cạnh; rừng lá rụng dày. | — | thời gian trôi, mỏi mòn | 2 |
| 87 | P20-a | Trên đường rừng, Fern chốt mốc: đã nửa năm đi tìm. | "Frieren-sama, đã được nửa năm kể từ lúc chúng ta tìm kiếm anh thảo lam rồi đấy ạ." | kiệt kiên nhẫn | **3** |
| 88 | P20-b | Frieren thản nhiên, còn đề nghị **mở rộng** phạm vi tìm. | "Chúng ta có nên mở rộng thêm phạm vi tìm kiếm không nhỉ?" | vô tư tàn nhẫn | **3** |
| 89 | P20-c | Cận Fern, im lặng. | "…" | nuốt lời | **3** |
| 90 | P20-d | Ngôi nhà đá phủ dây leo của bà lão. | — | chuyển cảnh | 1 |
| 91 | P20-e | Fern đứng ở cửa — lần này đi **một mình**. | "Ôi chà, hiếm khi mới thấy cháu đến đây một mình đó." | bất thường | **3** |
| 92 | P21-a | Bà lão rót nước, nhắc đã lâu kể từ khi hai người tới làng. | "Cũng đã được một khoảng thời gian kể từ lúc cả hai đến ngôi làng này đấy nhỉ." | dẫn chuyện | 2 |
| 93 | P21-b | Cận Fern, mắt chùng. | — | nặng lòng | 2 |
| 94 | P21-c | Bà lão hỏi thẳng kết quả. | "Cháu đã tìm được anh thảo lam chưa?" | dịu | 2 |
| 95 | P21-d | Fern hỏi ngược lại — câu hỏi thật ra là dành cho chính mình. | "Bà nghĩ chúng cháu sẽ tìm được sao ạ?" | hoài nghi | **3** |
| 96 | P21-e | Bà lão im lặng, cúi mặt. | "…" | không nỡ đáp | 2 |
| 97 | P21-f | Fern quay lưng, nói ra điều đã giữ lâu: cứ đà này phải tìm vài năm, cả thập kỷ; niềm say mê phép thuật của Frieren là bất thường. | "Niềm say mê phép thuật của Frieren-sama quả thật là rất bất thường," | bức bối | **3** |
| 98 | P21-g | Bà lão ngồi nghe. | — | lắng nghe | 1 |
| 99 | P22-a | Fern nói hết: Frieren đủ mạnh để cứu rất nhiều người, không nên phí thời gian vào một thứ **không tồn tại**. | "Đáng lẽ ngài ấy không nên dành thời gian vào một thứ không tồn tại mới phải chứ ạ." | tức, thương | **3** |
| 100 | P22-b | Bà lão quay lưng, không đồng tình. | — | điềm tĩnh | 2 |
| 101 | P22-c | Bà lão đứng bên tủ, nói Frieren có cách trân trọng chuyện đó theo kiểu khác. | "Bà không nghĩ vậy đâu." / "…Frieren-san có một sự tôn trọng khác đối với chuyện đó mà thôi." | bao dung | **3** |
| 102 | P22-d | Fern hỏi mình sai ở đâu; bà lão cười gọi đó là tuổi trẻ. | "Suy nghĩ của cháu có gì sai sao ạ?" / "Quả là tuổi trẻ nhỉ." | ngỡ ngàng | 2 |
| 103 | P22-e | Bà lão nói thêm: Frieren trưởng thành hơn hẳn cả hai bà cháu. | "Và ngoài ra thì, ngài ấy còn trưởng thành hơn hẳn chúng ta cơ mà, thế nên là…" | nhắc nhở | 2 |
| 104 | P22-f | Cận bàn tay bà lão chìa ra **một túi vải nhỏ**, kèm lời khuyên nói thật lòng với Frieren. | "…nếu cháu bày tỏ những cảm xúc này đến với ngài ấy bằng cả tấm lòng, thì chắc chắn là ngài ấy sẽ hiểu mà thôi." | dịu dàng, chốt | **3** |
| 105 | P23-a | Trời mây, tán rừng. | — | chuyển cảnh | 1 |
| 106 | P23-b | Frieren và Fern ngồi trên một thân cây đổ trong rừng, hoa trắng mọc quanh. | — | tạm nghỉ | 1 |
| 107 | P23-c | Cận hai người trên thân cây. | — | sắp nói thật | 2 |
| 108 | P23-d | Cận lưng Frieren. | — | chờ | 1 |
| 109 | P23-e | Cận mắt Fern — lấy can đảm. | — | căng | 2 |
| 110 | P23-f | Fern đưa túi hạt giống, giải thích bà lão giữ lại vì tính chất dược liệu, loại này có họ gần với anh thảo lam. | "Có vẻ như đây là loại hạt giống có liên quan mật thiết đã được bà ấy lưu trữ lại vì tính chất dược liệu đấy ạ." | rụt rè | **3** |
| 111 | P23-g | Fern đề nghị **trồng loại này quanh tượng Himmel thay vì tiếp tục đi tìm** — câu bị cắt ngang. | "Nếu như chúng ta trồng chúng quanh tượng của Himmel-sama thay vì đi t-…" | cầu xin | **3** |
| 112 | P24-a | Frieren hiểu ra. | "Ta hiểu rồi, Fern à." | vỡ lẽ | **3** |
| 113 | P24-b | Frieren bước tới, đặt tay lên đầu Fern; thừa nhận mình đã làm Fern lo, và rằng thời gian này **không còn là của riêng cô nữa**. | "Đây không còn là thời gian của riêng mình ta nữa rồi." | thấm, dịu | **3** |
| 114 | P24-c | Cận Fern dưới bàn tay Frieren. | — | ngỡ ngàng | 2 |
| 115 | P24-d | Frieren ra điều kiện: tìm thêm "một chút nữa" rồi dừng. | "Chúng ta sẽ dừng lại sau khi tìm kiếm thêm chút nữa nhé." | nhượng bộ nửa vời | **3** |
| 116 | P24-e | Cận Fern, mắt tròn. | — | nghi ngờ | 1 |
| 117 | P24-f | Fern hỏi "chút nữa" là mấy năm; Frieren nói chỉ một chút thôi. | "'Chút nữa' là còn bao nhiêu năm nữa đây ạ?" / "Chỉ là một chút nữa thôi mà." | lệch thời gian, hài | **3** |
| 118 | P24-g | Frieren đưa ngón tay lên môi ra hiệu im; Fern bắt đầu mắng, bị cắt ngang. | "Ngài quả thực là hết sức bướng bỉnh đ-…" | bị chặn | 2 |
| 119 | P25-a | Cận Frieren liếc mắt sang một bên (SFX "chira"). | — | phát hiện | 2 |
| 120 | P25-b | Một con chuột hạt giống ngồi trên thân cây đổ; Fern bật thành tiếng. | "A." | ngạc nhiên | 2 |
| 121 | P25-c | Khung lớn: một con **chuột hạt giống to** đứng giữa rừng, miệng ngậm gì đó, hai người ngồi phía sau. | — | mở nút | **3** |
| 122 | P25-d | Frieren rủ đuổi theo nó. | "Chúng ta đuổi theo nó nhé?" | hứng thú | **3** |
| 123 | P25-e | Rừng cây. | — | chuyển tiếp | 1 |
| 124 | P25-f | Hai người men theo rừng. | — | đuổi theo | 1 |
| 125 | P26-a | Vừa đi Fern vừa hỏi vì sao Frieren mải tiếp thu phép thuật; Frieren nói chỉ là sở thích. | "…sao ngài lại tiếp thu phép thuật vậy ạ?" / "Đó chỉ là sở thích của ta mà thôi." | truy vấn | **3** |
| 126 | P26-b | Fern không tin. | "Trông có vẻ như không giống vậy đâu ạ." | không tin | 2 |
| 127 | P26-c | Cận Frieren khẳng định, kể trước kia mình còn sống thờ ơ và lười nhác hơn. | "Trước đây ta còn sống thờ ơ và lười nhác hơn nữa cơ." | tự trào | **3** |
| 128 | P26-d | **HỒI TƯỞNG:** vùng đất đá hoang, bốn bóng người của tổ đội đi tới. | — | quá khứ | 2 |
| 129 | P26-e | Frieren thời trẻ lơ lửng, vác gậy phép, mắt lim dim. | — | uể oải | 2 |
| 130 | P27-a | **HỒI TƯỞNG — cánh đồng anh thảo lam bạt ngàn.** Cả tổ đội bốn người đứng giữa biển hoa, cánh hoa bay. | — | choáng ngợp | **3** |
| 131 | P27-b | Himmel giơ tay hứng cánh hoa, cười. | — | rạng rỡ | **3** |
| 132 | P27-c | Heiter (đeo kính) cười "Aha ha"; một đồng đội nữa đội vòng hoa cười "Ufu fu". Có dòng chữ viết tay **KHÔNG ĐỌC ĐƯỢC** ở góc panel. | — | đùa giỡn | 2 |
| 133 | P27-d | Himmel đặt một **vòng hoa anh thảo lam** lên đầu Frieren. | — | trìu mến | **3** |
| 134 | P27-e | Cận Himmel mỉm cười nhìn cô. | — | ấm | **3** |
| 135 | P27-f | Cận Frieren đội vòng hoa, mặt không cảm xúc. | — | dửng dưng (mấu chốt) | **3** |
| 136 | P28-a | Trở lại hiện tại: Frieren ngồi xổm, gọi người đó là "một tên ngốc từng tán dương phép thuật của ta". | "Đã có một tên ngốc từng tán dương phép thuật mà ta tiếp thu được ấy mà." / "Tất cả chỉ có vậy mà thôi." | giấu sau giọng bỡn | **3** |
| 137 | P28-b | Cận Fern nghe. | — | thấm | 2 |
| 138 | P28-c | Fern nhận xét lý do ấy ngớ ngẩn. | "Đúng là một lí do hết sức ngớ ngẩn đấy ạ." | thẳng thắn | 2 |
| 139 | P28-d | Frieren đồng ý, cười nhẹ. | "Quả là vậy nhỉ." | chấp nhận | **3** |
| 140 | P28-e | Hai người tiếp tục đi trong rừng. | — | chuyển tiếp | 1 |
| 141 | P28-f | Khung lớn: một **tháp đá đổ nát** cao vút hiện ra giữa rừng, Frieren đứng dưới chân. | — | phát hiện | **3** |
| 142 | P29-a | Toàn cảnh chân tháp, một người đứng nhìn lên. | — | dò xét | 1 |
| 143 | P29-b | Cận vách tháp nứt nẻ: **con chuột hạt giống** đang leo lên các khe đá. | — | lần theo | 2 |
| 144 | P29-c | Hai người đứng trong rừng bên tháp. | — | chờ | 1 |
| 145 | P29-d | Một **cánh hoa** rơi xuống cỏ. | — | tín hiệu | **3** |
| 146 | P29-e | Frieren nhận ra vật vừa bay xuống. | "Cái đó…" / "Là cánh hoa nhỉ." | nín thở | **3** |
| 147 | P30-a | Frieren giải thích tập tính chuột hạt giống: chôn giấu thức ăn ở nơi an toàn xa kẻ thù; Fern khen chúng khôn. | "…nghe như thể là một loài vật khôn ngoan vậy ạ." | giảng giải | 2 |
| 148 | P30-b | Frieren bác lại. | "Nói thế cũng không chính xác đâu." | bẻ | 2 |
| 149 | P30-c | Frieren nói thêm: chúng giấu nhiều chỗ quá nên **quên luôn chỗ đã giấu**. | "…nên là cũng hay quên mất cả nơi mà mình đã từng giấu đó." | mỉa mai tự chiếu | **3** |
| 150 | P30-d | Bóng người nhỏ đứng dưới chân tháp, cánh hoa rơi. | — | hồi hộp | 2 |
| 151 | P30-e | Khung lớn: Frieren bay vút lên dọc thân tháp, cầm gậy phép. | — | dồn | **3** |
| 152 | P31-a | **HỒI TƯỞNG:** một đồng đội hỏi lại tên loài hoa. | "Anh thảo lam sao?" | gợi | 2 |
| 153 | P31-b | Himmel ngồi trong biển hoa cạnh Frieren, khoe đó là hoa ở quê nhà mình. | "Đó là loài hoa ở quê nhà tôi đấy. Tuyệt đẹp lắm đó nha." | tự hào, ấm | **3** |
| 154 | P31-c | Himmel thêm một câu khoe mẽ điển hình; ai đó giục khởi hành. | "Mà, cũng chẳng thể nào bằng tôi được." / "Chúng ta khởi hành thôi nhỉ?" | đùa | 2 |
| 155 | P31-d | Cận Frieren đội vòng hoa, được gọi tên. | "Frieren này." | quay lại | 2 |
| 156 | P31-e | Cận Himmel: **lời hứa** sẽ cho cô ngắm cánh đồng ấy vào một ngày nào đó. | "Tôi muốn cho cậu được ngắm nhìn nó vào một ngày nào đó." | dịu dàng | **3** |
| 157 | P31-f | Frieren đáp hờ hững, hẹn "khi nào cậu có dịp" — không biết mình vừa tiêu mất cơ hội cuối. | "Vậy à." / "Khi nào mà cậu có dịp đi nhé." | thờ ơ (đau về sau) | **3** |
| 158 | P32-a | **KHUNG TRÀN TRANG — ĐỈNH CHƯƠNG.** Đỉnh tháp đổ nát nở kín **anh thảo lam**, cánh hoa bay mù trời; Frieren lơ lửng ở mép tháp nhìn vào. | — | vỡ oà lặng | **3** |
| 159 | P32-b | Cận Frieren: đoán nó ở đây nhưng không ngờ nhiều đến thế. | "Mình cũng đã ngờ là nó sẽ ở đây rồi, nhưng mà…" / "Không ngờ là lại nhiều đến thế này." | sững | **3** |
| 160 | P32-c | Frieren đứng giữa biển hoa, nói với người đã khuất. | **"Chậm trễ quá đấy, Himmel à."** | nghẹn, trách yêu | **3** |
| 161 | P33-a | Trên đỉnh tháp, Frieren nói giờ đã có thể tạo ra anh thảo lam. | "Không ngờ chúng ta lại tìm được nó thật này…" / "Giờ thì ta có thể tạo ra anh thảo lam rồi." | nhẹ nhõm | **3** |
| 162 | P33-b | Fern thú nhận vẫn không lý giải nổi vì sao Frieren dốc cả tâm huyết vào phép thuật. | "Em vẫn chẳng thể lí giải nổi." | bối rối | **3** |
| 163 | P33-c | Frieren nói mình lại nghĩ Fern hiểu được, vì Fern chưa từ bỏ việc trở thành pháp sư. | "Bởi vì Fern vẫn chưa từ bỏ việc trở thành pháp sư mà." | tin tưởng | **3** |
| 164 | P33-d | Cận Fern phản ứng. | — | chối | 2 |
| 165 | P33-e | Fern phủ nhận: em chỉ theo bất cứ thứ gì cho em sức mạnh tự lực cánh sinh. | "Em chỉ đơn thuần là thuận theo bất cứ thứ gì miễn sao là mình có thể đạt được sức mạnh để tự lực cánh sinh mà thôi." | phòng thủ | **3** |
| 166 | P33-f | Fern nói tiếp "dù đó không phải phép thuật đi chăng…" — bị cắt. | "Dù cho đó không có phải là phép thuật đi chăng n-…" | bị chặn | 2 |
| 167 | P34-a | Frieren chìa tay, **tạo ra một bông anh thảo lam** bằng phép thuật, và chốt lại. | "…nhưng mà em đã chọn phép thuật rồi đó thôi." | dịu, sắc | **3** |
| 168 | P34-b | Cận nghiêng Fern nhìn bông hoa. | — | lặng người | **3** |
| 169 | P34-c | **HỒI TƯỞNG:** Heiter (đeo kính) ngồi sau lưng Fern bé, tay đỡ; Fern chụm hai tay tạo một quả cầu sáng, bướm bay quanh — buổi học phép đầu tiên. | — | ấm, mất mát | **3** |
| 170 | P34-d | Cận Fern hiện tại, mắt đỏ, khẽ đáp. | "…Dạ phải ạ." | đầu hàng, thừa nhận | **3** |
| 171 | P34-e | Một bóng người bay lên trên đỉnh tháp phủ hoa. | — | khép cảnh | 2 |
| 172 | P35-a | **KHUNG LỚN:** tượng Himmel trong rừng, chân tượng giờ là **cả một luống anh thảo lam nở rộ**. | — | thành quả, nghẹn | **3** |
| 173 | P35-b | Bà lão đứng giữa Frieren và Fern trong biển hoa, không ngờ đời mình còn được thấy lại anh thảo lam. | "Không ngờ lại có ngày bà già này lại được nhìn thấy anh thảo lam đấy." / "Quả thật là tráng lệ nhỉ." | mãn nguyện | **3** |
| 174 | P35-c | Bà lão cảm ơn Frieren, nói từ nay pho tượng sẽ không bao giờ bị lãng quên nữa. | "Cảm ơn ngài nhé, **Frieren-san**." / "Chắc chắn bức tượng này sẽ không bao giờ bị lãng quên nữa rồi." | biết ơn | **3** |
| 175 | P36-a | Ba người trong rừng, bà lão quay lưng đi về. | — | chia tay | 1 |
| 176 | P36-b | Frieren sực nhớ còn một việc. | "À, suýt nữa thì quên." | tinh nghịch | 2 |
| 177 | P36-c | Ba người đứng trước tượng. | — | chờ | 1 |
| 178 | P36-d | Frieren bay lên tới ngang đầu tượng. | — | dồn | 2 |
| 179 | P36-e | **CHỐT CHƯƠNG:** cận mặt tượng Himmel — trên đầu tượng là **vòng hoa anh thảo lam**, đúng kiểu anh từng đội cho Frieren. Bà lão khen đáng yêu. | "Xong." / "Ôi chà, trông đáng yêu thật đó." | trả lại món nợ 26 năm | **3** |
| 180 | P36-f | Khung rộng: làng và núi, hai người lên đường. | "Giờ thì chúng ta đi thôi nhỉ?" | khép, đi tiếp | **3** |

> **Ghi chú đếm:** bảng trên gộp 7 panel montage không lời của P19 vào một dòng (#86).
> Tổng panel thực tế: **185 panel nội dung** (P04–P36) + 1 trang tranh tên chương (P03).

---

## C. Điểm cao trào

C3 có **nhiều đỉnh**, không phải một. Xếp theo mạch:

1. **P08-e → P09-d · Đỉnh nền móng.** Pho tượng Himmel mục nát trong rừng, dân làng đã quên.
   Bà lão kể ra lý do bà không quên được: hồi bé chính bà là đứa trẻ ngã giữa đống đổ nát mà Himmel
   đứng chắn để cứu. *"Cứ để kệ thế này quả thực là quá đỗi thương tâm mà."*
2. **P10-c → P10-d · Đỉnh hài-đau.** Frieren gạt đi bằng giọng cợt nhả ("nhân quả", "lỗi của Himmel
   vì đã quá khoe mẽ"), rồi hồi tưởng 18 tiếng anh loay hoay chọn dáng — để cuối cùng chọn tư thế
   đơn giản nhất. Cùng một pho tượng, hai người nhớ hai chuyện khác hẳn nhau.
3. **P11-b · Đỉnh trớ trêu lặng.** Bà lão nhắc "hình như cũng có một pháp sư elf trong nhóm anh hùng"
   — ngay trước mặt chính pháp sư elf đó. Frieren không đính chính.
4. **P13-c → P13-f · Đỉnh khởi động.** Frieren chọn anh thảo lam, thú nhận **chính cô cũng chưa từng
   thấy nó**, rồi ba chữ đặt nền cho cả chương: *"Đó là loại hoa quê nhà của Himmel."*
5. **P18-a/b · Đỉnh câu hỏi.** Fern: *"Ngài làm chuyện này vì Himmel-sama sao ạ?"* —
   Frieren: *"Không, chắc như đinh đóng cột là vì ta mà thôi."* Câu này sẽ bị chính chương lật lại.
6. **P20-a → P22-f · Đỉnh xung đột.** Nửa năm trôi qua, Frieren đòi mở rộng phạm vi tìm.
   Fern đi gặp bà lão một mình, nói ra điều cay nhất: *"Đáng lẽ ngài ấy không nên dành thời gian vào
   một thứ không tồn tại mới phải chứ ạ."* Bà lão đáp bằng túi hạt giống và một lời khuyên.
7. **P24-b · Đỉnh quan hệ.** Frieren đặt tay lên đầu Fern:
   *"Đây không còn là thời gian của riêng mình ta nữa rồi."* — lần đầu cô tự điều chỉnh nhịp sống
   elf của mình vì một con người.
8. **P27 (cả trang) · Đỉnh hồi tưởng.** Cánh đồng anh thảo lam bạt ngàn, Himmel đội vòng hoa lên đầu
   Frieren — và cận cảnh cuối trang là khuôn mặt cô **hoàn toàn dửng dưng**. Đây là "trọng lực" của chương.
9. **P30-c · Đỉnh ẩn dụ.** Frieren nói về chuột hạt giống: *"Chúng giấu ở rất nhiều chỗ, nên là cũng
   hay quên mất cả nơi mà mình đã từng giấu đó."* Câu này mô tả chính cô.
10. **P31-e/f · CÚ LẬT NGƯỢC VỀ QUÁ KHỨ.** Himmel: *"Tôi muốn cho cậu được ngắm nhìn nó vào một ngày
    nào đó."* — Frieren: *"Khi nào mà cậu có dịp đi nhé."* Cô đã từ chối lời mời, và anh đã hết dịp.
11. **P32 (khung tràn trang) · ĐỈNH CẢM XÚC CHÍNH.** Đỉnh tháp đổ nát nở kín anh thảo lam.
    Frieren: **"Chậm trễ quá đấy, Himmel à."** — 26 năm muộn, và người trách móc không còn ai để nghe.
12. **P34-a → P34-d · CÚ LẬT VỀ FERN.** Fern khăng khăng mình chỉ chọn sức mạnh chứ không chọn phép
    thuật; Frieren tạo ra một bông anh thảo lam trong lòng bàn tay và đáp:
    *"…nhưng mà em đã chọn phép thuật rồi đó thôi."* Kèm hồi tưởng Heiter dạy Fern bé quả cầu sáng.
    Cả chương vừa kể chuyện Frieren tìm hoa, hoá ra cũng là chuyện Fern được trả lời.
13. **P36-e · CÚ CHỐT CUỐI TRANG CUỐI.** Frieren đặt **vòng hoa anh thảo lam lên đầu pho tượng Himmel**
    — trả lại đúng cái vòng hoa anh từng đội cho cô ở P27. *"Xong."*
    Đây là câu trả lời thật cho câu hỏi ở P18, và nó **lật ngược lời phủ nhận "vì ta mà thôi"**.
    Đọc thiếu trang này là hiểu sai toàn bộ chương.

---

## D. Chưa rõ — KHÔNG ĐOÁN

### D.1 Nhân vật mới ở C3, bible chưa có — **không tự đặt tên**

| Nhân vật | Những gì ảnh THẬT SỰ cho biết | Chưa rõ |
|---|---|---|
| **Bà lão nhà thảo dược học** (nhân vật khách chính của C3) | Nữ, già, tóc tết hai bên, khăn quàng cổ. Tự nhận **"Tôi là một nhà thảo dược học"** (P07). Sống trong nhà đá phủ dây leo ở làng thuộc **khu vực Turk**. Giữ cuốn sách thảo dược có **ép mẫu anh thảo lam khô** (P14) và túi hạt giống họ hàng gần (P22). Thuở nhỏ **chính là đứa bé được Himmel cứu** khi quái vật phá làng (P09). Là người duy nhất còn chăm pho tượng. Gọi Frieren là **"Frieren-san"** (P35) — khác với Fern gọi "Frieren-sama". Không nhận ra Frieren chính là pháp sư elf trong tổ đội (P11). | **TÊN — truyện không hề nói.** Tuổi chính xác. Có gia đình không. Vì sao bà biết tên loài hoa quê Himmel trong khi dân làng đã quên. Bà có bao giờ biết sự thật về Frieren hay không. |
| **Người đàn ông thuê việc ở P05** | Nam, thấp đậm, áo kẻ sọc, có xe kéo nông sản. Trả thù lao bằng một cuộn giấy/vật phẩm. Lên hình đúng 3 panel rồi biến mất. | **Tên. Có phải tộc người lùn hay không** — ảnh không nói, **không được suy từ ngoại hình.** Nghề nghiệp chính xác. |
| **Nghệ nhân tạc tượng (hồi tưởng P10)** | Nam, trung niên, ngồi tạc tượng, nổi cáu vì Himmel chỉnh dáng 18 tiếng. Chỉ xuất hiện trong một panel hồi tưởng, không có thoại bong bóng riêng. | Tên. Có còn sống ở thời hiện tại không. |
| **Quái vật phá làng (hồi tưởng P09)** | Bóng đen to, sừng cong, răng nhọn, khoác áo choàng, lao xuống bậc đá. Không thoại, không tên. | Là loại gì. **Không có bất kỳ dấu hiệu nào nối nó với Quỷ Vương — không được ám chỉ liên hệ đó.** Trận đó diễn ra năm nào. |
| **Đồng đội cười "Ufu fu" ở P27-c** | Một bóng người đội vòng hoa, đứng cạnh Heiter. Nét vẽ nhỏ, ở xa. | **Không xác định được chắc chắn là Eisen hay ai khác** — chỉ đoán theo bố cục thì không đủ. Ghi là "một đồng đội". |

### D.2 Thuật ngữ / địa danh mới — chưa có trong bible

| Mục | Bản dịch trong ảnh | Ghi chú |
|---|---|---|
| **anh thảo lam** | "anh thảo lam" (tên chương + P13, P14, P17, P31, P33, P35) | Loài hoa **quê nhà của Himmel**. Đã **tuyệt diệt** trên lục địa nhiều thập kỷ (P15). Frieren chưa từng tận mắt thấy cho tới C3. Bản dịch dùng **duy nhất một cách gọi** suốt chương — không có biến thể để phải chốt lại. |
| **khu vực Turk** | "Các vùng trung tâm, khu vực Turk." (P04) | Địa danh mới, nằm trong **các vùng trung tâm** (bible đã có cụm này). Chưa rõ Turk là vùng, hạt hay tên làng. |
| **chuột hạt giống** | "chuột hạt giống" (P16, P25, P30) | Bản dịch có chú thích riêng: *"Không nhầm đâu, là 'Chuột hạt giống' thật đó."* Loài "gây hại vì nó ăn hạt giống"; chôn thức ăn ở nơi an toàn rồi quên mất chỗ chôn. **Chính nó dẫn tới tháp hoa.** |
| **nhà thảo dược học** | "nhà thảo dược học" (P07) | Nghề của bà lão. Chưa rõ có phải là một nghề có phân cấp như "pháp sư"/"tư tế" hay không. |
| **tháp đá đổ nát ở P28–P34** | không được gọi tên | Truyện **không nói đó là tháp gì, của ai, có từ bao giờ**. Không được gọi là "tháp pháp sư", "phế tích Quỷ Vương" hay bất cứ tên nào. |

### D.3 Chi tiết mơ hồ trong chính C3

- **Thù lao ở P05 là vật gì** — chỉ thấy một cuộn giấy/cuộn vải trong tay. Được mô tả là "phép thuật
  có thể sản xuất trà ấm", nhưng hình vẽ không cho biết đó là cuộn da, giấy chép phép hay thứ khác.
- **Dòng chữ viết tay ở P27-c** (cạnh Heiter và đồng đội đang cười): **KHÔNG ĐỌC ĐƯỢC** — nét quá nhỏ
  và mờ. Không đoán.
- **Ai bay lên ở P34-e** — panel nhỏ, bóng người áo sẫm lơ lửng trên đỉnh tháp hoa, một bóng áo sáng
  đứng dưới. Suy theo màu áo thì là Fern bay còn Frieren đứng, **nhưng không đủ rõ để khẳng định.**
- **Mốc thời gian nội chương.** Chắc chắn: mở màn **26 năm sau khi Himmel qua đời** (P04);
  từ lúc bắt đầu tìm hoa tới P20 là **nửa năm** (P20-a). **Không rõ** tổng thời gian cả chương,
  cũng **không rõ** C3 cách C2 bao lâu — bible chỉ chốt C2 mở màn ở mốc 20 năm; phép trừ ra
  "6 năm sau C2" là **suy luận, không phải thứ truyện nói** → đừng đưa vào lời kể như dữ kiện.
- **Fern bao nhiêu tuổi ở C3** — vẫn chưa rõ, y như bible. Ảnh chỉ cho thấy em đã cao gần bằng Frieren.
- **Vì sao anh thảo lam tuyệt diệt** — bà lão chỉ nói "tất cả đều đã bị tuyệt diệt", không nêu nguyên nhân.
- **Vì sao riêng đỉnh tháp còn hoa** — truyện gợi ý qua tập tính chôn giấu của chuột hạt giống
  nhưng **không xác nhận thẳng**.
- **Frieren có thật sự làm việc này vì Himmel không** — cô nói "vì ta mà thôi" (P18), rồi đặt vòng hoa
  lên tượng anh (P36). Truyện **để ngỏ**, không có câu thoại nào chốt. Đừng viết lời kể như thể cô đã thừa nhận.

### D.4 Đối chiếu bible — những gì C3 KHÔNG đụng tới

- **Eisen**: sau C1 vẫn không có thông tin mới. P26-d/P27 chỉ là hồi tưởng thời tổ đội còn đủ bốn người;
  không nói gì về hiện tại của ông. Mục "Chưa tiết lộ" của bible giữ nguyên.
- **Heiter**: chỉ xuất hiện trong hai hồi tưởng (P10-c xưởng tạc tượng; P34-c dạy Fern bé).
  Không có thông tin mới ngoài những gì C2 đã kể.
- **Quỷ Vương / ma lực**: **C3 không nhắc tới Quỷ Vương một lần nào**, cũng không dùng từ
  "ma lực"/"mana" — chương này chỉ dùng **"phép thuật"**. Hai từ đã chốt trong bible vì thế
  không có xung đột mới ở C3.
- **Họ của năm nhân vật chính**: vẫn chưa có ai có họ.
- **Ý nghĩa tựa đề "Sousou no Frieren"**: C3 vẫn chưa giải thích.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** — 185 panel ở mục B có khớp với những gì bạn thấy trong ảnh không, đặc biệt
   là ba chỗ dễ đọc sai thứ tự: **P09** (hồi tưởng quái vật: hai panel nhỏ bên phải đọc trước khung lớn
   bên trái), **P23** (Fern đưa túi hạt giống trước, rồi mới tới lời đề nghị bị cắt ngang), và
   **P32** (khung tràn trang đọc trước hai panel dưới)?
2. **Tên nhân vật đúng chưa?** — Frieren · Himmel · Heiter · Fern đã lấy đúng theo bible.
   **Bà lão nhà thảo dược học được để trống tên** vì truyện không đặt tên — có duyệt cách gọi
   "bà lão nhà thảo dược học" trong lời kể không, hay muốn gọi khác? Và có đồng ý **không** suy
   nhân vật ở P05 là tộc người lùn, **không** nối con quái vật ở P09 với Quỷ Vương không?
3. **Trọng số hợp lý chưa?** — chương này có tới 13 điểm TS 3 ở mục C, trong đó **P32 (tháp hoa) và
   P36-e (vòng hoa trên tượng)** là hai đỉnh phải giữ nguyên nhịp chậm. Với ngân sách 1.470–1.680 từ,
   có cần hạ bớt TS ở cụm P19–P22 (montage + xung đột với Fern) để dồn chỗ cho P27 / P31 / P32 không?

**Không tự sang `/manga-narration`.**
