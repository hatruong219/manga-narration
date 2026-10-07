# BEAT SHEET — FRN Chapter 21 "Hèn nhát"

Nguồn ảnh: `truyen/FRN/prepare/C21/pages-clean/` — **nettruyen13s, rộng 1000px** (khác truyenqq 900px
các chương khác). Đã mở từng file bằng mắt, không suy theo khuôn C6/C7/C13-C15.

---

## A. Kiểm tra đầu vào

- Nhận đủ **25 file**: `FRN_C21_P01.jpg` → `FRN_C21_P25.jpg`, liên tục, không thiếu trang nào
  (đã đối chiếu `ls pages/` và `ls pages-clean/`, hai thư mục có cùng 25 file).
- `clean-pages.py` **không xoá file nào** (25/25 file có mặt ở cả `pages/` và `pages-clean/`);
  nó chỉ cắt vài px ở đáy một số trang:
  | File | pages/ (H) | pages-clean/ (H) | Cắt |
  |---|---|---|---|
  | P04 | 1436 | 1425 | 11px |
  | P06 | 1436 | 1426 | 10px |
  | P23 | 1416 | 1399 | 17px |
  | Các file còn lại | — | — | 0px (không đổi) |
- **Đã mở từng trang rác bằng mắt trước khi kết luận** (không suy theo khuôn C6/C7/C13-C15):
  - `P01` (1000×632) — banner quảng cáo các bộ truyện khác (Hatsukoi Zombie, Shinigami Bocchan,
    Komi-san…) kèm logo **7 FINGERS TEAM**. → **BỎ**.
  - `P02` (1000×800) — trang credit: bìa tập 2 *Sousou no Frieren*, dòng chữ **"Sousou no
    Frieren"**, **TRANSLATOR: Credemoe / EDITOR: Yahari! / PROOFREADER: Credemoe / QUALITY
    CHECKER: Credemoe**, link facebook/blogtruyen 7 Fingers Team. → **BỎ**. *(Khớp đúng nhóm dịch
    đã chốt trong bible: 7 Fingers Team — Credemoe/Yahari; QC bible ghi gộp
    "PROOFREADER/QC Credemoe", ở đây tách hai dòng nhưng cùng một người — không lệch.)*
  - `P24` (1000×625) — thông báo nội bộ nhóm dịch: **"THÔNG BÁO — 7 Fingers Team xin phép…
    Trưởng nhóm Credemoe"**. → **BỎ**.
  - `P25` (1000×522) — banner **"12 FINGERS TEAM"** (bản ghi khác của cùng nhóm, như các chương
    trước). → **BỎ**.
  - `P03` (1000×1435) — trang bìa chương, in rõ **"Chương 21 — Hèn nhát"**, tranh đen trắng hai
    nhân vật giữa đồng hoa dưới mưa cánh hoa. → **GIỮ** (trang tên chương).
  - `P21` (1000×1416), `P22` (1000×1416) — **tranh màu ký tên "abe tsukasa"**, không thoại. →
    **GIỮ** nhưng đánh dấu **KHÔNG CHẮC thuộc mạch truyện** (xem mục D), theo đúng tiền lệ
    C13-P21.
  - `P23` (1000×1416→1399 sau crop) — tranh màu Frieren + Fern đắp người tuyết trong rừng, không
    thoại, không chữ ký lộ rõ (có thể bị cắt ở góc). → **GIỮ**, cùng đánh dấu KHÔNG CHẮC thuộc
    mạch truyện (giống C13-P21).
  → **19 trang nội dung/minh hoạ dùng được: P03, P04–P20, P21, P22, P23. 4 trang BỎ: P01, P02,
  P24, P25.**
- **Xác minh chiều đọc phải→trái bằng bằng chứng nội dung** (không chỉ suy theo quy ước
  chung của manga Nhật): bản dịch tiếng Việt trong mỗi khung đã được nhóm dịch **sắp xếp lại
  theo đúng thứ tự đọc** (trên→dưới, khung phải→trái trong từng hàng) sao cho hội thoại nối
  mạch logic — ví dụ ở P04: quỷ hỏi "kế hoạch... đã thất bại toàn tập rồi nhỉ" (khung phải)
  được đáp lại bằng "máu vẫn không ngừng chảy... đành chấm dứt tại đây sao" (khung dưới) rồi
  "...đúng vậy..." — mạch hỏi–đáp chỉ khớp nghĩa khi đọc đúng thứ tự này. Tương tự toàn bộ
  chương: câu hỏi luôn nằm ở khung đọc trước, câu đáp nằm ở khung đọc ngay sau nó. Đã kiểm tra
  mẫu này lặp lại nhất quán qua nhiều trang (P04, P06, P07, P09, P10) → xác nhận đúng chiều
  phải→trái, trên→dưới theo chuẩn manga Nhật.
- Chương có **CÚ LẬT/HỒI TƯỞNG LỚN**: từ P08 tới hết P19 là một hồi tưởng dài (nguồn gốc
  Frieren gặp Flamme), lồng vào giữa một trận chiến **hiện tại** đang diễn ra ở P04–P07 và
  chốt lại ở hiện tại tại P20. Đọc thiếu đoạn nào cũng làm sai mốc thời gian của cả chương.

---

## B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang bìa chương: hai nhân vật (một tóc dài bín một bên tông tối, một tóc dài sáng cầm một cuốn sách) ngồi giữa đồng hoa dưới mưa cánh hoa. In tên chương. | "Chương 21 — Hèn nhát" | Tĩnh, hoài niệm | 1 |
| 2 | P04-a | Một quỷ có sừng ngồi một mình trên tường thành ban đêm. | — | Cô độc | 1 |
| 3 | P04-b | Quỷ đứng nhìn xuống một quỷ khác bị đánh gục, giễu cợt kế hoạch thất bại. | "Kế hoạch của ngươi lẫn đồng bọn đều đã thất bại toàn tập rồi nhỉ." | Giễu cợt | 2 |
| 4 | P04-c | Quỷ bị thương, máu chảy, chấp nhận thất bại. | "...Vậy là ta đành chấm dứt tại đây sao..." | Cam chịu | 2 |
| 5 | P04-d | Quỷ chỉ huy đứng trước một binh đoàn đông đảo, nhắc tới trận đấu khác đang diễn ra. **Lần đầu tên "FRIEREN" xuất hiện trong chương**, xác nhận "cô ta" đang đối đầu Aura chính là Frieren. | "Chắc hẳn giờ này cô ta đang chạm trán với Aura-sama rồi... Nhưng dù thế thì Frieren cũng không toàn mạng trở về được đâu..." | Lo lắng, đe doạ | 3 |
| 6 | P05-a | Quỷ nhắc lại: lần trước phải rút lui vì còn nhóm anh hùng phòng vệ, lần này thì khác. | "Cô ta chẳng còn một anh hùng nào đứng ra phòng vệ nữa rồi." | Toan tính | 2 |
| 7 | P05-b | Quỷ khác nhận định ma lực Frieren vẫn kém Aura, nhưng vẫn là mối đe doạ. | "...Quả thực thì Frieren là một mối đe dọa đối với bọn ta..." | Dè chừng | 2 |
| 8 | P05-c/d/e | Các quỷ (bao gồm một nữ quỷ) tranh luận: nếu đối đầu trực diện Frieren sẽ thua, nhưng cô không bao giờ đánh trực diện — sẽ đánh lừa Aura rồi giết. **Thiết lập chủ đề "lừa gạt" xuyên suốt chương.** | "Ngài ấy không bao giờ đối đầu trực diện với quỷ cả. Chắc chắn ngài ấy sẽ đánh lừa Aura rồi giết chết ả mà thôi." | Vừa sợ vừa tin tưởng | 2 |
| 9 | P06-a | Quỷ trên tường thành nhận xét gay gắt về "cô ta" — gọi thẳng bằng biệt danh gắn với Frieren. | "Ấy thế mà lại thiển cận lắm đấy. Cô ta, cái kẻ đưa tang ấy..." | Khinh miệt | 2 |
| 10 | P06-b/c | Cảnh tường thành ban đêm: một quỷ quỳ gục, một **nhân vật nữ tóc dài cầm trượng (CHƯA RÕ danh tính)** đứng im lặng. | "...Cái cảm giác bất an gì thế này..." | Bất an | 2 |
| 11 | P06-d | Hai quỷ kinh ngạc: đối thủ thi triển phép nhanh mà ma lực không hề hao hụt. | "...Lượng ma lực ít ỏi của con bé này..." | Kinh ngạc | 2 |
| 12 | P07-a | Quỷ giận dữ mắng hai người là "nỗi ô nhục của pháp sư" vì lối đánh né tránh. | "LŨ HÈN NHÁT. Hai đứa các ngươi là nỗi ô nhục của pháp sư..." | Phẫn nộ | 2 |
| 13 | P07-b/c | Quỷ khác (kiệt sức) nhận ra chiêu giấu ma lực, đoán Frieren cũng làm tương tự. | "...Không ngờ là còn có chiêu này nữa... Chắc hẳn Frieren cũng tương tự như đây." | Bàng hoàng | 2 |
| 14 | P07-d | Nhân vật tóc dài cầm trượng đáp lại, dùng kính ngữ khi nhắc Frieren (gợi ý cô KHÔNG phải Frieren). | "Frieren-sama cũng biết vậy mà." | Điềm tĩnh | 2 |
| 15 | P07-e | Vụ nổ lớn kết liễu quỷ. | (hiệu ứng nổ, không thoại) | Bùng nổ | 2 |
| 16 | P08-a | **HỒI TƯỞNG BẮT ĐẦU.** Một phụ nữ tóc dài bín một bên cùng một cô bé elf đi giữa một ngôi làng elf bị tàn phá, xác người và ngựa la liệt. | "Cảnh tượng ở ngôi làng elf này trông kinh hoàng thật đấy." | Kinh hoàng | 3 |
| 17 | P08-b | Người phụ nữ tiến tới chỗ cô bé đang ngồi cạnh một nấm mộ/hố đất, hỏi cô có phải người đã giết kẻ kia. | "Em đã giết hắn ta sao, hả cô bé đang trên bờ vực cái chết kia ơi?" | Dò xét | 2 |
| 18 | P08-c/d | Xác một tướng quân quỷ trong binh đoàn Quỷ Vương được lệnh tiêu diệt ngôi làng. Chữ lớn in tên địa danh mới. | "Tên này là tướng quân ở trong binh đoàn của Quỷ Vương... được lệnh dẫn quân tới đây để tiêu diệt ngôi làng này." / **"NGÔI VƯƠNG BAZAN."** | Nặng nề | 2 |
| 19 | P08-e | Người phụ nữ nhận xét cô bé đã đối đầu trực diện với lũ quỷ và có lượng ma lực lớn. | "Em chắc hẳn là mạnh lắm nhỉ?" | Ngạc nhiên xen lẫn đánh giá | 2 |
| 20 | P09-a/b | Người phụ nữ chê cách đánh trực diện của cô bé là thiển cận, đáng lẽ nên lánh xa/ẩn nấp/phục kích. | "Thiển cận quá đấy. Cô bé đúng là ngốc nghếch toàn tập mà." | Chê trách | 2 |
| 21 | P09-c/d/e | Cô bé ngồi một mình giữa đống tro tàn, gọi với theo người phụ nữ đang bỏ đi, nói rằng tin cô ấy sẽ hiểu được nỗi lòng mình. | "...Tôi thừa biết rằng cô sẽ hiểu được nỗi lòng này..." | Van nài, hy vọng | 2 |
| 22 | P10-a | Cô bé giải thích lý do tin tưởng: phép lực của người phụ nữ còn ghê gớm hơn cả cô. | "...Bởi vì phép lực của cô còn ghê gớm hơn cả tôi nữa..." | Ngưỡng mộ | 2 |
| 23 | P10-b/c | Người phụ nữ hỏi vì sao cô bé nghĩ vậy; cô bé đáp chỉ là linh cảm. Hai người ngồi cạnh nhau. | "...Chỉ là linh cảm mà thôi." | Mong manh, tin cậy | 2 |
| 24 | P10-d | Người phụ nữ hỏi tên cô bé. | "Tên em là gì thế?" | Mở đầu mối quan hệ | 2 |
| 25 | P11-a/b | Người phụ nữ nói nếu là cô bé thì đã bỏ chạy không do dự; hỏi ngôi làng giờ ra sao. | "Nếu ta mà là em, thì đã nhanh chân tháo chạy... Ngôi làng đó ra sao rồi?" | Thẳng thắn | 2 |
| 26 | P11-c/d | Cô bé kể làng bị tàn phá hết, phụ nữ và trẻ em đều bị đồ sát; cô không bảo vệ nổi họ dù là người mạnh nhất trong làng. | "Bị tàn phá hết rồi... Tôi chẳng thể bảo vệ nổi họ. Dù cho là kẻ mạnh nhất trong đó sao." | Bất lực, đau đớn | 3 |
| 27 | P11-e | Người phụ nữ tiếc nuối vì không cứu được làng, khen cô bé có tài, và quyết định **đích thân rèn giũa** cô. | "Tiếc là không được rồi. Em rất có tài. Chính tay ta sẽ rèn dũa em." | Quyết định bước ngoặt | 3 |
| 28 | P11-f | Cô bé xin được thả xuống; phụ nữ đáp: nếu không đi ngang qua thì cô bé đã chết, và cô đang trên bờ vực tuyệt vọng. | "Nếu như ta không đi qua, thì em đã chết mất tiêu rồi." | Trầm lắng | 2 |
| 29 | P12-a | Hai người tiếp tục hành trình; gặp ba quỷ mạnh hơn cả tên tướng quân đã bị giết, ban đầu che giấu ma lực để đề phòng phục kích. | "Bọn chúng thậm chí còn mạnh hơn cả tên tướng lĩnh mà em vừa triệt hạ nữa đó." | Căng thẳng | 2 |
| 30 | P12-b/c | Ba quỷ xuất hiện, tự tin phô ma lực sau khi biết đối phương là pháp sư. | "Sau khi biết tụi ta là pháp sư là liền mạnh dạn giải phóng ra luôn." | Ngạo mạn | 2 |
| 31 | P13-a/b | Quỷ ra lệnh: bỏ cô bé xuống và rời đi, vì lệnh của Quỷ Vương là **tàn sát toàn bộ tộc elf**. | "Tàn sát lũ elf. Đó là lệnh của Quỷ Vương." | Đe doạ, diệt chủng | 3 |
| 32 | P13-c/d | Người phụ nữ tự tin đáp trả: hiểu rõ nỗi lòng pháp sư uy lực, nắm chắc tâm can của quỷ trong lòng bàn tay. Chú thích tên cô bé lần đầu xuất hiện. | "Ta cũng nắm chắc tâm can của lũ quỷ ngay trong lòng bàn tay vậy." / **"FRIEREN."** | Tự tin tuyệt đối | 3 |
| 33 | P14-a/b | Quỷ sững sờ; người phụ nữ kết luận chúng chỉ là kẻ ngạo mạn ngu dốt và thiếu cẩn trọng. | "Nói thế cũng đồng nghĩa với việc bọn chúng chỉ là những kẻ ngạo mạn ngu dốt và thiếu cẩn trọng." | Lạnh lùng | 2 |
| 34 | P14-c | Vụ nổ khổng lồ trùm cả một vùng núi rừng, tiêu diệt ba quỷ. | (splash nổ lớn, không thoại) | Huỷ diệt | 3 |
| 35 | P15-a/b | Người phụ nữ giải thích: giết chúng bằng cách để chúng hiểu sai cách biệt ma lực — một cách hèn hạ, bẩn thỉu để đấu với pháp sư kiêu hãnh. Frieren đồng tình. | "Ta giết chúng bằng cách khiến chúng bị sai lầm về cách biệt giữa lượng ma lực... Đó là một cách hèn hạ và bẩn thỉu." / "Đúng vậy." | Thản nhiên | 2 |
| 36 | P15-c/d/e | Hai người tới một căn nhà đá trong rừng — nơi ở mới; vết thương của Frieren gần lành. | "Chắc cũng tới lúc luyện tập rồi đấy." | Ổn định, mở ra cuộc sống mới | 2 |
| 37 | P16-a | Frieren hỏi cách xưng hô; người phụ nữ bảo gọi là "Sư phụ". | "Gọi ta là Sư phụ." | Trang trọng | 2 |
| 38 | P17-a | **Tên thật được xác nhận: FLAMME.** | "Flamme." | Tiết lộ | 3 |
| 39 | P17-b/c/d | Chuỗi đối thoại song song: cả hai đều khinh bỉ quỷ tới mức muốn diệt trừ, đều đã mất tất cả vì quỷ, đều yêu phép thuật. | "Em đã mất tất cả vì lũ quỷ ấy." / "Ta cũng thế." / "Và em yêu phép thuật..." / "Ta cũng vậy." | Đồng cảm sâu sắc — đỉnh cảm xúc chương | 3 |
| 40 | P18-a | Cả hai tự nhận là "những kẻ hèn nhát duy nhất làm ô nhục phép thuật" — nhận danh xưng "hèn nhát" làm điểm chung. | "Vì vậy nên chúng ta là những kẻ hèn nhát duy nhất làm ô nhục phép thuật." | Chấp nhận, gắn kết | 3 |
| 41 | P18-b/c/d | Bài luyện đầu tiên: giới hạn giải phóng ma lực xuống dưới 1/10; Frieren làm được ngay, được khen kiểm soát tốt; Flamme nhận xét bất cứ elf nào cũng làm được (gợi ý sở trường bẩm sinh của elf). | "Bất cứ elf nào cũng làm được vậy ha." / "Quả không hổ danh. Em kiểm soát tốt thật đấy." | Bất ngờ nhẹ, hài lòng | 2 |
| 42 | P18-e/f | Bài tiếp theo: luyện cơ bản trong trạng thái giới hạn ma lực đó. Frieren tự tin thái quá. | "Chỉ vậy thôi ạ? Dễ như ăn kẹo nhỉ?" | Ngây thơ, tự tin | 2 |
| 43 | P19-a/b | Frieren hỏi phải giới hạn ma lực tới bao giờ, lo sẽ suy kiệt; Flamme đáp: cả phần đời còn lại. | "Em còn phải giới hạn ma lực đến khi nào nữa vậy ạ?" / "Cả phần đời của mình." | Choáng váng | 3 |
| 44 | P19-c | Flamme chốt lại bài học thành lời răn cả đời: Frieren sẽ phải lừa gạt lũ quỷ suốt phần đời của mình. | "Em sẽ phải lừa gạt lũ quỷ trong suốt phần đời của mình." | Định mệnh | 3 |
| 45 | P19-d | Splash: Frieren nhỏ đứng giữa hai đội quân đối lập — hình ảnh gợi lại bố cục "Ngôi Vương Bazan" ở đầu hồi tưởng, đóng lại vòng lặp. | (splash, không thoại) | Sử thi, khép hồi tưởng | 3 |
| 46 | P20-a | **HIỆN TẠI.** Frieren (thiết kế hiện tại: hai búi tóc, áo sọc) đối mặt trực diện với **AURA lần đầu lên hình** — quỷ cái có sừng, tóc vàng/trắng, giáp trang trí hình cán cân. | "Ngươi đã thất bại, Aura à." | Đối đầu trực diện — cú lật lớn | 3 |
| 47 | P20-b | Aura đáp: có vẻ Lugner đã chết; đao phủ của Frieren (ám chỉ Draht) cũng đã bị tiêu diệt cả. | "...Có vẻ như Lugner đã chết rồi nhỉ." | Bình thản trước tổn thất | 3 |
| 48 | P20-c | Frieren: ngươi đã phóng thích quá nhiều xác sống từ binh đoàn mà ta đang kiểm soát — cảnh xác chết la liệt trên mặt đất. | "Ngươi đã phóng thích quá nhiều xác sống từ binh đoàn mà ta đang kiểm soát rồi đấy." | Trách móc lạnh | 2 |
| 49 | P20-d/e | Aura: hạ được Frieren tại đây cũng là một phần thưởng xứng đáng; Frieren đáp tiếc nuối; Aura cảnh cáo Frieren đang phí phạm ma lực trước mặt mình. **Chốt chương ở thế đối đầu treo lửng.** | "Ngươi có nghĩ rằng việc tiêu hao lượng lớn ma lực trước mặt ta thế là một ý hay không vậy?" | Đe doạ, cliffhanger | 3 |
| 50 | P21-a | *(Tranh màu, không thoại — xem mục D)* Frieren đứng một mình trên đồi dưới ánh trăng, cầm trượng, nhìn về phía một toà thành/tàn tích xa xa. | — | Cô độc, chiêm nghiệm | 1 |
| 51 | P22-a | *(Tranh màu, không thoại — xem mục D)* Bốn nhân vật tựa vào lan can nhìn xuống: một người tóc xanh dương, một người tóc xanh lá đeo kính, một người đội sừng khoác đỏ, một nữ tai nhọn tóc trắng. | — | Hoài niệm (KHÔNG RÕ bối cảnh) | 1 |
| 52 | P23-a | *(Tranh màu, không thoại — xem mục D)* Frieren và Fern cùng đắp người tuyết trong rừng mùa đông. | — | Ấm áp, đời thường | 1 |

---

## C. Điểm cao trào

Chương có **nhiều đỉnh**, chia làm hai tuyến (hiện tại và hồi tưởng), khép lại bằng một cú lật nối hai tuyến:

1. **P08** — Cú chuyển cảnh vào hồi tưởng: ngôi làng elf bị tàn sát, hé lộ Frieren từng là nạn
   nhân/người sống sót duy nhất của một cuộc diệt chủng do Quỷ Vương ra lệnh (P13-a/b:
   *"Tàn sát lũ elf. Đó là lệnh của Quỷ Vương."*) — lore hoàn toàn mới, giải thích thêm cho
   việc "tộc elf đang tuyệt chủng dần" đã ghi ở bible C13.
2. **P13** — Tên **"FRIEREN"** được xác nhận lần đầu trong hồi tưởng, đúng lúc Flamme nhận nuôi/
   nhận làm học trò.
3. **P14** — Vụ nổ khổng lồ tiêu diệt ba quỷ mạnh — màn thể hiện sức mạnh đầu tiên của Flamme.
4. **P17** — Tên **"FLAMME"** được xác nhận + chuỗi đối thoại song song ba lần "Ta cũng thế" —
   **đỉnh cảm xúc lớn nhất chương**, trả lời câu hỏi bible đã treo từ C7: *vì sao Flamme nhận
   Frieren làm học trò* (đáp: cả hai đều mất tất cả vì quỷ, đều khinh bỉ quỷ, đều yêu phép thuật).
5. **P18–P19** — Bài học cốt lõi: *"chúng ta là những kẻ hèn nhát duy nhất làm ô nhục phép
   thuật"* và lời răn cả đời *"em sẽ phải lừa gạt lũ quỷ trong suốt phần đời của mình"* — đây
   chính là gốc rễ tính cách né tránh giao chiến trực diện của Frieren xuyên suốt cả bộ truyện.
6. **P20 (CHỐT CHƯƠNG — cú lật lớn nhất)** — Frieren đối đầu trực diện **AURA lần đầu lên hình
   trong cả bộ** (C14, C15 đều chỉ nhắc tên, chưa hiện diện); xác nhận **Lugner đã chết**
   (khép lại nhánh C15); mở ra thế đối đầu treo lửng giữa hai người mạnh nhất hai phe.

---

## D. Chưa rõ

- **Danh tính "nhân vật nữ tóc dài cầm trượng" ở P06–P07** (trận đánh hiện tại, trước khi vào
  hồi tưởng): bị quỷ gọi là "cái kẻ đưa tang ấy" (P06-a — biệt danh gắn với Frieren/tựa đề gốc
  bộ truyện *Sousou no Frieren*), nhưng chính cô lại nói **"Frieren-sama cũng biết vậy mà"**
  (P07-d) — dùng kính ngữ ở ngôi thứ ba, gợi ý cô **KHÔNG PHẢI** Frieren. Kiểu tóc của cô (xoã
  dài, cổ áo có nơ) cũng khác thiết kế Frieren xuất hiện ở P20 (hai búi tóc, áo sọc). **Không
  đủ căn cứ để gọi tên nhân vật này trong lời kể** — tạm mô tả là "một nữ pháp sư".
- **Người thứ hai trong "Hai đứa các ngươi là nỗi ô nhục của pháp sư"** (P07-a): quỷ nói với
  hai người nhưng khung hình chỉ cho thấy một nhân vật. Người còn lại CHƯA RÕ có mặt tại chỗ
  hay đang ở nơi khác (có thể ám chỉ Frieren đang đấu Aura ở xa).
- **"Ngôi Vương Bazan"** (P08-d): tên riêng hoàn toàn mới, in bằng chữ lớn kiểu hộp dẫn địa danh
  nhưng không có giải thích gì thêm trên trang — CHƯA RÕ là tên vương quốc, ngôi làng, hay danh
  xưng của trận địa/sự kiện. Cũng CHƯA RÕ đây có phải quê hương gốc của Frieren hay chỉ là nơi
  ngôi làng elf toạ lạc.
- **Câu "FLAMME." ở P17-a**: không chắc chắn 100% đây là Frieren hỏi lại/nói tên "Flamme" khi
  nhận ra, hay là chính người phụ nữ tự xưng tên thật ngay sau khi bảo gọi mình là "Sư phụ" —
  khung tách rời không có chủ ngữ rõ ràng. Dù vậy, xét theo mạch đối thoại (giới thiệu cách
  xưng hô rồi tới tên thật), khả năng cao là Flamme tự nói tên mình.
- **Trang bìa P03**: hai nhân vật trong tranh (tóc dài bín một bên tông tối + tóc dài sáng cầm
  sách) rất giống hoạ tiết Flamme + Frieren nhỏ, nhưng đây là tranh bìa minh hoạ không thoại,
  không có chữ tên xác nhận — **không nên chú thích tên nhân vật vào ảnh này** khi viết lời kể
  (giống quy tắc bible đã áp dụng cho C7-P03).
- **P21, P22 (tranh màu ký tên "abe tsukasa")**: không thoại, CHƯA RÕ có thuộc mạch truyện
  chương này hay là tranh minh hoạ rời (như C13-P21). P22 đặc biệt đáng ngờ: bốn nhân vật gồm
  một người tóc xanh dương (gợi nhớ màu tóc Himmel theo bible) đứng cạnh một người tóc xanh lá
  đeo kính, một người đội sừng khoác đỏ (có thể là quỷ, hoặc chỉ là trang phục), và một nữ tai
  nhọn tóc trắng — bối cảnh một ban công không xác định. **Không có chữ tên nào trên trang**,
  không nên gọi tên bất kỳ ai trong số này khi viết lời kể.
- **P23 (tranh màu Frieren + Fern đắp người tuyết)**: không thoại, không có mốc thời gian —
  CHƯA RÕ có thuộc mạch truyện C21 hay là tranh omake mùa đông độc lập, tương tự cách xử lý
  C13-P21.
- **"Hắn ta"/"tướng quân"** bị giết ở P08 (mở đầu hồi tưởng): không có tên riêng, chỉ được gọi
  "tướng quân ở trong binh đoàn của Quỷ Vương".
- **Quan hệ giữa "cô gái bị giam" ở C15** (tai nhọn, tự vệ bằng ma lực, giết Draht, chốt câu
  "Kẻ đầu tiên.") và **nhân vật nữ tóc dài cầm trượng ở C21-P06–P07** (cũng tai nhọn khả nghi,
  cũng đấu quỷ, có vẻ đang tiếp tục truy sát các mục tiêu tiếp theo mà "Kẻ đầu tiên" ngụ ý):
  **CHƯA CÓ bằng chứng chữ trên trang để nối hai nhân vật này làm một** — chỉ là một khả năng
  đáng lưu ý, không được khẳng định trong lời kể.
- Cơ chế chính xác đằng sau lời quỷ nói **"Frieren cũng tương tự như đây"** (P07-c): quỷ này
  CHƯA RÕ có từng biết mặt Frieren hay chỉ đang suy đoán theo danh tiếng.

---

## Báo cáo nhanh (để duyệt)

- **Tổng panel đã ghi:** 52 panel/beat, trải trên 19 trang nội dung/minh hoạ (P03, P04–P20,
  P21–P23); 4 trang rác (P01, P02, P24, P25) đã loại theo đúng cách nhóm dịch 7 Fingers Team
  dùng ở các chương nguồn nettruyen13s trước đó — **khớp bible**, không phát sinh khuôn rác mới.
- **Điểm cao trào:** 6 điểm — xem mục C (đỉnh lớn nhất là cú lật cuối chương P20: Aura lần đầu
  lên hình trực diện, xác nhận Lugner đã chết).
- **Mục "Chưa rõ" đáng chú ý nhất:** danh tính nhân vật nữ tóc dài cầm trượng ở P06–P07 (khả
  năng không phải Frieren dù được liên hệ tới biệt danh "kẻ đưa tang"); tên địa danh mới
  "Ngôi Vương Bazan"; tính xác thực tư cách nhân vật trong 2 tranh màu P21/P22 (đặc biệt P22 có
  người tóc xanh dương gợi nhớ Himmel nhưng không có chữ xác nhận).
- **Thuật ngữ/tên mới cần thêm vào bible (không lệch, chỉ là MỚI hoàn toàn so với C1–C15):**
  Aura (lần đầu lên hình trực diện, xác nhận là quỷ cái có sừng, giáp hình cán cân) · Lugner
  (xác nhận đã chết) · "Ngôi Vương Bazan" · lệnh "tàn sát lũ elf" của Quỷ Vương · nguồn gốc
  Frieren là người sống sót một ngôi làng elf bị quân Quỷ Vương xoá sổ · xác nhận bằng chữ in
  rằng Flamme cũng "mất tất cả vì quỷ" và "yêu phép thuật" giống Frieren · câu răn "hèn nhát"
  làm gốc triết lý né giao chiến trực diện của Frieren.
- **Tên nhóm dịch:** khớp hoàn toàn với bible (7 Fingers Team — TRANSLATOR Credemoe, EDITOR
  Yahari, PROOFREADER/QC Credemoe). Không lệch.

**Ba câu hỏi duyệt:**
1. Panel có thật không — đã mở từng trang bằng mắt, đối chiếu đủ 25 file, không thiếu trang,
   không suy trang rác theo khuôn chương khác?
2. Tên nhân vật đúng chưa — đặc biệt chỗ để ngỏ "nhân vật nữ tóc dài cầm trượng" ở P06–P07 và
   hai tranh màu P21/P22 chưa gán tên ai?
3. Trọng số (TS) đã hợp lý chưa — đỉnh P13/P14/P17/P19/P20 đã đúng mức 3 như mong đợi?
