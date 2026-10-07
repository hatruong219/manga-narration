# BEAT SHEET — FRN Chapter 22

## A. Kiểm tra đầu vào

**File nhận được (25 ảnh, `pages-clean/`):** FRN_C22_P01, P02, P04–P26 (không có P03).

**Đánh số trang gốc (góc dưới ảnh):** ảnh `P0N` mang số trang in = N−2. Xác nhận qua nhiều mẫu
(P04→"2", P05→"3", P06→"4", P17→"15", P19→"17", P20→"18", P21→"19", P22→"20", P23→"21", P24→"22").
→ Nội dung chương đánh số trang in **1–22**; trang in **22 nằm ở file P24** (trang cuối có nội
dung, không tính 2 trang thông báo/quảng cáo sau đó).

**⚠️ CẢNH BÁO — THIẾU TRANG:** File **P03 không tồn tại** cả ở `pages/` lẫn `pages-clean/` (đã
kiểm tra thư mục gốc, không phải lỗi của `clean-pages.py` cắt nhầm — trang này chưa từng được
crawl). Theo số trang in suy ra, đây là **trang in số 1 — nhiều khả năng là trang bìa màu/trang mở
đầu của chương** (P04 = trang in "2" mở thẳng vào giữa một cảnh đối thoại đã có ngữ cảnh, không bị
đứt lời thoại — nên khả năng cao trang mất là ảnh bìa/tên chương, không phải một khung thoại đang
dang dở). Không phát hiện thêm trang nào khác bị thiếu trong dải in 2–22.

**⚠️ ĐÃ THỬ VÁ, KHÔNG THÀNH CÔNG — MẤT VĨNH VIỄN.** Đã kiểm tra cả 2 nguồn:
- Nguồn chính truyenqq.com.vn: chương 22 đã bị **gỡ hẳn khỏi danh sách** (cùng với chương 6, 7,
  13, 14, 20, 21, 23, 24, 25, 43, 44, 45 — site đã xoá cả cụm chương này khỏi mục lục series).
- Nguồn backup nettruyen13s.com: chương vẫn còn, nhưng đúng file ảnh trang này (`0002.webp`) bị
  **hỏng/rỗng trên CDN của họ** (HTTP 200, Content-Length 0) — đã thử lại nhiều lần, thử các
  server proxy thay thế của chính site, và Wayback Machine — không nơi nào có bản lưu.
- **Kết luận: KHÔNG dùng lại thời gian tìm trang này nữa** — chấp nhận chương 22 thiếu đúng 1
  trang mở đầu (nhiều khả năng là bìa/tên chương, không phải khung thoại dang dở). Khi viết lời
  kể, bắt đầu thẳng từ P04 (trang in "2"), không cần dựng lại/suy đoán nội dung P03.

**Trang BỎ (không phải nội dung chương):**
- **P01** — ảnh collage quảng cáo các bộ truyện khác của nhóm dịch (không liên quan FRN).
- **P02** — bìa tập truyện + bảng credit nhóm dịch (7 Fingers Team: Credemoe, Yahari) — khớp
  **đúng tên nhóm dịch đã chốt trong bible** (mục Series Bible dòng đầu: "7 Fingers Team").
- **P25** — ảnh "THÔNG BÁO" của 7 Fingers Team (không liên quan nội dung truyện).
- **P26** — ảnh quảng cáo nhóm dịch khác "12 Fingers Team" (không liên quan FRN, không phải nhóm
  dịch của bộ này).

→ **Nhóm dịch khớp bible**: đúng "7 Fingers Team", Credemoe/Yahari — không có gì lệch.

**Xác minh chiều đọc (phải → trái):** Trang P20 (số in "18") có 2 khung ở hàng đầu: khung **phải**
(to, cảnh toàn quân) — Aura tuyên bố *"Phần thắng thuộc về ta rồi... Đích thân ta sẽ chặt đầu ngươi
bằng thanh kiếm này đây."*; khung **trái** (nhỏ) — Aura độc thoại *"Ta đã quá đa nghi mất rồi..."*.
Đọc phải→trái cho mạch hợp lý: tuyên bố hành động trước, tự nhận xét/hạ cảnh giác ngay sau — khớp
diễn biến bị lật kèo ở khung dưới cùng trang. Đã đọc toàn bộ 21 trang nội dung (P04→P24) theo đúng
thứ tự phải→trái, trên→dưới; không có trang nào bị nhảy cóc trong dải đã nhận.

**Ghi chú riêng cho chương này:** đây là chương **hoàn toàn hồi tưởng quá khứ** (không có khung nào
thuộc "hiện tại" của mạch Frieren–Fern–Stark) — mở bằng một trận chiến, lùi sâu hơn vào quá khứ để
giải thích, rồi quay lại kết thúc đúng trận đó ở cuối chương (kết cấu phi tuyến tính).

---

## B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P04-a | Một quỷ tộc sừng dài, tóc hồng/tím, tay cầm gậy trượng đầu cân, hỏi thẳng một pháp sư elf tóc trắng (búi đuôi ngựa, tai nhọn) có nên phí ma lực trước mặt mình không. | *"Việc tiêu hao lượng lớn ma lực trước mặt ta thế là một ý hay không vậy?"* | Khiêu khích, tự tin | 2 |
| 2 | P04-b | Khung chú thích giải thích cơ chế phép: đặt linh hồn cả hai lên cân, ai ma lực nhỉnh hơn thì thao túng được người kia. | *"Kẻ nào có lượng ma lực nhỉnh hơn thì sẽ thao túng được tên còn lại."* | Giải thích, đe doạ | 2 |
| 3 | P04-c | "Cán cân vàng lệnh" — quỷ tộc đứng trước cả một đội quân giáp trụ; pháp sư elf đứng một mình từ xa giữa sa mạc. | *"Cán cân vàng lệnh."* | Áp đảo, cô độc | 2 |
| 4 | P04-d | Pháp sư elf tự nhủ ma lực tỉ lệ với công khổ luyện; đối lập với suy đoán quỷ tộc ỷ vào ma lực khổng lồ dùng phép "dao hai lưỡi". | *"Dẫu sao thì ma lực cũng tỉ lệ thuận với công sức khổ luyện."* | Bình tĩnh, tính toán | 2 |
| 5 | P05-a→c | Quỷ tộc tự nhận đã sống hơn 500 năm — với loài quỷ là quãng đời dài, giờ tự thấy mình vô đối; ma lực toả ra là bằng chứng, quỷ vốn không thể giấu ma lực. | *"…giờ ả ta cũng được coi là vô đối rồi nhỉ."* | Tự mãn | 2 |
| 6 | P05-d | Quỷ tộc (tóc bện hai bên, sừng cong) hô tên phép **"Azeryuuze — PHÉP THUẬT THAO TÚNG"**; một elf khác đứng cạnh buông một câu tiếc nuối. | *"Azeryuuze. PHÉP THUẬT THAO TÚNG."* / *"Tiếc thật đấy."* | Bắt đầu giao tranh | 2 |
| 7 | P06-a→c | (Lùi xa hơn quá khứ) Một phụ nữ tóc dài bện một bên tóc (dáng giống Flamme đã biết từ C7) dẫn một bé gái elf tai nhọn đi qua thị trấn người, giảng giải: quyền lực loài người đến từ địa vị/của cải — có thể giả vờ; quyền lực loài quỷ đến từ ma lực — nhìn phát biết ngay, vì "chúng là quái vật nên không thay đổi gì". | *"Chỉ cần nhìn là em sẽ biết ngay thôi."* / *"Là bởi ma lực phải không ạ?"* | Dạy dỗ, tò mò | 2 |
| 8 | P07-a→c | Bà tiếp tục: quỷ không thể giấu ma lực **liên tục** vì đánh đổi vị thế — khác biệt giữa "quý tộc ẩn danh tạm giấu ma lực" và "quỷ mất danh tính vì tiêu xài địa vị"; quỷ luôn phô trương ma lực để tỏ ra hùng mạnh. | *"Việc nén ma lực liên tục không hề có nghĩa lý gì với chúng cả."* | Phân tích, nghiêm túc | 2 |
| 9 | P08-a→c | Bà nói: *"May sao mà em lại không phải là quỷ, Frieren nhỉ?"* — **lần đầu tên "Frieren" xuất hiện, xác nhận bé gái elf chính là Frieren thời thơ ấu**, đang học dưới một người được gọi "sư phụ". Frieren đáp: nhờ không phải quỷ nên em mới lừa dối được chúng. | *"May sao mà em lại không phải là quỷ, Frieren nhỉ?"* / *"Nhờ vậy mà em mới có thể lừa dối bọn chúng."* | Thân tình, sắc sảo | 3 |
| 10 | P08-d | Người phụ nữ hỏi lại: đã 3 năm kể từ lúc Frieren bắt đầu giới hạn ma lực; mừng vì niềm tin đặt đúng chỗ. | *"Đã được 3 năm kể từ lúc giới hạn ma lực rồi ha…?"* | Hài lòng | 2 |
| 11 | P09-a→d | Trong rừng, Frieren (đã lớn hơn chút) hỏi sư phụ sao bỗng dưng hỏi vậy; sư phụ hỏi thẳng: *"Frieren này, em vẫn còn yêu quý phép thuật chứ?"* — nhắc lại đã khoảng nửa thế kỷ trôi qua kể từ ngày Frieren từng bày tỏ niềm trân quý với phép thuật. | *"Frieren này, em vẫn còn yêu quý phép thuật chứ?"* | Trầm ngâm, quan tâm | 3 |
| 12 | P09-e→f | Sư phụ hỏi Frieren có hối hận không; Frieren đáp không hề. Sư phụ tự nhận xét: *"Rốt cuộc thì ta chỉ toàn dạy cho em nào là chiến với đấu thôi nhỉ."* | *"Người có hối hận không ạ?"* / *"Không hề."* | Áy náy nhẹ | 2 |
| 13 | P12-a | Sư phụ xin Frieren một thỉnh cầu; nói với tuổi thọ dài của Frieren, có khi cô đủ sức tiêu diệt cả Quỷ Vương — thấy may mắn vì đã giao phó lại phép thuật cho Frieren. | *"Với một tuổi đời dài đằng đẵng đến vậy, thì có khi em lại đủ khả năng để tiêu diệt cả Quỷ Vương không chừng."* | Tin tưởng, tiên tri | 3 |
| 14 | P12-b | Thỉnh cầu cụ thể: hãy tạo luống hoa quanh mộ của sư phụ — loại phép tạo ra luống hoa đẹp, **phép thuật bà yêu thích nhất**. | *"Hãy tạo ra luống hoa xung quanh mộ của ta nhé. Phép thuật mà ta yêu thích nhất."* | Dịu dàng, trăn trối | 3 |
| 15 | P13-a | Frieren đáp "Vậy hãy dạy cho em đi"; sư phụ kể phép hoa này cha mẹ bà dạy hồi nhỏ — khởi nguồn tình yêu phép thuật của bà. Dặn thêm: sống từ tốn, nhã nhặn trước đã; đừng nghĩ tới việc ghi danh sử sách — **chỉ khi nào tiêu diệt được Quỷ Vương thì hẵng làm vậy.** | *"Chỉ khi nào tiêu diệt được Quỷ Vương thì khi ấy hẵng làm vậy."* | Trăn trối, kỳ vọng | 3 |
| 16 | P13-b→e | Cảnh mộ phủ đầy hoa qua nhiều mùa (tuyết, hoa nở); Frieren một mình hái nấm, nấu ăn bên vách đá, đứng cạnh xác một quái thú khổng lồ đã ngã — thời gian trôi, Frieren sống đơn độc sau khi sư phụ mất. | (không thoại) | Cô tịch, thời gian trôi | 2 |
| 17 | P13-f | Frieren đứng nhìn về phía một toà lâu đài trên núi xa dưới đêm tối — hướng đi tiếp theo của cô. | (không thoại) | Quyết tâm lặng lẽ | 2 |
| 18 | P14-a→c | Ba người đàn ông (một đeo kính/áo tư tế, một đội mũ sừng của người lùn, một trẻ hơn) tiếp cận khu rừng nơi Frieren sống; nghe đồn có một pháp sư sống ở đây rất lâu rồi. | *"Nghe nói có một pháp sư đã sinh sống trong khu rừng này từ rất lâu rồi… và người đó là cô nhỉ?"* | Tò mò, dò hỏi | 2 |
| 19 | P14-d | Frieren tự nhận mình chỉ toàn vui chơi, chẳng có tài cán gì; một người hỏi ý kiến người đeo kính (tư tế) tên **Heiter** — "Cậu thấy sao, Heiter?" | *"Tôi sống quanh năm suốt tháng ở đây chỉ toàn vui chơi là chính ấy mà. Chẳng có tài cán nào đâu."* | Khiêm tốn/giấu mình | 2 |
| 20 | P17-a→b | Heiter nhận định: ma lực của Frieren chỉ bằng một nửa của ông, có thể coi là "pháp sư tầm trung" — Frieren xen vào phản đối bị chê "mất lòng". Người thứ ba (có vẻ là Eisen) bác lại: cô vượt xa mọi pháp sư ông từng gặp. | *"Ma lực của cô ấy chỉ bằng một nửa của tôi thôi… Có thể nói là một pháp sư tầm trung."* | Tranh luận, hài hước nhẹ | 2 |
| 21 | P17-c | Người còn lại (nhiều khả năng là Himmel — dựa theo tính cách hay dùng "linh cảm" đã biết từ C1, **nhưng trang này không in tên**) trả lời Frieren khi cô hỏi vì sao lại tin cô mạnh: *"Là linh cảm ấy mà."* | *"Là linh cảm ấy mà."* | Tự tin bộc trực | 2 |
| 22 | P17-d→f | Montage cảnh chiến trận xưa của Frieren: đối đầu một quái thú lớn, một ngai vàng có bóng đội sọ, một con rồng — gợi lại "truyền thuyết" về pháp sư elf bí ẩn. | (không thoại rõ) | Hào hùng, xa xưa | 2 |
| 23 | P18-a→b | Chú thích giới thiệu: một pháp sư Elf không rõ tuổi thọ, hành tung bí ẩn — Frieren, kẻ bỗng dưng xuất hiện từ 80 năm trước và cùng tổ đội Anh Hùng tiêu diệt Quỷ Vương. Cùng lúc, khung chiến đấu: Frieren tung phép lửa trắng, quỷ tộc tung phép lửa đen đối đầu. | *"Một pháp sư Elf không rõ tuổi thọ, hành tung bí ẩn."* | Căng thẳng, đối đầu | 3 |
| 24 | P19-a→b | Aura nhận xét: một pháp sư hùng mạnh mà lại thấp kém về ma lực đến vậy — "hoàn toàn rành mạch ngay trước mắt". Dù đã có gần một thế kỷ luyện tập, ma lực Frieren nhìn vẫn y hệt 80 năm trước — cây gậy cân bắt đầu đo lượng ma lực của Frieren. | *"Là một pháp sư hùng mạnh mà lại thấp kém về khoản ma lực đến vậy à."* | Coi thường, phân tích sai lầm | 2 |
| 25 | P19-c→e | Aura giễu: có phải Frieren chỉ chăm rèn kỹ năng mà quên nâng cao ma lực, hay do sống trác táng quên mất sự tình; tuyên bố Frieren không có cửa thắng. | *"Ngươi không có của để thắng ta đâu."* | Ngạo mạn | 2 |
| 26 | P20-a | Aura một mình phản tỉnh: đâu cần làm suy kiệt ma lực Frieren, mình đã quá đa nghi. | *"Ta đã quá đa nghi mất rồi."* | Chủ quan, buông lỏng cảnh giác | 2 |
| 27 | P20-b | Aura tuyên bố chiến thắng trước cả đội quân, định đích thân chặt đầu Frieren bằng kiếm — một hiệp sĩ (chưa rõ danh tính) đã quỳ gục trước mặt. | *"Phần thắng thuộc về ta rồi. Đích thân ta sẽ chặt đầu ngươi bằng thanh kiếm này đây."* | Áp đảo, sắp ra đòn kết liễu | 3 |
| 28 | P20-c | Cảnh toàn quân: Aura nhắc thầm phải củng cố lại binh sĩ vì đã triệt hạ quá nhiều xác sống của phe kia. | (song thoại nội tâm) | Tự mãn tiếp diễn | 1 |
| 29 | P20-d→e | **CÚ LẬT:** cây cân bất ngờ nghiêng về phía Frieren. Aura sững sờ: *"…Gì thế này?"* | *"Cán cân đang nghiêng về phía của Frieren ư…"* | Sốc, hoang mang | 3 |
| 30 | P21-a→b | Frieren giải thích: nàng đã **nén ma lực của chính mình** — "Ngươi đã tính toán sai lệch mất rồi, Aura à." | *"Ta đã nén ma lực của mình đấy."* / *"Người đã tính toán sai lệch mất rồi, Aura à."* | Bình thản, lật kèo | 3 |
| 31 | P21-c→d | Aura không tin nổi: không thể có chuyện đó, và nếu có thật thì sao mình lại không hề để ý? Frieren đáp: quỷ chỉ có thể cảm nhận CHÍNH XÁC lượng ma lực kiểu này thôi — kỹ thuật của sư phụ đã đúng. | *"Có vẻ như kỹ thuật của sư phụ đã đúng rồi nhỉ."* | Tự tin, biết ơn thầy | 3 |
| 32 | P22-a→b | Frieren: nàng đã dành phần lớn cuộc đời chỉ để giới hạn ma lực — đến mức mức ma lực bị giới hạn ấy đã trở thành "ma lực thông thường" của chính nàng. Aura mắng đó là "trò ngổ ngẩn". | *"Ta đã dành ra phần lớn đời mình chỉ để giới hạn ma lực của mình đấy."* | Điềm tĩnh, tiết lộ chiến thuật cả đời | 3 |
| 33 | P22-c→d | Frieren: nhưng nhờ vậy mà nàng có thể tiêu diệt được Aura. Aura gằn giọng gọi tên nàng. | *"Nhưng nhờ vậy mà ta có thể tiêu diệt được ngươi."* | Quyết đoán | 3 |
| 34 | P22-e→f | Frieren tự giới thiệu: kẻ đứng trước mặt ngươi là pháp sư đã sống ít nhất một thiên niên kỷ; Aura khẳng định lại mình là đại quỷ đã sống 500 năm — đừng có mà cợt nhả. | *"Là pháp sư đã sống ít nhất một thiên niên kỷ."* / *"Ta là đại quỷ đã sống 500 năm đấy nhé."* | Đối đầu ngang ngửa | 2 |
| 35 | P23-a→b | Cột lửa trắng khổng lồ bùng lên nơi Frieren đứng. Nàng đúc kết châm ngôn: loài quỷ lừa dối con người bằng ngôn từ — còn nàng lừa dối chúng bằng ma lực. | *"Loài quỷ lừa dối con người bằng ngôn từ, còn em thì hãy lừa dối chúng bằng ma lực nhé."* | Quyết liệt, đỉnh điểm sức mạnh | 3 |
| 36 | P24-a→b | **ĐỈNH CAO LẬT KÈO:** Frieren ra lệnh dùng chính phép thao túng đã bị lật ngược — *"Tự sát đi, Aura."* Aura gồng mình cưỡng lại trong vô vọng: *"Ta mà lại… …Không thể nào…"* | *"Tự sát đi, Aura."* | Bàng hoàng, tuyệt vọng (Aura) — lạnh lùng (Frieren) | 3 |
| 37 | P24-c→d | Cảnh chiến trường tan hoang, xác giáp trụ la liệt; Frieren một mình bước đi giữa đống đổ nát. | (không thoại) | Trống rỗng, dư âm chiến thắng đắng | 2 |

---

## C. Điểm cao trào

1. **#9 (P08):** Lần đầu tên **"Frieren"** xuất hiện trong chương — xác nhận bé gái elf đang học phép
   chính là Frieren thời thơ ấu, dưới trướng một người được gọi "sư phụ" (thiết kế tóc dài bện một
   bên khớp mô tả **Flamme** đã chốt ở bible mục 1 — tên riêng "Flamme" KHÔNG được in trên trang nào
   của C22, giữ đúng quy tắc bible "chỉ gọi tên ở chỗ có in tên").
2. **#14–15 (P12–P13):** **Cảnh trăn trối của sư phụ** — thỉnh cầu trồng hoa quanh mộ (phép thuật bà
   yêu thích nhất, học từ cha mẹ bà thời thơ ấu), dặn Frieren sống khiêm nhường, và **tiên đoán
   Frieren có thể là người tiêu diệt được Quỷ Vương**. Chương không vẽ cảnh chết trực tiếp — cắt
   thẳng sang cảnh ngôi mộ phủ hoa — nên đây là **suy luận có căn cứ mạnh, không phải cảnh tử vong
   được vẽ rõ**.
3. **#18–20 (P14–P17):** **Cảnh Himmel/Heiter/Eisen tìm gặp và tuyển mộ Frieren lần đầu tiên** — chưa
   từng được vẽ trực tiếp ở các chương trước (C1–C21 chỉ nhắc gián tiếp). Heiter được gọi tên rõ
   ràng; hai người còn lại không được xướng tên trên trang (xem mục D).
4. **#23, #29–36 (P18, P20–P24):** **Trận đánh Frieren vs. Aura — lần đầu tiên "Aura" xuất hiện trực
   diện, có tên, có thoại, có thiết kế nhân vật rõ ràng** trong toàn bộ các chương đã đọc (C14 mới chỉ
   nhắc tên). Cao trào kép: (a) cú lật cây cân nghiêng bất ngờ khi Frieren tiết lộ đã nén ma lực suốt
   đời để đánh lừa phép đo của Aura; (b) cú lật cuối — Frieren dùng chính phép thao túng của Aura để
   ra lệnh **"Tự sát đi, Aura"**, kết thúc chương giữa cảnh chiến trường tan hoang.

---

## D. Chưa rõ

- **Danh tính hai người đàn ông còn lại đi cùng Heiter ở cảnh tuyển mộ (P14–P17):** một người đội mũ
  có sừng lớn (dáng người lùn, gợi ý mạnh là **Eisen** theo mô tả bible "tộc người lùn") và một người
  trẻ hơn nói câu "Là linh cảm ấy mà" (gợi ý mạnh là **Himmel** — tính cách hay quyết theo trực giác,
  và Heiter hỏi trực tiếp "Cậu thấy sao, Heiter?" nghĩa là người hỏi không phải Heiter). **Cả hai đều
  KHÔNG có tên in trên trang trong C22** — đây là suy luận từ đặc điểm ngoại hình/tính cách đã biết
  từ C1, **không phải chữ trên trang của chương này**. Cần giữ nguyên tắc bible: đừng gọi thẳng tên
  hai người này khi viết lời kể cho đến khi có xác nhận bằng chữ in.
- **Người sư phụ dạy Frieren phép hoa và tiên đoán Quỷ Vương (P08–P13):** tên **"Flamme" KHÔNG được
  in** ở bất kỳ khung nào trong C22. Thiết kế (tóc dài bện một bên) khớp mô tả Flamme đã chốt ở bible,
  nhưng theo đúng quy tắc bible ("tên bà KHÔNG in trên hai chỗ đó, đừng chú thích tên vào ảnh" — áp
  dụng tương tự ở đây), **chưa nên khẳng định chắc 100% bằng chữ của chương này** dù suy luận là hợp
  lý cao. Cảnh này **cũng không vẽ trực tiếp cái chết của bà** — chỉ có thỉnh cầu cuối cùng rồi cắt
  sang mộ phủ hoa.
- **Hiệp sĩ quỳ gục trước Aura ở P20:** không rõ danh tính, phe nào (đồng minh Frieren hay lính riêng
  của Aura bị trừng phạt) — trang không cho biết.
- **Mốc thời gian trận Aura so với việc hạ Quỷ Vương:** khung chú thích P18 viết Frieren *"cùng với
  tổ đội Anh Hùng tiêu diệt Quỷ Vương"* ở thì đã hoàn thành, nhưng đây có thể là lối dẫn chuyện kiểu
  hồ sơ/tóm lược tổng quan (viết sau khi mọi chuyện đã xong) chứ không nhất thiết nghĩa là trận Aura
  xảy ra SAU khi hạ Quỷ Vương. **Đừng suy diễn thứ tự thời gian chính xác** giữa trận Aura và mốc hạ
  Quỷ Vương — trang không xác nhận rõ.
- **"Máy chém Aura" (biệt danh đã chốt ở bible từ C14) KHÔNG được nhắc lại bằng chữ trong C22** — chỉ
  thấy tên trơn "Aura" + hành động "đích thân chặt đầu ngươi bằng thanh kiếm này" (gợi liên hệ tới
  biệt danh nhưng không phải xác nhận lặp lại).
- **C22 không tự nhắc lại cụm "bảy ma thuật sư huỷ diệt"** cho Aura — nguồn xác nhận duy nhất của
  liên kết đó vẫn là C14-P09b như bible đã ghi, C22 không phải nguồn xác nhận thứ hai.
- **Trang bìa/tên chương (trang in số 1, file P03) bị thiếu hoàn toàn** — xem cảnh báo ở mục A.
  Không loại trừ khả năng trang đó có thông tin (VD: tên chương gốc tiếng Nhật, hoặc một khung mở đầu
  khác) chưa được đọc.
- **Quái thú khổng lồ Frieren ngồi lên ở P13 (montage sau khi sư phụ mất):** không có thoại, không rõ
  là loài gì, chết hay bị khuất phục — chỉ là một khung hình ảnh im lặng.
