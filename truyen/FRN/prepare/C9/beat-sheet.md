# BEAT SHEET — FRN C9 「Bóng ma tử thi」

Nguồn ảnh: `truyen/FRN/prepare/C9/pages-clean/` (21 file, `FRN_C9_P01`–`P21`)
Cốt truyện: Yamada Kanehito · Minh hoạ: Abe Tsukasa (in trên P02)
Tên chương: bản dịch in thẳng trên trang màu P02 — **"Chương 9 · Bóng ma tử thi"**. Đây là chữ trong ảnh, không phải tạm dịch.
Trạng thái: **ĐỦ 21/21 trang** · **94 panel** nội dung · **2 trang BỎ** (P01, P21) · 1 trang màu tên chương (P02) giữ làm hook.

> **Chiều đọc: PHẢI → TRÁI.** Đã xác minh bằng 4 chứng cứ độc lập, ghi rõ ở mục A.
> Panel đánh `P{số file}-a`, `-b`… theo thứ tự đọc phải→trái, trên→dưới.
> **Số trang IN trên ảnh = số file − 1** (P03 in "2", P08 in "7", P14 in "13", P20 in "19").
> Khác quy tắc "− 2" mà series-bible chốt cho C1/C2, vì C9 chỉ có **một** trang banner đầu thay vì hai.
> Beat sheet này dùng **số file**.

---

## A. Kiểm tra đầu vào

21 ảnh `FRN_C9_P01`–`P21`, **liên tục, không thiếu trang.**

### Trang BỎ / trang không phải nội dung truyện

| Trang | Kích thước (clean) | Kết luận | Bằng chứng trong ảnh |
|---|---|---|---|
| **P01** | 900×585 | **BỎ** | Banner quảng cáo **7 FINGERS TEAM** + link facebook.com/sevenfingersteam, ghép ảnh 7 bộ truyện khác (Komi-san, Hatsukoi Zombie, Shinigami Bocchan…). Không có một khung FRN nào. |
| **P02** | 900×1291 | **GIỮ — KHÔNG phải trang credit** | Trang **màu**, tiêu đề gốc 葬送のフリーレン, dòng Việt **"Chương 9  Bóng ma tử thi"**, tên tác giả 山田鐘人 / アベツカサ. Tranh Frieren cầm sách mở, bóng người mờ phía sau. → **Trang tên chương, ưu tiên làm hook/thumbnail.** |
| **P21** | 900×946 | **BỎ** | Banner **12 FINGERS TEAM** (bảng đen doodle, mốc 4/5/2020) + dải xanh "CẬP NHẬT CHƯƠNG MỚI SỚM NHẤT TẠI WEBSITE TRUYENQQQ.COM" ghép nhân vật Naruto/Deku/Tanjiro. Không có khung FRN. |

> ⚠ **Sửa giả định đầu vào:** brief giao việc nói "P01, P02 và trang cuối là banner + credit, khuôn lặp 900×585 / 900×720 / 900×946".
> Đã kiểm từng file: **khuôn 900×720 không tồn tại trong C9**, và **P02 là trang màu tên chương, không phải credit**.
> Chỉ P01 (900×585) và P21 (900×946) là banner. **Nếu bỏ P02 theo giả định ban đầu là mất luôn tên chương và trang màu đẹp nhất bộ.**

### `clean-pages.py` đã cắt bao nhiêu px

| Trang | Gốc (`pages/`) | Sau clean (`pages-clean/`) | Cắt |
|---|---|---|---|
| P01 | 900×1075 | 900×585 | **−490px** (vẫn còn 100% banner → bỏ cả trang) |
| P07 | 900×1291 | 900×1281 | −10px |
| P13 | 900×1291 | 900×1281 | −10px |
| P21 | 900×976 | 900×946 | **−30px** (vẫn còn 100% banner → bỏ cả trang) |
| P02–P06, P08–P12, P14–P19 | 900×1291 | không đổi | 0px |
| P20 | 900×1372 | không đổi | 0px |

Watermark site trên trang truyện: **không có** — đúng như bible ghi.
Trang cao bất thường: **P20 = 900×1372** (trang kết, nhiều panel hơn).

### Chứng cứ chiều đọc PHẢI → TRÁI

1. **P04, hàng 2** — panel **bên PHẢI** có lời ông lão: *"Kể từ giờ thì cháu hãy trở thành một cô bé ngoan và nghe theo những gì mà Frieren dặn nhé."* rồi bỏ lửng *"Nếu không thì…"*. Panel **bên TRÁI** là Fern hỏi lại *"…'nếu không thì'?"*. Câu hỏi lại **bắt buộc** đi sau câu bỏ lửng → phải trước, trái sau.
2. **P07, hàng 1** — bong bóng **phải**: *"Trông hai vị đây có vẻ đang muốn băng qua đèo nhỉ. Không nên đâu."* → bong bóng **trái**: *"Đã có rất nhiều người mất tích khi đi qua đó đấy."* (câu giải thích cho lời cảnh báo).
3. **P12, hàng 2** — bong bóng **phải** (Frieren giảng): *"Tấn công bằng cách tập trung lượng lớn ma lực… thì sẽ dễ dàng phân tán chúng thôi."* → bong bóng **trái** (Fern chốt lại): *"Vậy là em chỉ cần bắn vào ảo ảnh của người chết thôi nhỉ."* Học trò rút kết luận **sau** lời thầy.
4. **P20, hàng 2** — ba panel, hỏi-đáp ba nhịp chạy từ **phải sang trái**: *"Frieren-sama này."* (phải) → *"Đó là ảo ảnh của Heiter-sama. Là giả mạo nhỉ."* (giữa) → *"Đúng vậy."* (trái).

Chứng cứ phụ: **số trang in so le theo kiểu sách gáy phải** — P03 in số "2" ở mép **phải**-dưới, P04 in "3" ở mép **trái**-dưới, P08 in "7" mép trái, P20 in "19" mép trái.

### ⚠ Cảnh báo ngữ cảnh (KHÔNG phải lỗi ảnh)

Site thiếu **chương 6 và 7**, `series-bible.md` mới lập từ **C1–C2**. C9 dùng ít nhất **ba** thiết lập như thể người xem đã biết mà bible chưa hề có:
**sư phụ của Frieren** · **Aureole** · **thói quen "bắn vào ảo ảnh" của Frieren**.
Đã ghi hết xuống mục D. **Không suy diễn bù cho liền mạch.**

---

## B. Beat Sheet

**P01 — BỎ** (banner 7 Fingers Team).
**P02 — trang màu tên chương** "Chương 9 · Bóng ma tử thi". Không có beat truyện; dùng làm hook/thumbnail.

### Hồi tưởng — bên giường bệnh của Heiter (P03–P05)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Khung tràn trang: phòng gỗ, một **ông lão nằm trên giường bệnh**, **Fern còn nhỏ** bưng khay cháo nóng tới, **Frieren** đứng ở khung cửa nhìn vào. Không thoại | — | tĩnh, nặng | 3 |
| 2 | P04-a | Toàn cảnh căn phòng: Fern ngồi ghế cạnh giường, Frieren đã không còn trong khung | "Fern này, không sao cả chứ?" | dò hỏi | 1 |
| 3 | P04-b | Ông lão dặn Fern nghe lời Frieren, rồi bỏ lửng câu | "…nghe theo những gì mà Frieren dặn nhé." / "Nếu không thì…" | dặn dò, gài bẫy đùa | 2 |
| 4 | P04-c | Fern nhíu mày hỏi lại vế bỏ lửng | "…'nếu không thì'?" | cảnh giác | 2 |
| 5 | P04-d | Cận mặt ông lão, cười hiền — **lời hứa gốc của cả chương** | "Ta sẽ thực thể hóa sau khi chết mất." | đùa mà thật | **3** |
| 6 | P04-e | Nhìn từ sau lưng: Fern đứng im, ông lão cười | "Hahaha." | nhẹ bẫng | 1 |
| 7 | P05-a | Fern cười tinh quái, bẻ ngược lời hứa | "Heiter-sama sẽ thực thể hóa nếu như cháu là một đứa trẻ hư ạ?" | ranh mãnh — **xác nhận ông lão = Heiter** | **3** |
| 8 | P05-b | Cận nghiêng Heiter, cười méo, giọt mồ hôi | — | bị dồn, buồn cười | 2 |
| 9 | P05-c | Nhìn từ xa: Fern quỳ cạnh giường. Heiter đòi rút lời | "Cho phép ta rút lại lời nói vừa nãy nhé." / "Cháu càng ngày càng tinh ranh hơn đấy nhỉ?" | đầu hàng | 2 |
| 10 | P05-d | Heiter xoa đầu Fern, đổi lời hứa sang vế ngược lại | "Nếu như cháu làm một cô bé ngoan, thì có lẽ là ta sẽ thực thể hóa một chút để gặp lại cháu đấy.." | dịu, hứa hẹn | **3** |
| 11 | P05-e | Cận mặt **Fern đã lớn**, mắt nhắm — cắt khỏi hồi tưởng | — | lặng | 2 |

### Hiện tại — vùng Wille (P06–P09)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 12 | P06-a | Frieren và Fern ngồi trên sàn thùng xe ngựa, Frieren đọc sách | — | đường trường | 1 |
| 13 | P06-b | Xe ngựa đi trong rừng | "Chúng ta sẽ sớm đến ngôi làng thôi." / "…Vậy ạ." | uể oải | 1 |
| 14 | P06-c | Fern ngủ gật tựa vai, giật mình dậy | "Em sao vậy?" / "Dạ không đâu ạ." | giấu chuyện | 2 |
| 15 | P06-d | Toàn cảnh núi tuyết, xe ngựa nhỏ xíu. **Hai ô chú thích mốc thời gian và địa danh** | "28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời." / "Các vùng trung tâm, vùng Wille." | trần trụi | **3** |
| 16 | P06-e | Hai người bước vào phố làng lát đá, dân làng nhìn theo | — | lạ chỗ | 1 |
| 17 | P06-f | Sạp rau quả bên đường | — | đời thường | 1 |
| 18 | P07-a | **Bà bán hàng** chặn lời, cảnh báo đừng băng qua đèo | "Đã có rất nhiều người mất tích khi đi qua đó đấy." | can ngăn | 2 |
| 19 | P07-b | Frieren hỏi thẳng có quái vật không; bà kể **người mất tích bị vong hồn bắt đi**, có người bảo đã tận mắt thấy | "Chuyện kể rằng là họ đều bị các vong hồn bắt đi mất." | đồn đại | 2 |
| 20 | P07-c | Frieren đoán là xác sống; bà bảo không biết, gợi ý **đi hỏi trực tiếp người đã thấy** | "Nếu cô tò mò thì sao không thử đi hỏi trực tiếp xem?" | đẩy việc | 2 |
| 21 | P07-d | Hai người đứng hỏi chuyện một phụ nữ trước cửa nhà, một ông ngồi bậc thềm | — | điều tra | 1 |
| 22 | P07-e | Hai người đi trong ngõ hẹp | — | chuyển tiếp | 1 |
| 23 | P07-f | Quán rượu: một người đàn ông ngồi bàn kể chuyện, Frieren và Fern đứng nghe | — | điều tra | 1 |
| 24 | P07-g | Khung dọc: hai người đi xuống bậc đá | — | chuyển tiếp | 1 |
| 25 | P08-a | Hai người dừng bên bờ tường đá nhìn ra thung lũng | "Nếu đối chiếu các thông tin lại thì…" | tổng kết | 1 |
| 26 | P08-b | Fern chống cằm, chốt điểm chung của mọi lời khai: **vong hồn là người thân đã khuất, trông y như hồi còn sống**, và chỉ vài người thấy được | "…đều y như hồi còn sống vậy." | phân tích | **3** |
| 27 | P08-c | Trước cửa nhà trọ (biển INN) | "Thế tức là không phải xác sống rồi." / "Vậy sao ạ?" | bác bỏ | 2 |
| 28 | P08-d | Khung tối: **bầy zombie và hài cốt** lúc nhúc — hình dung về "xác sống" | "'Xác sống' thường được mô tả là những xác chết được điều khiển bởi phép thuật." | ghê rợn | 2 |
| 29 | P08-e | Cầu thang nhà trọ; Frieren vặn lại lô-gic | "Nếu là xác chết thì làm gì trông như vậy được chứ." | sắc | 2 |
| 30 | P08-f | Frieren chốt: thủ phạm là **một con yêu quái hoàn toàn khác hệ thống** | "…do một con yêu quái gây ra với hệ thống hoàn toàn khác hẳn đấy." | lạnh | **3** |
| 31 | P09-a | Phòng trọ nhìn từ xa; Fern hỏi sao Frieren rành thế | "Ngài có vẻ am hiểu về chuyện này nhỉ?" | tò mò | 2 |
| 32 | P09-b | Cận nghiêng Frieren: sinh vật tà ác, **nên tránh chạm mặt** | "…cần phải thận trọng để tránh chạm mặt nó nhiều nhất có thể." | né tránh | **3** |
| 33 | P09-c | Toàn cảnh phòng trọ hai giường | "Chúng ta sẽ rời làng vào sáng mai nhé." | quyết | 1 |
| 34 | P09-d | Fern đứng, Frieren ngồi mép giường. Fern nhắc dân làng đang gặp rắc rối; Frieren ví em với Himmel | "Em nói chuyện cứ như Himmel và mấy người khác đấy nhỉ." | chạm | **3** |
| 35 | P09-e | Nhìn từ sau lưng hai người. Fern viện đúng chữ của Heiter | "Bởi vì em là một cô gái ngoan, không như Frieren-sama đấy ạ." | đắc ý — **đá ngược về P05-d** | **3** |
| 36 | P09-f | Frieren nhượng bộ, viện cớ dù gì cũng phải qua đèo | "Mà, nếu Fern muốn thì được thôi." | chịu thua | 2 |

### Vào đèo — dựng luật (P10–P14)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 37 | P10-a | Khung ngang: dãy núi đen trải dài | — | mở cảnh | 1 |
| 38 | P10-b | Hai người đi vào đường mòn vách đá | — | chuyển tiếp | 1 |
| 39 | P10-c | Đường mòn men theo suối cạn | — | chuyển tiếp | 1 |
| 40 | P10-d | Đứng giữa lòng đường đá — **đúng nơi người dân biến mất** | "Đây là nơi mà dạo gần đây người dân đều bị biến mất đấy nhỉ." | nghi ngại | 2 |
| 41 | P10-e | Cận Frieren: manh mối rải rác khắp nơi | "Có quá nhiều manh mối… rải rác xung quanh này." | đọc hiện trường | 2 |
| 42 | P10-f | Fern nhận ra có dấu vết phép thuật; Frieren quay sang **khảo bài** | "…có dấu vết của phép thuật được dùng tại đây đấy ạ." / "Vậy em có biết đây là loại phép thuật gì không?" | thầy-trò | 2 |
| 43 | P11-a | Fern trả lời **phép ảo giác**, dẫn nguồn **sách sinh thái phép thuật**: có quái vật dùng ảo ảnh để thu hút con mồi | "Là phép ảo giác đúng chứ ạ?" | tự tin | **3** |
| 44 | P11-b | Khung ngang: hai bóng người nhỏ trên lối đá giữa rừng | — | chuyển tiếp | 1 |
| 45 | P11-c | **Khung lớn tối — chân dung con quái**: mặt thú dài, quấn chuỗi hạt, tóc dài toả ra. Ruby "Einsam" trên tên dịch | **"QUỶ BÓNG MA."** / "…con quỷ kén ăn khi chỉ chọn loài người làm con mồi." | rợn | **3** |
| 46 | P11-d | Fern ngơ ngác hỏi lại cách nó săn mồi | "Có thể thu hút con người bằng thứ ấy được sao ạ?" | không tin nổi | 2 |
| 47 | P12-a | Cận Frieren, nói rõ ảo ảnh là **người yêu dấu của con mồi** | "Nó cho con mồi xem ảo ảnh của những người yêu dấu đối với mình đó." | lạnh | **3** |
| 48 | P12-b | Toàn cảnh hai người đi xa nhau trên lối đá; Frieren hạ thấp mối nguy | "…cũng chẳng là gì đối với pháp sư cả đâu." | coi thường | 2 |
| 49 | P12-c | Hai người dừng lại; Frieren dạy cách phá: **dồn lớn ma lực, bắn như ma pháp công kích** | "Vậy là em chỉ cần bắn vào ảo ảnh của người chết thôi nhỉ." | bài học | 2 |
| 50 | P12-d | Cận Frieren, mắt sắc — **câu hỏi thật sự của cả chương** | "Em làm được chứ?" | thử thách | **3** |
| 51 | P12-e | Fern đáp gọn: dĩ nhiên, vì **em biết thừa chúng là giả mạo** | "Do là em đã biết chúng đều là giả mạo cả mà." | chắc nịch — sẽ bị lật | **3** |
| 52 | P13-a | Frieren đi trước, kể chuyện mình: **đã từng bắn vào ảo ảnh sư phụ dù ngài ấy cầu xin tha mạng** | "Ta đã từng bắn vào ảo ảnh sư phụ của mình dù cho ngài ấy đã cầu xin tha mạng đấy." | phẳng lặng — **nhân vật MỚI** | **3** |
| 53 | P13-b | Fern đứng khựng, không nói gì | "…." | chấn động | 2 |
| 54 | P13-c | Toàn cảnh hai người đi trong rừng; Frieren nói đã quen việc **sư phụ cầu xin suốt** nên chẳng thấy tội lỗi | "'Quen với việc sư phụ cầu xin' tức là sao chứ ạ…" | hài đen / rùng mình | 2 |
| 55 | P13-d | Cận Frieren, tự đính chính một nửa | "Nhưng dù vậy thì đó cũng không phải là một chuyện dễ chịu gì." | nứt ra một chút | **3** |
| 56 | P13-e | Khung ngang rỗng: thung lũng đá, không người | — | khoảng lặng | 1 |
| 57 | P14-a | Khung lớn: hai người đi xuống con đường rừng rợp bóng | — | chuyển tiếp | 1 |
| 58 | P14-b | Hai người giữa rừng tối | — | chuyển tiếp | 1 |
| 59 | P14-c | Cận nghiêng Frieren trong rừng | — | căng dần | 1 |
| 60 | P14-d | **Sương mù bắt đầu dâng** | "Hình như bắt đầu có sương mù rồi đấy ạ." / "Sắp rồi đấy nhỉ." | báo hiệu | 2 |
| 61 | P14-e | Cận Frieren dặn lần cuối | "Nếu như ảo ảnh có xuất hiện, thì đừng ngần ngại mà bắn nhé." | dặn dò | **3** |
| 62 | P14-f | Fern cầm ngang gậy phép, mặt lì | — | sẵn sàng | 2 |

### Ảo ảnh (P15–P19) — cao trào

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 63 | P15-a | Khung ngang: sương dày đặc, Frieren giơ tay chặn Fern lại | — | dừng | 2 |
| 64 | P15-b | Cận nghiêng Fern — **một giọng gọi tên em vang lên** | "Fern." | lạnh sống lưng | **3** |
| 65 | P15-c | Frieren quay lại; trong sương, **một bóng người khoác áo choàng đứng im** | — | hiện hình | **3** |
| 66 | P15-d | **Khung lớn: ông lão đeo kính, áo choàng, chống gậy, mỉm cười** — ảo ảnh Heiter. Chữ nhỏ gọi tên hiện tượng | "Đây rồi…" / "Là bóng ma tử thi…" | **nhan đề chương rơi xuống** | **3** |
| 67 | P15-e | Fern nâng gậy, tự nhủ | "Thật bình tĩnh…" / "Và bắn nào." | gồng | **3** |
| 68 | P15-f | Cận mặt ảo ảnh Heiter, cười hiền, **khen đúng thứ Fern muốn nghe nhất** | "Cháu càng lúc càng ra dáng một pháp sư hơn rồi đấy nhỉ." | đòn hiểm | **3** |
| 69 | P16-a | Ảo ảnh **dùng nguyên vế hứa của Heiter thật** | "Bởi vì cháu đã trở thành một cô bé ngoan, nên ta đã quyết định là sẽ thực thể hóa lại một chút đấy." | **vòng tròn khép lại với P05-d** | **3** |
| 70 | P16-b | Cận mặt Fern, mắt mở lớn, không nhúc nhích | — | tê liệt | **3** |
| 71 | P16-c | Ảo ảnh đứng cạnh Fern nói tiếp; **độc thoại Fern nhận ra nó đang đọc ký ức của mình** | "Đây là kí ức…" / "Kẻ này… với kí ức của mình…" | vỡ ra | **3** |
| 72 | P16-d | Cận Fern, tay nắm chặt, giọng run | "Đây đều là những kí ức thân thương của mình cả…" / "…Thật là quá đỗi tàn nhẫn mà…" | đau | **3** |
| 73 | P16-e | Khung nhỏ: Frieren gọi Fern | "Fern." | kéo về | 2 |
| 74 | P17-a | Khung nhìn từ trên: ba bóng người trong sương | — | bế tắc | 1 |
| 75 | P17-b | Fern hạ gậy, đứng chôn chân trước ảo ảnh; Frieren chốt một câu | "Có vẻ vô ích rồi đây." | thất bại — **hết thử thách của Fern** | **3** |
| 76 | P17-c | Khung lớn: **một bóng người khoác choàng trắng, tóc sáng, quay lưng** hiện ra trước mặt Frieren | — | trở tay | **3** |
| 77 | P17-d | Fern nhìn sang, nhận ra | "…Himmel xuất hiện à." | sửng sốt | **3** |
| 78 | P17-e | Hai khung cận Frieren — **độc thoại thú nhận**: đã tưởng sư phụ sẽ hiện ra lần nữa | "Mình cứ ngỡ là sư phụ sẽ xuất hiện thêm lần nữa chứ…" / "Có lẽ là mình đã thay đổi chút ít mất rồi…" | **beat cảm xúc lớn nhất của Frieren** | **3** |
| 79 | P17-f | Frieren chĩa gậy, đầu gậy đã tụ sáng; ảo ảnh gọi tên cô | "Frieren." | lạnh mà run | **3** |
| 80 | P18-a | **Khung lớn cận mặt Himmel**, cười nhẹ, tự nói câu kết liễu mình | **"Bắn tôi đi."** | **đỉnh 1** | **3** |
| 81 | P18-b | Frieren nạp ma lực, đáp lại | "Himmel chắc chắn sẽ nói như vậy ha." / "Đúng rồi nhỉ." | dứt khoát, cay đắng | **3** |
| 82 | P18-c | **Khung lớn: tia phép nổ tung cả vạt rừng** (ドォォォ) | — | dứt điểm | **3** |
| 83 | P18-d | Cận mặt Fern quay sang nhìn, môi hé | — | choáng | 2 |
| 84 | P19-a | **Khung tràn trang: một hình dạng khổng lồ tóc trắng dài, thân tối, giơ tay cầm vật xích lủng lẳng** trùm lên ảo ảnh Heiter; Fern quay lưng đứng trước nó, gậy giơ cao | — | lộ nguyên hình | **3** |
| 85 | P19-b | Cận mặt ảo ảnh Heiter đeo kính, vẫn cười | — | tàn nhẫn | **3** |
| 86 | P19-c | Cận Fern, **vòng ma trận sáng lên trước mặt**, mắt ướt nhưng không chớp | — | **đỉnh 2** | **3** |
| 87 | P19-d | **Khung ngang: phát bắn xé ngang màn sương**, ảo ảnh tan | — | dứt điểm | **3** |

### Kết (P20)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 88 | P20-a | Khung ngang: bãi rừng cháy nham nhở, Frieren và Fern đứng giữa | — | hậu chiến | 2 |
| 89 | P20-b | Fern chống gậy, gọi Frieren; Frieren nói đường đèo đã an toàn | "Vậy là từ giờ đường băng qua đèo đã an toàn trở lại rồi." / "Frieren-sama này." | lửng | 2 |
| 90 | P20-c | Cận nghiêng Frieren xác nhận hộ Fern | "Đó là ảo ảnh của Heiter-sama." / "Là giả mạo nhỉ." | đỡ lời | **3** |
| 91 | P20-d | Khung nhỏ: Fern đáp gọn một tiếng | "Đúng vậy." | nén | **3** |
| 92 | P20-e | Khung dọc lớn: hai người đi tiếp dọc bờ tường đá, ra khỏi đèo | — | đi tiếp | 2 |
| 93 | P20-f | **Cận Frieren cười nhẹ** — câu chốt chương | **"Lần tới hãy đi gặp người thật nhé."** | **cú lật, ấm** | **3** |
| 94 | P20-g | Hai gương mặt cạnh nhau; Frieren nói rõ đích đến | **"Do là chúng ta đang hướng về Aureole, vùng đất linh hồn yên nghỉ mà."** / "…Quả là vậy nhỉ." | **mở ra cả hành trình** | **3** |

**P21 — BỎ** (banner 12 Fingers Team + truyenqqq.com).

---

## C. Điểm cao trào

Chương này có **bốn** đỉnh, ba cảm xúc một hành động. Cả bốn đều đứng được riêng.

1. **P18-a → P18-c — "Bắn tôi đi."**
   Ảo ảnh Himmel tự đọc câu kết liễu chính mình, và Frieren xác nhận *"Himmel chắc chắn sẽ nói như vậy ha."* rồi bắn.
   Đỉnh **hành động** của chương. Mạnh vì nó đúng — con quỷ dựng ảo ảnh từ ký ức, mà ký ức Frieren về Himmel thì đúng là một người sẽ nói câu đó.

2. **P17-e — "Mình cứ ngỡ là sư phụ sẽ xuất hiện thêm lần nữa chứ… Có lẽ là mình đã thay đổi chút ít mất rồi…"**
   Đỉnh **cảm xúc của Frieren**, và là câu nặng nhất cả chương. Con quỷ chọn ảo ảnh theo "người yêu dấu nhất" (luật do chính Frieren nêu ở P12-a) — nên việc **Himmel hiện ra thay cho sư phụ** là một phép đo lạnh lùng: trong 28 năm, thứ đứng đầu lòng cô đã đổi chỗ. Frieren không khóc, chỉ nhận xét về chính mình.

3. **P19-c → P19-d — Fern bắn ảo ảnh Heiter.**
   Đỉnh **cảm xúc của Fern**. Cô bé đã tuyên bố ở P12-e *"em đã biết chúng đều là giả mạo cả mà"*, rồi đứng chết trân suốt P15–P17 (*"Có vẻ vô ích rồi đây."*), phải chờ tới khi Frieren dọn xong phần của mình mới bóp cò được. Biết là giả không làm cho việc bắn dễ hơn — đó là toàn bộ nội dung chương.

4. **P20-f → P20-g — cú lật cuối: "Lần tới hãy đi gặp người thật nhé." / "…chúng ta đang hướng về Aureole, vùng đất linh hồn yên nghỉ mà."**
   Đổi nghĩa toàn bộ phần đầu. Cả chương tưởng là một vụ trừ yêu dọc đường; hai khung cuối biến nó thành **lý do của cả chuyến đi**. Cái "thực thể hóa" mà Heiter hứa ở P04-d/P05-d, ảo ảnh không giữ nổi — nhưng đích đến thì giữ được.

**Cột sống nối hai đầu chương:** vế hứa của Heiter ở **P05-d** (*"Nếu như cháu làm một cô bé ngoan… ta sẽ thực thể hóa một chút để gặp lại cháu đấy.."*) được **con quỷ đọc lại gần như nguyên văn** ở **P16-a**. Fern còn tự viện đúng chữ đó ở **P09-e** trước khi vào đèo. Một câu, ba lần, ba nghĩa khác nhau — đây là chỗ để người kể im và cho nghe thoại gốc.

---

## D. Chưa rõ

**Không đoán bừa. Site thiếu C6–C7, nhiều mục dưới đây có thể đã được giới thiệu ở hai chương bị hụt đó.**

### D1. Nhân vật mới / chưa có trong bible

| Đối tượng | C9 cho biết gì | Chưa rõ |
|---|---|---|
| **Sư phụ của Frieren** | Chỉ **được nhắc bằng lời** ở P13-a/P13-c và P17-e. Frieren gọi là **"sư phụ"**, dùng **"ngài ấy"**. Frieren *"đã từng bắn vào ảo ảnh sư phụ của mình dù cho ngài ấy đã cầu xin tha mạng"* và *"đã quen với việc sư phụ cầu xin suốt rồi"*. P17-e cho thấy trước đây **ảo ảnh hiện ra cho Frieren luôn là sư phụ**. | **TÊN — chưa hề xuất hiện. KHÔNG ĐƯỢC ĐẶT TÊN.** Giới tính (bản dịch dùng "ngài ấy", không đủ kết luận) · còn sống hay đã chết · vì sao Frieren gặp ảo ảnh người này **nhiều lần** · "cầu xin suốt" là nghĩa đen hay đùa · có liên quan gì tới Ewig không. Bible C1–C2 ghi *"chưa rõ ai dạy cô phép thuật"* → **C9 là lần đầu nhân vật này được nhắc.** |
| **Bà bán hàng ở làng** (P07-a→c) | Phụ nữ tóc xoăn ngang vai, tạp dề, đứng cạnh sạp rau. Cảnh báo về đèo, kể chuyện vong hồn. | **CHƯA RÕ TÊN — đừng đặt biệt danh.** Không rõ có xuất hiện lại không. |
| Dân làng khác (P07-d, P07-f) | Một phụ nữ trước cửa nhà, một ông ngồi bậc thềm, một người đàn ông trong quán rượu. | Không ai có tên, không ai có thoại được ghi. Chỉ là cảnh điều tra. |

### D2. Địa danh / thuật ngữ mới (bible CHƯA có — cần bổ sung sau khi user duyệt)

| Chữ trong ảnh | Ở đâu | Chưa rõ |
|---|---|---|
| **Quỷ Bóng Ma** — ruby ghi **Einsam** | P11-c, P12-b | Bản dịch in tên Việt to, chữ *Einsam* nhỏ phía trên. **Chưa chốt lời kể dùng "Quỷ Bóng Ma" hay giữ "Einsam".** Không rõ nó có quan hệ gì với **Quỷ Vương** hay không — C9 chỉ nói nó *"xảo quyệt và tham lam trong số những kẻ cùng loài"*, không nhắc Quỷ Vương một lần. **Đừng nối hai thứ này.** |
| **Aureole, vùng đất linh hồn yên nghỉ** | P20-g | **Lần đầu tiên đích đến của chuyến đi được gọi tên.** Chưa rõ: ở đâu, còn bao xa, ai nói cho Frieren biết, vì sao cô tin ở đó gặp được người chết, và **liên quan gì tới "chuyện nữa muốn nhờ Eisen" ở C1-P35 hay không**. Nhiều khả năng đã được giới thiệu ở **C6 hoặc C7 (thiếu)**. |
| **vùng Wille** | P06-d | Một vùng thuộc **các vùng trung tâm**. Chưa rõ vị trí so với Thánh Thành Strahl. |
| **sách sinh thái phép thuật** | P11-a | Fern dẫn nguồn. Chưa rõ là một cuốn cụ thể hay tên một thể loại sách. **Không phải "sách ma thuật" của Ewig** — đừng gộp. |
| "ma pháp công kích" | P12-c | Bản dịch dùng cụm này cạnh **"ma lực"**. Bible chốt "ma lực"; **chưa chốt** cách gọi cho loại phép tấn công. |

### D3. Chi tiết mơ hồ trong ảnh

- **P19-a — hình dạng khổng lồ tóc trắng dài, thân tối, giơ tay cầm vật có xích.** Truyện **không** dán nhãn cho nó. Không thoại, không chú thích. Có thể là **Quỷ Bóng Ma lộ hình**, cũng có thể là một lớp ảo ảnh nữa. **Không suy diễn** — nếu cần nói, chỉ tả những gì thấy.
- **P11-a — ai nói câu nào.** Panel chỉ có mặt Fern. Bong bóng phải *"Là phép ảo giác đúng chứ ạ?"* có "ạ" → Fern. Bong bóng trái *"Trong cuốn sách sinh thái phép thuật được viết rằng…"* **không có đuôi câu phân biệt** và không thấy đuôi bong bóng chỉ vào ai. **Chưa chốt người nói.**
- **P15-b — ai gọi "Fern."** Giọng vang lên trước khi ảo ảnh lộ mặt. Có thể là ảo ảnh Heiter (P16-e Frieren mới gọi "Fern." rõ ràng). **Chưa chốt.**
- **Mốc thời gian của hồi tưởng P03–P05.** Ô chú thích chỉ ghi mốc cho **hiện tại** (28 năm sau khi Himmel mất). Cảnh giường bệnh **không có mốc**. Bible C2 có cảnh Heiter hấp hối nhưng **không có cảnh "ta sẽ thực thể hóa"** → **đây là cảnh mới, không phải cảnh C2 chiếu lại.** Chưa rõ nó nằm trước hay sau các cảnh C2-P29→P34.
- **Frieren có giải thích cho Fern về "sư phụ" hay không.** P13-c Fern hỏi thẳng *"'Quen với việc sư phụ cầu xin' tức là sao chứ ạ…"* — **Frieren không trả lời.** Câu hỏi bị bỏ treo tới hết chương. Đừng viết như thể đã được đáp.
- **Fern có khóc ở P19-c không.** Mắt ướt/loé sáng, nhưng nét vẽ **không** dứt khoát là nước mắt. Tả là "mắt ướt", đừng khẳng định "khóc".

### D4. Vẫn chưa tiết lộ (giữ nguyên từ bible, C9 không nói thêm)

Tuổi Frieren · tuổi Fern · họ của cả năm nhân vật · hình dạng và tên Quỷ Vương · Ewig là ai · **Eisen ra sao sau C1 (C9 cũng không nhắc một lần nào)** · ý nghĩa tựa đề "Sousou no Frieren" · ba yếu tố của phép thuật tầm xa (C2-P15).

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** 94 panel, phân bổ P03→P20. Đặc biệt xin soát lại **P07 (7 panel)** và **P20 (7 panel)** — hai trang chia ô lệch cột, tôi đọc cột giữa từ trên xuống rồi mới sang trái; nếu thứ tự cột của tôi sai thì beat 21–24 và 92–94 phải đảo.
2. **Tên nhân vật đúng chưa?** Ông lão giường bệnh = **Heiter**, chốt bằng chính lời Fern ở P05-a (*"Heiter-sama sẽ thực thể hóa…"*), không phải suy đoán từ hình. Bóng người choàng trắng ở P17-c = **Himmel**, chốt bằng lời Fern ở P17-d. **"Sư phụ" của Frieren để trống tên** theo đúng yêu cầu — xin xác nhận C6/C7 có thật sự chưa lên hình nhân vật này không.
3. **Trọng số hợp lý chưa?** Tôi đặt **TS 3 cho cả bốn đỉnh** ở mục C và cho toàn bộ chuỗi P16→P20. Nếu video 7–8 phút thì lượng TS 3 hiện tại (~40 panel) là **hơi nhiều** — cần user chỉ định giữ đỉnh nào làm trục, hạ phần còn lại xuống 2.

**Không tự sang `/manga-narration`.**
