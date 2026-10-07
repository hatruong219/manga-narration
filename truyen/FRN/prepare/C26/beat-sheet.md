# BEAT SHEET — FRN Chương 26 "Món quà dành cho chiến binh"

Nguồn ảnh: `truyen/FRN/prepare/C26/pages-clean/` (21 file, truyenqq 900px).
Đã đọc HẾT 21/21 file, P01 → P21, không nhảy cóc.

---

## A. Kiểm tra đầu vào

- Nhận đủ 21 file `FRN_C26_P01.jpg` → `FRN_C26_P21.jpg`, không thiếu trang liên tiếp.
- **Crop của `clean-pages.py`** (so `pages/` gốc với `pages-clean/`):
  - `P01`: 900×1075 → 900×585 (**cắt 490px** ở dưới) — nhưng phần còn lại **vẫn là banner quảng cáo bộ truyện khác** (collage "Hatsukoi Zombie", "Shinigami Bocchan…", "Komi-san…", credit 7 Fingers Team) — **không liên quan FRN, giữ nguyên diện BỎ**.
  - `P21`: 900×976 → 900×946 (**cắt 30px**) — vẫn là banner "12 FINGERS TEAM" + quảng cáo truyenqqq.com — **BỎ**.
  - `P02`–`P20`: **không đổi kích thước** (chỉ đổi từ ảnh xám 1 kênh sang RGB 3 kênh — không phải crop nội dung).
- **Trang BỎ (không phải nội dung truyện):**
  - `P01` — banner quảng cáo các bộ truyện khác của 7 Fingers Team, không có gì thuộc FRN.
  - `P02` — trang credit 7 Fingers Team + bìa "Sousou no Frieren", dùng lại khuôn "2 話 僧侶の嘘" (đúng mẫu credit tái sử dụng đã ghi nhận ở các chương trước — không phải tải nhầm chương).
  - `P21` — banner "12 FINGERS TEAM" + quảng cáo truyenqqq.com.
- **Trang nội dung: P03 → P20 (18 trang).** `P03` là trang tiêu đề gộp cảnh (chương "Chương 26 – Món quà dành cho chiến binh" + cảnh dã ngoại ba người) — tính là nội dung vì có cảnh, không phải trang trắng thuần tên chương.
- **Số in trên trang (góc trái/phải dưới mỗi trang) khớp đúng công thức "số in = số file − 2"** xuyên suốt `P04`(in "2") → `P20`(in "18") — đã kiểm bằng mắt từng file, không suy đoán. `P03` không thấy số in rõ (trang tiêu đề).
- **Đọc PHẢI → TRÁI — xác minh bằng chứng cứ (không chỉ giả định):**
  - `P10`: chuỗi hỏi–đáp liền mạch "STARK-SAMA NÀY. CẬU CÓ MUỐN THỨ GÌ KHÔNG?" → "À Ờ. THẾ LIÊN QUAN GÌ ĐẾN VỤ TÔI MUỐN GÌ?" chỉ khớp nghĩa theo đúng thứ tự đọc đã dùng.
  - `P15`: "TÔI CHỈ LÀ ĐỒ BỎ ĐI LUÔN THÁO CHẠY MÀ THÔI." → "CHIẾN BINH STARK MÀ TÔI BIẾT TỪ TRƯỚC ĐẾN NAY CHƯA TỪNG BỎ CHẠY LẦN NÀO CẢ." là một cặp than–đáp, thứ tự ngược sẽ vô nghĩa.
  - `P18`→`P19`: hồi tưởng "ANH ĐANG NẤU GÌ VẬY, ANH TRAI?" → "NGƯỜI CHIẾN BINH NỖ LỰC HẾT MÌNH…" → "ĐỪNG NÓI CHO CHA VÀ MỌI NGƯỜI BIẾT ĐẤY. LÀ MÓN BÍT TẾT HAMBURG ĐÓ. HÔM NAY LÀ SINH NHẬT CỦA EM MÀ." nối liền mạch xuyên hai trang, xác nhận thứ tự đọc đúng.
  - **Lưu ý:** vài trang có bố cục khung lệch (khung dọc cao xen khung ngang) mà ảnh 900px không đủ để thấy rãnh khung rõ — thứ tự trong-trang (a, b, c…) ở các trang đó suy theo mạch thoại liền nghĩa, không phải theo toạ độ pixel tuyệt đối. Đã đánh dấu cụ thể ở cột "Sự việc" chỗ nào còn không chắc.

---

## B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang tiêu đề: Stark, Frieren, Fern ngồi ăn dã ngoại trong rừng (giỏ đồ ăn, rìu lớn dựng cạnh gốc cây, tông nền có vệt mưa). Tên chương hiện: "Chương 26 – Món quà dành cho chiến binh". | (không thoại — chỉ tên chương) | yên bình, mở màn | 1 |
| 2 | P04-a | Khung dẫn: mốc thời gian + địa danh mới. | "29 năm đã trôi qua kể từ lúc Anh hùng Hummel qua đời." / "Các vùng phương Bắc, khu vực Appetit." | trung tính, đóng mốc | 2 |
| 3 | P04-b | Frieren và Fern tới một thị trấn, dừng ở quán trọ, nói chuyện với ông chủ trọ, bàn sẽ rảnh tới tối sau khi cất hành lý. | "Mãi mới đến thị trấn đấy nhỉ? Cuối cùng thì cũng có thể thả lỏng người rồi." | thư giãn | 1 |
| 4 | P04-c | Frieren nằm dài trên giường trọ (cầm một khung ảnh nhỏ), chợt nhớ ra hôm nay là sinh nhật Stark. | "À mà ta vừa mới sực nhớ ra hôm nay là sinh nhật tuổi 18 của Stark thì phải." | bất ngờ nhẹ | 2 |
| 5 | P04-d | Cận cảnh khung ảnh Frieren đang cầm/nhìn. **CHƯA RÕ ảnh chụp ai** — không đủ chi tiết để gọi tên. | (không thoại rõ) | hoài niệm mơ hồ | 1 |
| 6 | P04-e | Fern hỏi Frieren có định làm gì không, gợi ý đi xem cửa hàng; Frieren từ chối, muốn ở lại phòng trọ đọc sách phép. | "Frieren-sama này, ngài có tính làm gì không ạ? Hay là chúng ta lại đi xem qua các cửa hàng và các món đồ đây?" / "À thôi. Hôm nay ta sẽ từ từ tận hưởng cuốn sách phép này ở trong phòng trọ." | thường nhật | 1 |
| 7 | P05-a | Fern lo lắng: không biết Stark thích gì; Frieren trêu Fern "tấm lòng ấm áp mà không thấu hiểu nổi à". | "Nhưng em có biết Stark-sama thích gì đâu?" | bối rối, hài nhẹ | 1 |
| 8 | P05-b | Bàn tính đi mua quà ngay trong thị trấn này vì chưa chuẩn bị gì. | "Thì giờ chỉ cần đi mua chút gì ở thị trấn này thôi?" / "Em… chưa chuẩn bị được gì cả." | sốt ruột | 1 |
| 9 | P05-c | Frieren cầm ra một lọ thuốc "làm tan chảy quần áo" làm ứng viên quà, tự nhận đó là món mình thích. | "Lọ thuốc làm tan chảy quần áo." / "Dĩ nhiên là món đồ mà ta yêu thích rồi." | hài, lố bịch | 2 |
| 10 | P05-d | Fern hỏi lại Frieren đã định tặng Stark cái gì chưa; Frieren có vẻ hào hứng khoe. | "Vậy ngài đã tính tặng cậu ấy cái gì chưa ạ?" | tò mò | 1 |
| 11 | P05-e | Frieren (quỳ xuống) đưa cho Fern xem "món quà" đó, khẳng định ai nhận được cũng sẽ cảm động, dẫn lời sư phụ. | "Nếu ai mà nhận được món quà này thì sẽ cảm động lắm đó… sư phụ đã bảo ta như thế đấy." | mỉa mai/hài | 1 |
| 12 | P06-a | Fern cận mặt, nhắc lại rằng đã từng bảo Frieren phải trả lại đúng lọ thuốc thô thiển này khi mua nó. | "Cái lọ thuốc thô thiển này… em nhớ là mình đã bảo ngài phải trả lại khi ngài mua nó rồi cơ mà nhỉ?" | bực dọc | 1 |
| 13 | P06-b | Cảnh đổ/tạt (âm thanh "đổ đổ đổ", "Á á á!") — lọ thuốc gây phản ứng hài hước, không rõ ai bị tạt trúng ai. **CHƯA RÕ chi tiết ai đổ, ai dính.** | "Áá á!" | hài, hỗn loạn | 1 |
| 14 | P06-c | Fern bỏ đi, mặc kệ Frieren với trò đùa của cô. | "Thôi em mặc xác Frieren-sama luôn đấy." | dứt khoát, hài | 1 |
| 15 | P06-d | Frieren ngồi một mình, băn khoăn nên tặng gì, cầm lên một cuốn sách. | "Thế giờ phải tặng gì đây ta…" / "Là cái này à." | phân vân | 1 |
| 16 | P06-e | Frieren cuộn trong chăn, vẫn tiếc nuối về lọ thuốc bị gạt bỏ. | "…Lọ thuốc này thú vị thế cơ mà…" | hài, dai dẳng | 1 |
| 17 | P07-a | Fern ra phố tìm Stark, tự nhủ đành phải hỏi thẳng dù dễ lộ ý định. | "Đành phải hỏi trực tiếp vậy… Tuy làm vậy thì cũng sẽ dễ bị lộ…" | quyết tâm, hơi lo | 1 |
| 18 | P07-b | Hỏi thăm dân làng — không thấy Stark ở nhà. | "Ra ngoài rồi sao…" | tìm kiếm | 1 |
| 19 | P07-c | Dân làng kể Stark vừa cứu một bé mèo mắc kẹt trên cây. | "Anh ấy đã mang bé mèo xuống khi nó bị mắc kẹt trên cây đó ạ." / "Chiến binh mang trên lưng cây rìu à?" | ấm áp | 1 |
| 20 | P07-d | Thêm: Stark giúp đẩy xe hàng, ngăn đàn gia súc chạy loạn, chơi với trẻ con trong làng — hình ảnh Stark được cả làng quý mến. | "Cậu ta vừa giúp bác đẩy xe hàng đấy." / "Thằng bé vừa ngăn đàn gia súc của ông khỏi chạy như điên." / "Ảnh vừa chơi với tụi em xong." | ấm áp, gây thiện cảm | 2 |
| 21 | P08-a | Fern âm thầm nghĩ (bong bóng mây): không đời nào Stark thích nổi lọ thuốc kỳ quặc đó. | "Không đời nào Stark-sama lại ưng ý cái lọ thuốc sặc mùi biến thái đó đâu…" | tự trào | 1 |
| 22 | P08-b | Hai người dân gần đó bàn tán về ai đó "giúp nhiều người" và khen "Frieren-sama khiêm nhã quá". **CHƯA RÕ** — lời khen có nhắm đúng đối tượng hay là dân làng nhầm công của Stark sang Frieren; không đủ căn cứ để khẳng định. | "Giúp nhiều người thật ha…" / "Frieren-sama khiêm nhã quá đi." | mơ hồ | 1 |
| 23 | P08-c | Fern tìm thấy Stark, gọi tên nhưng bị cắt ngang; Fern buột miệng chê "biến thái", Stark tự ti về vẻ ngoài mình lúc đó. | "Stark-sa-…" / "Eo ơi biến thái." / "Trông giống vếu ghê." | ngượng, hài | 1 |
| 24 | P09-a | Stark tự trách mình "y như cục phân", nhận ra Fern đang tới. | "Giờ lại y như cục phân rồi." / "Ô kìa." | tự ti, hài | 1 |
| 25 | P09-b | Fern hoảng vì không biết đáp sao với chuyện vừa rồi; Stark tự nhủ lát nữa sẽ kể cho Fern nghe "chuyện này". | "Tôi không biết phải đáp sao hết!!!" / "Chắc tí nữa kể Fern nghe về cái này vậy." | rối, tò mò | 1 |
| 26 | P09-c | Fern thầm nghĩ mình đã nhầm, thấy Stark "chẳng khác gì một đứa trẻ". Stark rủ Fern đi tản bộ, cô đồng ý. | "Mình nhầm thật rồi. Cậu ta chẳng khác gì một đứa trẻ cả…" / "Cậu đi tản bộ với tôi chút nhé?" / "Ừ được thôi." | dịu lại | 1 |
| 27 | P09-d | Stark xin lỗi Fern (**CHƯA RÕ vì chuyện gì cụ thể**); Frieren xuất hiện đúng lúc, nhận ra mây báo mưa. | "…Thành thật xin lỗi." / "Không có gì đâu ạ." / "A, Fern, vừa đúng lúc lắm. Đám mây này… Stark-sama." | dịu, chuyển cảnh | 1 |
| 28 | P10-a | Cả ba đi dạo; Fern loay hoay tìm cách hỏi Stark một cách tự nhiên. | "Làm thế nào để tỏ ra tự nhiên đây…" | hồi hộp | 1 |
| 29 | P10-b | Fern buột miệng hỏi thẳng Stark có muốn gì không; Stark ngơ ngác không hiểu liên quan gì. | "Stark-sama này. Cậu có muốn thứ gì không?" / "À ờ. Thế liên quan gì đến vụ tôi muốn gì?" | lúng túng | 1 |
| 30 | P10-c | Fern để lộ: hôm nay là sinh nhật Stark. Anh bực mình vì bị chọc, đòi dẹp chuyện đó qua. | "Thì hôm nay là sinh nhật của Stark-sama mà." / "…Cậu làm tôi bực rồi đấy. Thôi dẹp đi." | ngại ngùng, phòng thủ | 2 |
| 31 | P10-d | Fern giữ vững: đó là quà sinh nhật cho Stark; Stark ngạc nhiên hỏi lại cô định tặng gì. | "Thì là quà sinh nhật của Stark-sama ấy." / "Ớ? Cô tính tặng gì cho tôi á?" | bất ngờ | 1 |
| 32 | P11-a | Stark hỏi lại: đến cả gia đình cũng chưa từng tặng quà sinh nhật cho cậu sao? Stark thú nhận chưa từng nhận quà sinh nhật nào — kể cả từ gia đình đã mất hay từ sư phụ (Eisen) — nên có hơi bỡ ngỡ. | "Rốt cuộc cậu sống trong phong tục nào vậy?" / "Trước đây… tôi chưa từng được nhận bất cứ món quà sinh nhật nào cả. Kể cả là quà từ gia đình quá cố hay từ sư phụ." | chùng xuống, hé lộ | 3 |
| 33 | P11-b | Stark trấn an Frieren là không có ý trách; rồi tự kể: sinh ra ở "làng chiến binh" — nơi không có chỗ đứng cho kẻ yếu kém. Anh tự nhận mình "chưa bao giờ được đánh giá cao". | "Tôi sinh ra ở làng chiến binh, một nơi không hề có chỗ đứng cho những kẻ yếu kém." / "Không đâu. Chỉ là tôi chưa bao giờ được đánh giá cao thôi." | tự ti, bắt đầu hồi tưởng | 3 |
| 34 | P11-c | **Hồi tưởng mở ra** (bối cảnh doanh trại): một chiến binh áo choàng trắng được khen ngợi vì "không một giọt máu hay vết bùn nào nhuốm phải" trên áo — biểu tượng đẳng cấp trong làng. | "Không hề có một giọt máu hay vết bùn nào nhuốm phải, huống chi là một vết thương kia kìa." | trang nghiêm | 1 |
| 35 | P11-d | Một chỉ huy áo đen mắng một chiến binh khác vì chật vật trước một con quái, bảo "noi gương Stolz đi" — **lần đầu tên "Stolz" xuất hiện** (nhân vật mới, chưa có trong bible). | "Đối phương chỉ là một con quái mà cũng chật vật thế à? Noi gương Stolz đi." | phê phán, áp lực | 2 |
| 36 | P12-a | Toàn cảnh làng chiến binh (chưa có tên riêng). | (không thoại) | thiết lập bối cảnh | 1 |
| 37 | P12-b | Một người đàn ông áo choàng trắng (dáng là cha) công khai khen ngợi Stolz là niềm tự hào cả làng; Stolz đáp khiêm tốn "cha đã quá khen". | "Con chính là niềm tự hào của cả làng đấy, Stolz à." / "Cha đã quá khen rồi." | tự hào (của gia đình Stolz) | 2 |
| 38 | P12-c | Dân làng giải thích thêm: áo choàng trắng không tì vết = minh chứng là chiến binh tài giỏi nhất làng. | "Không một vết nhơ trên áo choàng trắng là minh chứng rõ ràng nhất…" | ngưỡng mộ | 1 |
| 39 | P12-d | Một người đàn ông có sẹo, vẻ hoài nghi, nhận xét dù luyện tập ngày đêm cũng chẳng thể đương đầu nổi quái vật — rồi buông một câu so sánh gay gắt, gọi thẳng tên Stark là "cái loại vứt đi" so với Stolz. **CHƯA RÕ người nói câu này có phải cha của Stark/Stolz hay một nhân vật khác** — ảnh không xác nhận danh tính người có sẹo. | "Thì vẫn chẳng thể đương đầu nổi với lũ quái vật." / "So với con thì thằng Stark đúng là cái loại vứt đi." | cay nghiệt, tổn thương | 3 |
| 40 | P12-e | Trời đổ mưa; nhóm người rời đi. Phía sau, Stark nhỏ đang một mình luyện kiếm ngoài mưa. | "Trời đổ mưa rồi. Mau về thôi." | cô đơn, tương phản | 2 |
| 41 | P13-a | Một người áo choàng trắng (lớn tuổi hơn, có vẻ là bậc trưởng bối/cha) đi ngang chỗ Stark tập, dặn người đang huấn luyện cậu đừng quát nạt quá, và nói làm vậy "chỉ tổ phí thời gian" rồi bỏ đi trước. | "Đừng có nạt nộ nó nhiều quá đấy. Ta sẽ về trước." / "Với lại làm vậy chỉ tổ phí thời gian mà thôi." | lạnh nhạt, coi thường | 2 |
| 42 | P13-b | Người ở lại — **anh trai của Stark** (chưa có tên riêng trong ảnh) — tự nói một mình, xác nhận đang huấn luyện "đứa em bất tài của mình". | "Con qua huấn luyện đứa em bất tài của mình đây." | mỉa mai bề ngoài, che giấu sự quan tâm | 2 |
| 43 | P13-c | Stark nhỏ tiếp tục vụt kiếm vào hình nộm tập giữa mưa; anh trai đứng lặng quan sát không nói gì. | "・・・" | căng thẳng, im lặng | 1 |
| 44 | P13-d | Stark nhỏ ngẩng lên, bật khóc, xin lỗi anh trai (**chưa rõ vì lỗi gì cụ thể trong khung này**). | "…Anh trai… Em xin lỗi…" | đau lòng | 2 |
| 45 | P14-a | Anh trai quỳ xuống, chỉnh lại tư thế cầm kiếm cho Stark, khen sự tập trung là tốt. | "Tập trung thế là tốt." | dịu dàng | 2 |
| 46 | P14-b | Anh trai khẳng định tin Stark sẽ trở nên mạnh mẽ, chỉ là tư thế hiện tại có hơi sai. | "Anh tin chắc rằng em sẽ trở nên mạnh mẽ thôi. Nhưng giờ tư thế có hơi sai chút rồi." | ấm áp, hy vọng | 3 |
| 47 | P14-c | Cắt về hiện tại: Stark kể tiếp với Frieren rằng trong cả làng, chỉ có anh trai là đối xử khác với cậu. | "Kể ra thì có mỗi anh tôi là khác so với những người còn lại." | trân trọng, u hoài | 2 |
| 48 | P14-d | **Cú lật/đỉnh hồi tưởng:** Stark thú nhận khi làng bị "quỷ dữ" tấn công, cậu đã bỏ mặc anh trai và chạy thục mạng — kèm tranh làng cháy, hình nộm chiến binh khổng lồ tối màu giữa lửa. | "Nhưng dù vậy thì khi làng tôi bị tấn công bởi quỷ dữ, thì tôi đã bỏ mặc anh mình và chạy thục mạng." | day dứt, tội lỗi | 3 |
| 49 | P15-a | Hiện tại: Frieren gọi tên Stark; Stark tự nhận mình chưa từng được gia đình trọng dụng, chỉ là "đồ bỏ đi luôn tháo chạy". | "Bảo sao mà tôi lại không được gia đình mình trọng dụng. Tôi chỉ là đồ bỏ đi luôn tháo chạy mà thôi." | tự ti, cay đắng | 2 |
| 50 | P15-b | **Đỉnh cảm xúc chính:** Frieren phản bác dứt khoát — chiến binh Stark mà cô biết chưa từng bỏ chạy lần nào; quá khứ ra sao thì giờ không còn vướng bận. | "Chiến binh Stark mà tôi biết từ trước đến nay chưa từng bỏ chạy lần nào cả." / "Quá khứ cậu có ra sao thì giờ cũng không còn vướng bận nữa." | an ủi, khẳng định, ấm lòng | 3 |
| 51 | P15-c | Frieren chuyển mạch nhẹ nhàng, rủ Stark cùng đi chọn quà sinh nhật; Stark ban đầu từ chối, Frieren doạ sẽ tự chọn nếu cậu không chọn; Stark đùa lại có khi mai sau lại tháo chạy không chừng, rồi bỏ lửng câu nói. | "Mình cùng đi chọn quà sinh nhật nhé." / "…Thôi được rồi." / "Dễ có khi mai sau tôi lại tháo chạy không chừng." / "Nhưng tôi…" | nhẹ nhõm dần, còn vướng mắc | 2 |
| 52 | P16-a | Ba người đi mua sắm; Stark từ chối một món trang sức vì đắt, "không kham nổi". | "Đắt lắm, tôi không kham nổi." / "Vậy à." | ngại ngùng | 1 |
| 53 | P16-b | Frieren gợi ý món khác. | "Thế cái này thì sao?" | tò mò | 1 |
| 54 | P16-c | Chuyển cảnh: hành lang quán trọ. | (không thoại) | chuyển cảnh | 1 |
| 55 | P16-d | Tại bàn ăn: hoá ra "món quà" thật sự là một bữa tối — Stark ngỡ ngàng khi biết hôm nay là sinh nhật dành cho chính mình; hỏi về đĩa bít tết hamburg khổng lồ. | "Cô nói gì vậy chứ? Đây chính là sinh nhật dành cho tôi đấy." / "Frieren-sama, cái bít tết hamburg siêu to khổng lồ này là sao thế ạ?" | ấm áp, bất ngờ | 2 |
| 56 | P16-e | Frieren giải thích: cô luôn làm món này vào dịp này; nói thêm rằng sư phụ (Flamme) chưa từng tặng cô món quà nào — rồi bỏ lửng câu, một cô gái tai nhọn (Frieren) bưng đĩa thức ăn nóng hổi ra; người ở nhà bếp nhận xét hai đứa về muộn. | "Người luôn làm món bít tết hamburg nhân dịp này đó." / "Sư phụ chưa từng tặng tôi bất cứ món quà nào, nhưng mà…" / "Về rồi à? Hai đứa muộn quá đó." | ấm cúng, còn treo lửng | 2 |
| 57 | P17-a | Stark ngơ ngác hỏi lại "nói gì cơ?"; Fern ngạc nhiên hỏi liệu Eisen chưa từng kể cho Stark nghe chuyện này. | "Nói gì cơ?" / "Stark, Eisen chưa nói cho cậu biết à?" | tò mò | 1 |
| 58 | P17-b | Frieren tự nhận mình cũng "hậu đậu" nên phần nào hiểu được; Stark tự trào "chiến binh đúng là hậu đậu thật đấy", khiến Fern bất ngờ vì Frieren nói câu đó. | "Ừ thì đúng là ta cũng là kẻ hậu đậu, nên ta cũng hiểu được phần nào." / "Chiến binh đúng là hậu đậu thật đấy." / "Frieren-sama mà lại nói ra câu đó sao ạ?" | tự trào, ấm áp | 2 |
| 59 | P17-c | Frieren buông một câu triết lý: suy tư sẽ chẳng thể được thấu hiểu nếu không nói ra bằng lời; Stark tự nhận xét "ngốc nghếch quá nhỉ". | "Những suy tư sẽ chẳng thể nào được thấu hiểu nếu như không diễn tả bằng lời." / "Ngốc nghếch quá nhỉ." | trầm lắng, thấm thía | 2 |
| 60 | P17-d | **Bắc cầu sang hồi tưởng khác** (cảnh lửa trại trước đó): Fern kể lại cô để ý rằng cứ đến sinh nhật ai đó, Eisen lại làm món bít tết hamburg siêu to khổng lồ này — nhưng không hiểu để làm gì; Frieren đáp lửng "và vì vậy…", dẫn vào lời giải thích của Eisen. | "Giờ tôi mới để ý là cứ lúc nào đến sinh nhật của ai đó là cậu lại làm món bít tết hamburg siêu to khổng lồ này. Nhưng mà… để làm gì chứ?" / "Và vì vậy…" | tò mò, chuẩn bị đỉnh | 2 |
| 61 | P18-a | **Hồi tưởng Eisen**: ông trao món bít tết hamburg cho Frieren như quà sinh nhật từ ông, giải thích đây là phong tục ở chỗ ông — món quà dành cho những chiến binh đã nỗ lực hết mình. | "Cứ coi như là một món quà sinh nhật từ tôi đi." / "Đây là phong tục ở chỗ tôi. Một món quà dành cho những chiến binh đã nỗ lực hết mình." | ấm áp, trang trọng | 2 |
| 62 | P18-b | Frieren hỏi lại thế nào là "nỗ lực hết mình"; Eisen đáp ai nỗ lực hết mình thì đều là chiến binh cả; Stark phản bác nhẹ rằng cả nhóm đâu phải chiến binh. | "Ai mà nỗ lực hết mình thì đều là chiến binh hết." / "Nhưng Eisen à, tụi tôi không phải chiến binh." | ấm áp, hài nhẹ | 1 |
| 63 | P18-c | **Hồi tưởng lồng hồi tưởng:** Stark nhỏ hỏi anh trai đang nấu gì trong bếp; anh trai bắt đầu giải thích, câu nói bị ngắt giữa chừng nối sang trang sau. | "Anh đang nấu gì vậy, anh trai?" / "Người chiến binh nỗ lực hết mình…" | ấm áp, hé lộ | 2 |
| 64 | P19-a | **Đỉnh cảm xúc của chương:** cận cảnh anh trai dặn Stark giữ bí mật với cha và mọi người — hoá ra món bít tết hamburg là quà sinh nhật bí mật riêng anh làm cho Stark hằng năm. | "Đừng nói cho cha và mọi người biết đấy." / "Là món bít tết hamburg đó. Hôm nay là sinh nhật của em mà." | ấm áp, xót xa (khán giả đã biết kết cục) | 3 |
| 65 | P19-b | Cắt về Stark nhỏ ngồi ăn một mình trong im lặng (khung không thoại). | (không thoại) | cô đơn | 2 |
| 66 | P19-c | **Cú lật bi kịch:** làng bốc cháy, quái vật đen khổng lồ xuất hiện; anh trai đặt tay lên vai Stark, bảo em phải chạy để sống. | "Hãy chạy đi. Em phải sống, Stark à." | đau đớn, hy sinh | 3 |
| 67 | P19-d | Anh trai quay lưng bước về phía quái vật cùng những người làng khác, bỏ lại Stark phía sau. | (không thoại — hình ảnh lưng áo choàng giữa biển lửa) | bi tráng | 3 |
| 68 | P20-a | Toàn cảnh lưng anh trai bước vào trận chiến (khung lớn, để HOLD). | (không thoại) | bi tráng, lặng người | 2 |
| 69 | P20-b | Hiện tại: Stark ăn xong miếng bít tết, khen ngon. | "Ngon lắm." | ấm lòng | 2 |
| 70 | P20-c | Frieren tiết lộ nhẹ nhàng: chính Eisen đã đưa công thức món này cho cô; hỏi lại Stark có ngon không. | "Eisen đưa cho tôi công thức đấy." / "Thế, có ngon không nào?" | ấm áp | 2 |
| 71 | P20-d | Fern chêm vào đùa vui, rót thêm sốt; còn dư chút ít nên hỏi Stark có muốn thêm không — khép chương trong không khí ấm cúng. | "Em lại đổ tiếp vào đầu ngài bây giờ." / "À mà trong này vẫn còn sót lại chút ít, nên nếu cậu muốn thì…" | ấm áp, khép lại nhẹ nhàng | 2 |

---

## C. Điểm cao trào

Chương có **hai đỉnh cảm xúc chính**, nối với nhau bằng cùng một món ăn (bít tết hamburg):

1. **Đỉnh 1 — sự khẳng định (P15-b):** Sau khi Stark tự nhận mình "chỉ là đồ bỏ đi luôn tháo chạy", Frieren phản bác dứt khoát: *"Chiến binh Stark mà tôi biết từ trước đến nay chưa từng bỏ chạy lần nào cả."* Đây là điểm bản lề — chuyển câu chuyện từ tự ti sang được nhìn nhận lại.
2. **Đỉnh 2 — cú lật bi kịch của hồi tưởng (P19-a → P19-d):** Món bít tết hamburg hoá ra là truyền thống sinh nhật bí mật của **anh trai Stark** dành riêng cho cậu ("Đừng nói cho cha và mọi người biết đấy… Hôm nay là sinh nhật của em mà"), ngay sau đó cắt sang cảnh làng cháy, anh trai bảo Stark chạy để sống rồi một mình bước vào trận chiến với quái vật. Đây là đỉnh bi kịch giải thích toàn bộ mặc cảm "bỏ chạy" của Stark.
3. **Dư chấn ở hiện tại (P20-b → P20-d):** Stark ăn ngon lành món bít tết hamburg do Frieren nấu theo đúng công thức của Eisen — mà (theo mạch truyện) chính là công thức bắt nguồn giống hệt món quà bí mật năm xưa của anh trai cậu. Truyện **không nói thẳng** hai truyền thống này có liên hệ nhân quả hay chỉ là trùng hợp cảm xúc — xem mục D.
4. **Điểm phụ (hài, P05–P06):** mạch truyện phụ về "lọ thuốc làm tan chảy quần áo" — Frieren định chọn làm quà, bị Fern gạt bỏ — tạo tương phản nhẹ nhàng trước khi vào phần nặng của chương.

---

## D. Chưa rõ

- **"Stolz" (P11-d, P12-b) — tên nhân vật mới, CHƯA CÓ trong series-bible.** Được cha giới thiệu công khai là "niềm tự hào của cả làng"; một chỉ huy khác nhắc "noi gương Stolz đi" khi mắng một chiến binh chật vật trước quái vật. **CHƯA RÕ Stolz có phải chính là "anh trai của Stark"** xuất hiện từ P13 trở đi hay không — ảnh không có một câu nào nối thẳng hai cái tên/vai này với nhau. Ngoại hình hai người (tóc, áo choàng trắng không tì vết) khá giống nhau và bối cảnh (cùng làng, cùng khen ngợi bởi người cha) gợi ý mạnh, nhưng **đây chỉ là suy đoán, không phải chữ in trên trang** — không được gộp hai vai này làm một trong lời kể tới khi có chương sau xác nhận.
- **"Anh trai của Stark" — chưa có tên riêng.** Là người duy nhất trong làng đối xử tử tế với Stark thời thơ ấu, huấn luyện cậu, bí mật làm bít tết hamburg mừng sinh nhật cậu hằng năm (giấu cha), và hy sinh (ngụ ý, không xác nhận trực tiếp cái chết) khi bảo Stark chạy trốn lúc làng bị quỷ dữ tấn công. Đây là câu trả lời mới cho mục "CHƯA RÕ quê quán, gia đình Stark" trong bible — **quê quán = "làng chiến binh" (chưa có tên riêng)**, nay xác nhận Stark **có một anh trai đã mất trong vụ tấn công đó.**
- **Người đàn ông có sẹo (P12-d)** buông câu "So với con thì thằng Stark đúng là cái loại vứt đi" — **CHƯA RÕ danh tính** (có thể là cha của Stark/Stolz, có thể là người khác trong làng). Không đủ căn cứ để gọi là "cha Stark".
- **Người áo choàng trắng dặn "đừng nạt nộ nó" rồi bỏ đi (P13-a)** — **CHƯA RÕ** đây có phải cùng người với ông cha ở P12-b hay là một trưởng bối khác của làng.
- **"Khu vực Appetit" (P04-a)** — địa danh mới, chưa có trong bible mục 2b (danh sách địa danh).
- **"29 năm đã trôi qua kể từ lúc Anh hùng Hummel qua đời" (P04-a)** — **LỆCH CHÍNH TẢ SO VỚI BIBLE.** Bible đã chốt tên nhân vật là **"Himmel"** xuyên suốt C1–C15; bản dịch chương này in **"Hummel"**. Cần đối chiếu thêm các chương gần đây (C16–C25, hiện chưa có beat sheet) xem đây là lỗi đánh máy một lần hay nhóm dịch (nguồn/kỳ dịch) đã đổi cách phiên âm từ chương nào — **beat sheet KHÔNG tự sửa thành "Himmel"**, chỉ ghi nhận để người duyệt quyết định.
  - Mốc năm "29" tiếp nối đúng mạch tăng dần từ "28 năm" đã chốt cho C12–C14, không có gì bất thường.
- **Bức ảnh/khung ảnh nhỏ Frieren cầm ở P04-c/P04-d** — không rõ ảnh chụp ai (không đủ chi tiết khuôn mặt/độ phân giải 900px để nhận diện).
- **P06-b (cảnh đổ/tạt, "Á á á!")** — không đủ rõ ai đổ thứ gì lên ai; chỉ chắc là hệ quả hài hước từ vụ lọ thuốc.
- **P08-b** — hai người dân khen "Frieren-sama khiêm nhã quá đi" ngay sau khi nhắc "giúp nhiều người" — **CHƯA RÕ** lời khen này nhắm đúng Frieren hay là dân làng nhầm lẫn công lao vốn là của Stark (loạt việc tốt vừa liệt kê ở P07 đều là của Stark, không phải Frieren). Không đủ căn cứ để khẳng định theo hướng nào.
- **P09-d — Stark xin lỗi Fern ("Thành thật xin lỗi")** — không rõ xin lỗi về chuyện gì cụ thể trong khung này.
- **P13-d — Stark nhỏ khóc xin lỗi anh trai** — không rõ đang xin lỗi vì lỗi cụ thể gì (có thể chỉ là xúc động chung, không phải một lỗi rõ ràng).
- **Quan hệ nhân quả giữa "phong tục" của Eisen và "truyền thống bí mật" của anh trai Stark (P18–P19)** — truyện đặt hai chi tiết cạnh nhau (cùng là bít tết hamburg, cùng ý nghĩa "quà cho chiến binh nỗ lực hết mình") nhưng **không có một câu nào xác nhận Eisen biết về người anh trai, hay ngược lại**. Đây có thể là sự cộng hưởng cảm xúc chủ đích của tác giả chứ không phải một chi tiết cốt truyện đã xác nhận — đừng viết lời kể như thể đã có bằng chứng nối hai điều này.
- **"Quỷ dữ" tấn công làng Stark (P14-d, P19-c)** — khớp với chi tiết đã ghi trong bible từ C10-P23 ("làng cũ bị quỷ dữ tấn công và cậu đã bỏ chạy") nhưng **KHÔNG có tên gọi cụ thể cho con quái/quỷ đó**, và **KHÔNG có bằng chứng nối nó với Quỷ Vương hay bất kỳ quỷ tộc nào đã biết** (Aura, Granat, Lugner…) — giữ nguyên diện tách biệt, đừng gộp.
- **Số phận cụ thể của anh trai Stark** — chương chỉ dừng ở hình ảnh anh bước về phía quái vật giữa lửa; **không có khung nào xác nhận trực tiếp anh đã chết** (dù ngụ ý rất mạnh qua bối cảnh + toàn bộ giọng hồi tưởng day dứt của Stark). Đừng khẳng định "đã chết" như một sự kiện chắc chắn 100% nếu muốn giữ đúng "chỉ ghi điều thấy trong ảnh".
- **Chương C16–C25 chưa có beat sheet** (thư mục `prepare/C16`…`C25` mới chỉ có `pages`/`pages-clean`, chưa qua bước đọc hiểu) — nghĩa là series-bible.md hiện dừng ở C15, và bất kỳ chi tiết nào phát triển thêm ở C16–C25 (nếu có) về Stark/gia đình/Eisen **chưa được đối chiếu** khi lập beat sheet này. Nếu các chương đó đã hé lộ thêm về anh trai Stark hoặc "Stolz", cần gộp lại khi cập nhật bible.

---

## Câu hỏi duyệt

1. **Panel có thật không?** — Đã đọc đủ 21/21 file, không suy diễn khung nào ngoài ảnh; các đoạn không chắc chắn đã đánh dấu CHƯA RÕ ở mục D thay vì đoán.
2. **Tên nhân vật đúng chưa?** — Cần chốt: (a) xử lý chênh lệch "Hummel" (chương này) vs "Himmel" (bible C1–C15); (b) có ghi nhận "Stolz" là nhân vật mới và giữ tách biệt với "anh trai của Stark" như bản beat sheet này hay không.
3. **Trọng số đã hợp lý chưa?** — Đỉnh chính đặt ở P15-b (lời khẳng định của Frieren) và P19 (cú lật bi kịch anh trai/quỷ dữ); phần lọ thuốc P05–P06 cố tình để trọng số thấp (hài mở đầu, không phải đỉnh).
