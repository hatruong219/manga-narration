# BEAT SHEET — FRN Chapter 14 "Quái vật biết nói"

## A. Kiểm tra đầu vào

- Nhận đủ **28 file** `FRN_C14_P01.jpg` → `FRN_C14_P28.jpg`, đã mở và đọc hết, không nhảy cóc.
- Nguồn: **nettruyen13s, khổ 1000px** (giống khuôn C6/C7 trong bible, khác 10 chương truyenqq 900px).
- Không có tool `identify`/PIL trong môi trường này nên **không đo được clean-pages.py đã cắt bao nhiêu px** —
  chỉ so được kích thước file gốc trong `pages-clean/` bằng `file`. Tất cả trang nội dung đều rộng đúng
  1000px, không thấy dấu hiệu bị cắt lệch khung khi xem bằng mắt (không sót banner ngang, không mất chữ ở mép).
- **Khuôn trang của chương này** (kiểm bằng mắt từng trang, không suy theo khuôn cũ):
  - `P01` (1000×632) — banner quảng cáo 7 Fingers Team (các bộ truyện khác nhóm dịch). **BỎ**.
  - `P02` (1000×800) — trang credit "Sousou no Frieren", TRANSLATOR Credemoe · EDITOR Yahari! ·
    PROOFREADER Credemoe · QUALITY CHECKER Credemoe, tên nhóm **7 Fingers Team** — **khớp bible**
    (bible trước đó chỉ xác nhận 7 Fingers Team cho C1/C2, nay xác nhận thêm C14 cùng nhóm).
    Khung tiếng Nhật "2話 僧侶の嘘" (tên chương 2) bị dùng lại làm khuôn — **đúng như bible đã ghi chú**,
    không phải dấu hiệu tải nhầm chương. **BỎ** (không phải nội dung truyện).
  - `P03` (1000×1435) — **trang tên chương, GIỮ**: "Chương 14: Quái vật biết nói", có hình một lính gác
    giáp trụ khổng lồ và Frieren áp sát, phía xa hai bóng dáng đồng hành.
  - `P04`–`P20` (1000×1424–1573) — **nội dung truyện, 17 trang, GIỮ hết**.
  - `P21` (1000×1572) — bìa tiếng Nhật *Sousou no Frieren FRIEREN VOL.1* (ảnh xám, không thoại). **BỎ**.
  - `P22` (1000×785) — minh hoạ màu quảng bá (nhóm nhân vật đi giữa đám đông, phong cách anime) — không
    khớp bối cảnh chương 14, không có thoại. **BỎ**.
  - `P23` (1000×1572) — minh hoạ màu bonus: Frieren ngồi một mình dưới gốc cây cùng bản đồ, không thoại,
    không nối vào mạch truyện chương này. **BỎ**.
  - `P24` (1000×1572) — minh hoạ đen trắng bonus: Frieren và Fern ngủ dưới gốc cây cạnh chồng sách, không
    thoại. **BỎ**.
  - `P25` (1000×1572) — minh hoạ màu bonus: hai nhân vật (một tóc bện vàng, một là Frieren) đứng ở cửa một
    công trình đá giữa rừng, không thoại, không rõ liên hệ chương 14. **BỎ**.
  - `P26` (1000×785) — bìa quảng bá *FRIEREN VOL.2* dạng collage nhiều khung nhỏ + dòng "Vol.2" tiếng Nhật.
    **BỎ**.
  - `P27` (1000×625) — "THÔNG BÁO" của 7 Fingers Team (không nhận thêm nhân sự / không liên quan web dịch
    truyện / không nhận donate), ký tên trưởng nhóm Credemoe. **BỎ**.
  - `P28` (1000×522) — banner "12 FINGERS TEAM" (ghi rõ mốc "4/5/2020"), giống khuôn banner cuối C1/C2 bible
    đã ghi. **BỎ**.
  - → **Chương này có 10 trang rác/bonus (P01,P02,P21–P28), nhiều hơn hẳn 2 trang thường thấy ở C6/C7** —
    do nguồn kèm theo 6 trang minh hoạ quảng bá (artbook/bìa tập) chèn sau truyện, không phải lỗi tải chương.
  - **Còn 18 trang nội dung: P03–P20.**

- **Xác minh chiều đọc PHẢI → TRÁI bằng chứng cứ trong chính chương này** (không suy từ kiến thức ngoài):
  Ở `P17` (theo cách đánh số beat sheet dưới đây, tức file `FRN_C14_P17.jpg`), hàng panel cuối trang có
  hai khung: khung bên **phải** là câu hỏi của Himmel "LẠI 'MẸ ƠI' NỮA À?", khung bên **trái** là lời giải
  thích dài của Frieren về việc loài quỷ sống cô độc, không có khái niệm "gia đình". Về mặt logic hội thoại,
  câu hỏi phải đến trước câu trả lời — tức khung **phải đọc trước khung trái**. Đây là bằng chứng chiều đọc
  phải→trái chuẩn truyện tranh Nhật, áp dụng cho toàn chương. **Lưu ý:** vì Read tool không cho toạ độ pixel
  chính xác từng khung, thứ tự panel `-a, -b, -c…` dưới đây được suy theo logic mạch truyện đã đọc hiểu,
  không phải đo toạ độ tuyệt đối — cần người duyệt kiểm lại nếu nghi ngờ một khung cụ thể.

---

## B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang tên chương: một lính gác giáp trụ khổng lồ đứng ở cổng thị trấn, Frieren áp sát bên chân giáp; xa xa hai bóng dáng đồng hành (khớp Fern, Stark) đứng chờ. | "Chương 14: Quái vật biết nói" | Tò mò, báo hiệu | 2 |
| 2 | P04-a | Toàn cảnh thị trấn có tường thành giữa rừng phương Bắc; hai khung dẫn: mốc 28 năm từ khi Himmel mất, địa danh "lãnh địa Graf Granat". | "28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời." | Trung tính, mở màn | 2 |
| 3 | P04-b | Frieren, Fern, Stark bàn ai sẽ đi mua đồ. | "Nào, giờ hãy quyết định xem ai sẽ là người đi mua đồ thôi." | Bình thường | 1 |
| 4 | P04-c | Cả nhóm vào cổng, thấy rất nhiều lính gác, nghi có chuyện. | "Có nhiều lính gác quá nhỉ?" | Cảnh giác | 1 |
| 5 | P04-d | Lính gọi tên Frieren, xác nhận đang trong thị trấn. | "Frieren-sama, chúng ta đang trong thị trấn đấy." | Trung tính | 1 |
| 6 | P05-a | Một đoàn quỷ (Granat và tuỳ tùng có sừng) diễu hành qua phố; dân chúng cúi rạp. | (không thoại — SFX bước chân) | Căng thẳng | 2 |
| 7 | P05-b | Frieren buột miệng gọi thẳng "Quỷ."; Fern ngơ ngác. | "Quỷ." / "Dạ?" | Cảnh giác, bất ngờ | 2 |
| 8 | P05-c | Toàn cảnh phố: dân chúng quỳ rạp khi đoàn quỷ đi qua. | — | U ám | 1 |
| 9 | P05-d | Cận mặt Granat, biểu cảm trầm ngâm. | — | Dò xét | 1 |
| 10 | P05-e | Frieren bị ghì úp xuống nền đá giữa phố. | — | Bạo lực bất ngờ | 2 |
| 11 | P05-f | Lính gác quát Frieren vì hành động (không rõ chính xác cô đã làm gì trước đó — ảnh không cho thấy động tác tấn công cụ thể). | "Con kia!! Mày đang tính làm gì thế hả!?" | Hoảng loạn, quát nạt | 2 |
| 12 | P06-a | Một người chất vấn Granat giữa đám đông đang tụ tập. | "Graf Granat, ngươi đang muốn gây náo loạn à?" | Căng thẳng | 2 |
| 13 | P06-b | Ai đó thắc mắc lại cụm từ "sứ giả hoà bình" gán cho con quỷ. | "…'Sứ giả hoà bình'?" | Nghi hoặc | 1 |
| 14 | P06-c | Nhận xét: đa số nhóm Frieren chỉ là mạo hiểm giả vô danh. | "Đa số những kẻ này đều là mạo hiểm giả vô danh cả." | Coi thường | 1 |
| 15 | P06-d | Granat đáp lời "Ngài Lugner": ghét quỷ tận xương nhưng không ngu muội bắt sứ giả hoà bình. | "Ta đây luôn căm ghét bọn quỷ các ngài… nhưng ta cũng không ngu muội đến mức bắt lấy sứ giả hoà bình đâu." | Mỉa mai, đe doạ ngầm | 2 |
| 16 | P06-e | Granat quỳ trước Frieren, nhận xét ánh mắt cô "điềm tĩnh, ác ý, thiếu thiện ý". | "Sao mà đôi mắt ngươi lại điềm tĩnh, ác ý và thiếu thiện ý đến nhường này nhỉ." | Dò xét, rợn người | 2 |
| 17 | P06-f | Granat: sẽ bỏ qua chuyện này. | "Nếu là thế thì ta sẽ bỏ qua một bên vậy." | Nhượng bộ giả tạo | 1 |
| 18 | P07-a | Granat nói: ngay cả dân thị trấn ghét quỷ vẫn nhìn quỷ "như nhìn con người". | "…thì chúng cũng chỉ căm ghét trong sợ sệt, và vẫn nhìn bọn ta với ánh mắt như nhìn con người vậy." | Châm biếm | 2 |
| 19 | P07-b | Cận mắt Frieren, lạnh lùng quan sát. | — | Lạnh lùng | 2 |
| 20 | P07-c | Đối đáp gay gắt về bản chất quỷ: "dã thú bắt chước tiếng người" — Granat nhận xét ánh mắt Frieren nhìn quỷ như nhìn dã thú thật sự. | "Lũ quỷ các ngươi chỉ là những con dã thú bắt chước tiếng người… Nhưng đôi mắt của ngươi đây… lại cứ như thể đang nhìn vào một con dã thú ấy nhỉ." | Đối đầu tư tưởng | 3 |
| 21 | P07-d | Lệnh tống giam Frieren vào ngục dinh thự; Granat mỉm cười. | "Đưa con nhỏ đó vào ngục dinh thự đi." | Đe doạ | 2 |
| 22 | P08-a | Lính áp giải Frieren và Stark tới cửa ngục. | — | Căng thẳng | 1 |
| 23 | P08-b | Toàn cảnh tháp ngục nhìn từ ngoài. | — | Trung tính | 1 |
| 24 | P08-c | Fern đứng ngoài song sắt gọi Frieren. | "Frieren-sama." | Lo lắng nhẹ | 1 |
| 25 | P08-d | Frieren ngồi trong ngục, than chán. | "Chán quá đi à." | Chán nản, hài hước | 1 |
| 26 | P08-e | Fern trêu Frieren lãng phí thời gian; Frieren đáp lại cũng đâu muốn ở đây. | "Frieren-sama thích lãng phí thời gian quá ha." / "Biết sao được, ta cũng có muốn ở đây đâu." | Bông đùa giữa nguy hiểm | 1 |
| 27 | P08-f | Fern dặn mang sách phép tới, nhắc lại yêu cầu (của phía thị trấn) rằng Frieren "tự kiểm điểm bản thân" trong ngục khoảng 2–3 năm. | "Họ nói là cô hãy tự giác kiểm điểm lại bản thân trong đây tầm 2 đến 3 năm đấy." | Trớ trêu | 2 |
| 28 | P09-a | Fern hỏi thực hư vụ "sứ giả hoà bình" — con quỷ tên **Máy chém Aura**. | "Ngài có biết Máy chém Aura không ạ?" | Tò mò | 2 |
| 29 | P09-b | Frieren giải thích: đó là đại quỷ phục vụ dưới trướng Quỷ Vương, một trong **bảy ma thuật sư huỷ diệt**; hầu hết thuộc hạ Quỷ Vương đã bị diệt trong chiến tranh với nhóm anh hùng. | "Đó là một con đại quỷ phục vụ dưới trướng Quỷ Vương, và là một trong bảy ma thuật sư huỷ diệt." | Nghiêm trọng | 3 |
| 30 | P09-c | Aura đã đề nghị giao ước hoà bình vì mệt mỏi với cuộc chiến không hồi kết. | "Có vẻ như Aura đã đề nghị giao ước hoà bình sau khi càng ngày càng thấy mệt mỏi với trận chiến không hồi kết này." | Trầm | 2 |
| 31 | P09-d | Thị trấn từng chiến tranh dài với quân đội của Aura, nhưng ả đã **lấy lại sức mạnh từ 28 năm trước**. | "Aura đã lấy lại được sức mạnh của mình từ 28 năm trước." | Nặng nề | 2 |
| 32 | P09-e | Frieren kết luận thẳng: đàm phán với quỷ là vô ích, một nước đi sai lầm. | "Đàm phán với lũ quỷ là điều vô ích. Một nước đi sai lầm." | Dứt khoát, bi quan | 3 |
| 33 | P10-a | Fern phản biện: quỷ là quái vật ăn thịt người — đã bao giờ nghĩ vì sao chúng dùng chung ngôn ngữ với con người chưa? | "Quỷ là những con quái vật ăn thịt người. Cậu đã bao giờ suy nghĩ tới việc vì sao loài quỷ lại dùng chung ngôn ngữ với con người chưa?" | Thắc mắc | 2 |
| 34 | P10-b | Stark: nếu đàm phán được thì tốt hơn; Frieren phản bác "đâu có vô ích chứ" (đối lập quan điểm). | "Chúng biết nói đấy chứ. Nếu chúng ta có thể đàm phán và giải quyết mâu thuẫn thì còn gì tuyệt vời hơn nữa?" | Tranh luận | 2 |
| 35 | P10-c | Chuyển cảnh hồi tưởng: giữa rừng, dân làng vây quanh một hiệp sĩ trẻ (Himmel) đang cầm kiếm trước một bé gái có sừng đang quỳ, gào giục kết liễu. | "Anh hùng!! Xin hãy mau chóng kết liễu nó đi ạ!!" | Áp lực đám đông | 3 |
| 36 | P10-d | Himmel do dự: đó chỉ là một đứa trẻ. | "…Đó chỉ là một đứa trẻ…" | Giằng xé đạo đức | 2 |
| 37 | P11-a | Himmel giơ kiếm, độc thoại đau đớn (không chắc chắn lời của Himmel hay của bé quỷ — xem mục D). | "…Đau quá…" | Đau đớn/giằng xé | 2 |
| 38 | P11-b | Người cha gào lên rằng chính con quỷ đã ăn thịt con gái ông; có người đáp lại "thì sao chứ". | "Chính nó đã ăn thịt con gái của tôi đấy!!" / "Thì sao chứ!?" | Phẫn nộ | 2 |
| 39 | P11-c | Bé quỷ khóc gọi "Mẹ ơi". | "Mẹ ơi…" | Đáng thương/gây nghi hoặc | 2 |
| 40 | P11-d | Người cha quỳ xa than đau đớn. | "…Đau lắm…" | Đau khổ | 1 |
| 41 | P11-e | Toàn cảnh dân làng vây quanh chờ phán quyết. | — | Căng thẳng tập thể | 1 |
| 42 | P12-a | Một người trong đám đông (có vẻ chức sắc tôn giáo) nói nếu giết đứa trẻ thì loài người cũng chẳng khác gì quỷ. | "Nếu làm thế thì chúng ta cũng chẳng khác loài quỷ là bao cả." | Do dự đạo đức | 1 |
| 43 | P12-b | Frieren can thiệp, định tự tay xử lý, chĩa vũ khí vào bé quỷ. | "Thôi đủ rồi. Để tôi xử nó vậy." | Lạnh lùng, quyết đoán | 2 |
| 44 | P12-c | Trưởng làng (người có ria mép) phản đối cách xử quá tay, hỏi có thể cho con bé cơ hội chuộc lỗi không, và rằng nó không nhất thiết phải ăn thịt người. | "Liệu không thể để cho con bé có cơ hội để chuộc lỗi hay sao? Con bé không nhất thiết là phải ăn thịt người, phải chứ?" | Nhân từ, mạo hiểm | 2 |
| 45 | P12-d | Trưởng làng nhận nuôi bé quỷ làm người giúp việc đồng áng. | "Trùng hợp thay là ta cũng đang tìm người làm đồng giúp đấy. Hãy tới sống ở nhà ta nhé." | Hy vọng mong manh | 2 |
| 46 | P12-e | Người cha mất con quỳ khóc xin lại con; Frieren im lặng không đáp. | "…Con tôi… Trả lại con cho tôi…" / "…" | Đau thương bị bỏ qua | 3 |
| 47 | P13-a | (Chêm ngắn giữa hồi tưởng) Himmel nói Frieren biết bé quỷ có thể nói; Frieren đáp cụt lủn. | "Frieren, con bé có thể nói." / "Ừm." | Trung tính, dồn nén | 1 |
| 48 | P13-b | Himmel muốn thử xem chuyện gì sẽ xảy ra vì đằng nào cũng dừng ở làng; Frieren cảnh báo cậu sẽ hối hận nếu không giết ngay, bỏ lửng lý do. | "Cậu sẽ thấy hối hận nếu như không giết nó ngay đấy, Himmel à. Dù gì thì nó cũng là…" | Bất an, linh cảm xấu | 3 |
| 49 | P13-c | Chuỗi ảnh yên bình: bé quỷ chơi giữa cánh đồng hoa cùng trẻ con làng, sống cùng trưởng làng, ăn cơm chung bàn, hái hoa, dạo phố cùng ông. | — | Ấm áp, tạm yên | 2 |
| 50 | P14-a | Thời gian sau: làng bốc cháy dữ dội, bé quỷ đứng giữa lửa, một xác người nằm gần đó. | (SFX lửa cháy) | Kinh hoàng, đảo ngược | 3 |
| 51 | P14-b | Himmel chất vấn tại sao bé quỷ giết trưởng làng. | "…Tại sao ngươi lại giết trưởng làng hả?" | Phẫn nộ, đau đớn | 3 |
| 52 | P14-c | Dân làng thất thần, cho biết đây không phải lần đầu ("lại nữa à"), đáng lẽ nên giết nó ngay từ đầu. | "Lại nữa à." / "…Đáng lẽ lúc ấy chúng ta nên giết ngươi ngay mới phải…" | Hối hận, tuyệt vọng | 2 |
| 53 | P15-a | Bé quỷ biện minh chỉ muốn sống yên bình, đổ lỗi cho thái độ thù địch của dân làng suốt những ngày qua. | "Ta chỉ muốn sống yên bình thôi mà." / "Ta lúc nào cũng thấy thái độ thù địch của các ngươi trong suốt mấy ngày vừa qua rồi đấy nhé." | Biện minh lạnh người | 2 |
| 54 | P15-b | Bé quỷ bế một đứa trẻ khác, tiết lộ đó là "con nhỏ thay thế" cho đứa mà nó đã ăn, chuẩn bị sẵn như một món quà/con tin. | "Là con nhỏ thay thế cho đứa mà ta đã ăn đấy. Chính vì thế nên ta mới chuẩn bị cho ngươi thứ này đây." | Rợn người | 3 |
| 55 | P15-c | Dân làng nhận ra đứa trẻ bị bắt chính là con gái ruột của trưởng làng đã chết. | "Trưởng làng có còn sống nữa đâu chứ?" / "Đó là con gái của trưởng làng mà." | Bàng hoàng | 2 |
| 56 | P16-a | Frieren nhận xét đây là một quyết định sai lầm, nhìn bé quỷ bế đứa trẻ đang ngủ. | "Có vẻ như đây là một quyết định sai lầm rồi nhỉ." | Chua chát | 2 |
| 57 | P16-b | Đoàn người đối đầu bé quỷ giữa quảng trường thị trấn. | — | Căng thẳng cao trào | 1 |
| 58 | P16-c | Bé quỷ tuyên bố giữ đứa trẻ làm con tin nếu tình hình đã thành ra thế này (kèm hành động cắt gì đó, SFX "キッ"). | "Nếu đã thành ra thế này, thì ta đành giữ lấy đứa trẻ này làm con tin vậy…" | Đe doạ trần trụi | 3 |
| 59 | P16-d | Cảnh xa: ba bóng người tản ra — một người bế thi thể/đứa trẻ rời đi, một người khác cầm bông hoa, một bóng nhỏ bước theo (chi tiết không rõ ràng — xem mục D). | — | Man mác, khép lại một vòng bi kịch | 2 |
| 60 | P17-a | (Khép đoạn hồi tưởng bằng câu hỏi mở đầu đã thấy ở P13) Frieren hỏi Himmel có muốn can thiệp không; Himmel chỉ ậm ừ. | "Cậu không muốn can thiệp gì chứ, Himmel?" / "…Ừm." | Nặng nề, chờ quyết định | 2 |
| 61 | P17-b | Frieren ra tay chém bé quỷ (SFX "ド"). | (SFX) | Bạo lực dứt khoát | 3 |
| 62 | P17-c | Bé quỷ trút hơi cuối, gọi lại "Mẹ ơi" một lần nữa (thấy từ xa, hai bóng nhỏ trên bậc thang). | "…Mẹ ơi…" | Bi thương, ám ảnh | 3 |
| 63 | P17-d | Frieren giải thích với Himmel: quỷ giống quái vật, không có tập tính nuôi dạy con cái, cả đời chỉ có một mình — nên không tồn tại khái niệm "gia đình" với chúng. | "Giống quỷ các ngươi hiển nhiên là loài cô độc rồi. Thế nên làm gì tồn tại khái niệm 'gia đình'." | Lạnh lùng phân tích | 2 |
| 64 | P17-e | Himmel hỏi lại vì sao vẫn nghe "mẹ ơi" một lần nữa. | "Lại 'mẹ ơi' nữa à?" | Nghi hoặc | 1 |
| 65 | P18-a | Frieren (hồi tưởng xa hơn, hoặc suy luận lại) đặt câu hỏi ngược cho bé quỷ vì sao vẫn dùng "mẹ ơi"; bé quỷ đáp: làm vậy thì sẽ không bị giết. | "Vậy có sao ngươi vẫn còn dùng 'mẹ ơi' đó chứ?" / "…Nếu làm vậy thì các ngươi sẽ không giết ta nữa, đúng chứ?" | Thao túng trần trụi | 3 |
| 66 | P18-b | Cắt về hiện tại: trong một thư viện/kho sách, Frieren dặn Stark đừng quên mang sách phép thuật. | "Mà đừng có quên sách phép thuật đấy nhá." | Trung tính | 1 |
| 67 | P18-c | Frieren dẫn lời pháp sư vĩ đại Flamme: bà từng định nghĩa "con quỷ" là những **con quái vật biết nói**. | "Pháp sư vĩ đại Flamme cũng đã định nghĩa những 'con quỷ' là những con quái vật biết nói." | Trọng lượng triết lý | 3 |
| 68 | P18-d | "Ngôn ngữ" với loài quỷ chỉ là công cụ để đánh lừa con người. | "'Ngôn ngữ' với chúng là thứ công cụ để đánh lừa con người." | Lạnh lùng | 2 |
| 69 | P18-e | Tổ tiên loài quỷ là một loài quái vật chuyên thốt câu "cứu với" từ trong bóng tối để dụ dỗ con người. | "Tổ tiên của chúng là một loài quái vật chuyên thốt ra câu 'cứu với' từ trong bóng tối nhằm để dụ dỗ con người cả đấy." | Rợn người | 2 |
| 70 | P19-a | Trong dinh thự Granat: một nhân vật quỷ tộc (tóc dài, có nữ hầu quỷ và một người đàn ông đứng hầu) nhận xét Granat đến muộn — đó là chiến thuật ngoại giao của con người. | "Graf Granat đến muộn rồi nhỉ?" / "Đó là một trong những chiến thuật ngoại giao của con người đấy." | Bình thản, mưu mô | 1 |
| 71 | P19-b | Toàn cảnh dinh thự Granat từ ngoài, giữa rừng. | — | Trung tính | 1 |
| 72 | P19-c | Cận mắt nhân vật quỷ tộc bí ẩn này. | — | Dò xét | 1 |
| 73 | P19-d | Nhân vật này thừa nhận con nhỏ pháp sư (Frieren) mới là thứ khiến mình vướng mắc, cảm giác từng thấy vẻ mặt đó ở đâu rồi. | "Nhưng mà con nhỏ pháp sư đó mới là thứ làm ta vướng mắc. Ta từng thấy vẻ mặt đó ở đâu rồi nhỉ…" | Bối rối hiếm thấy | 3 |
| 74 | P19-e | Nhân vật này bật cười mắt, nhắc lại câu nói cũ "chỉ là những con dã thú bắt chước tiếng người". | "Ta vô tình bật cười mắt rồi." / "'Chỉ là những con dã thú bắt chước tiếng người' à." | Châm biếm ngầm, gợi mở | 3 |
| 75 | P20-a | Nhân vật quỷ tộc tiếp tục: chỉ có một lý do khiến kẻ săn thịt người mới phát ra tiếng người. | "Chỉ có một lí do duy nhất mà những kẻ săn thịt người mới phát ra tiếng người mà thôi." | Lạnh lùng khẳng định | 2 |
| 76 | P20-b | Kết luận: con nhỏ pháp sư (Frieren) là kẻ duy nhất trong thị trấn hiểu đúng bản chất loài quỷ — "một biểu hiện rất chính xác". | "Con nhỏ đó là kẻ duy nhất biết bản chất của quỷ trong thị trấn này." / "Đó là một biểu hiện rất chính xác." | Thừa nhận đối thủ | 3 |
| 77 | P20-c | Cắt cảnh về ngục giam: Frieren kết luận với Stark rằng ngôn ngữ loài quỷ không phải để giao tiếp mà để đánh lừa. | "Đó không phải là ngôn ngữ dùng để giao tiếp, mà là để đánh lừa." | Dứt khoát | 3 |
| 78 | P20-d | Frieren tự nhủ sẽ thoát khỏi ngục một khi tình thế trở nên rối ren. | "Mình sẽ thoát ra khỏi nhà ngục này một khi tình thế trở nên rối ren vậy." | Bình thản trước hiểm nguy | 2 |
| 79 | P20-e | Chốt chương: Frieren dự báo thị trấn này sẽ không tồn tại được lâu nữa. | "Thị trấn này sẽ không còn tồn tại dài lâu được nữa rồi đây." | U ám, cảnh báo — cliffhanger | 3 |

---

## C. Điểm cao trào

1. **Phản xạ của Frieren khi thấy đoàn quỷ** (P05: "Quỷ." → bị ghì xuống đất) — mở màn xung đột của chương.
2. **Đối đáp "dã thú bắt chước tiếng người"** giữa Granat và Frieren (P07) — đỉnh đối đầu tư tưởng đầu tiên,
   xác lập chủ đề "quỷ nói được nhưng không phải để giao tiếp".
3. **Tiết lộ tên Aura — "Máy chém Aura"** và lịch sử hoà ước 28 năm (P09) — mốc thông tin quan trọng nhất
   chương, lần đầu có tên riêng cho một trong "bảy ma thuật sư huỷ diệt" (trước đây bible ghi "chưa ai có tên").
4. **Himmel do dự không giết đứa trẻ** giữa áp lực đám đông (P10–P11) — mở đầu hồi tưởng, đặt vấn đề đạo đức.
5. **Trưởng làng nhận nuôi bé quỷ bất chấp người cha mất con phản đối, Frieren im lặng** (P12) — cao trào
   cảm xúc đầu của hồi tưởng.
6. **Làng cháy, trưởng làng chết, dân làng thốt "lại nữa à"** (P14) — cú lật giữa hồi tưởng, hé lộ đây là
   một vòng lặp đã xảy ra nhiều lần.
7. **Bé quỷ dùng con gái trưởng làng đã chết làm "vật thay thế"/con tin** (P15) — đỉnh rợn người của mạch
   hồi tưởng.
8. **Frieren xuống tay giết bé quỷ, tiếng "Mẹ ơi" vang lên lần cuối** (P17) — đỉnh bi kịch của cả hồi tưởng.
9. **Bài học về "quái vật biết nói" từ lời Flamme** (P18) — đỉnh triết lý, đúng chủ đề tên chương.
10. **Nhân vật quỷ tộc bí ẩn trong dinh Granat nhận ra và thừa nhận sự sắc sảo của Frieren, mỉm cười** (P19–P20)
    — cú lật ngầm mở sang tuyến truyện đối phương, gợi ý một mối liên hệ chưa được xác nhận bằng chữ.
11. **Câu chốt chương:** "Thị trấn này sẽ không còn tồn tại dài lâu được nữa rồi đây." (P20) — cliffhanger.

---

## D. Chưa rõ

- **Danh tính nhân vật quỷ tộc ngồi sofa trong dinh Granat** (P19–P20, tóc dài, có nữ hầu quỷ và một người
  đàn ông đứng hầu): ảnh **không in tên** tại các khung này. Rất có thể liên quan tới Aura (nội dung phù hợp:
  bàn về "chiến thuật ngoại giao con người", nhận ra Frieren) nhưng **KHÔNG được khẳng định là Aura** —
  đây là suy đoán, không phải chữ trên trang.
- **"Ngài Lugner"**: được Granat gọi bằng kính ngữ ở P06, nhưng ảnh không nói rõ đây là ai (quan chức con
  người? người phát ngôn thị trấn?) hay xác nhận chính xác ai là người nói câu "Graf Granat, ngươi đang
  muốn gây náo loạn à?" — gán tạm theo bố cục khung, cần soi lại khi viết lời kể.
- **Danh tính bé quỷ trong hồi tưởng** (làng bị đốt, trưởng làng bị giết): không có tên riêng nào được in.
  **Không được nối** bé quỷ này với Aura hiện tại — chương không có một dòng chữ nào xác nhận đây là cùng
  một cá thể, dù nội dung có thể gợi ý một "vòng lặp" lặp lại qua nhiều làng/nhiều năm.
- **Trưởng làng, người cha mất con gái**: đều không có tên riêng.
- **Mốc thời gian của đoạn hồi tưởng**: không có hộp chữ ghi "X năm trước" nào xuất hiện trong toàn bộ đoạn
  hồi tưởng (P10–P17) — chỉ biết chắc nó diễn ra khi Himmel còn trẻ (thời tổ đội, trước hoặc trong C1).
- **Câu "…Đau quá…" (P11-a)**: không chắc chắn 100% đây là lời độc thoại của Himmel (giằng xé đạo đức) hay
  tiếng rên của bé quỷ — vị trí bong bóng gần khung mặt Himmel nhưng ảnh không có mũi tên chỉ rõ.
  **Không được gán chắc cho một trong hai bên khi viết lời kể** mà chưa xem lại ảnh gốc phóng to.
  Tương tự "…Đau lắm…" (P11-d) gán cho người cha theo suy luận vị trí, không có chỉ dẫn tuyệt đối.
- **Cảnh cuối hồi tưởng (P16-d)**: ba bóng người ở xa (một bế thi thể/đứa trẻ, một cầm hoa, một bóng nhỏ đi
  theo) — ảnh vẽ nhỏ, tối, không đọc rõ ai đang bế gì và họ đang đi đâu. Không suy diễn thêm.
- **Một vài lượt thoại tranh luận ở P06 và P10** (ví dụ "…'Sứ giả hoà bình'?", "Chính vì không thể giải
  quyết nên mới là vô ích") — khung nhỏ, góc nghiêng, **không chắc chắn tuyệt đối ai trong nhóm Frieren/
  Fern/Stark là người nói** dù đã gán theo suy luận hợp lý nhất từ tư thế nhân vật.
- **Vì sao chương có tới 6 trang minh hoạ bonus/bìa tập (P21–P26)** kèm theo — không rõ đây là do người
  crawl gộp luôn phần "extra" của raw hay do nguồn gốc vốn đính kèm; không ảnh hưởng nội dung beat sheet
  nhưng cần lưu ý khi làm `shots.tsv` để không vô tình cắt nhầm các trang này vào video.

---

## Câu hỏi duyệt

1. Panel có thật không — đã đúng dựa trên ảnh, không bịa?
2. Tên nhân vật đã đúng chưa (đặc biệt: Frieren/Himmel dùng đúng, "Aura"/"Graf Granat"/"Ngài Lugner" là
   thuật ngữ MỚI chưa có trong bible, cần chốt cách gọi trước khi viết lời kể)?
3. Trọng số (TS) đã hợp lý chưa — đặc biệt cụm hồi tưởng P10–P17 và đoạn dinh thự Granat P19–P20?
