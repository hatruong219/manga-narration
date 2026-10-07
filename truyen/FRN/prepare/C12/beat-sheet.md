# BEAT SHEET — FRN Chương 12 · "Cửa ngõ phương bắc"

> Bước ĐỌC HIỂU. **Chưa viết lời kể.** Dừng chờ duyệt.
> Nguồn: `truyen/FRN/prepare/C12/pages-clean/` · Bible: `truyen/FRN/series-bible.md`

---

### A. Kiểm tra đầu vào

**Nhận 22 file, đọc đủ 22/22, không nhảy cóc:** `FRN_C12_P01` → `FRN_C12_P22`.
Đánh số liên tiếp, **không thiếu trang nào**.

**Trang KHÔNG phải nội dung truyện — đánh BỎ (đã mở ảnh kiểm từng cái, không loại theo kích thước suông):**

| File | Khổ | Nội dung thực tế | Kết luận |
|---|---|---|---|
| `P01` | 900×585 | Banner quảng cáo 7 Fingers Team (ảnh ghép các bộ Hatsukoi Zombie, Komi-san…, link facebook) | **BỎ** |
| `P02` | 900×720 | Trang credit 7 Fingers Team — TRANSLATOR/PROOFREADER/QC Credemoe, EDITOR Yahari | **BỎ** |
| `P03` | 900×1291 | **Bìa tạp chí** Weekly Shonen Sunday No.35 · 2020.8.12 (ảnh màu Frieren + Fern, chữ Nhật, không có bản dịch) — không phải trang truyện | **BỎ khỏi beat** (dùng được làm thumbnail) |
| `P22` | 900×946 | Banner 12 Fingers Team + quảng cáo truyenqqq.com | **BỎ** |

→ **Nội dung truyện: 18 trang, `P04`–`P21`.** Tổng **111 panel**.

**clean-pages.py đã cắt (so `pages/` với `pages-clean/`):**

| File | Trước | Sau | Cắt |
|---|---|---|---|
| `P01` | 900×1075 | 900×585 | **−490px** |
| `P16` | 900×1291 | 900×1281 | **−10px** (dải đáy, không mất khung truyện) |
| `P22` | 900×976 | 900×946 | **−30px** |
| 19 file còn lại | — | — | **không cắt** |

**Số trang in trên ảnh = số file − 2** (đúng quy ước bible): `P04` in "1", `P21` in "19". Beat sheet dưới đây **dùng số FILE**.

**Chiều đọc: PHẢI → TRÁI (manga Nhật). Xác minh bằng 4 chứng cứ trong chính ảnh chương này:**

1. **Số trang in ở mép — chứng cứ mạnh nhất.** Số LẺ luôn nằm ở **mép TRÁI** (`P07`="5", `P09`="7", `P11`="9", `P13`="11", `P15`="13", `P17`="15", `P19`="17", `P21`="19"), số CHẴN luôn ở **mép PHẢI** (`P06`="4", `P08`="6", `P10`="8", `P12`="10", `P18`="16", `P20`="18"). Đóng sách kiểu Nhật (gáy bên phải) mới cho trang lẻ nằm bên trái.
2. **`P04`, khung hẻm phố:** hai bong bóng trong CÙNG một khung — "Thế khi nào thì chúng tôi mới được phép đấy?" nằm **bên phải**, "Ai mà biết được." nằm **bên trái**. Hỏi phải đứng trước đáp → đọc phải sang trái.
3. **`P09`, hàng khung cuối (3 khung):** khung PHẢI "Ờmm... gì vậy? Cô giận gì à?" → khung GIỮA "Stark-sama." → khung TRÁI "Rồi rồi... tôi sẽ cho một nửa mà." Đọc trái→phải thì câu thoại vô nghĩa.
4. **`P10`, hàng khung đầu:** khung PHẢI Fern hỏi "Nếu như chúng ta phải ở lại đây ít nhất là 2 năm lận thì cậu sẽ thấy thế nào?" → khung TRÁI đáp "Hà? Ai lại muốn thế chứ."

Ngoài ra dải chữ Nhật dọc ở mép trái `P04` xếp cột theo hướng phải→trái, cùng quy ước.

---

### B. Beat Sheet

Trọng số: **3** = khoảnh khắc quyết định · **2** = nhịp chính · **1** = chuyển tiếp.

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P04-a | Toàn cảnh màu: pháo đài tường thành nằm trong lòng núi. Hộp dẫn truyện mở chương bằng một mốc thời gian | "28 năm đã trôi qua kể từ lúc anh hùng Himmel qua đời." | lặng, mở màn | 3 |
| 2 | P04-b | Cổng thành đóng, lính gác ngồi canh, dân qua lại lác đác | "bức tường thành kiên cố gần hẻm núi Bakur" | tù đọng | 2 |
| 3 | P04-c | Lính gác đội mũ trụ giải thích với khách lữ hành: vùng trung tâm đầy quái vật, hiện không ai được vượt biên | "hiện giờ không ai được phép vượt biên hết" | cứng rắn | 2 |
| 4 | P04-d | Hai khách lữ hành hỏi khi nào mới được qua — không ai biết | "Ai mà biết được." | bế tắc | 1 |
| 5 | P04-e | Cận mặt lính gác: từ ngày anh ta nhậm chức, chưa một người hay quái vật nào đi qua cổng | "thì không có một con người hay quái vật nào đi qua nữa rồi" | nặng nề | 2 |
| 6 | P05-a | **Trang màu đôi — tên chương "Chương 12 · Cửa ngõ phương bắc".** Frieren đứng giữa, Fern bên trái khung, chàng trai tóc đỏ vác rìu bên phải khung | "Sao cũng được thôi." / "Có vẻ vui ạ." (dòng chữ tay nhỏ cạnh Fern: **KHÔNG ĐỌC ĐƯỢC**) | giới thiệu tổ đội ba người | 3 |
| 7 | P06-a | Một cảnh vệ chạy tới báo: viên thị trấn cho gọi đội trưởng cảnh vệ | "viên thị trấn đang cho gọi ngài ạ" | công vụ | 1 |
| 8 | P06-b | Hai người dân bình phẩm về cảnh vệ vừa từ chối khách: nghiêm khắc thế mới đúng | "Phải nghiêm khắc với du khách bên ngoài…" | dửng dưng | 1 |
| 9 | P06-c | Đội trưởng cảnh vệ dặn thẳng mặt nhóm Frieren trước khi đi | "Xin đừng gây ra bất cứ rắc rối nào cho thị trấn này nhé." | răn đe | 2 |
| 10 | P06-d | Cả ba đứng lại trong hẻm, chưa biết làm gì tiếp | — | hụt hơi | 1 |
| 11 | P06-e | Cận mặt Frieren: thị trấn có vẻ an toàn, nghỉ chân ít lâu cũng được | "cứ nghỉ chân ít lâu cũng được" | thong thả | 2 |
| 12 | P06-f | Frieren mừng ra mặt: rốt cuộc cũng có thời gian đi lùng phép thuật; giục tới quầy phép thuật trước cả khi nhận phòng | "Cuối cùng thì ta cũng được thong thả tìm kiếm ma pháp sau bấy lâu nay rồi." | háo hức | 3 |
| 13 | P06-g | Fern phản ứng: biên giới đã chặn thì cũng chẳng còn cách nào khác | "chúng ta làm gì có cách nào khác nữa chứ…" | cam chịu | 2 |
| 14 | P06-h | Nhóm tách ra — Frieren đi đặt phòng | "Hay là chúng ta tách ra nhé?" | rời rạc | 1 |
| 15 | P07-a | Còn lại hai người, chàng trai tóc đỏ rủ Fern đi ăn | "…có muốn đi ăn gì không?" | ngập ngừng | 2 |
| 16 | P07-b | Fern không nhận lời; cậu ta đành đi một mình | "…Rồi. Thế tôi tự đi một mình vậy." | cụt hứng | 2 |
| 17 | P07-c | Fern đi hỏi tin ở sạp hoa quả: phương bắc đang dồn quân chinh phục, chừng 2 năm nữa biên giới mới mở lại | "Chắc cũng phải mất tầm 2 năm nữa thì biên giới mới được mở lại đây." | tin dữ | 3 |
| 18 | P07-d | Cậu tóc đỏ lê bước một mình trong hẻm, hiệu ứng "Sầu…" | "Sầu…" | tủi | 2 |
| 19 | P07-e | Fern hỏi thêm người bán hàng, chỉ nhận thêm tin xấu về buôn bán sa sút | "Giờ nghề kinh doanh ở đây cũng dần dà suy thoái rồi." | im lặng | 1 |
| 20 | P07-f | Fern đứng lại một mình giữa hẻm vắng | — | trống | 1 |
| 21 | P07-g | Ngoại cảnh một quán rượu có biển hiệu | — | chuyển cảnh | 1 |
| 22 | P07-h | Cận ly kem trái cây phủ kín quả mọng và bánh | — | thèm, ấm | 2 |
| 23 | P08-a | Cậu tóc đỏ ngồi một mình ở quầy bar, gọi món quen ngày bé | "Hoài niệm thật đấy… cái món Jumbo Berry đặc biệt này." | hoài niệm | 3 |
| 24 | P08-b | Hồi tưởng: hồi bé cậu ăn không hết, phải để sư phụ ăn nốt | "cháu chẳng thể ăn hết nổi và rồi lại phải để cho sư phụ ăn nốt" | ấm áp | 3 |
| 25 | P08-c | Món được bưng ra — nhỏ hơn cậu tưởng rất nhiều | "Cơ mà, nó bé thế này à…" | hẫng | 3 |
| 26 | P08-d | Cậu cúi nhìn ly kem, tự nhận ra điều đó nghĩa là gì | "Vậy ạ, cháu đã lớn rồi à…" | chùng | 3 |
| 27 | P08-e | Ông chủ quán cười: ly kem không nhỏ đi, chỉ là cậu đã lớn | "Đấy là do giờ cậu đã lớn rồi đó, chàng trai à…" | hiền hậu | 3 |
| 28 | P08-f | **Ông chủ quán biết rõ sư phụ cậu — gọi đích danh Eisen**, nhắc cậu nên hiếu thuận vì ông đã có tuổi | "Ngài Eisen giờ cũng đã có tuổi rồi mà…" | nhắc nhở | 3 |
| 29 | P08-g | Cậu nhớ lại dáng Eisen đội mũ sừng: hồi bé cái gì cũng to lớn, kể cả bờ vai sư phụ — rồi bờ vai ấy teo nhỏ lại lúc nào không hay | "đến cả bờ vai rộng lớn của sư phụ mà còn dần thu nhỏ lại trước khi cháu kịp nhận ra nhỉ" | xót, **đỉnh 1** | 3 |
| 30 | P09-a | Ông chủ quán góp lời về sự tàn nhẫn của thời gian; cậu vẫn cố cãi là ly kem bé thật | "Thời gian thấm thoát thoi đưa quả là tàn nhẫn nhỉ…" | trầm | 3 |
| 31 | P09-b | Cận mặt cậu, cười gượng cho qua | "Cũng tầm giữa thế ạ." | giấu | 2 |
| 32 | P09-c | Fern đột ngột hiện ra sau lưng; cậu giật mình chống chế là tự bỏ tiền túi, không chểnh mảng | "Tôi không có chểnh mảng đâu nhá!!" | hốt hoảng, hài | 3 |
| 33 | P09-d | Fern ngồi xuống cạnh, im lặng nhìn thẳng | "…" (dấu chấm lửng) | căng ngầm | 2 |
| 34 | P09-e | Fern gọi một cốc sữa | "Cho tôi một cốc sữa." | lạnh | 1 |
| 35 | P09-f | Toàn cảnh quầy bar, cậu dò hỏi vì sao Fern có vẻ giận | "Ờmm… gì vậy? Cô giận gì à?" | dò dẫm | 2 |
| 36 | P09-g | Fern chỉ gọi tên cậu — **"Stark-sama"** (lần đầu tên nhân vật này xuất hiện trong bản dịch) | "Stark-sama." | áp lực | 3 |
| 37 | P09-h | Cậu đầu hàng, chia đôi phần kem | "Rồi rồi… tôi sẽ cho một nửa mà." | nhượng bộ, hài | 2 |
| 38 | P10-a | Fern nói không phải chuyện ly kem, mà hỏi: nếu phải kẹt ở đây ít nhất 2 năm thì cậu nghĩ sao | "Nếu như chúng ta phải ở lại đây ít nhất là 2 năm lận thì cậu sẽ thấy thế nào?" | thăm dò | 3 |
| 39 | P10-b | Cậu đáp ngay, không cần nghĩ | "Hà? Ai lại muốn thế chứ." | dứt khoát | 3 |
| 40 | P10-c | Fern nhẹ cả người khi nghe câu đó; ông chủ quán không hiểu cô bé bị làm sao | "Phải ha. Tất nhiên là sẽ không muốn thế rồi nhỉ." | nhẹ nhõm | 3 |
| 41 | P10-d | Cậu gục xuống quầy hoang mang; Fern kết luận hóa ra cậu cũng là người bình thường | "Hóa ra Stark-sama là một người bình thường." | hài, ấm | 2 |
| 42 | P10-e | Fern cảm ơn; cậu nhận lời giúp tìm cách vượt biên giới | "Được thôi, tôi sẽ giúp cô." | kết đồng minh | 3 |
| 43 | P10-f | Hai người bước về phía cổng thành đóng kín | — | khởi động | 1 |
| 44 | P11-a | Đứng dưới chân tường, Fern hỏi sao không bay qua | "Chúng ta không thể bay qua được sao?" | dò cách | 2 |
| 45 | P11-b | Giải thích: biên giới có **rào chắn ma phép** uy lực kéo dài tới tận mây, không bay qua được; nhưng nhờ nó mà quái vật trên không cũng không lao xuống được | "một rào chắn ma phép uy lực kéo dài đến tận đến trời mây" | thất vọng | 3 |
| 46 | P11-c | Hai người chuyển hướng: đi hỏi giới thương gia | "Chúng ta đi tra hỏi mấy thương gia nhé?" | đổi kế | 2 |
| 47 | P11-d | Ngoại cảnh dinh thự/nhà thương gia trong thị trấn | — | chuyển cảnh | 1 |
| 48 | P11-e | Trong phòng khách, một thương gia tiếp hai người | — | điều tra | 1 |
| 49 | P12-a | Kết quả các cuộc hỏi: giao thương đóng hoàn toàn, đến đoàn lữ hành có hộ tống cũng bị cấm; phương bắc đang nguy kịch | "Vậy ra giao thương ở đây đã hoàn toàn bị đóng rồi à…" | bí bách | 3 |
| 50 | P12-b | Fern không chịu dừng: đề nghị hỏi cả chợ đen lẫn đám trộm cắp | "Hãy đi tra hỏi cả người ở chợ đen lẫn mấy tên trộm cắp nữa nào." | lì | 3 |
| 51 | P12-c | Stark thấy làm vậy quá nguy hiểm | "…chẳng phải sẽ rất nguy hiểm hay sao?" | lo | 2 |
| 52 | P12-d | Stark tự trấn an: trông khỏe khoắn, lại khá giỏi lừa gạt | "tôi cũng khá giỏi khoản lừa gạt đấy nhé" | gồng | 2 |
| 53 | P12-e | Fern chốt hạ một câu về khuôn mặt cậu ta | "Chắc hẳn là do khuôn mặt sặc mùi phản diện đó ha." | hài, khô | 2 |
| 54 | P12-f | Stark cụt hứng | "Im đi." | quê | 1 |
| 55 | P12-g | Toàn cảnh khu nhà cũ nát — vùng chợ đen | — | chuyển cảnh, tối | 1 |
| 56 | P13-a | Khu chợ đen: người ngồi bệt, kẻ bán hàng che mặt, hàng hóa bày trên thùng gỗ | — | nhơ nhớp | 2 |
| 57 | P13-b | Stark kề rìu tra hỏi một gã đàn ông; Fern đứng phía sau nhìn | — | bạo lực ngầm | 3 |
| 58 | P13-c | Hai người lọt giữa đám khách lạ trong một quán đông đúc | — | lạc lõng | 2 |
| 59 | P13-d | Một đám côn đồ vác gậy lao tới; Fern vẫn đứng yên, Stark quay lại | — | nguy hiểm | 3 |
| 60 | P13-e | Hậu cảnh: hai gã say/ngã gục dưới chân tường, Fern đứng nhìn | — | lạnh | 2 |
| 61 | P13-f | Đứng trên tường thành, kết luận: **vô ích** | "Vô ích mất rồi." | kiệt sức | 3 |
| 62 | P13-g | Stark nhìn cổng thành: nơi này như một cuộc chiến phòng thủ, cổng không mở thì không đi đâu được | "Nếu cánh cổng kia mà không mở thì chúng ta cũng chẳng thể đi đâu được." | bó tay | 3 |
| 63 | P14-a | Fern rủ thử tới trạm gác, dù đã biết là vô vọng | "dù gì thì cũng vô vọng mất rồi mà?" | nản mà vẫn đi | 2 |
| 64 | P14-b | Stark im lặng nhìn cô bé, rồi hỏi lại | "…Sao thế?" | thắc mắc | 1 |
| 65 | P14-c | Fern nói cô chỉ thấy Stark đang rất chịu hợp tác | "Tôi chỉ thấy Stark-sama đang vô cùng hợp tác mà thôi." | dò xét | 2 |
| 66 | P14-d | Stark vặn lại rằng chính cô là người đề nghị, và cậu cũng chẳng muốn chờ | "Và tôi cũng chẳng muốn phải chờ đợi." | thẳng | 2 |
| 67 | P14-e | Fern nhận xét: thế này thì cậu còn tuyệt vọng hơn cả cô | "cậu tuyệt vọng hơn cả tôi nữa đấy" | sắc | 3 |
| 68 | P14-f | Trên bậc thang tường thành, Stark buông một câu bỏ lửng — cậu không có nhiều thời gian; Fern hỏi lại nghĩa là sao | "Mà, tôi cũng đâu có nhiều thời gian." | mở nút | 3 |
| 69 | P15-a | **Hồi tưởng (khung viền đen):** trên chính bức tường này, Eisen đội mũ sừng dẫn cậu bé tóc đỏ lên ngắm phương bắc | "Ta có thể thấy rõ phía bắc luôn." | ký ức | 3 |
| 70 | P15-b | Hộp dẫn: sư phụ đã dắt cậu tới đây từ khi còn nhỏ | "Sư phụ đã dắt tôi tới đây từ lúc còn nhỏ đấy." | ấm | 2 |
| 71 | P15-c | Cậu bé hỏi về chuyến hành trình; Eisen hỏi lại có muốn nghe không | "Chuyến hành trình đó ra sao vậy ạ?" / "Con muốn nghe à?" | háo hức | 3 |
| 72 | P15-d | **Eisen chỉ ra phương bắc: tổ đội anh hùng đã khởi hành từ chính nơi này** | "Tổ đội anh hùng bọn ta đã khởi hành từ đây, rồi tới các vùng phía bắc đấy." | trang trọng, **đỉnh 2** | 3 |
| 73 | P15-e | Hộp dẫn: sư phụ ít nói về bản thân, nhưng kể chuyện nhóm anh hùng thì rất hào hứng | "người lại rất hào hứng khi nói về chuyến hành trình của nhóm anh hùng" | trìu mến | 3 |
| 74 | P16-a | Cận Eisen: cả đời dài đằng đẵng, ông quý trọng mười năm phiêu lưu ấy hơn bất cứ thứ gì | "quý trọng giây phút phiêu lưu chỉ dài có một thập kỷ ấy hơn bất cứ thứ gì" | thấm, **đỉnh 2** | 3 |
| 75 | P16-b | Về hiện tại: Stark tin Frieren cũng cảm thấy y như vậy | "tôi tin chắc rằng Frieren cũng cảm thấy như vậy" | chắc chắn | 3 |
| 76 | P16-c | Cận Fern mỉm cười, thừa nhận | "Cũng phải ha." | dịu | 3 |
| 77 | P16-d | Stark: tuổi Eisen giờ không đi phiêu lưu được nữa | "tuổi của sư phụ cũng không còn khả năng đi phiêu lưu nữa rồi" | ngậm ngùi | 3 |
| 78 | P16-e | Vì thế cậu nhận trọng trách: phải hưởng trọn thú vui của chuyến đi "nhảm nhí" này rồi kể lại cho sư phụ — và chính ông bảo cậu đi theo hai người | "Để rồi truyền tải lại câu chuyện thú vị đó cho người." | sứ mệnh | 3 |
| 79 | P17-a | **Khung lớn:** Stark vác rìu quay đầu nhìn lại — đó là cách cậu báo đáp sư phụ; và **nếu cứ dừng bước thế này thì sư phụ sẽ không còn nữa** | "Bởi nếu như cứ dừng bước thế này, thì sư phụ sẽ không còn nữa mất." | cấp bách, **đỉnh 3** | 3 |
| 80 | P17-b | Cận Fern: vậy thì không thể dậm chân ở nơi này được | "chúng ta không thể dậm chân ở nơi này được nhỉ?" | quyết | 3 |
| 81 | P17-c | Fern nói thêm: cô nghĩ Frieren thì vẫn còn sống lâu lắm | "tôi nghĩ cô ấy vẫn còn khả năng sống lâu lắm" | đối chiếu hai kiểu thời gian | 3 |
| 82 | P17-d | Toàn cảnh dãy nhà trong khu thành | — | chuyển cảnh | 1 |
| 83 | P17-e | Hai người xuống tới dãy nhà | — | chuyển tiếp | 1 |
| 84 | P18-a | Frieren nấp sau góc tường, ra hiệu im lặng: **cô đang bị truy lùng** | "Bé tiếng thôi. Ta đang bị truy lùng mất rồi." | hài, báo động | 3 |
| 85 | P18-b | Fern sững người hỏi ngài làm gì ở đây | "Frieren-sama, ngài làm gì ở đây vậy ạ?" | ngơ ngác | 2 |
| 86 | P18-c | Cả ba nép trong hẻm nhìn ra | — | căng | 1 |
| 87 | P18-d | Đội trưởng cảnh vệ mặc giáp đầy đủ xuất hiện, đi cùng viên thị trấn | — | uy hiếp | 3 |
| 88 | P18-e | Cận mũ giáp — ánh mắt xoáy qua khe mũ | — | lạnh gáy | 2 |
| 89 | P18-f | Đội trưởng vung tay, cả hàng lính dàn sau lưng | — | áp đảo | 3 |
| 90 | P18-g | Giáp trụ tiến thẳng tới chỗ ba người; Stark hỏi Frieren đã làm gì, cô chối là chỉ đi ngắm cửa hàng phép thuật | "Tôi chỉ vừa mới tham quan mấy cửa hàng phép thuật thôi mà." | chột dạ, hài | 3 |
| 91 | P19-a | **Cú lật:** đội trưởng cảnh vệ quỳ rạp xuống đất xin lỗi, gọi đích danh **Frieren-sama** | "Chúng tôi thành thực xin lỗi ngài!! Frieren-sama!!" | lật, **đỉnh 4** | 3 |
| 92 | P19-b | Ông ta xin được tha thứ cho "kẻ ngu muội" | "Xin hãy tha thứ cho kẻ ngu muội này ạ!!" | cung kính thái quá | 2 |
| 93 | P19-c | Cận Frieren toát mồ hôi, thấy chuyện bắt đầu hỏng | "Vụ này bắt đầu thấy không ổn rồi à nha…" | hoảng ngầm, hài | 3 |
| 94 | P19-d | Frieren chữa cháy: không bận tâm, cảnh vệ chỉ làm nghĩa vụ | "cậu ấy chỉ đang làm nghĩa vụ của mình thôi mà" | gượng | 2 |
| 95 | P19-e | Frieren cố nói thêm là cô không gấp, còn đang tính nghỉ ngơi | "tôi cũng đang tính nghỉ ngơi chút…" | chống chế | 2 |
| 96 | P19-f | Viên thị trấn thay mặt dân chúng tạ lỗi vì đã cư xử không phải phép với cô | "tôi xin thay mặt người dân cáo lỗi trước ngài ạ" | trịnh trọng | 3 |
| 97 | P19-g | **Viên thị trấn tự suy ra động cơ:** phương bắc vẫn còn xung đột với **tàn dư quân đội của Quỷ Vương**, hẳn ngài định lên bắc lần nữa vì đau xót cho dân — tấm lòng của một anh hùng | "Tấm lòng đó quả thực là của một vị anh hùng mà." | hiểu lầm đẹp đẽ | 3 |
| 98 | P20-a | Ông nói dân phương bắc sẽ rất cảm kích, và **mời cô cứ tự do băng qua biên giới** | "ngài cứ tự do băng qua biên giới đi ạ" | mở nút | 3 |
| 99 | P20-b | Khung nhỏ: Frieren cứng đờ, không kịp cải chính | — | dở khóc dở cười | 3 |
| 100 | P20-c | **Khung lớn:** cánh hoa bay, dân chúng đứng chật hai bên, ba người đi giữa quảng trường về phía cổng thành | — | trang trọng, ngượng | 3 |
| 101 | P20-d | Toàn cảnh tường thành phía trên đám đông | — | hoành tráng | 1 |
| 102 | P20-e | Đội trưởng cảnh vệ cùng hàng lính đứng nghiêm tiễn | — | nghi lễ | 2 |
| 103 | P20-f | Fern thắc mắc sao ngay từ đầu không xưng danh Frieren cho nhanh | "Sao từ đầu chúng ta không xưng danh Frieren-sama luôn nhỉ?" | tỉnh táo | 3 |
| 104 | P20-g | Frieren: nói ra cũng vô ích thôi — kèm câu lẩm bẩm là cô còn muốn thưởng thức nữa | "Có nói ra thì cũng vô ích cả thôi." | né | 3 |
| 105 | P21-a | Cận Frieren: cô không thích cảnh được tung hô thế này | "Vả lại ta cũng không thích thế này cho lắm." | khó chịu | 3 |
| 106 | P21-b | Stark thừa nhận khung cảnh khó mà giữ bình tĩnh — nhưng nó làm cậu thấy vui | "Thế mà nó lại làm tôi thấy vui đấy." | rung động | 3 |
| 107 | P21-c | **Khung hồi tưởng (phủ tone):** cũng đám đông ấy, cũng cánh hoa ấy — hai người lớn khoác áo choàng, **một người đeo kính**, đi giữa hàng người tiễn | — | chồng lớp thời gian, **đỉnh 5** | 3 |
| 108 | P21-d | Stark nối lại: chắc sư phụ cũng mang đúng cảm xúc này khi lên phương bắc | "Đến cả sư phụ cũng mang theo cái cảm xúc này khi đến phương bắc đấy nhỉ." | thấm | 3 |
| 109 | P21-e | Cận mắt Fern — im lặng | — | lắng | 2 |
| 110 | P21-f | Frieren bật khóc nhè: cô vẫn tiếc chuyện chưa được đi lùng phép thuật; Fern lẩm bẩm ngài ấy vẫn còn bận tâm chuyện đó | "AAAAA~ cơ mà ta muốn tìm kiếm phép thuật quá đi à…" | hài, xả căng | 3 |
| 111 | P21-g | **Khung kết:** cánh cổng thành mở ra, ba người rời đám đông bước về phương bắc | "Kể cũng phải ha." | mở đường, khép chương | 3 |

---

### C. Điểm cao trào

Chương này **không có đỉnh hành động**; năm đỉnh đều là đỉnh cảm xúc, xếp theo thứ tự xuất hiện:

1. **Ly kem không hề nhỏ đi — P08-c → P08-g.** Món quà tuổi thơ bưng ra bé hơn trong trí nhớ; ông chủ quán nói thẳng "Đấy là do giờ cậu đã lớn rồi đó"; rồi cậu tóc đỏ nhớ ra bờ vai sư phụ cũng đã teo nhỏ lại lúc nào không hay. **Đây là chỗ bộ FRN đánh đúng chủ đề thời gian, hợp với giọng "kể lạnh".**
2. **Bức tường này là nơi tổ đội anh hùng khởi hành — P15-d → P16-a.** Hồi tưởng Eisen dắt cậu bé lên tường chỉ về phương bắc, nối vào câu "cả cuộc đời dài đằng đẵng, sư phụ quý trọng mười năm phiêu lưu ấy hơn bất cứ thứ gì". Nối thẳng với C1 (chuyến đi 10 năm) mà không phải nhắc lại.
3. **"Nếu cứ dừng bước thế này thì sư phụ sẽ không còn nữa mất." — P17-a.** Khung lớn, lý do thật khiến cậu sốt ruột vượt biên: **đồng hồ của cậu và của Eisen chạy nhanh hơn của Frieren.** Ngay sau đó Fern đặt cạnh câu "tôi nghĩ cô ấy vẫn còn sống lâu lắm" — hai thang thời gian va nhau trong hai khung liền.
4. **Cú lật hài — P19-a.** Toàn bộ nửa chương vật lộn tìm đường chui qua biên giới bị xóa sạch bằng một cái quỳ lạy: đội trưởng cảnh vệ nhận ra Frieren, viên thị trấn tự suy ra một động cơ anh hùng mà cô không hề có, và cổng mở. **Cú lật đổi nghĩa phần đầu: cái họ thiếu không phải phép thuật hay tiền, mà là chịu xưng tên.**
5. **Cú lật cuối / khung đóng chương — P21-c → P21-g.** Đúng cảnh dân chúng tiễn ấy được chồng lên một khung hồi tưởng cùng bố cục: đoàn người áo choàng năm xưa đi qua cùng cánh cổng. Rồi cắt phắt sang Frieren mếu máo tiếc quầy phép thuật, và cổng mở ra phương bắc. **Hai mươi tám năm sau, cùng một cánh cổng, một tổ đội khác.**

---

### D. Chưa rõ — KHÔNG đoán bừa

**1. Nhân vật MỚI, bible chưa có — cần user chốt trước khi viết lời kể:**

| Mô tả trong ảnh | Bằng chứng tên | Vấn đề cần chốt |
|---|---|---|
| Thanh niên tóc đỏ dựng, vác **rìu lớn**, áo khoác đỏ cổ đứng. Đi cùng Frieren và Fern từ đầu chương. **Là đệ tử của Eisen** (P08-f: ông chủ quán nhắc "Ngài Eisen"; P15: hồi tưởng Eisen dạy cậu). | Bản dịch in **"Stark-sama"** (P09-g, P10-d, P14-c) — Fern gọi. Dải chữ Nhật quảng cáo ở mép `P04` ghi 戦士の弟子・シュタルク ("đệ tử của chiến binh, Shutaruku"). | Bible chưa có mục này. **Chưa rõ**: tuổi, họ, ra mắt từ chương nào (C3–C11 chưa có beat sheet), đại từ người kể sẽ dùng (Himmel đã lấy "anh"). Theo luật bible thì bỏ `-sama` → **"Stark"**, nhưng cần user duyệt vì đây là tên mới. |
| **Đội trưởng cảnh vệ** — nam, giáp trụ kín mít, mũ có mào. Nghiêm khắc chặn khách, sau quỳ lạy Frieren. | Chỉ có chức danh "đội trưởng cảnh vệ". | **CHƯA RÕ tên.** Đừng đặt biệt danh. |
| **Viên thị trấn** — ông già tóc bạc buộc sau, khăn quàng cổ, áo vest. Thay mặt dân cáo lỗi và mở biên giới. | Chỉ có chức danh "viên thị trấn". | **CHƯA RÕ tên** và chưa rõ "viên thị trấn" là thị trưởng hay một chức khác. |
| **Ông chủ quán rượu** — nam, trung niên, tóc vuốt ngược, nơ cổ. **Biết Eisen** và biết Stark từ hồi bé. | Không có tên. | **CHƯA RÕ tên**, chưa rõ quen Eisen thế nào, chưa rõ có phải người trong tổ đội cũ quen biết hay không. |

**2. Chi tiết trong ảnh chưa xác định được:**

- **P21-c — khung hồi tưởng đoàn người tiễn.** Thấy rõ **một người đeo kính** (bible: Heiter là người đeo kính) và một người nữa tóc sẫm, áo choàng cổ cao. **Không đủ nét để khẳng định đó là Himmel / Heiter / Eisen / Frieren.** Không được gọi tên trong lời kể; chỉ được tả "những người đi qua cùng cánh cổng này năm xưa". Ảnh gốc 900px không cho phép phóng to xác minh.
- **P21-g — "Kể cũng phải ha."** Bong bóng nằm trong khung toàn cảnh cổng thành, **không rõ của ai** (Fern hay Frieren).
- **P05 (trang màu đôi) — dòng chữ tay nhỏ cạnh Fern: KHÔNG ĐỌC ĐƯỢC** (cỡ chữ quá nhỏ ở 900px). Chỉ đọc chắc được "Sao cũng được thôi." và "Có vẻ vui ạ.".
- **P05, P03 — khối chữ Nhật dọc không có bản dịch** (lời quảng cáo của tạp chí). Không dùng làm nguồn cho lời kể.
- **P12-b/c — thứ tự người nói.** Bố cục khung khiến không chắc 100% câu "Không. Hãy đi tra hỏi cả người ở chợ đen lẫn mấy tên trộm cắp nữa nào." là của Fern hay Stark; ngữ cảnh nghiêng về **Fern** (Stark là người phản đối vì nguy hiểm). Cần user xác nhận nếu định trích thoại này.

**3. Cốt truyện chương này nêu ra nhưng CHƯA giải thích — không được suy đoán:**

- **28 năm kể từ khi Himmel mất** (P04-a). Bible mới ghi tới mốc "20 năm sau khi Himmel qua đời" ở C2 → **cần cập nhật bible sau khi duyệt.**
- **Hẻm núi Bakur** — địa danh mới, chưa rõ nằm ở đâu so với Thánh Thành Strahl.
- **Rào chắn ma phép ở biên giới** (P11-b): ai dựng, dựng khi nào, vì sao kéo tới tận mây — truyện không nói.
- **Tàn dư quân đội của Quỷ Vương ở phương bắc** (P19-g): chỉ là lời viên thị trấn nghe nói lại, chưa lên hình.
- **"Ta đang bị truy lùng mất rồi"** (P18-a): Frieren nói mình chỉ đi ngắm cửa hàng phép thuật — **truyện không xác nhận cô có làm gì hay không.** Không được kể như thể cô có tội hay vô tội.
- **Eisen hiện ra sao:** chỉ biết qua lời Stark là "tuổi đã không còn khả năng đi phiêu lưu nữa" và lời ông chủ quán là "đã có tuổi rồi". **Không có khung nào cho thấy Eisen ở hiện tại** — cả hai khung có ông đều là hồi tưởng (P08-g, P15). Không được viết ông đang ốm hay sắp mất.
- **Vì sao Eisen bảo Stark đi theo Frieren và Fern** (P16-e) — chưa kể chi tiết; cũng chưa rõ có liên quan gì tới "chuyện nữa muốn nhờ cậu" mà Frieren nói ở C1-P35 hay không. **Không được nối hai chi tiết này.**
- **Nhóm ba người đang đi đâu / mục tiêu chuyến đi phương bắc** — chương này không nhắc lại.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** 111 panel trên 18 trang nội dung (`P04`–`P21`), mỗi dòng đều dẫn được về một khung cụ thể. Chỗ nào bác thấy sai khung, chỉ số dòng để tôi mở lại đúng trang đó.
2. **Tên nhân vật đúng chưa?** Frieren / Fern / Eisen / Himmel / Quỷ Vương lấy từ bible. **Nhân vật tóc đỏ vác rìu: bản dịch in "Stark-sama" — có chốt gọi "Stark" và bỏ `-sama` theo luật bible không, và người kể dùng đại từ gì cho cậu ta?** Ba nhân vật phụ còn lại tôi để nguyên chức danh, chưa đặt tên.
3. **Trọng số hợp lý chưa?** Tôi để TS3 dày ở hai cụm P08–P09 (ly kem) và P15–P17 (hồi tưởng Eisen + "sư phụ sẽ không còn nữa"), coi đó là xương sống cảm xúc, còn cú quỳ lạy P19 là cú lật. Nếu bác muốn video nghiêng về mạch hài (Frieren bị truy lùng) thì tôi đảo trọng số lại.

**Không tự sang `/manga-narration`.**
