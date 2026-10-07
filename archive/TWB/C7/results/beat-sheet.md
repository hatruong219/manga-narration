# BEAT SHEET — Twilight Blade C7 "Nỗi hối hận sau đó"

Nguồn ảnh: `series/TWB/C7/pages-clean/`
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **ĐỦ 21/21 trang** · 74 beat · 3 mục BỎ (banner P01, banner P20, cả trang P21)
Tên gọi & thuật ngữ bám `series/TWB/series-bible.md` (bản lập từ C1).

---

### A. Kiểm tra đầu vào

21 ảnh `TWB_C7_P01`–`P21`, đánh số liên tục, **không thiếu trang**.

Kích thước & mức cắt của `clean-pages.py` (so với `pages/`):

| Trang | Raw | Clean | Đã cắt |
|---|---|---|---|
| P01 | 822×1500 | 822×1052 | **448px mép TRÊN** |
| P02 | 822×610 | 822×610 | không cắt (trang ngắn) |
| P03–P19 | 822×1200 | 822×1200 | không cắt |
| P20 | 822×1500 | 822×1500 | không cắt |
| P21 | 822×610 | 822×582 | 28px mép DƯỚI |

**⚠ Ba cảnh báo cho khâu dựng:**

1. **P01 vẫn còn nguyên một banner quảng cáo FoxTruyen.Net** chiếm ~450px đầu trang (hình con cáo + khung "Kho Truyện Cực Lớn"). `clean-pages.py` chỉ bóc được banner thứ nhất, còn banner thứ hai nằm nguyên trong ảnh clean → **phải crop thêm ~450px mép trên P01 khi dựng.**
2. **P20 còn banner quảng cáo ở ĐÁY** (~250px, dải "HẾT TRUYỆN RỒI! — KHÁM PHÁ THÊM TẠI: FoxTruyen.Net") → phải crop mép dưới.
3. **P21 = 100% quảng cáo** (FoxTruyen.Net + TruyenQQQ.com + dàn nhân vật series khác), không có một khung truyện nào → **BỎ.**

Khác C1: chapter này **không có watermark chìm ở góc trên** các trang; chỉ có hai banner đầu/cuối nói trên.

**⚠ Bất thường về cấu trúc trang:** trang **P12** mang logo bộ truyện `あわいの焔刃` kèm dòng **"HẾT TRUYỆN"** ở đáy, nhưng truyện vẫn chạy tiếp liền mạch từ P13 đến P20 (nối thẳng cảnh Yojin bị cảnh sát dẫn đi ở P12, không có trang tiêu đề mới). Xem mục D.

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| — | P01-ad | Banner quảng cáo FoxTruyen.Net đầu trang | — | — | **BỎ** |
| 1 | P01-a | Phòng bệnh. Một người phụ nữ tóc dài vừa tỉnh, đang nhai táo, nhìn con mình mà mất một nhịp mới nhận ra. Dải tiêu đề: Chương 7 — "Nỗi hối hận sau đó". Dòng dọc lề phải ghi bà đã được giải thoát khỏi sự tẩy não sau trận chiến | "Ờ... Yamato đó hả?" | ngỡ ngàng, thiết lập | 3 |
| 2 | P01-b | Yamato (đeo kính, khăn quàng) ngồi cạnh giường; mẹ chuyển ngay sang cằn nhằn chuyện việc làm thêm của cậu | "Còn việc làm thêm thì sao?" | lải nhải, ấm | 1 |
| 3 | P02-a | Mẹ đổi mục tiêu, tra hỏi vết thương trên người con | "Vết thương kia là sao thế?!" | nghi ngờ | 2 |
| 4 | P02-b | Cận mặt mẹ, vừa nuốt vừa truy tiếp — cả bàn tay Yamato cũng băng bó | "Tay con cũng bị thương kìa!" | truy tới cùng | 2 |
| 5 | P02-c | Toàn cảnh phòng bệnh: mẹ tỉnh bơ bảo mình chỉ hơi mệt; Yamato cúi đầu, gằn lại rằng bà mới là người vừa tỉnh dậy | "Mẹ vừa mới tỉnh lại thôi đấy." | hài chua, lo | 2 |
| 6 | P03-a | Cận Yamato cúi mặt, mồ hôi chảy. Cậu bắt đầu một câu thật rồi nuốt lại giữa chừng | "Tự làm tự chịu thôi... hay đúng hơn là..." | giấu chuyện | 3 |
| 7 | P03-b | Mẹ gạt phắt, sợ con lại đi đánh nhau — **chốt tuổi Yamato: 19** | "Con đã 19 tuổi rồi đấy..." | mắng yêu | 2 |
| 8 | P03-c | Hai mẹ con cãi vụn vặt xem ai mới là người cần nghỉ ngơi; bà dúi cho cậu quả táo | "Này, ăn táo đi!" | ồn ào, thân | 1 |
| 9 | P03-d | Ngoài cửa phòng bệnh, một người đàn ông tóc sáng mặc đồ đen đang cầm điện thoại, quay lại | "Hả..." | cắt lạnh | 2 |
| 10 | P04-a | Hành lang bệnh viện. Người đó là **Yojin**; anh nhận xét mẹ Yamato trông đã khoẻ lại | "Phải nói là khoẻ quá mức luôn ấy chứ..." | nhẹ nhõm | 1 |
| 11 | P04-b | Yamato càu nhàu rằng mẹ chẳng thèm đếm xỉa đến chuyện người khác đang lo cho bà | "Chẳng thèm quan tâm đến sự lo lắng của người khác gì cả..." | dỗi | 1 |
| 12 | P04-c | Máy bán nước tự động nhả lon; Yamato hỏi việc "đưa đón" của Yojin đã xong chưa | "Ý anh 'đưa đón' là xong rồi sao?" | chuyển cảnh | 1 |
| 13 | P04-d | Ghế đá ngoài sân: Yojin đưa lon nước cho Yamato, nói mọi chuyện đã suôn sẻ. Yamato dò hỏi tên cậu bé, và chuyện hai người sống chung | "Hikari-kun đúng không?" | dò hỏi | 2 |
| 14 | P04-e | Yojin xác nhận: vừa sống chung vừa làm vệ sĩ, vì **cậu bé có thể chất rất dễ thu hút quái vật** | "Thể chất rất dễ thu hút quái vật." | tiết lộ | 3 |
| 15 | P04-f | Cận Yamato, mắt tối lại — cậu tự nối được mạch | "Thảo nào tên đó cũng nhắm vào cậu bé ấy..." | nối mạch | 3 |
| 16 | P05-a | Yojin cắt ngang dòng suy nghĩ đó bằng một câu phủ đầu | "Không phải lỗi của cậu đâu." | trấn an | 3 |
| 17 | P05-b | Yamato quay mặt đi, nói câu đang đè nặng | "Có khi tại tôi mà mẹ suýt bị giết..." | tội lỗi | 3 |
| 18 | P05-c | Khung phòng bệnh: **mẹ Yamato đã bị con quái vật thao túng ý chí**; người thường không có cách nào chống lại bọn chúng | "Bị thao túng ý chí bởi con quái vật đó." | lạnh | 3 |
| 19 | P05-d | Cận Yojin: trách nhiệm lần này hoàn toàn thuộc về anh, vì săn bọn chúng là việc của giới pháp sư | "Trách nhiệm lần này hoàn toàn thuộc về tôi." | gánh tội | 3 |
| 20 | P06-a | Yojin xin lỗi, nhắc tới vết thương trên tay Yamato | "Chắc là đau lắm nhỉ." | áy náy | 2 |
| 21 | P06-b | Yamato cúi đầu, không đáp | — | dồn nén | 2 |
| 22 | P06-c | Yojin chìa ra một thứ trong hộp nhỏ | "Tôi muốn đưa cho cậu cái này." | chuyển | 1 |
| 23 | P06-d | Cận lòng bàn tay: **một chiếc tràng hạt** | "Cái gì thế này... tràng hạt à?" | vật khoá | 3 |
| 24 | P07-a | Khung cận mặt một con quái vật đang há miệng. Lời giải thích: thứ bọn chúng thèm là **"giới lực"** — nói cách khác là linh hồn con người | "Là năng lượng của linh hồn." | rợn, lore | 3 |
| 25 | P07-b | Yojin: đeo tràng hạt vào thì quái vật khó đánh hơi được giới lực. Chú thích nhỏ ghi **chiếc còn lại là dành cho mẹ Yamato** | "Quái vật sẽ khó đánh hơi được giới lực của cậu." | lore | 3 |
| 26 | P07-c | Yojin hứa sẽ không để chuyện tương tự lặp lại; Yamato chỉ ậm ừ, không nhận lời hứa đó | "...Hừm..." | hứa hụt | 3 |
| 27 | P07-d | Yojin quay đi, dặn với lại một câu rất đời | "Hãy hoà thuận với mẹ cậu nhé." | ấm | 2 |
| 28 | P08-a | Yojin thả một con chim sẻ đeo vòng dây bện đậu trên ngón tay | "Được rồi, nhờ người nhé." | lạ, lore | 3 |
| 29 | P08-b | Cận con chim sẻ đeo vòng, mỏ há — nó là đường truyền tin của anh | "...Báo cáo đến đây là hết." | lore | 2 |
| 30 | P08-c | Yojin đứng một mình giữa bãi đất: để mục tiêu tuột khỏi tay, lại để người thường bị cuốn vào | "...Thất bại lớn rồi." | tự trách | 3 |
| 31 | P08-d | Một cái tên bật ra trong đầu anh: **"KARI KURA"** | "...'Kari Kura'..." | mở đầu mối | 3 |
| 32 | P08-e | Hồi tưởng: Yojin rút kiếm giữa mảnh vỡ bay, không tin nổi mình đã để nó chạy thoát | "Lại để nó trốn mất..." | tiếc, hận | 3 |
| 33 | P09-a | Yojin ráp mạch: kẻ đó mượn tay con quái vật để bắt cóc Hikari — nhưng có chỗ không khớp | "...Để bắt cóc Hikari-kun sao?" | suy luận | 3 |
| 34 | P09-b | Khung vệt cháy tối đặc: **chính nó là chủ nhân của "vết tay"** — nối thẳng về vết cháy hình bàn tay khổng lồ ở căn hộ Fujino (C1, P50) | "Nó chính là chủ nhân của 'vết tay' đó." | nối về C1 | 3 |
| 35 | P09-c | Hồi tưởng chung cư: cấp dưới của Yojin đã được cắt canh chừng, mà Hikari lúc đó vẫn đang ở trong nhà | "Dù đã cho cấp dưới canh chừng," | lỗ hổng | 2 |
| 36 | P09-d | Khung sinh vật đeo dây bện trắng: mục tiêu của nó là Hikari — vậy sao lúc đó nó lại xuất hiện ở nơi kia? | "Tại sao lúc đó nó lại xuất hiện ở nơi đó?" | vênh logic | 3 |
| 37 | P09-e | Yojin toát mồ hôi. Giả thuyết mới: **mục tiêu thật là chính anh, và nó định diệt luôn cả anh** | "Nếu vậy, nó định tiêu diệt luôn cả mình..." | lạnh sống lưng | 3 |
| 38 | P10-a | Tiếng hô vang "Bắt đầu thôi—". Yojin đang đứng bên ngoài hàng rào một sân trường trong giờ thể dục | "!!" | giật | 2 |
| 39 | P10-b | Trong hàng học sinh có **Hikari** | "Hikari-kun!" | khoá mục tiêu | 3 |
| 40 | P10-c | Hồi tưởng sáng nay ở cửa nhà: Hikari nói mình không sao, nên Yojin mới tạt qua quan sát | "Cháu không sao đâu ạ!" | bảo bọc | 2 |
| 41 | P10-d | Yojin vẫn thấy sắc mặt cậu bé kém, tính chuyện ép cậu nghỉ học | "Có khi nào mình nên ép cậu bé nghỉ ngơi không nhỉ..." | lo thái quá | 2 |
| 42 | P11-a | Giờ thể dục là một trận bóng. Hikari cướp được bóng; Yojin lo cậu chạy nhanh quá sẽ ngã | "Không khéo lại ngã bây giờ?!" | hài, thắt | 2 |
| 43 | P11-b | Yojin tự kìm: cứ quan sát đã, xông vào là bảo hộ quá đà | "Không, thế thì bảo hộ quá đà rồi." | tự chấn | 2 |
| 44 | P11-c | Hikari dẫn bóng qua cả hàng thủ, đám bạn reo lên | "Dẫn bóng đỉnh quá!" | sáng bừng | 2 |
| 45 | P11-d | Hikari sút tung lưới | "Vào!" | bung sáng | 3 |
| 46 | P12-a | Yojin ôm đầu, mắt trợn, hoảng vì một viễn cảnh hoàn toàn khác. Cùng lúc một viên cảnh sát vỗ vai anh | "Chẳng lẽ lại trở thành cầu thủ bóng đá?!" | hài đỉnh | 3 |
| 47 | P12-b | Yojin lắp bắp tự nhận là phụ huynh của học sinh trong trường, rồi tự chối ngay | "Tôi là... phụ huynh của học sinh ở đây..." | lúng túng | 2 |
| 48 | P12-c | Cảnh sát nói thẳng lý do: có người dân báo án **một gã đàn ông mặc đồ đen đang nhòm ngó học sinh cấp 2** | "Một gã đàn ông mặc đồ đen đang nhòm ngó các em học sinh cấp 2..." | lật góc nhìn | 3 |
| 49 | P12-d | Yojin bị mời về đồn trước ánh mắt người qua đường; Hikari chibi vẫy tay hỏi vọng theo. **Trang đóng bằng logo bộ truyện + dòng "HẾT TRUYỆN"** | "Phiền anh đi theo tôi về đồn một chuyến nhé?" | hài, kết giả | 3 |
| 50 | P13-a | Yamato lao tới quàng vai viên cảnh sát, bảo lãnh cho Yojin | "Hơn nữa còn là người quen của cháu nữa!" | cứu bồ | 3 |
| 51 | P13-b | Viên cảnh sát nhận ra Yamato ngay và hỏi thăm mẹ cậu — **hai người quen nhau từ trước** | "Hoá ra là Yamato đó hả! Lâu rồi không gặp nhé." | manh mối lai lịch | 2 |
| 52 | P13-c | Cảnh sát dặn với theo như dặn một đứa từng quậy; Yamato cười xoà. Yojin cảm ơn cậu | "Cháu không lại quậy phá gì đấy chứ?" | hé quá khứ | 3 |
| 53 | P14-a | Yamato thú nhận hồi đi học toàn cúp học, từng bị chính chú cảnh sát đó khuyên bảo mãi | "Tuy toàn cúp học là chính..." | tự giễu | 2 |
| 54 | P14-b | Yamato giải thích vì sao có mặt ở đây: nhà bố mẹ gần đó, và **chính cậu cũng từng học ở trường cấp 2 này** | "Hồi trước tôi cũng học ở trường cấp 2 này đấy." | trùng hợp | 2 |
| 55 | P14-c | Yojin để ý **Yamato chưa đeo tràng hạt** — cậu đã đưa cả hai chiếc cho mẹ | "Tôi đưa cả hai cái cho mẹ đeo rồi." | báo động ngầm | 3 |
| 56 | P14-d | Yamato ngửa bài, đây mới là lý do cậu tới | "Dạy cho tôi cách đánh bại quái vật." | xoay trục | 3 |
| 57 | P15-a | Yamato cười, trình bày cái lợi: hết sợ, lại bảo vệ được mẹ | "Một mũi tên trúng hai đích luôn!" | hăm hở | 2 |
| 58 | P15-b | Cận mắt Yojin, hai chữ cắt ngang | "Không được." | chặn đứng | 3 |
| 59 | P15-c | Yojin dội nước lạnh: biết cách đánh bại cũng chưa chắc giữ được mạng | "...Cũng chưa chắc cậu sẽ không bị yêu quái giết chết." | lạnh | 3 |
| 60 | P16-a | Yamato gân cổ cãi lại, cả khuôn mặt chiếm trọn khung | "Anh đã cứu chúng tôi mà!" | bật lại | 3 |
| 61 | P16-b | Hồi tưởng tấm lưng Yojin cầm kiếm giữa mảnh vỡ | "Là nhờ có anh đã chiến đấu bảo vệ chúng tôi!" | biết ơn | 2 |
| 62 | P16-c | Nếu hôm đó cứ để nguyên, hai mẹ con đã bị tên đó ăn thịt | "Cả tôi và mẹ đều đã bị tên đó ăn thịt rồi." | ghi nợ | 3 |
| 63 | P17-a | Yamato hét, nước mắt trào, bác thẳng cách Yojin nhận tội | "Anh nói tất cả là trách nhiệm của anh, nhưng tôi thì không muốn nghĩ như vậy!" | vỡ | 3 |
| 64 | P17-b | **CÚ LẬT. Hồi tưởng: giữa những cánh tay quái vật, chính Yamato đã chỉ đường — dù bị đe doạ, cậu vẫn tiếp tay cho nó, và không hề nghĩ nó sẽ làm gì với "đứa trẻ bị bắt đi"** | "Thì chính tôi cũng đã tiếp tay cho nó." | tự tố | 3 |
| 65 | P17-c | Hồi tưởng xa hơn: Yamato cúi gằm ở đồn công an bên cạnh mẹ. Từ xưa cậu đã toàn làm trò ngốc nghếch và đổ rắc rối lên đầu bà | "Từ xưa tôi đã thế rồi..." | gốc rễ | 3 |
| 66 | P18-a | Yamato nói ra điều duy nhất cậu chắc chắn — đúng nhan đề chương | "Tôi không muốn trốn tránh nỗi hối hận này!" | đỉnh cảm xúc | 3 |
| 67 | P18-b | Yamato cúi gập người trước mặt Yojin | "Làm ơn hãy giúp tôi...!!" | dứt khoát | 3 |
| 68 | P18-c | Yojin đứng yên, rồi đáp gọn | "...Tôi hiểu rồi." | ngã ngũ | 3 |
| 69 | P19-a | Yojin thở dài thườn thượt, mặt méo đi | "Đúng là như thế thật nhỉ...... haizz..." | xả căng | 2 |
| 70 | P19-b | Yojin nói vì sao anh gật: ý chí của Yamato, và cả nỗi hối hận của cậu, anh hiểu rất rõ | "Và cả nỗi hối hận của cậu nữa... tôi hiểu rất rõ." | đồng bệnh | 3 |
| 71 | P19-c | Yamato vẫn gân lên thuyết phục, không nhận ra Yojin đã đồng ý từ lúc nào | "Tôi hiểu mà." | hài | 1 |
| 72 | P20-a | Yojin nói thẳng lý do thật: có nói gì thì Yamato cũng sẽ không bỏ cuộc | "Dù tôi có nói gì đi nữa thì cậu cũng sẽ không bỏ cuộc đâu nhỉ." | chấp nhận | 3 |
| 73 | P20-b | Yojin cười, giao kèo kèm cảnh báo cuối | "Cố mà dốc hết sức sống chết mà làm nhé." | giao kèo | 3 |
| 74 | P20-c | **Máy quay kéo ra: suốt cuộc nói chuyện đó, cả hai đang nấp sau hàng rào sân trường, rình Hikari.** Yamato bật ngửa, Yojin suỵt bắt cậu im. Dòng chữ lề: "sự kính trọng và một chút cảm giác kỳ lạ...?" | "Anh thực sự rình coi người ta đấy à?!" | hài, lật khung | 3 |
| — | P20-ad | Banner quảng cáo FoxTruyen.Net ở đáy trang | — | — | **BỎ** |
| — | P21 | Trang quảng cáo toàn phần (FoxTruyen.Net + TruyenQQQ.com) | — | — | **BỎ** |

---

### C. Điểm cao trào

Chapter này có **bốn đỉnh khác loại**, và một trong số đó đọc ngược lại toàn bộ phần đầu.

**1. Đỉnh lore — P08-d → P09-e (kẻ đứng sau lộ mặt một nửa).**
Cái tên **"Kari Kura"** bật ra ở P08-d, rồi P09-b chốt: chính nó là chủ nhân của **"vết tay"** — tức vết cháy hình bàn tay khổng lồ ở căn hộ Fujino trong C1. Từ đó C7 kéo mạch sang một chỗ hoàn toàn mới ở P09-e: Yojin ngờ rằng mục tiêu thật của kẻ địch không phải Hikari mà là **chính anh**, và Hikari chỉ là mồi. Đây là dữ kiện mới nặng nhất của chapter.

**2. Đỉnh hài — P12 (cả trang).**
Yojin lo Hikari ngã, lo Hikari ốm, lo cả chuyện Hikari sẽ thành cầu thủ bóng đá — rồi bị cảnh sát mời về đồn vì có người báo án "gã đàn ông mặc đồ đen nhòm ngó học sinh cấp 2". Trang tự đóng lại bằng logo và dòng **"HẾT TRUYỆN"**, một cái kết giả để cắt nhịp.

**3. Đỉnh cảm xúc — P17-b → P18 (và đây là cú lật thật).**
P17-b lật ngửa ván bài: **chính Yamato, dù bị đe doạ, đã tiếp tay cho con quái vật, và chẳng hề nghĩ nó sẽ làm gì với đứa trẻ bị bắt đi.** Cú lật này đổi nghĩa toàn bộ nửa đầu chapter:
- P03-a, câu Yamato nuốt lại giữa chừng — "tự làm tự chịu thôi... hay đúng hơn là..." — hoá ra là một lời thú tội bị chặn ngang.
- P05-a, "**không phải lỗi của cậu đâu**", và P05-d, "**trách nhiệm lần này hoàn toàn thuộc về tôi**": Yojin đang gánh tội thay cho một người thật sự có phần lỗi. Đọc lại thì hai câu an ủi ấy mang hai nghĩa cùng lúc — hoặc anh chưa biết, hoặc anh biết và vẫn chọn nói thế.
- P07-c, Yamato **không nhận lời hứa** của Yojin mà chỉ ậm ừ; và P14-c, cậu **đưa cả hai chiếc tràng hạt cho mẹ, không giữ chiếc nào**. Cả hai chi tiết ban đầu trông như khiêm nhường, sau P17-b thì đọc ra là một người tự thấy mình không xứng được bảo vệ.
Từ đó P18 mới đủ nặng: cậu không xin được tha, cậu xin được **không trốn nỗi hối hận này** — đúng nhan đề chương.

**4. Cú lật khung cuối — P20-c.**
Khung cuối kéo máy quay ra: toàn bộ cuộc đối thoại nghiêm trọng vừa rồi diễn ra khi hai người đang **nấp sau hàng rào sân trường rình Hikari**. Nó không đổi nghĩa cốt truyện, nhưng đổi hẳn tông của cả đoạn P14–P20 và là cú đóng chapter.

**Trục nên dùng khi viết lời kể:** một người xin được dạy cách chiến đấu, một người nhận trách nhiệm về mình — và cả hai đều đang giấu phần của mình trong cùng một vụ.

---

### D. Chưa rõ

**Về đầu vào / bối cảnh series**
- **Chưa đọc C2–C6.** `tracker.csv` mới đánh dấu C1, và `series-bible.md` ghi rõ là bản lập từ chapter 1. Beat sheet này dựng từ C1 + C7, nên mọi thứ xảy ra giữa hai mốc đó đều **chưa xác minh**: Yojin và Yamato quen nhau từ đâu, trận chiến khiến mẹ Yamato bị thao túng diễn ra ở chapter nào, Yamato bị ai đe doạ.
- **P12 mang logo bộ truyện + "HẾT TRUYỆN" nhưng truyện chạy tiếp tới P20.** Chưa rõ đây là gag "kết giả" của chính tác giả hay bản up đã ghép chương 7 với một phần ngoại truyện. Không có trang tiêu đề thứ hai để phân định. **Cần user xác nhận trước khi chia video.**

**Về nhân vật**
- **Yamato**: chưa thấy họ. Chưa rõ cậu xuất hiện lần đầu ở chapter nào.
- **Mẹ Yamato**: chưa có tên. Chưa rõ bà còn nhớ gì về quãng bị thao túng ý chí.
- **Viên cảnh sát**: chưa có tên; quen Yamato từ hồi cậu còn đi học nhưng chưa rõ ở mức nào.
- **"Đứa trẻ bị bắt đi" ở P17-b**: khung chỉ nói "đứa trẻ", không gọi tên. **Chưa rõ có phải Hikari hay không** — không được suy ra.
- **Yojin có biết Yamato đã tiếp tay không, và biết từ lúc nào**: C7 không nói. Ở P05 anh nói "không phải lỗi của cậu đâu" trước khi Yamato thú nhận ở P17, nhưng chapter không xác nhận anh biết hay không biết.

**Về thuật ngữ — có 3 chỗ vênh với `series-bible.md`, cần user chốt, tôi không tự đổi**
- Bản dịch C7 gọi lũ sinh vật là **"quái vật"** (P04, P05, P07, P14) và một lần **"yêu quái"** (P15-c). Series bible đã chốt dùng **"oán hồn"**. Chưa xác minh đây có cùng một loại sinh vật với C1 hay không.
- P05-d dịch nghề của Yojin là **"pháp sư ngoại đạo"**; series bible chốt **"pháp sư trừ tà"** (theo C1, P34). Cùng một nghề hay hai khái niệm khác nhau — chưa rõ.
- **"Giới lực"** (P07-a, P07-b) là thuật ngữ mới, chưa có trong bible. C7 giải thích là "năng lượng của linh hồn", nhưng chưa rõ chữ gốc và quan hệ với "thể chất đặc biệt" của Hikari.

**Về chi tiết trong khung**
- **"Kari Kura"** (P08-d): mới chỉ là một cái tên bật ra trong đầu Yojin. Chưa rõ là người, là oán hồn, hay là tên một tổ chức. **Không được đoán.**
- Con chim sẻ đeo vòng dây bện (P08-a, P08-b): chưa rõ là thức thần hay vật thường, và chưa rõ nó báo cáo **về cho ai** — vẫn đúng với ghi chú "không được bịa tên tổ chức" trong bible.
- Tràng hạt (P06-d): chưa rõ ai làm ra, và ngoài việc che giới lực thì còn tác dụng gì.
- Sinh vật đeo dây bện trắng ở P09-d: chưa rõ có phải Kari Kura, hay chỉ là con quái vật mà nó sai khiến.
- Khung nhỏ ba bóng người ở P04 (giữa dưới): chưa rõ là hồi tưởng hay khung minh hoạ; chữ trong khung quá nhỏ, **KHÔNG ĐỌC ĐƯỢC** phần chú thích.
- P12-c cho biết Hikari học **cấp 2**; bible mới chỉ ghi "học sinh". Nên cập nhật khi user duyệt.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** — Đặc biệt xin soát lại beat 64 (P17-b): tôi đọc khung đó là Yamato thừa nhận chính cậu đã tiếp tay cho con quái vật và không nghĩ tới đứa trẻ bị bắt đi. Nếu đọc sai chỗ này thì toàn bộ mục C sụp.
2. **Tên nhân vật đúng chưa?** — `Yojin` và `Hikari` lấy từ series bible. `Yamato` và mẹ cậu là nhân vật chưa có trong bible (xuất hiện ở C2–C6 mà mình chưa đọc); anh/chị xác nhận cách gọi giúp.
3. **Trọng số hợp lý chưa?** — Tôi để 3 điểm TS=3 cụm dày nhất ở P08–P09 (lore Kari Kura), P17–P18 (thú tội) và P20-c (lật khung). Nếu video 180 giây muốn nghiêng hẳn về mạch cảm xúc thì nên hạ cụm P08–P09 xuống 2.

**Chưa sang `/manga-narration`.**
