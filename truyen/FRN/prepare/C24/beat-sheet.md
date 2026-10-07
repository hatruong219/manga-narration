# Beat Sheet — FRN Chapter 24 "Mong muốn của Elf"

### A. Kiểm tra đầu vào

- Nhận đủ **23 file**: `FRN_C24_P01.jpg` → `FRN_C24_P23.jpg`, liên tục, không thiếu trang.
  Đã đọc hết `pages-clean/`, đối chiếu với `pages/` (bản gốc chưa crop) để biết chỗ nào bị cắt.
- **Nguồn ảnh: nettruyen13s, rộng 1000px** — khớp mô tả trong nhiệm vụ, khác khuôn truyenqq
  (900px) của C1–C5/C8–C12. Đã **mở từng file bằng mắt**, không suy theo khuôn chương khác.
- **`clean-pages.py` đã cắt**: `P09` (1435px → 1424px, cắt **11px**) và `P13` (1435px → 1424px,
  cắt **11px**). Các file còn lại **chiều cao pages-clean = chiều cao pages gốc, không bị cắt gì**
  (kể cả P20 cao bất thường 1526px — clean-pages không đụng vào, xem lý do bên dưới).
- **Trang BỎ (chrome, không phải nội dung truyện)** — đã mở từng ảnh, không suy theo khuôn C6/C7/C13-15:
  - `P01` (1000×600) — banner "12 Fingers Team" tranh đôi nam nữ cầm tay, lời cảm ơn độc giả.
    Đặt ở đầu file nhưng nội dung giống banner tổng kết — vẫn là **chrome quảng cáo nhóm dịch**, không có
    thoại truyện.
  - `P02` (1000×800) — trang bìa tập truyện ghép đôi (bìa gốc Nhật + bìa credit): in tên tác giả
    **YAMADA KANEHITO / ABE TSUKASA** (khớp bible), thông tin **TRANSLATOR Credemoe · EDITOR Yahari
    · PROOFREADER Credemoe · QUALITY CHECKER Credemoe** và logo **"12 FINGERS TEAM"**.
  - `P21` (1000×1195) — tranh fanart chữ ký `@abetsukasa`, vẽ Stark cận mặt, không có thoại/panel
    truyện. Cùng dạng với tranh màu bonus đã gặp ở C13-P21 — **giữ lại để dùng thumbnail, không đưa
    vào mạch beat sheet**.
  - `P22` (1000×600) — banner "Tuyển thành viên" của nhóm dịch (quảng cáo tuyển translator/editor).
  - `P23` (1000×522) — banner kỷ niệm ngày ra mắt nhóm "12 FINGERS TEAM" (4/5/2020).
  → Trang GIỮ (nội dung truyện): **P03 → P20 (18 trang)**.
- **Số trang in trên ảnh xác nhận không thiếu trang**: quy luật "số in = số file − 2" đúng cho suốt
  P05(→3) · P06(→4) · P07(→5) · P08(→6) · P10(→8) · P11(→9) · P12(→10) · P14(→12) · P15(→13) ·
  P16(→14) · P17(→15) · P18(→16) · P19(→17) · P20(→18) — dãy số liên tục 3…18, không nhảy cóc.
  P03 là trang tên chương (không đánh số), P04 và P09/P13 không soi rõ số in nhưng nằm đúng vị trí
  trong dãy liên tục nên không nghi ngờ mất trang.
- **P20 cao bất thường (1526px so với ~1435px các trang khác)** — đã mở xem: không phải trang đôi,
  chỉ là trang có nhiều khung dọc xếp chồng (bao gồm khung toàn cảnh dãy núi). Không cần PAN ngang.
- **Xác minh chiều đọc PHẢI → TRÁI (bằng chứng cụ thể)**:
  1. Trang tên chương (P03) giữ nguyên tiêu đề gốc tiếng Nhật in dọc theo cột, chạy dọc theo **mép
     phải** trang — đúng bố cục gốc tiếng Nhật (chữ dọc luôn bắt đầu từ phải), scanlation không lật
     trang mà chỉ dịch chữ trong bong bóng.
  2. Trong toàn bộ 18 trang nội dung, các khung có nhiều ô đều có **lời thoại chỉ tạo thành mạch
     nghĩa hợp lý khi đọc khung phải trước, khung trái sau** (ví dụ P04 hàng 2: khung phải là câu mỉa
     mai của Frieren "Còn chưa kịp đến dãy núi Schewer thì lại mắc kẹt ở đây à" đọc trước, rồi mới đến
     khung trái là Fern hốt hoảng gọi Stark dậy — khớp trình tự phản ứng: thấy Stark ngã trước, giục
     dậy sau). Áp dụng nhất quán cho các trang nhiều khung khác (P06, P08, P11).
  → Kết luận: nguồn đọc **phải → trái** đúng chuẩn manga Nhật, khớp với toàn bộ các chapter trước đó
  trong bộ.
- **Nhóm dịch: tên banner ghi "12 Fingers Team", KHÁC chữ "7 Fingers Team" bible đang chốt** (dòng mở
  đầu series-bible.md) — nhưng **thành viên trùng khớp 100%**: TRANSLATOR Credemoe, EDITOR Yahari,
  PROOFREADER/QC Credemoe, đúng những cái tên bible đã ghi từ C1/C2. Slogan trên banner "Khi 7 ngón là
  chưa đủ" (P01) xác nhận đây là **cùng một nhóm đổi tên từ "7 Fingers" sang "12 Fingers"**, không phải
  nhóm dịch khác chen vào. Xem thêm mục D.

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang tên chương: Frieren (tai nhọn lộ rõ), Fern ló ra sau cửa, Stark quỳ đắp người tuyết trước một căn nhà gỗ giữa bão tuyết. Chữ "Chương 24: Mong muốn của Elf". | — | Tĩnh, mở màn | 1 |
| 2 | P04-a | Hộp dẫn mở chương: "28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời. Các vùng phương Bắc, khu vực Decke." Hai bóng người giữa bão tuyết, một người ngã gục. | "Lạc mất rồi nè." | Lạc lõng | 2 |
| 3 | P04-b | Frieren mỉa mai khi thấy Stark ngã gục giữa bão. | "Còn chưa kịp đến dãy núi Schewer thì lại mắc kẹt ở đây à, hách dịch thật đấy." | Châm biếm nhẹ | 1 |
| 4 | P04-c | Fern hoảng hốt lay gọi Stark giữa tuyết. | "Stark-sama, mau dậy đi nào! Nếu cứ ngủ ở đây thì cậu sẽ toi luôn đấy!" | Hoảng hốt | 2 |
| 5 | P04-d | Frieren giải thích không thể dùng phép nhấc Stark giữa bão vì sẽ bị gió thổi bay; Fern hỏi vậy phải làm sao. | "Làm vậy thì sẽ bị thổi bay đi mất." / "Giờ phải làm sao đây ạ?" | Bí bách | 1 |
| 6 | P04-e | Stark mê man, ảo giác nhớ về ly kem tuổi thơ. | "Trước giờ cái món Jumbo Berry đặc biệt vẫn bé như thế này sao... Sao tôi biết được chứ!" | Hài, mê sảng | 1 |
| 7 | P04-f | Cả nhóm quyết định dắt/lôi Stark đi từng chút một qua bão tuyết. | "Vậy là chỉ còn cách dắt từng chút một thế này thôi." | Gắng gượng | 1 |
| 8 | P05-a | Fern cõng/dìu Stark, hỏi có nên bỏ cậu lại; Stark mê sảng lẩm bẩm khen thơm. | "Em bỏ cậu ta lại được không ạ?" / "Thơm thật đó..." | Hài hước | 1 |
| 9 | P05-b | Frieren đến lượt kéo Stark, than nặng. | "...Nặng quá. Sao cái tên này lại nặng đến vậy chứ." | Than vãn | 1 |
| 10 | P05-c | Fern nghi ngờ trí nhớ đường đi của Frieren đã cũ 80 năm. | "Ngài có chắc như lòng bàn tay không đó?" / "Cái đấy là chuyện của 80 năm về trước rồi, phải không ạ?" | Nghi ngại | 1 |
| 11 | P05-d | Frieren trấn an: tới chân núi sẽ có chỗ lánh nạn, bảo mọi người cố chịu đựng. | "Nếu bước được đến chân núi, thì chắc sẽ có một chỗ cho chúng ta lánh nạn đấy." | Quyết tâm | 1 |
| 12 | P05-e | Nhóm phát hiện một căn nhà gỗ giữa bão, nghe có tiếng động bên trong. | "Em thấy có tiếng gì đó. Có ai đang ở trong đấy thì phải ạ?" | Cảnh giác | 2 |
| 13 | P05-f | Frieren mừng vì nơi trú ẩn cũ (từ 80 năm trước) vẫn còn được dùng. | "Vậy ra chỗ này vẫn còn được giữ gìn thường xuyên à." | Nhẹ nhõm | 1 |
| 14 | P05-g | Frieren quyết định cứ vào trong trước, kẻo bị đóng băng ngoài này. | "Sao cũng được, cứ vào trước đã... chúng ta sẽ bị đóng băng hết đấy." | Cấp bách | 1 |
| 15 | P06-a | Trong nhà: một người đàn ông tai nhọn cởi trần đang tự tập luyện, tự động viên bản thân. | "Tốt lắm, tốt lắm." / "Ấm hẳn lên rồi!!!" | Hài, bất ngờ | 2 |
| 16 | P06-b | Người đàn ông tiếp tục tập luyện hò hét, trong khi ba người lặng lẽ nhìn qua khe cửa. | "HÂY!!" | Hài | 1 |
| 17 | P06-c | Nhóm khiêng Stark bước vào, Frieren lên tiếng xin phép. | "Mạn phép nhé." | Bình thản | 1 |
| 18 | P07-a | Fern (hoặc Stark) thì thầm cảnh báo có "một tên biến thái" trong nhà. | "Bởi có một tên biến thái đang trong đó đấy ạ." | Dè chừng | 1 |
| 19 | P07-b | Fern giục Frieren rời đi tìm chỗ khác. | "Frieren-sama, chỗ này không ổn đâu. Chúng ta đi tìm nơi khác thôi ạ." | Lo lắng | 1 |
| 20 | P07-c | Stark lắp bắp giục đi ngay (gọi nhầm tên Frieren vì hoảng). | "Mình mau đi thôi, Frieren-sâama." | Hoảng | 1 |
| 21 | P07-d | Người đàn ông lạ nghe thấy, lên tiếng phản đối bị gọi là biến thái, rồi hỏi thẳng Frieren có phải elf không. | "Gọi người khác là biến thái là bất lịch sự lắm đấy nhé." / "Cô là elf à?" | Bất ngờ, dò xét | 2 |
| 22 | P08-a | Người đàn ông lạ nói cứ tưởng tộc elf đã tuyệt chủng; Frieren đáp cũng nghĩ vậy. | "Tôi cứ tưởng là loài elf chúng ta đã bị tuyệt chủng rồi cơ." / "Tôi cũng thế." | Ngỡ ngàng | 2 |
| 23 | P08-b | Ông ta cảm ơn vì được gặp lại một pháp sư, và cảm ơn Fern đã nhóm lửa giúp. | "Tôi quả có phước khi lại được gặp pháp sư mà. Cảm ơn cô bé đằng kia đã nhóm lửa giúp nhé." | Biết ơn | 1 |
| 24 | P08-c | Ông ta cho biết đã khoảng 300 năm mới gặp lại một người đồng hương (elf) như thế này. | "Có lẽ đã khoảng 300 năm rồi tôi mới có dịp gặp lại đồng hương thế này đấy." | Xúc động nhẹ | 2 |
| 25 | P08-d | Kể lại: vừa băng qua dãy núi Schewer thì mất than củi giữa bão tuyết, nên phải tập squat để giữ ấm sống sót. | "Tôi vừa băng qua dãy núi Schewer thì lại để mất than củi trong trận bão tuyết này." / "...tôi đành phải tập squat đấy." | Tự trào | 1 |
| 26 | P08-e | Tự giới thiệu tên và nghề nghiệp. | "Tôi là Kraft, một võ sư." | Tự tin | 3 |
| 27 | P08-f | Fern (hoặc người nghe) bối rối chưa hiểu rõ tình huống. | "Em vẫn chưa hiểu rõ cho lắm..." / "Vậy à..." | Bối rối, hài | 1 |
| 28 | P09-a | Fern tự giới thiệu mình và Stark. | "Tôi là Fern, cũng là pháp sư. Còn đây là Stark-sama, một chiến binh." | Lịch sự | 1 |
| 29 | P09-b | Frieren tự giới thiệu. | "Còn tôi là pháp sư Frieren." | Điềm tĩnh | 1 |
| 30 | P09-c | Fern lo lắng về thân nhiệt của Stark đang hạ. | "Frieren-sama. Thân nhiệt của Stark-sama đang..." | Lo lắng | 1 |
| 31 | P09-d | Kraft nghe nhóm nhắc tới đích đến là vùng đất linh hồn Aureole, nhận xét đó là một đức tin mãnh liệt; đáp lại là mình cũng chỉ nửa tin nửa ngờ. | "Vùng đất linh hồn Aureole à... Quả là một đức tin mãnh liệt mà." / "Tôi chỉ nửa tin nửa ngờ mà thôi." | Tò mò, hoài nghi | 2 |
| 32 | P09-e/f | Toàn cảnh căn nhà gỗ giữa núi tuyết; bên trong lò sưởi có quần áo hong khô. | — | Tĩnh lặng | 1 |
| 33 | P10-a | Stark tỉnh dậy trong cảm giác ấm áp dễ chịu, chưa hiểu chuyện gì xảy ra. | "Mình sao vậy nè...? Ấm và thoải mái quá..." | Mơ màng | 1 |
| 34 | P10-b | Stark mở mắt thấy gương mặt Kraft sát bên mình. | (SFX mở mắt) | Bất ngờ | 2 |
| 35 | P10-c | Stark hét lên hoảng loạn. | "CÁI ÔNG NÀO ĐÂY!?" | Hoảng loạn, hài | 2 |
| 36 | P10-d | Kraft phân bua đã cố hết sức sưởi ấm cho Stark (bằng thân nhiệt) mà bị phản ứng như vậy. | "Tôi đã cố gắng sưởi ấm cho cậu hết mức mà vẫn còn tỏ cái thái độ gì thế hả?" | Ấm ức, hài | 1 |
| 37 | P10-e | Stark quay sang khen thân hình cường tráng của Kraft; Frieren và Fern (quấn chăn gần đó) than phiền ồn ào. | "Ông anh có cơ thể cường tráng nhỉ?" / "Ồn quá đó..." | Hài | 1 |
| 38 | P11-a | Stark hỏi tên Kraft, đoán chắc ông phải là võ sư giỏi. | "Tên ông anh là gì thế?" | Ngưỡng mộ | 1 |
| 39 | P11-b | Kraft xưng danh lại: võ sư Kraft; Stark thật thà đáp chưa từng nghe tên qua (hụt hẫng nhẹ, hài). | "Võ sư Kraft ấy mà." / "Chưa từng nghe nói qua." | Hài | 1 |
| 40 | P11-c | Fern gọi lo lắng "Stark-sama?"; Stark thanh minh mình không có ý gì (với việc khen ngợi Kraft). | "Stark-sama?" / "Tôi làm gì có ý đấy đâu." | Bối rối | 1 |
| 41 | P11-d | Kraft phân công: Stark nghỉ ngơi, hai cô gái giúp khiêng lương thực từ xe hàng gần đó. | "Cậu cứ nghỉ ngơi đi đã nhé. Còn hai cô hãy giúp tôi đi xách mấy thùng lương thực nào." | Chủ động | 1 |
| 42 | P12-a | Frieren nhận định chỉ có điên mới băng núi Schewer lúc này, nên cả nhóm sẽ phải ở lại đây một thời gian. | "Chỉ có điên mới băng qua dãy núi Schewer trong lúc này mà thôi... chúng ta sẽ phải ở lại đây ít lâu nữa." | Chấp nhận | 2 |
| 43 | P12-b | Kraft vui mừng vì có đồ ăn đông lạnh để chế biến nhờ số lương thực nhóm giúp khiêng, mời họ lấy tùy thích. | "Cứ lấy bao nhiêu tùy thích đi nhé." | Hào phóng | 1 |
| 44 | P12-c | Kraft nhận xét cũng chẳng biết gì về Frieren, rồi hỏi thẳng liệu Frieren có biết gì về mình không. | "Ngay cả tôi cũng chẳng biết gì về cô nữa là." / "Frieren này, cô có biết gì về tôi không?" | Dò hỏi | 2 |
| 45 | P12-d | Frieren im lặng, rồi hỏi lại ý ông muốn nói gì; ai đó giải thích Frieren là pháp sư của tiểu đội anh hùng, Kraft hỏi tiếp "còn trước đó thì sao". | "....." / "Anh đang muốn ngụ ý điều gì vậy?" / "Ngài ấy là pháp sư của tiểu đội anh hùng đấy." / "Còn trước đó thì sao?" | Dò xét, hơi nặng nề | 3 |
| 46 | P12-e | Kraft kết luận: dù sao "chúng ta là elf mà" — ngụ ý muốn hiểu thêm về cuộc đời dài của một elf khác. | "Chúng ta là elf mà." | Đồng cảm ngầm | 2 |
| 47 | P13-a→h | **Chuỗi montage thời gian trôi qua mùa đông**: cả nhóm ngủ chung trong túp lều, ăn cơm quanh lò sưởi, Fern và Stark chẻ củi, Kraft hướng dẫn Stark tập luyện, Frieren và Fern khiêng đồ giữa tuyết, Kraft và Stark săn thỏ, Frieren hái một bông hoa giữa cánh đồng tuyết, Kraft chỉ cho Stark xem gì đó trong sách/vật. | — | Ấm áp, gắn bó dần | 2 |
| 48 | P14-a | Cảnh rừng cây xanh tươi — thời gian đã chuyển sang mùa xuân/hè, tuyết tan. | — | Chuyển mùa | 1 |
| 49 | P14-b | Kraft cảm ơn cả nhóm vì đã giúp anh sống sót qua mùa đông dài ở phương Bắc, tặng một món đồ nhỏ tự làm. | "Nhờ có các cô cậu, mà chúng ta mới có thể an toàn sống sót qua mùa đông dài đằng đẵng của các vùng phương Bắc thế này đây." | Biết ơn | 2 |
| 50 | P14-c | Frieren nhận ra đã gần nửa năm trôi qua kể từ khi họ mắc kẹt ở đây. | "Đã sắp gần nửa năm rồi nhỉ." | Hoài niệm | 1 |
| 51 | P14-d | Frieren hỏi vì sao Kraft tin vào nữ thần nhiều đến vậy; Kraft ngược lại nhận xét Frieren không tin. | "Tại sao Kraft lại tin vào nữ thần nhiều đến vậy?" / "Nói vậy tức là Frieren không tin rồi ha." | Tò mò | 1 |
| 52 | P14-e | Kraft nhờ Frieren chuyển một món quà (bùa/vật nhỏ) cho Fern, khen cô bé có đức tin mãnh liệt. | "Hãy đưa cái này cho Fern nhé. Cô bé có một đức tin mãnh liệt đấy." | Trân trọng | 1 |
| 53 | P14-f | Kraft đoán Fern chịu ảnh hưởng từ vị tư tế đã nuôi dưỡng cô, không quên bày tỏ lòng biết ơn nữ thần. | "Chắc hẳn là do cô bé đã chịu ảnh hưởng bởi vị tư tế đã nuôi dưỡng mình nhỉ." | Suy ngẫm | 2 |
| 54 | P15-a | Kraft thổ lộ giờ đã tin nữ thần từ tận đáy lòng; nhận xét Frieren "vẫn còn trẻ" khi hoài nghi (ông từng nghĩ như vậy). | "Giờ tôi đã tin vào nữ thần từ tận đáy lòng mình rồi." / "Vậy là cô vẫn còn trẻ nhỉ." | Điềm đạm | 2 |
| 55 | P15-b | Minh hoạ Nữ thần tạo hóa: gần như chưa từng xuất hiện trong lịch sử thế giới ngoài thời đại thần thoại. | "Nữ thần tạo hóa, ngoại trừ thời đại thần thoại, hầu như chưa bao giờ xuất hiện trong lịch sử lâu đời của thế giới này." | Trang nghiêm | 2 |
| 56 | P15-c | Kraft: tất cả những người từng biết chiến công và hành động công lý của ông đều đã mất; nếu nữ thần không tồn tại thì ông sẽ "gặp rắc rối" (không ai còn nhớ/ghi nhận ông). | "Tất cả những người biết về chiến công lẫn hành động về công lý của tôi đều đã mất cả rồi." / "Nếu ngài ấy không tồn tại, thì tôi sẽ gặp rắc rối mất thôi." | Cô đơn, trầm | 3 |
| 57 | P15-d | Frieren nghĩ thầm đã ở đây lâu rồi; hồi tưởng minh hoạ nữ thần khen ngợi Kraft đã sống một cuộc đời tuyệt đẹp; Kraft ước khi chết sẽ được nữ thần ca ngợi trên thiên đường. | "Con đã rất nỗ lực rồi, Kraft à. Cuộc sống của con thật là tuyệt đẹp." / "Tôi muốn khi mình chết đi thì sẽ được nữ thần ca ngợi ở trên thiên đường đấy." | Khao khát được công nhận | 3 |
| 58 | P15-e | Kraft: sẽ đau khổ biết bao nếu sống, cống hiến cho đời mà chẳng ai hay biết; nói thẳng với Frieren rằng ông biết cô cũng hiểu cảm giác đó. | "Chẳng phải là sẽ thật đau khổ nếu như sống trên đời, cống hiến cho đời mà chẳng hề có ai hay biết hay sao." / "Tôi cũng biết chứ. Frieren à." | Thấu hiểu, nặng lòng | 3 |
| 59 | P16-a | Kraft nối thẳng: chẳng phải thiên đường (Aureole mà Frieren tìm) cũng là cùng một mong muốn đó sao. | "Chẳng phải thiên đường cũng vậy cả sao? Frieren." | Thấu hiểu sâu sắc | 3 |
| 60 | P16-b | Frieren gọi đó là "mong muốn của loài elf"; Kraft đồng tình. | "Đó chỉ là mong muốn của loài elf mà thôi." / "Quả thực là thế nhỉ." | Đồng cảm | 2 |
| 61 | P16-c | Kraft đề nghị Frieren kể về bản thân, vì ông đã kể về mình rồi; Frieren miễn cưỡng đồng ý. | "Kể cho tôi nghe về bản thân cô đi. Tôi cũng đã nói rồi mà." / "Mà sao cũng được." | Ngần ngại | 1 |
| 62 | P16-d | Cận mặt Frieren trầm ngâm trước khi kể chuyện. | — | Trầm ngâm | 1 |
| 63 | P16-e | Kraft: nếu Frieren không tin nữ thần, thì thay mặt ngài ấy, chính ông sẽ tự ngợi ca cô. | "Nếu như cô không tin vào nữ thần, vậy thì thay mặt ngài ấy, tôi sẽ tự mình ngợi ca cô." | Ấm áp, chân thành | 3 |
| 64 | P17-a | **Hồi tưởng do Frieren kể lại**: cô bất ngờ khi biết Heiter đã trả tiền tu sửa viện phí cho trại trẻ mồ côi trong làng. | "Tôi không ngờ là Heiter lại trả viện phí tu sửa cho trại trẻ mồ côi ở trong ngôi làng này đấy." | Bất ngờ | 1 |
| 65 | P17-b | Heiter giải thích: vì ông cũng từng là trẻ mồ côi. | "Bởi tôi cũng đã từng là trẻ mồ côi ấy mà." | Trầm lắng | 2 |
| 66 | P17-c | Cảnh quán rượu: Frieren trêu Heiter sao lại thành thật vậy. | "Ha ha ha. Sao mà lại thành thật thế này." | Trêu đùa | 1 |
| 67 | P17-d | Heiter hỏi Frieren có bất ngờ lắm không, rồi gọi tên cô. | "Cậu ngạc nhiên lắm à?" / "Frieren này." | Nghiêm túc dần | 1 |
| 68 | P17-e | Heiter hỏi thẳng: liệu Frieren có ai đó để ngợi ca mình không. | "Cậu có ai đó để ngợi ca mình không?" | Nghiêm túc, gốc rễ câu hỏi | 3 |
| 69 | P17-f | Frieren ngạc nhiên hỏi vì sao ông hỏi vậy; Heiter đáp chắc chắn nữ thần sẽ ngợi ca ông vì đã sống trong sạch, đúng mực. | "Sao bỗng dưng cậu lại hỏi thế?" / "Chắc chắn nữ thần sẽ ngợi ca tôi vì đã sống trong sạch và đúng mực đấy." | Tự trào | 2 |
| 70 | P17-g | Frieren giễu Heiter đang say mà lại nói câu đó, gọi lại biệt danh cũ. | "Cậu vừa thốt ra câu gì trong lúc đang say đấy hả, đồ tư tế thúi này." | Trêu chọc, thân mật | 1 |
| 71 | P18-a | Frieren tự nhận mình chỉ sống bơ phờ suốt quãng đời qua, chẳng có gì đáng ngợi ca. | "Tôi chỉ sống bơ phờ trong suốt quãng đời qua mà thôi. Chẳng có gì đáng để mà ngợi ca cả đâu." | Tự ti nhẹ | 2 |
| 72 | P18-b | Heiter đề nghị: nếu Frieren kể cho ông nghe về bản thân, ông sẽ thay mặt nữ thần ngợi ca cô — **câu gốc mà Kraft lặp lại gần như nguyên văn ở hiện tại (P16-e)**. | "Nếu cậu nói cho tôi biết về bản thân mình, thì tôi sẽ thay mặt ngài ấy ngợi ca cậu cho." | Ấm áp, then chốt | 3 |
| 73 | P18-c | Heiter nhắc họ đã cùng nhau trải qua rất nhiều năm tháng rồi. | "Chúng ta đã cùng nhau trải qua rất nhiều năm tháng rồi còn gì?" | Gắn bó | 1 |
| 74 | P18-d | Frieren nhận xét Heiter đã dành cả đời vì niềm tin đó. | "Có vẻ như cậu đã dành cả đời mình vì nó nhỉ." | Suy ngẫm | 1 |
| 75 | P18-e | Heiter hỏi ngược về việc Frieren duy trì nền tảng ma lực của mình — thành quả của nỗ lực chăm chỉ. | "Cả chuyện cậu duy trì nền ma lực của mình sao? Đó chính là thành quả cho những nỗ lực chăm chỉ của cậu đấy thôi." | Công nhận | 2 |
| 76 | P18-f | Heiter nói không bận tâm việc bị hỏi, vì dù sao cũng là tài liệu hữu ích tham khảo cho tương lai. | "Tôi không bận tâm đâu. Dù gì thì đó cũng sẽ là tài liệu hữu ích để tham khảo cho tương lai mà." | Cởi mở | 1 |
| 77 | P18-g/h | Frieren hỏi lại ý ông là gì, rồi gạt đi bảo chuyện mình chẳng có gì thú vị. | "Là sao?" / "Cơ mà cũng chẳng phải là chuyện gì thú vị đâu." | Né tránh nhẹ | 1 |
| 78 | P19-a | Frieren hỏi Heiter liệu tư tế có luôn phải độc thân hay không (nhìn ông chơi đùa với trẻ mồ côi). | "Chẳng phải tư tế sẽ luôn luôn độc thân hay sao?" | Tò mò | 1 |
| 79 | P19-b | Heiter đáp: những đứa trẻ của ông rồi sẽ trở thành pháp sư. | "Những đứa trẻ của tôi có lẽ là sẽ trở thành pháp sư đấy." | Kỳ vọng | 2 |
| 80 | P19-c/d | Heiter cười xòa, nói mình sẽ không cô đơn vì đã có một chàng trai từng tán dương ông. | "Ha ha ha." / "Tôi sẽ không làm vậy đâu. Bởi lẽ đã có một chàng trai tán dương tôi rồi." | Ấm áp | 2 |
| 81 | P19-e | Frieren trêu: sao lại có lắm kẻ "quái dị" sùng bái nữ thần đến thế. | "Sao lại có lắm kẻ quái dị phục tùng nữ thần thế nhỉ." | Trêu đùa | 1 |
| 82 | P19-f/g | Heiter ngập ngừng rồi tiết lộ: người đó giờ đã ở trên thiên đường rồi (đã mất). **Danh tính "chàng trai" không được nêu tên trực tiếp trong khung này — xem mục D.** | "À không, cậu ta đã... đang ở trên thiên đường rồi." | Chùng xuống, tiếc thương | 3 |
| 83 | P19-h | Frieren lặng người không đáp. | "......" | Lặng người | 2 |
| 84 | P19-i | Cắt về hiện tại: Kraft đáp lại câu chuyện, khen Frieren có nhiều bạn tốt, dặn hãy trân trọng họ. | "Cô có nhiều bạn tốt thật đấy, Frieren à. Hãy trân trọng họ nhé." | Ấm áp | 2 |
| 85 | P20-a/b | Frieren đồng tình; Kraft nói vậy thì biết đâu ông sẽ có ngày gặp được "cậu ấy" (người đã mất, trên thiên đường). | "Đúng vậy nhỉ." / "Thế thì tôi có thể gặp cậu ấy vào một ngày nào đó rồi." | Hy vọng nhẹ | 2 |
| 86 | P20-c | Toàn cảnh dãy núi — đánh dấu đoạn đường phía trước, thời điểm chia tay đã tới. | — | Mênh mang | 1 |
| 87 | P20-d | Kraft từ biệt: tin rằng đây không phải lời chia tay cuối cùng, hẹn gặp lại dù bao thế kỷ trôi qua. | "Rồi chúng ta sẽ còn gặp lại, dù cho có bao nhiêu thế kỷ trôi qua đi nữa." / "Tôi không hề nghĩ rằng đây sẽ là lời chia tay cuối cùng đâu." | Xúc động, hy vọng | 3 |
| 88 | P20-e/f | Kraft chỉ về một hướng khác, tách đường với nhóm; ảnh khép lại với hai nhóm đi hai hướng giữa vùng núi. | "Tôi sẽ đi về phía này." | Chia tay, lắng đọng | 3 |

### C. Điểm cao trào

Chương này không có twist hành động — cao trào là **cảm xúc, dồn dần qua nhiều đỉnh nhỏ** đúng
tinh thần "cú lật là thời gian" của bộ:

1. **P08-e** — Kraft tự giới thiệu tên, lộ diện là **elf thứ hai xuất hiện trực diện trong toàn bộ
   series** (trước đó elf khác chỉ được nhắc lời, chưa ai lên hình). Đỉnh về mặt lore.
2. **P15-c → P15-e** — Kraft thổ lộ động cơ tin vào nữ thần: sợ bị lãng quên, sợ cống hiến cả đời
   mà không ai hay biết. Đây là đỉnh cảm xúc trung tâm, đặt nền cho chủ đề "mong muốn của elf".
3. **P16-a → P16-e** — Kraft nối thẳng "thiên đường" (Aureole mà Frieren tìm) với chính nỗi sợ bị
   lãng quên đó, rồi hứa sẽ tự mình ngợi ca Frieren nếu cô không tin nữ thần. Đỉnh thứ hai, bản lề
   dẫn vào hồi tưởng.
4. **P18-b** — Trong hồi tưởng, Heiter nói gần như **nguyên văn cùng một lời hứa** ("tôi sẽ thay
   mặt ngài ấy ngợi ca cậu") mà Kraft vừa nói ở hiện tại. Đây là **cú lật kiểu "thời gian"** đặc
   trưng của bộ: một câu nói cũ dội lại nguyên vẹn ở một khung cảnh mới, hé lộ rằng nỗi cô đơn của
   Frieren đã luôn được những người quanh cô âm thầm để ý.
5. **P19-f/g** — Heiter tiết lộ "chàng trai từng tán dương tôi" nay đã ở trên thiên đường (đã mất) —
   một mất mát ngầm, danh tính bỏ ngỏ (xem mục D), gợi cảm giác tiếc nuối.
6. **P20-d → P20-f** — Chia tay Kraft sau gần nửa năm cùng sống sót qua mùa đông; lời hẹn "gặp lại dù
   bao thế kỷ trôi qua" chốt chủ đề: hai kẻ sống đời dài đằng đẵng học cách tin rằng mình sẽ được nhớ đến.

### D. Chưa rõ

- **Kraft** — elf, võ sư ("Tôi là Kraft, một võ sư" — P08-e), thân hình vạm vỡ, thường cởi trần tập
  luyện để giữ ấm. Tin vào nữ thần "từ tận đáy lòng". Vừa băng qua **dãy núi Schewer** thì mất than
  củi giữa bão. Nói đã khoảng **300 năm** kể từ lần cuối gặp một elf khác (P08-c) — **đây là mốc
  của riêng Kraft, KHÔNG PHẢI cùng một sự kiện với mốc "~400 năm" Frieren tự kể ở C13** — hai người
  hai trải nghiệm khác nhau, đừng gộp làm một. **CHƯA RÕ**: họ, tuổi, quê quán, vì sao một mình ở
  vùng phương Bắc, quan hệ (nếu có) với các nhân vật khác trong bộ.
- **Địa danh mới**: **"khu vực Decke"** (P04-a, hộp dẫn mở chương — vùng phương Bắc, nơi nhóm bị
  mắc kẹt) và **"dãy núi Schewer"** (nhắc nhiều lần P04, P08, P12 — dãy núi chắn đường lên phương
  bắc mà "chỉ có điên mới băng qua" giữa bão). Cả hai **chưa có trong series-bible.md**, cần thêm
  vào mục 2b (địa danh) khi cập nhật bible.
- **"Nữ thần tạo hóa"** (P15-b) — mở rộng thêm cho mục "nữ thần" đã có trong bible: theo lời Kraft,
  bà **hầu như chưa từng xuất hiện trong lịch sử thế giới ngoại trừ thời đại thần thoại**. Đây là
  lời của Kraft, một tín đồ — **CHƯA RÕ** đây có phải là thông tin khách quan của thế giới truyện
  hay chỉ là niềm tin cá nhân của riêng ông.
- **Danh tính "chàng trai tán dương" Heiter** (P19-f/g, "đã ở trên thiên đường rồi") — **ảnh KHÔNG
  nêu tên trực tiếp**. Rất có khả năng ám chỉ **Himmel** (đã mất, từng đồng đội thân thiết với
  Heiter) nhưng đây là suy luận, **KHÔNG được khẳng định trong lời kể** nếu chưa có bằng chứng chữ
  in nào khác xác nhận. Cần soi lại nếu chương sau nhắc lại.
- **Món quà Kraft tặng Fern** (qua tay Frieren, P14-e) — hình dạng vật thể chỉ thấy trong bản vẽ
  đen trắng nhỏ, không đủ rõ để mô tả chi tiết (có thể là một loại bùa/mặt dây chuyền tương tự cái
  Kraft đeo) — **KHÔNG ĐỌC ĐƯỢC rõ chi tiết**, cần soi ảnh gốc kỹ hơn nếu muốn tả trong lời kể.
- **Tên nhóm dịch trên banner ghi "12 Fingers Team"**, khác chữ **"7 Fingers Team"** bible đang
  chốt ở dòng mở đầu — nhưng **thành viên (Credemoe, Yahari) trùng khớp hoàn toàn**, và slogan
  "Khi 7 ngón là chưa đủ" (P01) xác nhận đây là **cùng một nhóm đổi tên**, không phải nhóm dịch
  mới. Đề xuất cập nhật dòng mở đầu bible thành "7 Fingers Team (C1–C2) → đổi tên thành 12 Fingers
  Team (từ C24 trở đi, xác nhận cùng nhóm qua P01/P02)" khi rảnh cập nhật bible.
- **Bối cảnh trước C24**: bible hiện mới cập nhật tới hết C15 (arc phụ phe quỷ); **C16–C23 chưa có
  beat-sheet, cũng chưa được đọc** trong phiên này. C24 dường như quay lại tuyến chính (Frieren,
  Fern, Stark) sau khoảng "28 năm" — **CHƯA RÕ** điều gì xảy ra ở C16–C23 nối giữa C15 và C24, chỉ
  biết dòng thời gian "28 năm kể từ khi Himmel mất" vẫn được giữ nguyên, không có gì mâu thuẫn với
  các mốc đã biết.
