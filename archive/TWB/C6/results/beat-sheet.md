# BEAT SHEET — Twilight Blade C6 "Khôi lỗi chi mẫu"

Nguồn ảnh: `series/TWB/C6/pages-clean/`
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **ĐỦ 22/22 trang** · 72 panel có nội dung · 1 trang BỎ

### A. Kiểm tra đầu vào

22 ảnh `TWB_C6_P01`–`P22`, liên tục, **không thiếu trang**.

| Trang | Raw → Clean | Cắt | Ghi chú |
|---|---|---|---|
| P01 | 822×1500 → 822×1052 | **448px ở ĐÁY** | ⚠ Banner FoxTruyen **vẫn còn ở ĐẦU trang** (~460px trên cùng) — `clean-pages.py` cắt nhầm phía. **Phải crop mép trên khi dựng.** |
| P02 | 822×610 → không đổi | 0 | Trang ngắn: dải cuối cảnh + logo tiêu đề bộ + banner tên chương |
| P03–P20 | 822×1200 → không đổi | 0 | Sạch |
| P21 | 900×1500 → không đổi | 0 | ⚠ **Còn dải quảng cáo "HẾT TRUYỆN RỒI!" ở đáy** (~200px). Dải "CÒN TIẾP" là nội dung truyện, giữ lại. |
| P22 | 900×811 → 900×781 | 30px | **BỎ — toàn bộ là quảng cáo FoxTruyen / TruyenQQQ, không có nội dung truyện.** |

Lưu ý khổ ảnh: P01–P20 rộng 822px, **P21–P22 rộng 900px** → khác nguồn, phải canh lại khi lên khung 9:16.

**Overlay không phải nội dung gốc:** ở P01 có dòng chữ viết tay của nhóm dịch/site
*"YOJIN BỊ TẨY NÃO!! TRẬN CHIẾN NÀY RỒI SẼ ĐI VỀ ĐÂU...!?"* — đây là **lời quảng cáo chèn thêm**,
không phải thoại trong truyện. Không được đọc như lời nhân vật.

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P01-a | Mở giữa trận: **Yojin đứng đó với một mặt nạ trắng úp kín mặt**, buông thõng tay. Cách đó vài bước, một thanh niên đeo kính, má dán băng, đang đỡ lấy người phụ nữ tóc đen dài gục xuống | "THẬT LÀ NGU NGỐC LÀM…" | ngột ngạt, sai trái | 3 |
| 2 | P02-a | Câu nói vắt sang, kèm logo tiêu đề bộ | "…SAO, HỠI KẺ NGOẠI ĐẠO KIA…" | khinh miệt | 2 |
| 3 | P02-b | **Đại cảnh lộ diện oán hồn**: một khuôn mặt khổng lồ tóc đen, cười nhe răng, vây quanh là bầy búp bê hình thai nhi treo trên dây. Banner tên chương: **"Chương 6 — Khôi lỗi chi mẫu"** | "NẾU NGƯƠI CỨ MẶC KỆ… THÌ TỐT BIẾT MẤY…" | ghê rợn | 3 |
| 4 | P03-a | Thanh niên đeo kính bị đánh bật ngược, mắt trợn trắng | — | choáng | 2 |
| 5 | P03-b | Cận mặt Yojin sau lớp mặt nạ — có một khối thịt nhỏ bám ở miệng mặt nạ | "NÀY ĐẠI PHÁP SƯ…!" | lạnh, không hồn | 3 |
| 6 | P03-c | Thanh niên bị một bàn tay siết cổ, vẫn cố gọi Yojin | "KHÔNG THỂ NÀO ANH ĐÙA TÔI À…" | không tin nổi | 3 |
| 7 | P03-d | Một đòn giáng xuống | "VÔ ÍCH THÔI." / "Á!?" | tàn nhẫn | 2 |
| 8 | P03-e | Thân người phụ nữ tiến tới, trên ngực có một hạt tròn nhỏ. Thanh niên van xin | "M-MẸ…" · "DỪNG… LẠI…" | tuyệt vọng | 3 |
| 9 | P03-f | Bàn tay người mẹ bóp lấy mặt cậu, cậu gào lên | "HỤ…" | đau, bất lực | 2 |
| 10 | P04-a | Oán hồn tuyên bố qua miệng người mẹ: bà ấy **không còn là mẹ của cậu, mà là "con" của nó** | "KẺ NÀY… KHÔNG PHẢI LÀ MẸ CỦA NGƯƠI— MÀ LÀ CON CỦA TA." | lật ngửa, lạnh | 3 |
| 11 | P04-b | Giữa bầy búp bê thai nhi, nó giảng lý lẽ: sinh vật sống không ai chống lại nổi cái gọi là "mẹ", và mẹ duy nhất là nó | "CHỈ CÓ DUY NHẤT NGƯỜI MẸ LÀ TA ĐÂY." | ngạo mạn | 3 |
| 12 | P04-c | Nó coi việc sai khiến là quyền đương nhiên | "MỌI THỨ CỦA CON CÁI ĐỀU THUỘC VỀ NGƯỜI MẸ." | biến thái | 2 |
| 13 | P04-d | Thanh niên phản bác: mày chỉ coi bà ấy là quân cờ | "MÀY CHỈ ĐANG COI BÀ ẤY NHƯ MỘT QUÂN CỜ TAY SAI THÔI…!" | phẫn nộ | 3 |
| 14 | P05-a | Cậu bị quật nằm sấp, điện thoại văng khỏi tay | "CÁC NGƯƠI ĐÃ HẾT GIÁ TRỊ LỢI DỤNG RỒI." | hết đường | 2 |
| 15 | P05-b | Cậu ngẩng lên, chưa hiểu chuyện gì | "HẢ…!?" | hoang mang | 1 |
| 16 | P05-c | **Yojin đeo mặt nạ đứng sừng sững, tay cầm cán ô**, tuyên bố sẽ lấy linh hồn cậu — "theo đúng kế hoạch" | "TA XIN PHÉP NHẬN LẤY LINH HỒN CỦA NGƯƠI NHÉ." | rợn người | 3 |
| 17 | P05-d | Lý do: linh lực của cậu thuộc hạng thượng phẩm | "NGƯƠI SỞ HỮU MỘT NGUỒN LINH LỰC… CỰC KỲ THƯỢNG HẠNG…" | thèm khát | 3 |
| 18 | P05-e | Cận mặt nạ — tham vọng tiến hoá | "TA SẼ CÒN TIẾN HÓA XA HƠN NỮA…!" | đói khát | 3 |
| 19 | P06-a | **Hồi tưởng sáng trắng**: người mẹ cười, gọi tên con — **"YAMATO"** | "MẸ KHÔNG SAO ĐÂU, CON ĐỪNG LO LẮNG NHÉ!" | ấm, xót | 3 |
| 20 | P06-b | Cắt phắt về hiện tại: oán hồn thè lưỡi, nói linh lực di truyền qua huyết thống nên đòi ăn cả hai mẹ con | "CẢ HAI MẸ CON CÁC NGƯƠI HÃY CÙNG NHAU TRỞ THÀNH CHẤT DINH DƯỠNG…" | tương phản gắt | 3 |
| 21 | P06-c | Hồi tưởng: mẹ sửa cổ áo cho Yamato ở cửa ngày cậu đi xa, bảo đừng gửi tiền về | "CON PHẢI TỰ BIẾT TRÂN TRỌNG BẢN THÂN MÌNH NHẤT ĐẤY." | dịu, nhói | 3 |
| 22 | P06-d | Hiện tại: Yamato gần như hết hơi | "-DỪNG LẠI ĐI… MẸ… ÍT NHẤT LÀ MẸ TÔI…" | van nài | 3 |
| 23 | P06-e | Hồi tưởng đóng lại bằng câu của mẹ | "CUỘC ĐỜI CỦA CON LÀ CỦA CHÍNH CON KIA MÀ!" | ấm, đau | 3 |
| 24 | P06-f | Oán hồn cười phá lên chế nhạo | "LŨ YẾU ĐUỐI CÁC NGƯƠI CHỈ GIỎI GÀO KHÓC THÔI NHỈ!" | hả hê | 2 |
| 25 | P07-a | **Trang trắng toàn tốc độ tuyến** — một đòn chém xé qua, mặt nạ trắng vỡ | — | nổ tung | 3 |
| 26 | P08-a | Lưỡi kiếm đen xuyên thẳng vào miệng đang há của thứ chiếm xác người mẹ | — | dứt khoát | 3 |
| 27 | P08-b | Yamato nằm dưới đất, nhìn lên | — | sững | 1 |
| 28 | P08-c | Đại cảnh oán hồn gào; **phía xa, Yojin đứng thẳng, kiếm trong tay** — mặt nạ đã rơi | (gào) | đảo chiều | 3 |
| 29 | P09-a | Mặt nạ vỡ nằm lăn lóc; giọng mỉa của Yojin | "DĂM BA CÁI TRÒ VẶT VÃNH NÀY LẠI HOẠT ĐỘNG TỐT GHÊ NHỈ." | mỉa mai lạnh | 3 |
| 30 | P09-b | Người mẹ bật ngửa; oán hồn hoảng | "C-CÁI GÌ…" | chột dạ | 2 |
| 31 | P09-c | Bóng Yojin bước tới trên nền phố đêm | "KH-KHÁNG CỰ ĐƯỢC Ư…!?" / "NGÀY XƯA TÔI CÓ… TU LUYỆN MỘT CHÚT ẤY MÀ." | uy hiếp | 3 |
| 32 | P09-d | **Yojin toàn thân, tay gãi cổ, thản nhiên**: loại thuật tẩy não cỡ này anh đã rèn để kháng được | "…TÔI ĐÃ RÈN LUYỆN ĐỂ CÓ KHẢ NĂNG KHÁNG CỰ RỒI." | bình thản áp đảo | 3 |
| 33 | P09-e | Hạ nhiệt: anh vẫn hơi "say" thuật, doạ nôn ra cơm nắm vừa ăn | "CHẮC LÁT NỮA TÔI SẼ NÔN RA MẤY MIẾNG CƠM NẮM…" | hài khô | 2 |
| 34 | P10-a | Oán hồn cay cú, vẫn bịt miệng Yamato: dù là đại pháp sư thì cũng chỉ là con người | "DẪU CÓ LÀ ĐẠI PHÁP SƯ THÌ CHUNG QUY CŨNG CHỈ LÀ CON NGƯỜI." | tức tối | 3 |
| 35 | P10-b | Nó không hiểu vì sao bản năng phục tùng "người mẹ" lại thất bại | "BẢN NĂNG CỦA NGƯƠI ĐÁNG LẼ RA KHÔNG THỂ CHỐNG LẠI NGƯỜI MẸ ĐƯỢC CHỨ…!!" | hoang mang | 3 |
| 36 | P10-c | Yamato thều thào gọi mẹ; Yojin nhại lại hai chữ "bản năng" | "BẢN NĂNG À…" | lạnh | 2 |
| 37 | P10-d | Giày Yojin bước tới sát | "…CÓ VẺ NHƯ NGƯƠI VẪN CHƯA BIẾT MỘT ĐIỀU." | dồn | 3 |
| 38 | P10-e | Thân người mẹ run bần bật | "Ư… Ư…!!!" | căng | 2 |
| 39 | P11-a | Mảnh mặt nạ vỡ rơi | — | chuyển tiếp | 1 |
| 40 | P11-b | **Hạt đen bị rút khỏi người mẹ** | — | gỡ được | 3 |
| 41 | P11-c | Yamato quệt miệng, thở dốc | — | kiệt sức | 1 |
| 42 | P11-d | **Yojin nói thẳng vào mặt nó**: ý chí con người mãnh liệt và hung tợn hơn bản năng gấp vạn lần | "Ý CHÍ CỦA CON NGƯỜI… CÒN MÃNH LIỆT VÀ HUNG TỢN HƠN BẢN NĂNG GẤP VẠN LẦN." | **câu chốt chủ đề** | 3 |
| 43 | P12-a | Oán hồn gào át đi giữa bầy búp bê | "ĐỪNG CÓ NÓI NĂNG HÀM HỒ!!" | cuống | 2 |
| 44 | P12-b | Yojin cúi xuống, quay lưng; oán hồn coi thường "kháng cự với chả ý chí" | "MẤY THỨ ĐÓ ĐỀU…" | khinh | 2 |
| 45 | P12-c | Nó doạ sẽ thao túng lại bao nhiêu lần tuỳ thích — Yojin **cầm kiếm rút khỏi vỏ ô, đi thẳng tới** | "TA SẼ THAO TÚNG NÓ LẠI BAO NHIÊU LẦN TÙY THÍCH!" | tiến công | 3 |
| 46 | P13-a | Cận con mắt oán hồn, vẫn ngoan cố | "TẤT CẢ ĐỀU VÔ ÍCH THÔI." | cố chấp | 2 |
| 47 | P13-b | Đầu nó bị nghiền xuống, Yojin trả lại đúng câu ấy | "ĐÚNG LÀ VÔ ÍCH MÀ." | lạnh gáy | 3 |
| 48 | P14-a | Mặt oán hồn bét nát; Yojin phán: mày quá yếu nên không thao túng được tao | "MÀY QUÁ YẾU… NÊN KHÔNG THỂ THAO TÚNG TAO ĐƯỢC ĐÂU." | áp đảo tuyệt đối | 3 |
| 49 | P14-b | Cận Yojin, mắt không chớp | "CỨ VIỆC GÀO THÉT BAO NHIÊU TÙY THÍCH ĐI." | tàn nhẫn nguội | 3 |
| 50 | P15-a | Yamato thở phào | "MAY QUÁ…" | nhẹ nhõm | 2 |
| 51 | P15-b | Người mẹ nằm thở đều — bà còn sống | (tiếng thở) | ấm | 3 |
| 52 | P15-c | Mảnh mặt nạ vỡ lăn xuống; Yamato ôm mẹ giật mình | "Á!!" | giật | 1 |
| 53 | P15-d | Yojin cúi xuống, áo rách, người bê bết | "TA CÓ VÀI ĐIỀU MUỐN HỎI NGƯƠI ĐÂY." | đổi giọng | 3 |
| 54 | P15-e | Yojin đứng trước cái xác mềm nhũn của oán hồn | "GIỜ THÌ…" | lạnh | 2 |
| 55 | P16-a | Oán hồn thoi thóp | "HỤ…" | hấp hối | 1 |
| 56 | P16-b | **Yojin tra khảo: mày biết rõ về đứa trẻ đó, kể cả vết thương ở mắt nó** — vết đó là do một quái vật gây ra, đúng không | "…BAO GỒM CẢ VẾT THƯƠNG Ở MẮT CỦA NÓ NHỈ." · "LÀM CÁCH NÀO MÀ MI BIẾT?" | **mục đích thật lộ ra** | 3 |
| 57 | P16-c | Oán hồn ú ớ từng âm rời rạc; Yojin ép | "HI… KA… A…" / "TRẢ LỜI ĐI." | nghẹt | 3 |
| 58 | P17-a | **Đại cảnh cả trang: một quái vật khổng lồ quấn dây thừng shimenawa hiện lên**, Yojin nhỏ xíu dưới chân. Nó nhả ra từng âm | "KA… RI… KU… RA…" | choáng ngợp | 3 |
| 59 | P18-a | Yojin ngẩng nhìn, không hoảng | — | tĩnh | 2 |
| 60 | P18-b | Yamato ôm mẹ lùi lại | — | sợ | 1 |
| 61 | P18-c | Cận đôi mắt Yojin sắc lạnh | — | quyết | 3 |
| 62 | P18-d | Bàn tay Yojin đưa lưỡi kiếm mảnh cắt ngang thân quái vật | — | dứt | 3 |
| 63 | P19-a | **Quái vật nổ tung thành mảng đen**; Yojin còn nguyên tư thế vừa chém | "!!" | bùng nổ | 3 |
| 64 | P19-b | Yojin quay lưng, đứng giữa khoảng trống | — | lắng | 1 |
| 65 | P19-c | Yamato hét, che mặt vì mảnh vỡ | "Á!" | hoảng | 1 |
| 66 | P20-a | Lưng Yojin; câu hỏi bỏ lửng: thứ vừa rồi cũng là quái vật sao | "THỨ ĐÓ CŨNG LÀ QUÁI VẬT SAO…?" | nghi hoặc | 3 |
| 67 | P20-b | Yamato hỏi dồn: nó biến mất rồi? vừa rồi là cái gì? | "VỪA RỒI LÀ CÁI GÌ THẾ…" | hoang mang | 2 |
| 68 | P20-c | **Yojin tra kiếm về vỏ ô** — và tự trả lời mình | "RA LÀ VẬY…" | vỡ lẽ, nén | 3 |
| 69 | P20-d | Cận mặt người mẹ bất tỉnh — bình yên trở lại | — | dịu | 2 |
| 70 | P21-a | **Phòng bệnh, đêm.** Mẹ nằm ngủ; Yamato gọi khẽ | "MẸ…" | lặng, ấm | 3 |
| 71 | P21-b | Trời đêm, trăng lưỡi liềm. Một hộp chữ trơ trọi: **KARI KURA** | "KARI KURA" | **cú lật** | 3 |
| 72 | P21-c | Cận nghiêng mặt Yojin trong đêm — hoá ra cả trận này anh chỉ cần một thứ: cái tên | "… TA ĐÃ BIẾT TÊN NGƯƠI." + dải "CÒN TIẾP" | lạnh, đóng chương | 3 |
| — | P22 | Toàn trang quảng cáo FoxTruyen / TruyenQQQ | — | — | **BỎ** |

### C. Điểm cao trào

Chương có **bốn đỉnh**, mỗi đỉnh một loại:

1. **Đỉnh ghê rợn — P04-a/P04-b.** Oán hồn tuyên bố người mẹ giờ là "con của ta" và dựng
   nguyên một hệ lý lẽ: sinh vật sống không thể chống lại thứ mang tên *mẹ*. Đây là chỗ
   đặt tên chương "Khôi lỗi chi mẫu" vào đúng nghĩa của nó.

2. **Đỉnh cảm xúc — P06 (a → e).** Ba mảnh hồi tưởng xen thẳng vào cảnh tra tấn: mẹ gọi
   "Yamato", mẹ sửa cổ áo bảo đừng gửi tiền về, mẹ nói "cuộc đời của con là của chính con".
   Chính ba câu này bẻ gãy lý lẽ "mẹ thì con phải nghe" của oán hồn — người mẹ thật đã dạy
   cậu ngược lại.

3. **Đỉnh hành động — P07 → P09-d.** Mặt nạ vỡ; Yojin thoát khỏi thuật tẩy não và nói câu
   lật thế trận: anh **đã rèn để kháng loại thuật này từ trước**. Toàn bộ đoạn P01–P06 đọc
   lại thành một cái bẫy mà kẻ đặt bẫy không biết mình đang bị thả cho diễn.
   Chốt tư tưởng ở **P11-d**: *"Ý chí của con người còn mãnh liệt và hung tợn hơn bản năng
   gấp vạn lần."*

4. **CÚ LẬT CUỐI — P15-d → P21-c (đỉnh thật).**
   Yojin không giết ngay. Anh dừng lại để **tra khảo về "đứa trẻ" và vết thương ở mắt nó**
   (P16-b) — tức là **trận này chưa bao giờ là trận cứu mẹ con Yamato; cứu người chỉ là
   phần đi kèm.** Oán hồn ú ớ từng âm rời (P16-c → P17-a), một quái vật khổng lồ quấn
   shimenawa trồi lên, Yojin chém bay nó, rồi tra kiếm về vỏ và nói *"Ra là vậy…"* (P20-c).
   Trang cuối đóng lại bằng hai chữ **KARI KURA** và câu *"… ta đã biết tên ngươi."*

   → **Đổi nghĩa toàn bộ phần đầu:** những âm rời rạc ở P16–P17 không phải tiếng hấp hối,
   mà là **một cái tên bị moi ra**. Việc Yojin để mình bị tẩy não, để bị kéo vào tận đây,
   và việc anh dừng tay đúng lúc — tất cả đều để lấy cái tên đó.

### D. Chưa rõ

**Không đoán bừa — những mục dưới đây phải hỏi/đọc thêm chapter trước khi viết lời kể.**

1. **Yamato là ai, họ là gì.** Tên "Yamato" chỉ xuất hiện đúng một lần, trong hồi tưởng
   người mẹ gọi (P06-a). Không rõ họ, không rõ quan hệ với Yojin, không rõ vì sao cậu có
   "nguồn linh lực cực kỳ thượng hạng" (P05-d). **Chưa có trong series-bible.**
2. **Mẹ Yamato chưa có tên.** Chỉ gọi "mẹ".
3. **"Đại pháp sư" chỉ ai.** Đọc theo mạch (P09-d Yojin nói anh đã rèn kháng thuật, P10-a
   oán hồn cay cú vì bị kháng lệnh) thì **nhiều khả năng là Yojin**. Nhưng ở P03-b câu
   "Này đại pháp sư…!" phát ra từ khung cận mặt Yojin đang đeo mặt nạ, nên **cũng có thể là
   Yamato gọi Yojin từ ngoài khung**. Chưa chốt được người nói. → **Trong lời kể nên dùng
   "pháp sư trừ tà" theo bible, tránh gán "đại pháp sư" cho ai.**
4. **KARIKURA là tên của cái gì.** Tên con quái vật khổng lồ ở P17? Tên kẻ đứng sau đã ra
   lệnh? Hay tên con quái vật đã gây vết thương ở mắt "đứa trẻ"? Truyện không nói. Câu
   "ta đã biết tên ngươi" ở P21-c cũng không chỉ rõ "ngươi" là ai. **Không được suy diễn.**
5. **"Đứa trẻ" ở P16-b có phải Hikari không.** Mạch C1 (Yojin được lệnh giám sát Hikari,
   Hikari có thể chất thu hút oán hồn) khớp rất sát, nhưng **trong C6 cái tên Hikari không
   hề được nói ra**. Ngoài ra bible ghi Hikari có **vết trên trán**, còn C6 nói **"vết thương
   ở mắt"** — chưa xác nhận là cùng một vết. → Chỉ được gọi "đứa trẻ đó" cho tới khi đối
   chiếu C2–C5.
6. **Loại quái vật ở P17.** Nó được quấn dây shimenawa (dây thừng thần đạo) — chi tiết này
   chưa được giải thích. Chưa rõ nó là "oán hồn" theo đúng thuật ngữ bible, hay một loại
   khác; chính Yojin cũng hỏi "Thứ đó cũng là quái vật sao…?" (P20-a). **Không tự dán nhãn.**
7. **Vì sao Yojin bị tẩy não, và bị từ khi nào.** Chương mở ra khi anh đã bị khống chế rồi.
   Không thấy cảnh anh bị dính thuật.
8. **Ai nói câu ở P20-a** ("Thứ đó cũng là quái vật sao…?"). Đuôi bóng thoại nằm phía Yojin
   nên ghi là Yojin, nhưng khung kế bên là Yamato đang hỏi dồn — có thể là cùng một chuỗi.
9. **Vũ khí của Yojin.** Trong chương này là **kiếm giấu trong cán ô** (P12-c rút ra, P20-c
   tra lại). C1 chỉ thấy anh cầm ô. Chưa rõ đây là bảo bối riêng hay đồ tiêu chuẩn.
10. **Hạt đen bị rút khỏi người mẹ ở P11-b** là gì — lõi của oán hồn, hay vật trung gian
    khống chế. Truyện không gọi tên.
11. **Đoạn thoại ở P02-a/P05-a**: chưa chắc 100% người nói là oán hồn hay Yojin đang bị
    khống chế nói hộ — hai giọng chồng nhau suốt phần đầu.
12. **Thiếu beat sheet C2–C5.** Repo hiện chỉ có `C1/results/beat-sheet.md`. Mọi suy đoán
    về mạch nối C5→C6 đều chưa có căn cứ trong repo.

---

## DỪNG Ở ĐÂY — chờ duyệt

1. **Panel có thật không?** — 72 panel trên có đúng là những gì nhìn thấy trong ảnh không,
   đặc biệt P03-a (ai bị đánh văng) và P08-c (Yojin đứng ở nền xa)?
2. **Tên nhân vật đúng chưa?** — "Yamato" (P06-a) và "KARI KURA" (P21-b) là hai tên mới,
   chưa có trong series-bible. Có cần cập nhật bible trước khi viết lời không?
3. **Trọng số hợp lý chưa?** — cú lật được đặt ở P15-d→P21-c (mục tiêu thật của Yojin là
   moi cái tên). Nếu bạn thấy đỉnh nằm ở chỗ khác (ví dụ P09-d, lúc mặt nạ vỡ), nói để
   chỉnh lại TS trước khi sang bước viết lời.

**Không tự sang `/manga-narration`.**
