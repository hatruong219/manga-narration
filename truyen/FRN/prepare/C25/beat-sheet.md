# BEAT SHEET — FRN Chương 25 "Làng kiếm"

Nguồn ảnh: `truyen/FRN/prepare/C25/pages-clean/` (22 file, nettruyen13s 1000px).
Đã đọc HẾT 22 file theo đúng thứ tự P01→P22, mở từng ảnh xem tận mắt trước khi xếp loại.

---

## A. Kiểm tra đầu vào

**Nhận đủ 22 file, không mất trang liên tiếp:** `FRN_C25_P01.jpg` → `FRN_C25_P22.jpg`.

**Đã mở từng file bằng mắt (không suy theo khuôn C6/C7/C13-15) để phân loại:**

| File | Kích thước (pages-clean) | Nội dung thấy được | Kết luận |
|---|---|---|---|
| P01 | 1000×600 | Ảnh "12 Fingers Team" tay nắm tay, dòng chữ "Cảm ơn vì đã đi cùng chúng tôi..." | **BỎ** — banner nhóm dịch |
| P02 | 1000×800 | Trái: bìa in Vol.2 gốc tiếng Nhật. Phải: bảng credit "TRANSLATOR: Credemoe · EDITOR: Yahari! · PROOFREADER: Credemoe · QUALITY CHECKER: Credemoe", link Facebook/Web, logo "12 FINGERS TEAM — Khi 7 ngón là chưa đủ" | **BỎ** — trang credit |
| P03–P20 | 1000×1435 (riêng P09 1000×1424, P20 1000×1525) | Nội dung truyện liên tục, có số trang in ở góc (2,3,5,6,…18) khớp quy luật "số in = số file − 2" | **GIỮ** — 18 trang nội dung |
| P21 | 1000×600 | "Tuyển thành viên" — tin tuyển CTV dịch của "12 Fingers Team", nhân vật minh hoạ rời + chibi | **BỎ** — quảng cáo nội bộ nhóm dịch |
| P22 | 1000×522 | Ảnh kỷ niệm "12 FINGERS TEAM" phong cách bảng đen, chữ ký "Khai trương", không liên quan cốt truyện | **BỎ** — banner/ảnh kỷ niệm nhóm dịch |

→ **Còn 18 trang nội dung: P03–P20**, đúng khuôn của các chương nguồn nettruyen13s trước
(C13/C14/C15: bỏ đầu 2 + cuối 2 trang).

**Cắt bởi `clean-pages.py`:** chỉ P09 bị cắt — từ 1435px (bản `pages/`) xuống còn 1424px trong
`pages-clean/` (**cắt 11px**, không ảnh hưởng nội dung khung, không mất chữ).

**Tên nhóm dịch — SO VỚI BIBLE:** Bible ghi nhóm dịch của C1/C2 là **"7 Fingers Team"** (TRANSLATOR
Credemoe · EDITOR Yahari · PROOFREADER/QC Credemoe). Trang credit P02 của C25 vẫn giữ **đúng ba cái
tên nhân sự này** (Credemoe/Yahari), nhưng tên nhóm đã đổi thành **"12 Fingers Team"**, với khẩu
hiệu "Khi 7 ngón là chưa đủ" — rõ ràng là **cùng một nhóm đổi thương hiệu từ 7 lên 12 Fingers**,
không phải một nhóm khác. Không lệch nhân sự, chỉ lệch tên thương hiệu — cần cập nhật bible.

**Xác minh chiều đọc phải→trái:** trang P16 (số in "14"), hàng khung trên: khung PHẢI vẽ một bóng
vuốt khổng lồ đổ xuống, Frieren đứng cạnh Stark đang nằm gục hỏi "Cậu vẫn còn cử động được đúng
chứ?"; khung TRÁI vẽ đòn chém hạ gục con sói (hiệu ứng chém, máu bắn). Theo mạch truyện, việc phát
hiện quái vật đe doạ + Stark đã ngã (khung phải) phải diễn ra TRƯỚC đòn kết liễu (khung trái) — chỉ
hợp lý khi đọc khung phải trước, khung trái sau. **Kết luận: bản scan giữ nguyên bố cục gốc, đọc
phải→trái đúng chuẩn manga Nhật**, không bị lật để chuyển thành đọc trái→phải.

---

## B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang tên chương (splash toàn trang): xe ngựa đi trong rừng mưa, chở ba bóng người chưa rõ mặt (một người đeo kính, một người trùm mũ hé miệng ngạc nhiên, một cô bé tai nhọn tóc dài buộc hai bên). Tiêu đề "Chương 25: Làng kiếm". | — | Bí ẩn, gợi mở | 2 |
| 2 | P04-a/b | (Hồi tưởng) Đoàn 4 người xưa đi về phía một toà lâu đài xa; cắt sang cảnh họ quỳ trước ngai nhà vua. | — | Hoài niệm | 1 |
| 3 | P04-c/d/e | Đoàn bốn người (người cầm kiếm, hai người còn lại, một người đội mũ sừng) bàn về phần thưởng ít ỏi từ vua. | *"Rốt cuộc nhà vua vẫn chỉ đưa cho chúng ta có 10 đồng thôi à?"* / *"Bởi đã có rất nhiều anh hùng ra đi mà không thể đánh bại được Quỷ Vương ấy mà. Đừng có càu nhàu thế chứ."* | Trào phúng nhẹ | 1 |
| 4 | P04-f | Hai người (một cầm kiếm, một đeo kính) đi trong mưa, một câu ngắn khép cảnh. | *"…Quả là vậy nhỉ."* | Trầm, chuyển cảnh | 1 |
| 5 | P05-a | Người đeo kính hỏi người cầm kiếm về thanh "Kiếm Anh Hùng"; được đáp đó chỉ là bản sao. | *"Nè, thanh kiếm đó là 'Kiếm Anh Hùng' nhỉ?"* / *"Đây chỉ là bản sao mà thôi."* | Tò mò | 2 |
| 6 | P05-b/c | (Hồi tưởng lồng hồi tưởng) Một cậu bé nhận thanh kiếm bản sao vì đã cứu một người bán hàng rong khỏi quái vật; người tặng dặn "dành cho người hùng tương lai". | *"Chú ấy nói 'dành cho người hùng tương lai'. Như là giao phó cho những đứa trẻ vậy."* | Ấm áp, ngây thơ | 2 |
| 7 | P05-d/e/f | Chú thích: cậu bé đi cùng là "một cậu trai phiền phước tên là Heiter" ở bản làng dành cho trẻ mồ côi cạnh đó; người nghe hỏi đùa đó có phải động lực làm anh hùng không — được đáp "À không đâu." | *"Đấy lại là một cậu trai phiền phước tên là 'Heiter' ở bên bản làng dành cho trẻ mồ côi cơ."* | Nhẹ nhàng, lấp lửng | 2 |
| 8 | P06-a/b | Người kể tự nhủ vì bị chê là "chỉ có thanh kiếm giả nên chỉ là anh hùng giả", đã quyết tâm một ngày cầm được Kiếm Anh Hùng THẬT để hạ Quỷ Vương. | *"Cậu ấy nói với tôi rằng 'Cậu chỉ có mỗi thanh kiếm giả, nên chỉ là một anh hùng giả mà thôi'."* / *"Rồi sẽ có một ngày tôi cầm được 'Kiếm Anh Hùng' thật ở trên tay mình và hạ gục Quỷ Vương."* | Quyết tâm | 3 |
| 9 | P06-c/d | Chốt hồi tưởng: cậu trai phiền phước tên Heiter năm nào giờ đã thành "một tư tế giả, chỉ biết rượu với chè"; người nghe khẳng định lại. | *"Nhưng đáng buồn thay là dòng chảy thời gian lại quá đỗi tàn nhẫn."* / *"Tôi là hàng thật đấy nhé."* | Chua xót pha hài | 3 |
| 10 | P07-a/b | Hiện tại: Fern báo Frieren đã tỉnh; Frieren còn ngái ngủ tự hỏi có phải đang mơ. | *"Frieren-sama, cuối cùng thì ngài cũng dậy rồi."* / *"…Là mơ sao?"* | Mơ màng | 1 |
| 11 | P07-c | Hộp dẫn mốc + địa danh: **Các vùng phương Bắc, dãy núi Schewer** · **29 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời.** | — | Trang trọng | 2 |
| 12 | P07-d/e | Đoàn đi trong bão tuyết; Stark báo đã đánh giá thấp thời tiết, phải tiếp tục đi về phía bắc tới một ngôi làng. Fern cõng Frieren trên lưng; Frieren nghĩ cảnh này quen thuộc, ngỡ vẫn đang mơ. | *"Ta đã đánh giá quá thấp thời tiết trên dãy núi này mất rồi."* / *"…Sao cảnh này trông quen thế nhỉ. Chắc là mình vẫn còn đang mơ rồi… Nếu đúng là vậy thì thật tốt quá…"* | Mệt mỏi, hoài niệm nhẹ | 2 |
| 13 | P08-a/b/c | Đoạn hài: Fern hỏi Frieren có tự đi được không; Frieren gọi ai đó "biến thái"; Stark trêu đề nghị cõng hộ. | *"Biến thái."* / *"Hay để tôi cõng hộ tiếp nhé."* | Hài hước | 1 |
| 14 | P08-d/e | Bão tuyết ngớt; nhóm thấy nhẹ nhõm. | *"Ta cứ ngỡ là mình sẽ bị chết cóng cơ…"* / *"Có vẻ bão tuyết đã ngừng rồi nhỉ?"* | Nhẹ nhõm | 1 |
| 15 | P09-a/b | Trên đường vào làng, thấy một căn lều thợ săn bị phá huỷ; được biết đó là do "Chúa Sơn Lâm" gây ra — Frieren ngạc nhiên vì chưa từng nghe tới thứ này. | *"Có một căn lều bị phá huỷ ở bên ngoài ngôi làng này đúng không?"* / *"Do Chúa Sơn Lâm gây ra đấy ạ."* / *"'Chúa Sơn Lâm' sao? Trước đây từng có một thứ như thế không vậy?"* | Cảnh giác | 2 |
| 16 | P09-c/d/e | Nhóm dân làng ra đón; một người tự giới thiệu "đời thứ 49", bị nhận xét là còn trẻ để làm trưởng làng ("cha truyền con nối", "trẻ thật đấy"). Cô bé trưởng làng chào Frieren, nói đã đợi ngài suốt. | *"Dạ vâng, tôi là đời thứ 49 ạ."* / *"Chúng tôi đã đợi ngài suốt đấy, Frieren-sama à."* | Trang trọng, hồi hộp | 2 |
| 17 | P10-a | Toàn cảnh làng: "Chào mừng các vị ghé qua Làng Kiếm." | — | Ấm áp | 1 |
| 18 | P10-b/c/d | Stark hỏi cô bé trưởng làng biết gì về làng; được xác nhận đây là **Làng Kiếm**, nơi trông coi **Kiếm Anh Hùng** — thanh kiếm huyền thoại do nữ thần ban tặng, hiện cất tại một thánh địa gần đó. | *"Đó là một thanh kiếm danh bất hư truyền được ban tặng bởi nữ thần và hiện đang được cất giữ tại thánh địa gần đây đấy."* / *"Thì bởi đây là ngôi làng trông coi 'Kiếm Anh Hùng' mà."* | Tự hào | 2 |
| 19 | P11-a/b | Lịch sử: rất nhiều anh hùng từng thử rút kiếm mà không xê dịch nổi, mãi tới **80 năm trước** mới có người rút được. | *"Mãi đến tận từ 80 năm trước mới có một người rút được đấy."* | Kính nể | 2 |
| 20 | P11-c/d | Xác nhận: người rút được chính là **Himmel**. Cô bé trưởng làng nói chưa từng nghe Heiter kể chuyện này. | *"Và người rút được là Himmel-sama à."* / *"Đúng vậy."* / *"Không. Heiter-sama chưa bao giờ kể về nó cả."* | Ngạc nhiên nhẹ | 3 |
| 21 | P11-e/f | Nhóm được dẫn vào một căn nhà trong làng. | *"Lối này ạ."* | Chuyển cảnh | 1 |
| 22 | P12-a/b | Trong nhà, cô bé trách khéo Frieren: đã hứa quay lại sau nửa thế kỷ mà giờ mới tới, khiến người "dễ tính" như cô cũng phải bực. | *"Ngài đã hứa là sẽ quay trở lại đây sau nửa thế kỷ nữa, ấy thế mà…"* | Trách móc nhẹ, hài | 2 |
| 23 | P12-c/d | Bàn về "nghĩa vụ": Frieren nói đã bảo là an toàn sau 80 năm; cô bé nhắc đời con cháu vệ binh vẫn phải hoàn thành nghĩa vụ, và dạo gần đây Chúa Sơn Lâm nổi tính hung bạo nên hơi hỗn loạn. | *"Ta đã nói là sẽ an toàn sau 80 năm cơ mà."* / *"Đặc biệt là dạo gần đây Chúa Sơn Lâm rất hay nổi tính hung bạo, nên thành ra có hơi hỗn loạn chút."* | Lo lắng | 2 |
| 24 | P12-e/f | "Nghĩa vụ" được làm rõ là **tiêu diệt quái vật**; nhóm quyết định bắt đầu ngay hôm đó thay vì đợi. | *"Là 'tiêu diệt quái vật' đấy. Chúng thường hay lảng vảng ở quanh đây lắm."* / *"Xong càng sớm thì càng tốt mà."* | Quyết đoán | 1 |
| 25 | P13-a/b | Frieren bay trên bầu trời tuyết bằng gậy phép; Stark cận chiến một con sói/quái vật bằng rìu lớn. | — | Căng thẳng | 2 |
| 26 | P13-c | Frieren bắn một luồng phép công kích quét ngang. | — | Áp đảo | 2 |
| 27 | P13-d/e | Cô bé trưởng làng và một cụ già đồng hành bàn về việc Himmel là anh hùng nên khó nhờ ai khác; nhận xét gần làng vẫn có nhiều quái vật; có ý kiến nên thuê mạo hiểm giả khác dọn dẹp — bị bỏ lửng. | *"Nhưng bởi Himmel là anh hùng đấy."* / *"Dù đang ở gần làng thế này mà vẫn có nhiều quái vật quá đấy."* / *"Nếu thế này thì sao cô không nhờ những mạo hiểm giả khác ra tay dẹp đi?"* | Băn khoăn | 1 |
| 28 | P14-a/b | Stark một mình phát hiện bầy sói tụ trước cửa hang, nhận xét khu này quá nhiều quái vật. | *"Chúng đang tụ thành bầy ở trước cửa hang kìa."* | Cảnh giác | 2 |
| 29 | P14-c/d/e | Stark tiến vào hang, sững người gọi Frieren khi thấy thứ gì đó bên trong. | *"Frieren. Đây là…"* | Bất ngờ | 2 |
| 30 | P14-f | Một con quái thú lớn lông trắng, nhiều mắt gầm gừ hiện ra, tư thế chồm tới. | (âm thanh gầm) | Đe doạ, cao trào bắt đầu | 3 |
| 31 | P15-a/b | Xác nhận đây chính là **Chúa Sơn Lâm** — cận cảnh đầu quái thú khổng lồ. | *"Đó là Chúa Sơn Lâm đấy."* | Choáng ngợp | 3 |
| 32 | P15-c/d | Frieren hỏi thẳng con quái vật đã làm Chúa Sơn Lâm suốt 80 năm từ khi nào; nó đáp không hề biết gì về chuyện đó. | *"Và thế là mày trở thành Chúa Sơn Lâm trong suốt 80 năm sao? Mày mới tới đây à?"* / *"Ra thế. Ta không hề biết đến luôn đấy."* | Lạ lùng, gần như triết lý | 2 |
| 33 | P15-e/f | Stark đã ngã gục trên tuyết; Frieren gọi tên cậu, bay tới. | *"Stark."* | Lo lắng | 2 |
| 34 | P16-a/b | (Đọc phải→trái) Bóng vuốt khổng lồ đổ xuống, Frieren hỏi Stark còn cử động được không; sau đó đòn chém của Frieren hạ gục quái thú. | *"Cậu vẫn còn cử động được đúng chứ?"* | Căng thẳng đỉnh điểm | 3 |
| 35 | P16-c/d | Đòn phép tiếp tục giáng xuống; Stark (đã tỉnh, chỉ trầy xước) buông một câu bực dọc về con quái vật. | *"Cái con quái thô lỗ này…"* | Nhẹ nhõm pha bực | 1 |
| 36 | P17-a/b | Frieren khen ngợi (không rõ khen Stark hay tự nhận xét đòn đánh); đòn phép quét hạ gục quái thú hoàn toàn. | *"Làm tốt lắm."* | Thắng lợi | 2 |
| 37 | P17-c/d | Trong hang sau khi giết quái vật, Stark phát hiện: **Kiếm Anh Hùng vẫn còn cắm ở đây** — một phiến đá khác với thanh kiếm cắm sẵn. Nhóm hỏi nghĩa vụ đã xong; cô bé trưởng làng sững sờ hỏi Frieren chuyện này là sao. | *"Kiếm Anh Hùng vẫn còn ở đây mà."* / *"Frieren. Thế này là sao hả?"* | Bối rối, cú lật bắt đầu | 3 |
| 38 | P18-a/b | Giải thích: chính vì thanh kiếm thật này mà quái vật liên tục kéo tới đây phá — dù có kết giới bảo vệ, chúng vẫn không cưỡng được thôi thúc huỷ diệt kiếm vì nó là nỗi khiếp đảm với chúng. | *"Chính vì nó nên lũ quái vật mới thường xuyên bén mảng đến đây đấy."* / *"Thanh kiếm ấy là nỗi khiếp đảm đối với chúng mà."* | Nặng nề | 2 |
| 39 | P18-c/d | **Cú lật trung tâm chương:** cô bé trưởng làng nói thẳng — Himmel KHÔNG hề rút nổi thanh kiếm thật này. Stark định thanh minh; Frieren xác nhận. | *"Himmel không thể rút nổi thanh kiếm ấy."* / *"…Đúng vậy."* | Sững sờ | 3 |
| 40 | P18-e | Ông già đeo kính đi cùng nhóm làng kết luận: người thử lần này (ngụ ý Stark) cũng không phải anh hùng đích thực. | *"Vậy là người lần này cũng không phải là anh hùng đích thực rồi."* | Chua chát | 2 |
| 41 | P19-a/b | (Hồi tưởng khép lại mạch mở đầu chương) Himmel — người từng bị chê "chỉ có kiếm giả" — cười nói: thật hay giả không quan trọng, cậu vẫn sẽ đánh bại Quỷ Vương và giành lại hoà bình. | *"Vậy thì là thật hay giả thì cũng đâu có quan trọng gì chứ. Tôi vẫn sẽ đánh bại Quỷ Vương và giành lại hoà bình cho thế giới này mà thôi."* / *"Làm anh hùng giả thì cũng có sao đâu nào."* | Đỉnh cảm xúc, khẳng khái | 3 |
| 42 | P19-c/d | Fern hỏi vì sao sự thật ấy lại bị giấu kín; Frieren đoán là do những người muốn Himmel là anh hùng đã cố tình giấu. | *"Vậy sao sự thật đó lại bị giấu kín ạ?"* / *"Có lẽ đó là do những người muốn Himmel là anh hùng đã cố tình làm vậy đấy."* | Trầm ngâm | 2 |
| 43 | P19-e/f | Frieren chốt: và rồi Himmel đã thành công — dù không có thanh kiếm đó trong tay, anh vẫn cứu được thế giới; cậu ấy đích thực là một người hùng. | *"Và rồi Himmel đã thành công. Dù không có thanh kiếm đó trong tay, thì Himmel vẫn giải cứu được thế giới này."* / *"Cậu ấy đích thực là một người hùng mà."* | Đỉnh cảm xúc, ấm áp | 3 |
| 44 | P20-a/b | Cô bé trưởng làng suy ngẫm: hình tượng "anh hùng" sẽ được hậu thế tôn vinh mà không cần xin phép, có khi cả câu chuyện gốc cũng bị che khuất; và những giai thoại khó nghe kiểu "anh hùng không rút nổi kiếm" sẽ gây tiếng xấu. | *"Hình tượng 'anh hùng' sẽ được các hậu thế tôn vinh hết lòng mà không cần phải xin phép."* / *"Những giai thoại khó nghe như 'anh hùng không thể rút nổi Kiếm Anh Hùng' sẽ gây tiếng xấu đúng chứ?"* | Suy tư | 2 |
| 45 | P20-c | Nhóm rời làng, đứng trước cổng cùng dân làng tiễn. | — | Chuyển cảnh | 1 |
| 46 | P20-d/e | Frieren hẹn quay lại sau nửa thế kỷ nữa; cô bé xin ngài lần sau đừng đến muộn, cảm tạ và tin Frieren sẽ làm tròn trách nhiệm. | *"Vậy ta sẽ quay lại sau nửa thế kỷ nữa nhé."* / *"Xin ngài lần sau đừng đến muộn nữa ạ."* / *"Tôi luôn tin rằng Frieren-sama sẽ làm tròn trách nhiệm ấy."* | Ấm áp, lưu luyến | 2 |
| 47 | P20-f | Chốt chương bằng đùa cợt: Frieren hỏi "di ngôn của bà cô bị cái khỉ gì thế?"; cô bé đáp đó cũng là di ngôn của bà mình. | *"Di ngôn của bà cô bị cái khỉ gì thế?"* / *"…Và đó cũng là di ngôn của bà tôi đấy."* | Hài, nhẹ nhàng khép lại | 1 |

---

## C. Điểm cao trào

Chương có **nhiều đỉnh xen kẽ hành động và cảm xúc**, không chỉ một cú lật:

1. **Đỉnh hành động:** trận đánh Chúa Sơn Lâm (#25–36, P13–P17) — Stark bị quật ngã, Frieren ra tay
   kết liễu bằng phép công kích lớn.
2. **Cú lật trung tâm của cả chương (#37–40, P17–P18):** phát hiện thanh **Kiếm Anh Hùng THẬT** vẫn
   còn cắm trong đá bên trong hang quái vật, và tuyên bố thẳng thừng **"Himmel không thể rút nổi
   thanh kiếm ấy"** — lật ngược huyền thoại làng vừa kể ở #19–20 rằng chính Himmel là người 80 năm
   trước đã rút được kiếm.
3. **Đỉnh cảm xúc/chủ đề (#41, #43, P19):** lời Himmel (hồi tưởng) *"Thật hay giả thì cũng đâu có
   quan trọng gì chứ. Tôi vẫn sẽ đánh bại Quỷ Vương…"* và lời chốt của Frieren *"Cậu ấy đích thực là
   một người hùng mà."* — đối trọng trực tiếp với cú lật #39, khẳng định giá trị anh hùng không nằm ở
   bảo vật.
4. **Mở đầu gieo mầm (#8, P06):** cậu bé (Himmel) quyết tâm trở thành anh hùng thật sau khi bị chê
   "chỉ có kiếm giả" — đây là hạt giống được trả lời lại đúng bằng đỉnh #41.
5. **Cú đệm hài hước khép chương (#47, P20):** cách chương hạ nhiệt căng thẳng bằng một câu đùa vô
   thưởng vô phạt, đúng phong cách các chương trước.

---

## D. Chưa rõ

- **Danh tính người kể chuyện tuổi trẻ ở P04–P06** (người cầm kiếm, sau này khẳng định "Tôi là hàng
  thật đấy nhé"): dựa theo tạo hình (không đeo kính, cầm kiếm) và theo nội dung khớp với Himmel đã
  được xác nhận ở P19–20, **nhiều khả năng là Himmel thời trẻ**, nhưng **cả đoạn P04–P06 không có
  chữ tên nào in trực tiếp** — gán tạm, cần soi lại khi viết lời kể.
- **Người đồng hành đeo kính trong hồi tưởng đó** (gọi là "Heiter" theo chú thích trong ảnh) —
  **KHÔNG rõ đây có phải chính là Heiter trong đoàn Himmel (tư tế, mất ở C2) hay không.** Chi tiết
  "chỉ biết rượu với chè" khớp mô tả Heiter trong bible (C1-P32: nghiện rượu), nên khả năng cao là
  cùng một người, nhưng ảnh không in tên đầy đủ ở đoạn này — **cần xác nhận thêm trước khi viết lời
  kể khẳng định chắc**.
- **Trang splash tên chương P03**: ba bóng người trên xe ngựa không rõ mặt/rõ tên — không chắc là
  đoàn hiện tại (Frieren/Fern/Stark) hay hình ảnh ẩn dụ cho đoàn Himmel thời trẻ trong hồi tưởng.
  Đừng chú thích tên vào ảnh này.
- **Cô bé "trưởng làng đời thứ 49"**: không có tên riêng nào in trên trang. Tai hơi nhọn trong một số
  khung nhưng KHÔNG đủ rõ để khẳng định là elf hay không — đừng gán chủng tộc.
- **Ông già đeo kính đi cùng cô bé trưởng làng** (xuất hiện P12, P16, P18): không có tên, không rõ
  vai trò cụ thể (cố vấn? người giám hộ? vệ binh khác?) — gọi bằng cụm mô tả, không đặt tên.
- **Ai là người vừa thử rút kiếm "lần này"** khiến ông già kết luận "không phải anh hùng đích thực"
  (P18-e): suy đoán hợp lý nhất là **Stark** (vì cậu là người đầu tiên vào hang và có mặt cạnh thanh
  kiếm), nhưng **ảnh không vẽ cảnh thử rút kiếm trực tiếp** — đừng khẳng định thay ảnh.
- **Lời hứa "nửa thế kỷ" của Frieren với làng** (P12, P20): chưa rõ được lập từ lần ghé thăm nào —
  không đủ dữ kiện để gắn vào bảng mốc thời gian hiện có của bible.
- **"Di ngôn của bà" ở câu đùa chốt chương** (P20): không rõ nội dung di ngôn là gì, "bà" của cô bé
  trưởng làng là ai — chỉ là mảng đùa ngoài lề, không có thêm dữ kiện.
- **Mốc thời gian chương này: "29 năm kể từ khi Himmel qua đời"** (P07) — đây là con số MỚI, tiếp
  ngay sau "28 năm" đã chốt cho C6–C14 trong bible. Cần thêm dòng mới vào bảng 4a khi cập nhật bible.
- **Địa danh mới: "dãy núi Schewer"** (Các vùng phương Bắc) — chưa có trong bible, cần bổ sung mục 2b.
- **Thuật ngữ mới cần thêm bible (mục 2c):** "Làng Kiếm" (tên làng/tên chương) · "Kiếm Anh Hùng"
  (thanh kiếm ban tặng bởi nữ thần, khác với "Kiếm anh hùng" bản sao mà Himmel từng nhận hồi nhỏ —
  **hai vật khác nhau, đừng gộp**) · "Chúa Sơn Lâm" (danh xưng/chức vị của quái thú trấn giữ khu vực,
  bản thân con quái vật hiện tại "không hề biết" mình mang danh này) · "nghĩa vụ" của dòng dõi vệ
  binh làng (tiêu diệt quái vật định kỳ, đã kéo dài 49 đời).
- **Tên nhóm dịch:** bible đang ghi "7 Fingers Team" cho C1/C2; C25 credit cùng êkíp
  (Credemoe/Yahari) nhưng dưới tên **"12 Fingers Team"** — cần cập nhật/ghi chú sự đổi tên này vào
  bible, không tự coi là nhóm khác.

---

## Câu hỏi duyệt

1. Panel có thật không — đúng những gì thấy trong ảnh, không suy diễn thêm?
2. Tên nhân vật đã đúng chưa — đặc biệt đoạn gán tạm "Himmel"/"Heiter" cho hồi tưởng P04–P06?
3. Trọng số đã hợp lý chưa — đặc biệt các mục cao trào ở C?
