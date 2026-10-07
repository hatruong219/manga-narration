# BEAT SHEET — Twilight Blade (TWB) · Chương 3 · "An toàn bên cạnh"

Nguồn: `series/TWB/C3/pages-clean/TWB_C3_P01.jpg` → `TWB_C3_P58.jpg` (đã đọc hết 58/58, đúng thứ tự).
Tên nhân vật & thuật ngữ theo `series/TWB/series-bible.md`.

---

### A. Kiểm tra đầu vào

**Đủ trang.** Nhận 58 ảnh, `TWB_C3_P01` → `TWB_C3_P58`, liên tiếp, **không thiếu trang nào**. Không có cảnh báo.

**Về `clean-pages.py`:** script này **không cắt px** — nó **tô trắng đè** lên dải chrome của site.
So kích thước `pages/` với `pages-clean/`: **0/58 trang bị đổi kích thước** (mọi trang giữ nguyên, rộng 1125px),
nhưng **58/58 trang khác byte** → đã xử lý bằng cách ghi đè, không crop.

**Chrome còn sót — phải xử lý khi dựng:**
- `P01`: banner quảng cáo TRUYENQQQ (hồng, ~630px trên cùng) + dòng promo **VẪN CÒN**, chưa bị bỏ. → **BỎ dải trên cùng của P01.**
- `P58`: banner TRUYENQQQ (xanh) + dòng promo **VẪN CÒN**. → **BỎ toàn bộ P58** trừ ô chữ "Còn tiếp…".
- Watermark `NetTruyen12s` góc trên trái còn ở P01, P05, P11, P17, P21, P23, P25, P27, P35, P43, P45, P49, P51, P57 → crop mép hoặc che khi dựng.

**Cấu trúc file ảnh (quan trọng cho khâu cắt panel):** đây là webtoon dạng dải dài bị cắt máy móc theo chiều cao.
- Trang **lẻ** (P01…P57) cao 1500px → chứa panel thật.
- Trang **chẵn** (P04, P08, P10, P12, … P56) chỉ cao **140–148px** → là **mẩu tràn** của panel ở trang lẻ ngay trước, thường chỉ dính một góc bóng thoại bị cắt đôi. **Không tính là panel riêng.** Trong bảng dưới, các mẩu này được gộp vào panel của trang trước.
- Ngoại lệ: `P02` (779px) và `P58` (780px) là trang có nội dung thật.

**Trang đánh dấu BỎ:**
| Trang | Lý do |
|---|---|
| P01 (dải trên ~630px) | Banner quảng cáo + dòng promo site |
| P05 | Trang bìa chương (title page "TWILIGHT BLADE") — không phải panel truyện |
| P06 | Dòng credit tác giả + thanh tiêu đề "CHAP 3 — An toàn bên cạnh" |
| P04, P08, P10, P12, P14, P16, P18, P20, P22, P24, P26, P28, P30, P32, P34, P36, P38, P40, P42, P44, P46, P48, P50, P52, P54, P56 | Mẩu tràn 140–148px, đã gộp vào panel trang trước |
| P58 | Banner quảng cáo (giữ lại mỗi ô "Còn tiếp…") |

**Tổng panel đếm được: 104.**

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P01-a | Mở lạnh. Một cái hộp mở ra: chuỗi hạt cầu nguyện và hai cây cọc nhọn bằng kim loại nằm trong lớp lót. Có ai đó đang bàn giao đồ. | "…tăng cường an ninh." | chuẩn bị, lạnh | 2 |
| 2 | P01-b | Cột điện, bầy quạ đậu kín dây, tiếng kêu. Khung chuyển không khí điềm gở. | "CAW" | điềm gở | 1 |
| 3 | P01-c | Mặt nghiêng một người đàn ông (KHÔNG RÕ AI) nhận đồ, hứa sẽ sẵn sàng cho mọi tình huống. | "Dĩ nhiên rồi, tôi sẽ chuẩn bị sẵn sàng…" | cam kết | 2 |
| 4 | P02-a | Cổ tay đeo đồng hồ, người kia chào đi. | "Chào nhé." | dứt | 1 |
| 5 | P02-b | Yojin áp cây cọc nhọn lên gò má mình, ánh kim loé "TING". Mắt sắc. | "Giờ thì… …đi thôi nào." | lạnh, vào trận | **3** |
| 6 | P02-c | Khung phụ: bàn tay nắm cây cọc/lưỡi dao. | — | siết | 1 |
| 7 | P03-a | Cắt thẳng sang lớp học. Một ông thầy đeo kính, tóc bạc, cầm tập hồ sơ, tự giới thiệu. | "Tôi là Shimizu, giáo viên chủ nhiệm của Hikari." | hiền lành | **3** |
| 8 | P03-b | Biển lớp "2-3" trên hành lang. Xác lập địa điểm. | — | trung tính | 1 |
| 9 | P03-c | Yojin ngồi nhét mình vào ghế học sinh bé xíu (ghế kêu "KREAK"), Hikari ngồi cạnh. Chào hỏi khách sáo. | "Tôi mới là người lấy làm vinh hạnh." | gượng, hài ngầm | 2 |
| 10 | P05 | *(Trang bìa chương — BỎ)* Tranh bìa: mặt Shimizu, mặt Hikari hoảng, Yojin đứng giữa bầy oán hồn. | "TWILIGHT BLADE" | — | — |
| 11 | P06 | *(BỎ)* Thanh tiêu đề: "CHAP 3 — An toàn bên cạnh". | — | — | — |
| 12 | P07-a | **MỘT TUẦN TRƯỚC.** Tờ thông báo "Buổi họp Phụ huynh – Học sinh sắp tới", lớp 2-3. | "MỘT TUẦN TRƯỚC…" | lùi thời gian | 2 |
| 13 | P07-b | Yojin ngồi một mình ở bàn, hai tay chắp trước miệng, mặt nặng như đang nhận lệnh tác chiến. | — | căng thẳng | 2 |
| 14 | P07-c | Cận mặt Yojin, ánh sáng gắt sau lưng. Anh tự tuyên bố mức độ của việc này. | "Đây sẽ là một nhiệm vụ quan trọng." | nghiêm trọng hoá | **3** |
| 15 | P07-d | Toàn cảnh căn phòng trống — hoá ra thứ anh gọi là nhiệm vụ chỉ là… | "một… …buổi họp phụ huynh." | hài, tương phản | **3** |
| 16 | P09-a | Hình dung: Hikari bé nhỏ đứng cạnh bóng thầy Shimizu to lù lù, tiếng ù "RRMMBBL". | "Thầy ấy đã có nhiều thời gian ở bên Hikari hơn mình…" | ghen tị, bất an | 2 |
| 17 | P09-b | Tờ phiếu nguyện vọng. Yojin tính toán: phải bảo vệ Hikari mà không lộ nghề. | "…mình cũng cần phải có được sự tin tưởng của thằng bé nữa." | toan tính | 2 |
| 18 | P09-c | Cận mắt Yojin bốc lửa, tự suy ra mức tin tưởng của Hikari dành cho thầy còn lớn hơn mình. | "…mức độ tin tưởng của Hikari dành cho thầy ấy cũng lớn hơn!" | ganh, dốc sức | 2 |
| 19 | P09-d | Tưởng tượng: thầy Shimizu giơ tấm bảng "NO", chặn tay lên đầu Hikari. | "…nếu mình làm dấy lên sự nghi ngờ của giáo viên!" | sợ hỏng việc | 2 |
| 20 | P11-a | **Trở lại hiện tại.** Toàn cảnh lớp học nhìn từ trần: ba người ngồi lọt thỏm giữa biển bàn ghế. Thầy xin lỗi vì báo gấp. | "KHÔNG ĐƯỢC PHÉP SAI SÓT!" | áp lực | 2 |
| 21 | P11-b | Shimizu cười hiền, ôm hồ sơ. Yojin thầm đánh giá là người tử tế. | "Trông thầy ấy có vẻ tử tế!" | nhẹ nhõm hụt | 1 |
| 22 | P11-c | Yojin cứng đơ người, hiệu ứng "STIFF", trả lời nhát gừng. | "Không có gì đâu ạ…" | cứng đờ | 2 |
| 23 | P11-d | Cận Shimizu cười, Yojin toát mồ hôi — anh thấy buổi họp này còn đáng sợ hơn đánh nhau với oán hồn. | "…cảm giác này lại còn đáng sợ hơn…" | hoảng hài | **3** |
| 24 | P13-a | Yojin cố tỏ ra cứng rắn, mời thầy "tung hết ra". | "Cứ tung ra hết những gì thầy có đi." | ra oai | 2 |
| 25 | P13-b | Shimizu giật mình "JOLT", gọi đúng họ Yojin. | "…anh Odaki…" | bất ngờ | 2 |
| 26 | P13-c | Shimizu gãi cổ, thú nhận chính thầy cũng đang lo, xin Yojin đừng căng. | "Xin anh đừng quá căng thẳng như vậy." | hoà giải | 2 |
| 27 | P13-d | Góc cao: ba người quanh hai bàn học ghép lại. | — | trung tính | 1 |
| 28 | P13-e | Cận mắt Yojin — anh hiểu lầm hoàn toàn, tưởng bị chê không xứng đáng. Chú thích nhỏ: "Mình thất bại rồi…" | "…tôi không xứng đáng với sự tin tưởng của thầy sao?!" | hiểu lầm, hoảng | **3** |
| 29 | P15-a | Shimizu nói về Hikari: học sinh chăm chỉ, chín chắn, tự lập. Hikari đỏ mặt. | "…là một học sinh rất chăm chỉ." | ấm | 2 |
| 30 | P15-b | Yojin quay sang nhìn Hikari, dấu "?" — anh không biết chuyện này. | "Anh biết đấy, Hikari…" | ngỡ ngàng | 2 |
| 31 | P15-c | Shimizu cúi nhìn hồ sơ, nói về việc đưa Hikari quay lại trường. | "…phần lớn trong việc giúp em ấy đi học trở lại…" | trân trọng | 2 |
| 32 | P15-d | Yojin và Hikari ngồi cạnh nhau, Hikari cúi mặt. Thầy kết luận mọi chuyện đã ổn định. | "…thằng bé đã bắt kịp được với các bạn còn lại trong lớp." | yên ổn | 2 |
| 33 | P15-e | Cận Yojin gật, nhẹ người. | "Đúng vậy." | nhẹ nhõm | 1 |
| 34 | P17-a | Shimizu nói tiếp: điều quan trọng hơn là Hikari đã có một nơi thấy an toàn, được che chở. | "…một nơi mang lại cảm giác an toàn và được che chở." | ấm, then chốt | **3** |
| 35 | P17-b | Hikari cúi đầu, đỏ mặt. | — | ngượng | 1 |
| 36 | P17-c | Yojin bật dấu "?!" — hiểu lệch hoàn toàn chữ "an toàn". | "Chẳng lẽ Hikari đã phát hiện ra chuyện về các oán linh rồi sao?!" | hoảng | **3** |
| 37 | P17-d | Hikari cúi gằm, tóc che mắt, nói về Yojin bằng giọng thật. | "…chú Yojin đã luôn rất tốt bụng ạ." | thành thật | **3** |
| 38 | P19-a | Hikari kể hồi nằm viện Yojin lúc nào cũng đến thăm. Yojin gạt đi, bảo đó chỉ là biện pháp đề phòng. | "Đó chỉ là một biện pháp đề phòng… thôi mà…" | chối, bối rối | 2 |
| 39 | P19-b | Cận mặt Yojin sững lại, mắt mở. | — | sững | 2 |
| 40 | P19-c | Hikari ngẩng lên nói say sưa: mỗi khi ở bên Yojin, cậu thấy mọi chuyện rồi sẽ ổn. | "Mỗi khi ở bên chú ấy…" | tin tưởng | **3** |
| 41 | P19-d | Shimizu mỉm cười tán thành. | "Ồ, vậy thì tuyệt quá." | ấm | 1 |
| 42 | P21-a | Yojin phủ nhận, rồi khựng lại: "Tôi hiểu rồi." | "Không phải đâu…" | chối bỏ | 2 |
| 43 | P21-b | Hai tấm lưng Yojin và Hikari ngồi quay đi. Độc thoại cay đắng: chính cái phần "thầy trừ tà" trong anh mới là thứ khiến thằng bé thấy an toàn. | "Chính cái phần 'thầy trừ tà' trong tôi mới là thứ khiến thằng bé có cảm giác an toàn đó." | chua chát | **3** |
| 44 | P21-c | Bàn tay Yojin siết trên đùi dưới gầm bàn. Anh chưa từng được ai nói với mình những lời như vậy. | "…chưa từng có ai nói với tôi những lời như thế trước đây cả." | xúc động nén | **3** |
| 45 | P23-a | Shimizu nói Hikari đã kể hoàn cảnh của Yojin cho thầy nghe; mời anh cứ hỏi. | "Hikari đã giải thích hoàn cảnh của anh cho tôi nghe rồi." | thân thiện | 2 |
| 46 | P23-b | Thầy chuyển chủ đề sang tương lai của Hikari. Yojin há hốc, chú thích nhỏ: "Đã bàn đến chuyện đó rồi sao?!" | "…thảo luận về tương lai của Hikari…" | hoảng hài | 2 |
| 47 | P23-c | Yojin ngồi cạnh Hikari, thầy hỏi thẳng cậu bé. | "Có điều gì cháu muốn làm khi lớn lên không?" | hồi hộp | 2 |
| 48 | P23-d | Góc cao: buổi tư vấn hướng nghiệp giữa năm hai. | — | thủ tục | 1 |
| 49 | P25-a | Hikari trả lời rụt rè: em muốn thành ai đó có thể giúp đỡ mọi người. | "Em cũng muốn trở thành… ai đó có thể giúp đỡ mọi người…" | thật thà | **3** |
| 50 | P25-b | Hikari quay lại nhìn Yojin, lúng túng. | "Oh, um…" | ngượng | 1 |
| 51 | P25-c | Shimizu và Hikari cùng cười, thầy khen. | "Tuyệt thật đấy." | ấm | 1 |
| 52 | P25-d | Thầy buông một câu vô tư: Yojin hẳn là hình mẫu lý tưởng cho Hikari. | "…anh Odaki hẳn sẽ là một hình mẫu lý tưởng đấy." | vô tư, mồi | 2 |
| 53 | P25-e | Cận Yojin, nửa mặt tối, cười lạnh — chặn ngay ý đó. | "Cháu sẽ không muốn trở thành một người giống như tôi đâu." | lạnh, tự khinh | **3** |
| 54 | P25-f | Hikari và thầy hoảng, hiệu ứng "DOOOM". Yojin giơ tay chữa cháy. | "Tại sao lại thế?" | hụt hẫng | 2 |
| 55 | P27-a | Yojin bịa một câu chuyện nghề: huấn luyện tàn khốc, chạy trên nước lẫn lửa. | "Họ bắt bạn phải chạy trên cả nước lẫn lửa!" | bịa, chống chế | 2 |
| 56 | P27-b | Yojin giơ tay, hạ giọng: công việc chỉ là săn "côn trùng rất, rất lớn". Thầy đớ người. | "…săn lùng những con côn trùng rất, rất lớn thôi." | nói dối nửa thật | **3** |
| 57 | P27-c | Cả ba trong khung: Yojin và Hikari gật lia lịa, thầy hoảng vì nghe như nghề nguy hiểm. | "Đó là một ngành nghề rất nguy hiểm!" | hài, náo | 2 |
| 58 | P27-d | Hikari ngẩng lên, mắt sáng. | "Oh…" | tò mò | 1 |
| 59 | P27-e | Cận Yojin nghiêng mặt, thật lòng: anh không muốn Hikari phải rơi vào nguy hiểm thêm lần nào nữa. | "…không muốn thằng bé phải rơi vào tình cảnh nguy hiểm như vậy một lần nào nữa." | bảo bọc, nặng | **3** |
| 60 | P29-a | Không khí giãn ra. Thầy bảo cứ từ từ, Hikari nói sẽ suy nghĩ thêm. | "Em sẽ suy nghĩ thêm về việc này." | dịu | 2 |
| 61 | P29-b | Yojin thở phào "HOO…". | "HOO…" | nhẹ nhõm | 1 |
| 62 | P29-c | Hikari nhìn nghiêng; chữ viết tay của Yojin đè lên: mình đã có được lòng tin của thằng bé. | "Mình đã có được lòng tin của thằng bé." | mừng thầm | **3** |
| 63 | P29-d | Chibi hài: thầy hỏi còn băn khoăn gì khác không, Yojin nghĩ lung tung về nghề nghiệp của Hikari. | "Anh có câu hỏi hay mối băn khoăn nào khác không?" | hài, hạ nhiệt | 1 |
| 64 | P31-a | **CẢ TRANG.** Ngay trên đầu thầy Shimizu — một con oán hồn khổng lồ: thân người trần, bốn cánh tay dang ra, bụng phình căng gân máu, đầu cuống nhọn chĩa xuống. Thầy vẫn cười hiền, nói tiếp như không có gì. | "Ví dụ như…" / "Bất cứ thứ gì cũng được." | rợn, cú bẻ lái | **3** |
| 65 | P33-a | Góc cao: bóng con oán hồn đổ trùm lên mặt bàn giữa ba người. Thầy vẫn đang nói về các sự kiện của trường. | "…các sự kiện của trường chúng tôi." | rợn gáy | **3** |
| 66 | P33-b | "KRAKL" — Yojin phóng cọc nhọn, đóng một cánh tay quái vật vào trần. | "KRAKL" | ra tay chớp nhoáng | **3** |
| 67 | P33-c | "THWK" — cọc thứ hai cắm vào cái túi bụng của con quái. | "THWK" | dứt khoát | 2 |
| 68 | P33-d | Hikari ngơ ngác nhìn lên; cận mắt Yojin lạnh tanh. | — | căng | 2 |
| 69 | P35-a | Yojin rút bút, giọng vẫn lịch sự — vừa đánh vừa giữ vỏ bọc buổi họp. | "…nếu thầy không phiền, tôi muốn ghi chép lại một chút." | hai tầng, lạnh | **3** |
| 70 | P35-b | Cây cọc cắm ngập, máu đen bắn vệt lên bảng — ngay sau lưng thầy Shimizu đang cắm cúi ghi chép. | — | tàn bạo ngầm | **3** |
| 71 | P35-c | Shimizu vẫn cười, bảo anh đừng ngại. | "Anh không cần phải thấy ngại." | vô tư | 1 |
| 72 | P35-d | Yojin đáp lấp liếm, nghĩ thầm: may quá mình có chuẩn bị trước — nối thẳng về cảnh mở đầu. | "May quá mình có chuẩn bị trước." | ghép nối | **3** |
| 73 | P35-e | Cận mắt Shimizu sau cặp kính, tiếng rên bắt đầu: "EEE…" | "EEE…" | lệch, đáng sợ | **3** |
| 74 | P37-a | Mắt Shimizu trợn trắng, bút rơi "KLAK". | "KLAK" | hỏng, rơi mặt nạ | **3** |
| 75 | P37-b | Hikari quay sang nhìn, chưa hiểu gì. | — | ngơ | 2 |
| 76 | P37-c | Bàn tay quái vật thò ra khỏi khung. | — | đe doạ | 2 |
| 77 | P37-d | **PANEL LỚN.** Thầy Shimizu bị điều khiển, chồm qua bàn, tay quái vật chồng lên tay thầy vươn thẳng tới Hikari. Hikari cứng người. Yojin đã kịp chen tay chặn giữa, giọng vẫn bình thản. | "Thầy Shimizu… …thầy làm rơi bút kìa." | cao trào, lạnh | **3** |
| 78 | P39-a | Yojin đâm một cây kim vào lưng thầy; Shimizu gục xuống bàn "SLUMP", sùi bọt mép. | "SLUMP" | dứt điểm | **3** |
| 79 | P39-b | "THROB THROB" — một khối thịt tròn có cuống dài được rút ra khỏi người thầy. Yojin hiểu ra cơ chế. | "Ra là vậy." | vỡ lẽ | **3** |
| 80 | P39-c | Yojin đỡ Shimizu, bắt mạch, kết luận: con này nhằm **kiểm soát**, không nhằm giết. | "Ý đồ hẳn là để kiểm soát chứ không phải để gây hại." | phân tích lạnh | **3** |
| 81 | P39-d | Hikari hoảng "Ôi không…". Yojin trấn an, bảo sẽ đưa thầy đi nghỉ, dặn cậu ngồi đợi. | "Cháu đợi ở đây nhé, được không?" | tách rời — mầm nguy | **3** |
| 82 | P41-a | Ngoài hành lang, Yojin dìu Shimizu trên vai, xin lỗi thầy vì đã chủ quan. | "Đáng lẽ tôi phải cảnh giác hơn…" | áy náy | 2 |
| 83 | P41-b | Hành lang trường dài, vắng, sáng trắng. | — | trống, gở | 1 |
| 84 | P41-c | Một con oán hồn thứ hai — cùng kiểu thân người tay dang, bụng túi — bám trên lưng một người khác. | — | leo thang | **3** |
| 85 | P41-d | Cận mắt Yojin, đồng tử co. | — | báo động | 2 |
| 86 | P41-e | Yojin bắt chuyện một thanh niên đứng ở cửa lớp, giả vờ hỏi đường. | "Cho hỏi, em có biết phòng y tế ở đâu không…" | giăng bẫy | 2 |
| 87 | P43-a | Yojin hét đánh lạc hướng. Thanh niên "Hả?!". | "Dây giày của em bị tuột kìa!" | mưu mẹo | 2 |
| 88 | P43-b | Thanh niên cúi xuống nhìn chân mình. | "Dây giày của em á?" | mắc bẫy | 1 |
| 89 | P43-c | Yojin rút lưỡi dao, lao tới, chém vào cái túi thịt trên lưng thanh niên. "SHWZRR" | "SHWZRR" | ra đòn | **3** |
| 90 | P45-a | **PANEL LỚN.** "SPLAT" — con oán hồn bị chém nát, bắn tung. Yojin đứng thẳng, mặt không đổi. | "SPLAT" | dứt khoát, lạnh | **3** |
| 91 | P45-b | Yojin đỡ thanh niên, nghĩ: không chỉ có một con — và nếu nhiều hơn một thì ổ của chúng phải ở ngay gần đây. | "…thì ổ của chúng chắc chắn phải ở gần đây." | vỡ quy mô | **3** |
| 92 | P47-a | **PANEL LỚN.** Yojin cầm ngược lưỡi dao, mặt nửa sáng nửa tối, tính tới nước diệt tận gốc. | "Nếu mình tiêu diệt nó…" | quyết | **3** |
| 93 | P47-b | "WHOA!" — thanh niên bật né ra sau, một vật tròn văng lên không. Cận một con mắt có vòng tròn đồng tâm. | "WHOA!" | lật kèo | **3** |
| 94 | P49-a | Bàn tay thanh niên bị lưỡi dao xuyên qua — "OWWW!" — nhưng không hề hấn gì. Yojin nhận ra vũ khí vô dụng với hắn. | "Chà, không có tác dụng rồi…" | hụt, xấu | **3** |
| 95 | P49-b | **PANEL LỚN.** Thanh niên (tóc nâu rối, áo khoác jean, khuyên tai, dây chuyền) tự tay rút con oán hồn ra khỏi vai mình "SHLP", cười toét. Hắn nói đã đoán trước là phải xử Yojin đầu tiên. | "Tao đã có linh cảm là sẽ phải giải quyết mày trước rồi mà." | phản diện lộ diện | **3** |
| 96 | P51-a | **PANEL LỚN.** Cận mặt thanh niên, mắt lim dim giễu cợt, tay cầm lưỡi dao vừa rút ra khỏi mình. | "Thế giờ tính sao đây, hả ông anh trừ tà?" | ngạo, áp đảo | **3** |
| 97 | P51-b | Yojin lùi lại, dao trong tay nhưng không dùng được. Bùng nổ chữ to: **hắn là người thường** — nên anh không được chém. Quanh đó có tiếng rên "Dừng lạiii…". | "CẬU TA LÀ NGƯỜI THƯỜNG!!" | bế tắc | **3** |
| 98 | P53-a | **PANEL LỚN.** Cả hành lang đầy giáo viên, nhân viên trường bị chiếm xác: mắt đục, miệng chảy dãi, tay cầm chổi, lảm nhảm những câu vụn của nhà trường. | "…ổôôổ hàành laang…" | ghê rợn, vây | **3** |
| 99 | P53-b | Thanh niên đứng giữa đám đông, cười, nói bạo lực không hợp gu hắn. | "…bạo lực thực sự không phải gu của tôi đâu…" | thong dong | **3** |
| 100 | P53-c | Cận một con mắt trắng dã của người bị chiếm. | — | rợn | 1 |
| 101 | P53-d | Mặt một người bị chiếm há miệng, nước dãi, rên: "Về… chỗ ngồi, cả lớp." | "…chỗôôô ngồi, cảả lớp." | méo mó, ám | **3** |
| 102 | P55-a | Góc cao: Yojin bị vây kín giữa hành lang. Thanh niên khuyên anh đầu hàng luôn cho rồi. | "…đầu hàng luôn đi cho rồi." | bị dồn | **3** |
| 103 | P55-b | Yojin hỏi thẳng hắn là ai, muốn gì. Qua ô cửa kính phía sau, **Hikari vẫn ngồi một mình trong lớp 2-3** — đúng chỗ Yojin bảo cậu đợi. | "Cậu là ai? Cậu muốn cái gì?" | căng, sợ thay | **3** |
| 104 | P55-c | Thanh niên ra điều kiện: lùi lại thì hắn sẽ nói. | "Lùi lại đi, rồi tôi sẽ nói cho anh biết." | thương lượng | 2 |
| 105 | P57-a | Cận mặt Yojin nghiêng, hé cười — không hề lùi. | "Chà…" | trở mình | **3** |
| 106 | P57-b | **PANEL CUỐI.** Yojin đứng thẳng giữa vòng vây, thong thả chỉnh lại cà vạt ("SHF"), đám bị chiếm xác lố nhố quanh anh. Câu chốt chương. | "…họ có bảo đây sẽ là một buổi họp phụ huynh mà." | lạnh, cú lật | **3** |
| — | P58 | *(BỎ — banner)* Ô chữ "Còn tiếp…" | "Còn tiếp…" | — | — |

> Ghi chú đánh số: bảng có 106 dòng nhưng 2 dòng (#10 P05, #11 P06) là trang tiêu đề đánh **BỎ**, không tính panel. **Tổng panel truyện thật = 104.**

---

### C. Điểm cao trào

Chương này có **bốn đỉnh**, cộng một cú lật câu chữ ở panel cuối.

**Đỉnh 1 — đỉnh cảm xúc (P21-b/c, panel 43–44).**
Hikari nói cậu thấy an toàn khi ở bên Yojin. Yojin không nhận lời khen ấy: anh kết luận thứ khiến thằng bé thấy an toàn chỉ là cái phần "thầy trừ tà" trong anh — rồi bàn tay siết lại dưới gầm bàn, "chưa từng có ai nói với tôi những lời như thế trước đây cả." Đây là chỗ nặng nhất về người, và nó đứng ngay trước khi truyện chuyển sang máu.

**Đỉnh 2 — đỉnh lật không khí (P31, panel 64).**
Cả trang: con oán hồn khổng lồ treo ngay trên đầu thầy Shimizu, trong khi thầy vẫn cười hiền nói tiếp. Mọi thứ hài hước và ấm áp ở 60 panel trước bị kéo tuột xuống trong một khung.

**Đỉnh 3 — đỉnh hành động (P37-d, panel 77).**
Thầy Shimizu bị điều khiển chồm qua bàn, bàn tay quái vật vươn thẳng tới Hikari. Yojin đã chặn tay ở đó từ trước, và vẫn nói bằng giọng lịch sự: "thầy làm rơi bút kìa." Đây là khoảnh khắc quyết định của chương — nó vừa cứu Hikari vừa cho thấy Yojin đã đánh nhau suốt buổi họp mà không ai biết.

**Đỉnh 4 — đỉnh phản diện (P49-b → P51, panel 95–97).**
Thanh niên lạ tự rút con oán hồn ra khỏi vai mình, cười, và Yojin nhận ra lưỡi dao vô dụng: hắn là **người thường**. Kẻ địch mới của bộ truyện lộ diện, và lộ diện đúng lúc Yojin mất thứ vũ khí duy nhất.

**Cú lật cuối (P57-b, panel 106) — đổi nghĩa toàn bộ phần đầu.**
Câu chốt "…họ có bảo đây sẽ là một buổi họp phụ huynh mà" đọc lại thì mang hai nghĩa, và nó khoá ngược ba thứ:
1. **Cảnh mở đầu (P01–P02)** — cái hộp cọc nhọn, câu "tăng cường an ninh", "đi thôi nào" — lúc đọc tưởng là chuẩn bị cho một nhiệm vụ trừ tà nào đó. Hoá ra đó là chuẩn bị cho **đúng buổi họp phụ huynh này**.
2. **Đoạn "MỘT TUẦN TRƯỚC" (P07)** — câu "Đây sẽ là một nhiệm vụ quan trọng" lúc đầu là cú hài (nhiệm vụ = đi họp phụ huynh). Đọc lại thì nó **không phải đùa**: đây đúng là nhiệm vụ, và anh đã đoán đúng.
3. **Câu "May quá mình có chuẩn bị trước" (P35-d)** — lúc đọc tưởng là nói về sổ ghi chép. Thật ra là về cọc nhọn.

Ba chi tiết đó — cái hộp, chữ "nhiệm vụ", câu "may quá có chuẩn bị" — để cạnh nhau thì tự nối thành một nghĩa khác.

---

### D. Chưa rõ

**Không đoán, ghi nguyên trạng:**

1. **Người đối thoại với Yojin ở P01–P02.** Chỉ thấy một bàn tay, một mặt nghiêng và cổ tay đeo đồng hồ. Không thấy mặt đủ rõ, không có tên, không nói mình thuộc đâu. → Không được gọi tên, không được suy ra là "cấp trên" hay "tổ chức".
2. **Tên và thân phận thanh niên phản diện (từ P41 đến hết).** Chưa xưng tên, chưa nói mình là ai hay muốn gì. Đặc điểm nhìn thấy: nam, trẻ, tóc nâu rối, áo khoác jean/bò, áo trong trắng, khuyên tai, dây chuyền. Hắn điều khiển được oán hồn, tự gỡ oán hồn khỏi người mình không hề hấn, và Yojin xác định hắn là **người thường**. → Trong video gọi là "thanh niên lạ" / "kẻ lạ", **không đặt biệt danh**.
3. **Vì sao lưỡi dao của Yojin không có tác dụng với hắn** (P49-a). Chỉ biết là không ăn thua và Yojin bật ra "cậu ta là người thường" — không rõ đó là lý do kỹ thuật (vũ khí chỉ ăn oán hồn) hay là nguyên tắc nghề (không được chém người). **Chưa rõ, không giải thích thay.**
4. **Ai nói câu "CẬU TA LÀ NGƯỜI THƯỜNG!!" và tiếng rên "DÙNGGG LẠIII…" ở P51-b.** Bóng thoại không rõ đuôi chỉ về ai. Có thể là tiếng bật ra trong đầu Yojin, cũng có thể là tiếng của đám bị chiếm xác. → Nếu dùng, phải kể theo hướng trung tính.
5. **"Vật tròn" văng ra ở P47-b và rơi loảng xoảng ở P48.** Nhìn rõ là một khối tròn có hoa văn, nhưng không đọc được nó là cái gì, của ai, có tác dụng gì.
6. **Bản chất con oán hồn ký sinh.** Thấy rõ hình dạng (thân người nhiều tay + túi bụng phình + cuống nhọn) và biết ý đồ là **kiểm soát chứ không giết** (Yojin nói ở P39-c). Nhưng chưa rõ nó vào người bằng cách nào, từ bao giờ, và "ổ" mà Yojin nhắc ở P45-b nằm ở đâu. **Không suy ra.**
7. **Thầy Shimizu bị chiếm từ lúc nào.** Panel P31 là lần đầu con quái hiện hình, nhưng không có gì trong ảnh nói nó bám thầy từ trước buổi họp hay mới bám trong lúc họp. Cũng **chưa rõ** những lời tốt đẹp thầy nói về Hikari ở P15–P17 là lời thật của thầy hay đã bị chi phối — ảnh không trả lời. → Đây là chỗ dễ kể sai nhất, phải để nguyên mơ hồ.
8. **Số người bị chiếm xác và phạm vi.** P53 cho thấy cả hành lang, gồm giáo viên và nhân viên, nhưng không đếm được và không rõ có lan ra ngoài trường không.
9. **Hikari có nhìn thấy con oán hồn không.** Ở P33-d cậu ngẩng lên nhìn về phía đó, mặt ngơ ngác; không có thoại nào xác nhận cậu thấy hay không thấy. **Không kết luận.**
10. **Chữ mờ / không đọc được:** dòng chữ nhỏ tiếng Nhật trong tờ thông báo P07-a và tờ phiếu nguyện vọng P09-b → **KHÔNG ĐỌC ĐƯỢC**, không dịch đoán.

**Lưu ý thuật ngữ (đối chiếu series-bible):**
Bản dịch chương 3 dùng cả **"oán linh"** (P11-d, P17-c) và **"linh hồn quấy phá"** (P19-a). Theo bible, trong video **chỉ dùng "oán hồn"** cho nhất quán với chương 1. Bảng trên trích nguyên văn thoại, nhưng khi viết lời kể phải quy về **oán hồn**.

**Tên mới cần bổ sung vào series-bible sau khi duyệt:**
- **Shimizu** — giáo viên chủ nhiệm lớp 2-3 của Hikari, nam, lớn tuổi, đeo kính, tóc bạc, mặc áo len. Bị oán hồn ký sinh điều khiển trong buổi họp, Yojin gỡ ra, còn sống, mạch bình thường.
- Xác nhận cách gọi **"anh Odaki"** — thầy Shimizu gọi Yojin bằng họ (P13-b, P25-d), khớp với "Yojin Odaki" trong bible.

---

## DỪNG Ở ĐÂY — chờ duyệt

Chưa viết lời kể, chưa sang `/manga-narration`. Ba câu hỏi duyệt:

1. **Panel có thật không?** — 104 panel ở mục B có khớp với ảnh không, đặc biệt các panel lớn P31, P37-d, P45-a, P49-b, P53-a, P57-b?
2. **Tên nhân vật đúng chưa?** — "Shimizu" (mới), "Yojin"/"anh Odaki", và cách gọi **"thanh niên lạ"** cho kẻ phản diện chưa có tên — có ổn không, hay muốn gọi khác?
3. **Trọng số hợp lý chưa?** — có 47 panel để TS 3. Với ngân sách 180 giây / 468 từ thì hơi nhiều; cần hạ bớt đỉnh nào xuống 2 để lời kể có chỗ thở?
