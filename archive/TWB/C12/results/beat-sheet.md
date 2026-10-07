# BEAT SHEET — TWB Chương 12: "Nơi phát ra tiếng nói"

Bộ: Twilight Blade (あわいの焔刃) · Chương 12 · đăng 10/09/2026
Nguồn đọc: `series/TWB/C12/pages-clean/` (23 ảnh) · Đọc đủ P01→P23, không nhảy trang.
Trạng thái: **CHƯA viết lời kể.** Dừng chờ duyệt.

---

### A. Kiểm tra đầu vào

**Ảnh đã nhận:** 23 file liên tiếp `TWB_C12_P01.jpg` → `TWB_C12_P23.jpg`. **Không thiếu trang.**
Kích thước gốc đồng nhất 822px chiều ngang.

**clean-pages đã cắt bao nhiêu px** (so `pages/` với `pages-clean/`):

| Trang | Gốc (W×H) | Sau clean | Cắt |
|---|---|---|---|
| P01 | 822×1500 | 822×1052 | **−448 px** |
| P02 | 822×1500 | 822×1470 | −30 px |
| P03–P21 | 822×770 / 1200 / 1500 | không đổi | 0 px |
| P22 | 822×1500 | 822×1470 | −30 px |
| P23 | 822×770 | 822×742 | −28 px |

**CẢNH BÁO — clean-pages chưa làm sạch hết. 3 trang là quảng cáo, 1 trang lẫn quảng cáo:**

- **P01 — BỎ.** Toàn bộ là ảnh quảng cáo một bộ manhwa màu khác + banner "NetTruyen12s.com". Không có nội dung chương.
- **P02 — DÙNG MỘT PHẦN.** ~68% phía trên là ảnh chụp fanpage Facebook + banner "NetTruyen13s.com" → bỏ. ~32% phía dưới **là trang mở chương thật**: logo tựa gốc あわいの焔刃, lời dẫn của biên tập và 2 bóng thoại đầu tiên. Khi dựng phải crop lấy phần dưới.
- **P22 — BỎ.** 100% ảnh chụp fanpage + banner quảng cáo.
- **P23 — BỎ.** 100% banner "NetTruyen12s.com" / "TruyenQQQ.com" + ảnh ghép nhân vật các bộ khác.

→ **20 trang có nội dung** (P02 phần dưới + P03→P21). **Đề nghị chạy lại `clean-pages.py` với ngưỡng mạnh hơn cho P01/P02/P22/P23 trước khi sang bước dựng.**

**Ghi chú đọc:** trang đọc theo chiều **phải → trái** (manga Nhật). Panel đánh số theo đúng thứ tự đọc đó.

**Ghi chú nghiêm trọng về series-bible:** bible hiện chỉ lập từ **C1**, và **C2→C11 chưa có beat sheet nào** trong repo. C12 xài dày đặc tên riêng và thuật ngữ không có trong bible (Yatsuha, Karikura, Ma Duyên, Akitsugu, giới lực, ngoại pháp sư, Linh Nghiệm, Khắc Viêm, Bá Pháp…). Toàn bộ đã đưa xuống mục D, **không tự đặt tên và không tự dịch khác**.

**Tên đã chốt ở bible và dùng lại nguyên trong beat sheet này:** **Yojin** (Yojin Odaki), **Hikari** (Hikari Fujino), **oán hồn**, **pháp sư trừ tà**, **thể chất đặc biệt**.

---

### B. Beat Sheet

**73 panel / 20 trang nội dung.**

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P02-a | Trang mở chương. Logo tựa gốc. Một bóng người tóc dài trắng đứng quay lưng trong rừng; lời dẫn biên tập báo có địch lạ. Hai bóng thoại của Yojin & Yatsuha vọng ra từ chỗ tối. | "Sử giả của Karikura...!" | ngợp, báo động | 3 |
| 2 | P03-a | Toàn cảnh: người tóc trắng dài, bàn tay đen vuốt nhọn. Yojin (áo khoác đen dài, cầm kiếm) và Yatsuha (áo khoác sáng) đứng thủ thế cách đó một quãng. Hộp tựa chương. | *(hộp tựa)* "Chương 12 — Nơi phát ra tiếng nói" | căng, mở màn | 3 |
| 3 | P03-b | Cận mặt Yojin — nhận ra thứ trước mặt không phải người. | "Người này... là yêu quái sao?!" | choáng | 2 |
| 4 | P03-c | Cận Yatsuha — thấy vô lý ở hai điểm: giờ giấc và hình dáng. | "Vẫn chưa đến giờ hoàng hôn, quá sớm đấy!" | ngờ vực | 2 |
| 5 | P03-d | Đối phương buông một tiếng cười nhẹ; nhận xét nó khác hẳn mọi thứ hai người từng gặp. | "Chà..." | lạnh, trịch thượng | 2 |
| 6 | P04-a | Người phụ nữ hiện rõ: tóc dài sáng, dấu chữ X trên trán, hai bàn tay hoá vuốt đen — nhưng giơ tay lên như đầu hàng và cười. | "Tôi không có ý định chiến đấu với các người đâu." | ngọt, sai chỗ | 3 |
| 7 | P04-b | Yojin và Yatsuha im lặng, không hạ vũ khí. Cô ta tự nhận phe mình. | "Bởi vì tôi thuộc phe ôn hoà mà." | nghi | 2 |
| 8 | P04-c | Yatsuha rút kiếm, bác thẳng — cô ta là thuộc hạ của "Ma Duyên". | "Kẻ thuộc hạ của 'Ma Duyên' mà lại bảo là ôn hoà?" | gắt, dứt khoát | 3 |
| 9 | P04-d | Khung chibi chèn: cô ta lại "Chà..." — không hề nao núng. | "Chà..." | tỉnh bơ | 1 |
| 10 | P05-a | Cận mặt cô ta, tay vuốt đen giơ ngang. Xác nhận Yatsuha đoán đúng, rồi nói về "ngài ấy" bằng giọng sùng bái. | "Việc ngài ấy là một tồn tại vĩ đại..." | sùng tín | 3 |
| 11 | P05-b | Yatsuha chốt lại điều vừa nghe. | "Vậy điều đó là đúng!" | căng | 2 |
| 12 | P05-c | Yojin ghì chuôi kiếm, nghe cô ta khẳng định mình không nói dối. | "...hoàn toàn không phải là dối trá đâu." | dè chừng | 2 |
| 13 | P05-d | Toàn cảnh: cô ta lơ lửng trên cao, hai người đứng dưới. Cô ta khai mình sinh ra vốn là thuộc hạ của Karikura. | "Tôi được sinh ra như một thuộc hạ của ngài Karikura." | phơi bài | 3 |
| 14 | P05-e | Cận mắt — một trong hai bắt được chữ "mệnh lệnh". | "...mệnh lệnh sao?" | bắt tín hiệu | 2 |
| 15 | P05-f | Cận vuốt đen. Câu bỏ lửng "trước đó thì..." | "Trước đó thì..." | gợn | 1 |
| 16 | P06-a | Hai khung nhỏ: mặt cô ta, và lưng Yojin — khoảnh khắc trước cú ra tay. | — | nín | 2 |
| 17 | P06-b | **Cô ta ra đòn trước.** Tóc dài quét như roi, Yojin dính đòn ở cự ly gần, Yatsuha bị hất văng sang phía bên kia khung. | *(hiệu ứng)* | vỡ trận | 3 |
| 18 | P06-c | Cận mắt Yojin — hét tên đồng đội. | "Yatsuha!" | hoảng | 3 |
| 19 | P06-d | Cô ta bình thản giải thích vì sao gạt Yatsuha ra: vướng. | "Vị này hơi cản trở một chút nhỉ." | lạnh, khinh | 3 |
| 20 | P07-a | Cô ta ghì chặt Yojin xuống bằng tóc và thân mình, ra lệnh anh đừng vùng vẫy. | "Đừng cựa quậy..." | đè nén | 3 |
| 21 | P07-b | Khung cận: tay Yojin vẫn nắm kiếm nhưng bị chặn. | — | bất lực | 2 |
| 22 | P07-c | Vuốt đen bổ xuống đất bên cạnh anh — đe doạ chứ không giết. | *(hiệu ứng)* | hăm doạ | 2 |
| 23 | P07-d | **Cô ta ngắm mặt Yojin và khen** — tóc vàng óng và mắt màu ngọn lửa. Giọng như đang tán tỉnh. | "Đẹp thật đấy." | lệch lạc, rợn | 3 |
| 24 | P07-e | Cô ta ngỏ lời muốn thân thiết, muốn nói chuyện — trong lúc vẫn đang đè anh. | "Anh có muốn nói chuyện với tôi không?" | rợn, dịu giọng | 3 |
| 25 | P08-a | Khung lớn: một **khuôn mặt quỷ tối sầm, răng nhe, mắt trắng** trồi lên ngay sau lưng cô ta. Cô ta chưa kịp quay đầu. | — | đột ngột, sát khí | 3 |
| 26 | P08-b | Cận: mắt xoáy của thứ vừa hiện ra, và mặt cô ta trợn lên. Một câu hai chữ. | "Buông... ra..." | lạnh gáy | 3 |
| 27 | P09-a | Nắm đấm lao tới — khung "!!". | *(hiệu ứng)* "!!" | bùng | 3 |
| 28 | P09-b | Cận mặt cô ta: mắt mở trắng dã, phần dưới mặt bị che như mang mặt nạ — lần đầu cô ta mất bình tĩnh. | — | choáng thật sự | 3 |
| 29 | P09-c | Cú va chạm nổ tung khung hình. | *(hiệu ứng)* | vỡ | 2 |
| 30 | P10-a | **Nguyên trang: một nhát chém xé ngang cả thung lũng rừng núi.** | *(hiệu ứng)* | choáng ngợp | 3 |
| 31 | P10-b | Bóng người cầm kiếm đứng giữa hố vừa tạo ra. | *(hiệu ứng)* | ngạo | 3 |
| 32 | P11-a | Yojin ngồi dậy, mắt trợn, gọi tên. | "Yatsu..." | sững | 2 |
| 33 | P11-b | Cận tay nắm chuôi kiếm. | — | siết | 1 |
| 34 | P11-c | Chỗ cô ta đứng chỉ còn một vũng xoáy như chất lỏng đang cuộn. | *(hiệu ứng)* | bất thường | 3 |
| 35 | P11-d | Cận Yatsuha: mặt lạnh, mắt không rời vũng xoáy. | — | lạnh, chưa xong | 2 |
| 36 | P12-a | **Cô ta tái tạo nguyên vẹn từ vũng chất lỏng** — không một vết thương — và tỏ ra ngạc nhiên vì Yatsuha nổi giận. | "Tại sao anh lại tức giận chứ?" | vô cảm, ngây | 3 |
| 37 | P12-b | Cận Yatsuha nghe câu "tôi có làm tổn thương anh đâu". | "...tôi đâu có làm tổn thương anh đâu..." | ghê tởm | 3 |
| 38 | P13-a | **Yojin bước lên, tự đặt mình làm mục tiêu**: nếu Karikura nhắm Hikari thì người cản đường lớn nhất là anh. | "Nếu mục đích của Karikura là Hikari-kun..." | quyết, gánh | 3 |
| 39 | P13-b | Yojin hỏi thẳng: vậy mục tiêu của cô là tôi, đúng không. | "...mục tiêu của cô là tôi đúng không?" | dồn | 3 |
| 40 | P13-c | **Yojin bùng lửa** — tóc hoá ngọn lửa, thân người phủ hoa văn đen. Anh gào đòi cô ta chỉ đánh mình anh. | "Đừng có đụng vào những người khác...!" | bùng nổ, bi | 3 |
| 41 | P13-d | Khung nhỏ: cô ta lùi lại, xin anh bình tĩnh, câu nói bị cắt ngang. | "Ô... xin hãy bình tĩnh lại...!" | lùi bước | 2 |
| 42 | P14-a | Một thân người bị đá/thổi bay lên trời trong quầng nổ. | *(hiệu ứng)* | văng | 3 |
| 43 | P14-b | Cận mặt cô ta đang gào — lần đầu mất hẳn vẻ nhã nhặn. | — | cuống | 2 |
| 44 | P14-c | Cô ta đứng dậy, ấn một dấu sáng, **xướng tên thuật**. | "Linh Nghiệm (Reigen)... phát động!" | lật thế | 3 |
| 45 | P15-a | **Nguyên trang: vụ nổ khổng lồ xé toang vách đá, một người bị hất bay trong đó.** Tên thuật đề bên phải. | "Khắc Viêm (Haramitsu)!!" | cao trào cháy | 3 |
| 46 | P16-a | Sau vụ nổ: cô ta với hai vuốt đen đứng giữa bãi đất cháy, xa xa còn một bóng người đứng vững. | — | tàn cuộc | 2 |
| 47 | P16-b | Cận mắt cô ta. | "Chà..." | bất ngờ | 2 |
| 48 | P16-c | **Yojin và Yatsuha đứng lại được.** Yatsuha chống kiếm, nói tỉnh bơ rằng mình chỉ định đánh cho cô ta ngất chứ không định đá văng đi. | "Tôi định đánh cho cô ngất đi thôi..." | tỉnh bơ, mạnh | 3 |
| 49 | P17-a | Cô ta soi thanh kiếm của Yatsuha, gọi đúng tên cơ chế: truyền "giới lực" vào vũ khí để biến hoá nó — **vũ khí của "ngoại pháp sư"**. | "Đây là vũ khí của ngoại pháp sư nhỉ." | đọc vị | 3 |
| 50 | P17-b | Cô ta giật mình "!" rồi lại "Chà..." | "Chà..." | hụt nhịp | 1 |
| 51 | P17-c | Yatsuha quát Yojin đừng ồn, địch vẫn còn; Yojin mừng vì Yatsuha còn sống. | "Yatsuha! May quá..." | nhẹ nhõm | 2 |
| 52 | P18-a | Cô ta nghe được tên Yojin và khen tên hay — vẫn đang chơi trò thân thiện. | "Yojin-sama sao! Tên hay thật đấy." | rợn, nhởn nhơ | 2 |
| 53 | P18-b | Bị hỏi ngược "chẳng lẽ cô sợ bị bỏ lại một mình sao?", cô ta **tiết lộ: ở phía bên kia cô ta đã cử một kẻ hầu cận tới rồi.** | "...tôi cũng đã gửi kẻ hầu cận tới rồi nên..." | **CÚ LẬT 1** | 3 |
| 54 | P18-c | Cận mắt cô ta. **"Hikari-sama cũng đang ở cùng cậu ta đấy."** — toàn bộ trận đánh vừa rồi là câu giờ. | "Hikari-sama cũng đang ở cùng cậu ta đấy." | **CÚ LẬT 1 — chốt** | 3 |
| 55 | P18-d | **Cắt cảnh sang phố xá đông người.** Một gã cơ bắp, tóc dựng, đứng quay lưng giữa đám đông dân thường. Một người tóc đen bật lên "Cái gì cơ...!?" | "Cái gì cơ...!?" | lạnh sống lưng | 3 |
| 56 | P19-a | Gã nhe nanh cười lớn, có con mắt thứ ba trên trán; hắn thấy "tình trạng bất thường" và phấn khích. | "Nhiệt huyết sôi trào rồi đây!!" | điên, hưng phấn | 3 |
| 57 | P19-b | Đám đông nhốn nháo: "cô đó đang chảy máu kìa!" | "Cô đó đang chảy máu kìa!" | hoảng loạn | 2 |
| 58 | P19-c | Một người dân chỉ trỏ, không hiểu đang nhìn thấy gì. | "Cái gì vậy người kia...!?" | hoang mang | 2 |
| 59 | P19-d | **Người tóc đen nhận ra điều bất thường nhất: người thường lại NHÌN THẤY được hắn.** | "Sao người thường lại thấy hắn được cơ chứ?!" | báo động đỏ | 3 |
| 60 | P19-e | Người tóc đen giơ tay, quyết chặn hắn ngay tại chỗ, xướng thuật. | "Bá Pháp (Kenhou)–" | quyết | 3 |
| 61 | P19-f | Mặt gã kia biến thành mặt quỷ, đòi đánh tử chiến. | "Chiến đấu tới chết!" | khát máu | 3 |
| 62 | P19-g | Khung chibi: hắn chợt sợ bị mắng nếu lơ là mệnh lệnh — nhắc tên **Akitsugu**. | "...thì Akitsugu sẽ cằn nhằn lắm đây..." | hài, hé lộ | 2 |
| 63 | P20-a | Đám đông dạt ra, có người ngã. | — | tán loạn | 1 |
| 64 | P20-b | Gã kia bật nhảy giữa sảnh gạch. | — | lao tới | 2 |
| 65 | P20-c | Một cú đấm vung ra chặn hắn. | — | va chạm | 2 |
| 66 | P20-d | Người dân bị hất ngã. | — | vạ lây | 1 |
| 67 | P20-e | Cận người tóc đen đang gào, tay che miệng. | — | cấp bách | 2 |
| 68 | P20-f | **Chữ khổng lồ xé dọc trang: "HIKARIIII!!!" / "MÀY Ở ĐÂU RỒIIII~~~!!!"** — hắn gọi thẳng tên Hikari giữa chỗ đông người. | "Hikariiii! Mày ở đâu rồiiii!!!" | **CÚ LẬT 2** | 3 |
| 69 | P21-a | Dải khung ngang: đám đông ngoái lại, vài gương mặt học sinh trong đó. | — | nghi hoặc | 2 |
| 70 | P21-b | Gã kia và một bóng người đứng đối mặt trên nền gạch — nhìn từ sau gáy một người tóc đen. | — | dồn tới | 2 |
| 71 | P21-c | Cận gáy tóc đen dựng — người vừa nghe thấy tên mình. | — | đứng hình | 3 |
| 72 | P21-d | **Khung lớn cuối chương: Hikari quay đầu lại, mắt mở to.** Cậu đang ở ngay giữa đám đông đó. | "...Hả?" | **ĐỈNH — cú lật cuối** | 3 |
| 73 | P21-e | Dòng chữ Nhật cuối trang: "Thời khắc chạm mặt đã ở ngay trước mắt…!! Kỳ sau đăng 23/9 (thứ Tư)!!" | *(caption biên tập)* | treo | 2 |

---

### C. Điểm cao trào

Chương có **bốn đỉnh**, và đỉnh cuối đổi nghĩa toàn bộ phần đầu.

**1. Đỉnh cảm xúc — P07-d/P07-e: "Đẹp thật đấy."**
Đối thủ ghì Yojin xuống rồi… khen mắt anh và rủ anh nói chuyện. Cái rợn ở đây không đến từ đòn đánh mà từ giọng điệu sai chỗ. Đây là panel định nghĩa nhân vật nữ này.

**2. Đỉnh hành động — P09→P10→P15: ba nhịp nổ liên tiếp.**
Cú đấm của Yatsuha (P09) → nhát chém xé cả thung lũng nguyên trang (P10) → và đòn trả "**Khắc Viêm (Haramitsu)**" nguyên trang của cô ta (P15). Ba panel full-page nằm sát nhau — nhịp mạnh nhất chương về mặt hình.

**3. Đỉnh nghĩa — P13-c: Yojin bốc lửa, gào "đừng đụng vào những người khác".**
Yojin tự đặt mình làm mồi để kéo địch khỏi Hikari. Đây là đỉnh đạo đức của nhân vật — và chính là chỗ cú lật cuối đâm vào.

**4. CÚ LẬT — P18-b/c, đóng đinh ở P20-f và P21-d.**
Cô ta nói "tôi thuộc phe ôn hoà", "tôi không có ý định chiến đấu" ngay từ P04 — và **cô ta không nói dối**. Cô ta chưa từng định thắng trận này. Cô ta đang **giữ chân** Yojin và Yatsuha trong rừng, trong lúc một kẻ hầu cận khác của Karikura đã ở sẵn ngoài phố cùng Hikari.

**Đọc lại thì đổi nghĩa toàn bộ phần đầu:**
- "Tôi không có ý định chiến đấu với các người đâu" (P04) — không phải lời dụ, là **mô tả đúng nhiệm vụ**: nhiệm vụ của cô ta là cầm chân, không phải giết.
- Mọi lần cô ta dừng tay, "Chà...", xin Yojin bình tĩnh, khen tên anh, rủ anh nói chuyện — **đều là câu giờ**.
- Câu nặng nhất của Yojin, "chỉ nhắm vào một mình tôi mà tới đây, đừng đụng vào những người khác" (P13-c), **đã sai từ lúc anh nói ra**. Anh đang chắn một cánh cửa mà địch không hề định đi qua.
- Trận đánh càng dữ, càng dài, thì cô ta **càng thắng**.

Đỉnh cuối là hình, không phải lời: gã kia gào tên Hikari giữa phố (P20-f) — và trang cuối, Hikari quay đầu lại (P21-d). Chương dừng đúng ở khoảnh khắc trước khi chạm mặt.

---

### D. Chưa rõ

**Không đoán, không bịa. Cần user chốt trước khi viết lời kể.**

**Tên nhân vật / thực thể chưa có trong series-bible:**

1. **Yatsuha** — đồng đội của Yojin, tóc ngắn, áo khoác sáng, dùng kiếm Nhật. Tên lấy từ chính thoại: Yojin gọi "Yatsuha!" (P06-c, P17-c) và Yatsuha gọi lại "đừng ầm ĩ nữa, Yojin!" (P17-c). **Giới tính: nam** (P12-a đối phương xưng "anh" với người này). Quan hệ với Yojin, vai trong tổ chức, xuất hiện từ chương nào — **chưa rõ**. Cách đọc TTS cho "Yatsuha" **chưa có trong `tts-pronounce.tsv`**.
2. **Nữ địch của chương — CHƯA CÓ TÊN.** Suốt 19 trang không ai gọi tên cô ta. Nhận dạng: nữ, tóc dài sáng, dấu chữ X trên trán, khuyên tròn, hai bàn tay hoá vuốt đen, thân thể tái tạo được từ chất lỏng (P11-c → P12-a). Tự nhận là "thuộc hạ của ngài Karikura", "phe ôn hoà". **Không được đặt tên thay.**
3. **Karikura** — nhân vật được nhắc tên nhiều nhất nhưng **chưa từng lên hình**. Được gọi là "ngài Karikura", "một tồn tại vĩ đại". P02 gọi nữ địch là "sử giả của Karikura". Là người ra mệnh lệnh nhắm vào Hikari. Quan hệ giữa Karikura và **oán hồn** (từ chuẩn của bible) — **chưa rõ**, chưa có panel nào nối hai thứ này.
4. **"Ma Duyên"** — Yatsuha nói cô ta là "kẻ thuộc hạ của 'Ma Duyên'" (P04-c), có dấu nháy trong bản dịch. Là tên tổ chức? tên khác của Karikura? tên một phe? **Chưa rõ.** Bible chưa có mục này.
5. **Gã ngoài phố** — cơ bắp, tóc dựng, có con mắt thứ ba trên trán, răng nanh, mặt hoá mặt quỷ khi hưng phấn. Chính là "kẻ hầu cận" nữ địch nói tới (P18-b). **Chưa có tên xác nhận.**
6. **Akitsugu** — chỉ xuất hiện đúng một lần, trong khung chibi P19-g: "…nhưng mà nếu xao nhãng mệnh lệnh… thì Akitsugu sẽ cằn nhằn lắm đây…". **Không xác định được Akitsugu là chính gã đó tự xưng tên mình, hay là một nhân vật thứ ba cấp trên sẽ mắng hắn.** Câu tiếng Việt đọc theo cả hai nghĩa đều được. **Phải chốt trước khi viết lời kể.**
7. **Người tóc đen ngoài phố** — đối đầu gã kia ở P18-d → P20, biết xướng thuật "Bá Pháp (Kenhou)", biết ngay rằng "người thường không được phép nhìn thấy hắn". **Chưa có tên, chưa rõ giới tính** (nét vẽ để mở), **chưa rõ phe**. Có thể là nhân vật từ C2–C11 mà bible chưa cập nhật.

**Thuật ngữ mới — bible chưa chốt bản dịch:**

| Xuất hiện | Nguyên văn trong bản dịch | Ghi chú |
|---|---|---|
| P03-c | **"giờ hoàng hôn"** | Mốc thời gian mà yêu quái/oán hồn mới được ra. Địch xuất hiện sớm hơn giờ này → đó là điều bất thường mở màn chương. Liên quan trực tiếp tới tựa bộ "Twilight Blade". |
| P03-b | **"yêu quái"** | Bản dịch C12 dùng "yêu quái". Bible chốt dùng **"oán hồn"** cho C1. **Chưa rõ hai từ là một loại hay hai loại khác nhau** — không được tự gộp. |
| P04-c | **"Ma Duyên"** | xem mục 4. |
| P17-a | **"giới lực"** | Thứ được truyền vào vũ khí để biến hoá nó. |
| P17-a | **"ngoại pháp sư"** | Bible chỉ có **"pháp sư trừ tà"**. Đây là từ khác, do địch dùng để gọi loại vũ khí của Yatsuha. **Chưa rõ có phải cùng một nghề hay không.** |
| P14-c | **Linh Nghiệm (Reigen)** | Thuật của nữ địch. Bản dịch để cả tên Việt lẫn romaji. |
| P15-a | **Khắc Viêm (Haramitsu)** | Thuật của nữ địch. |
| P19-e | **Bá Pháp (Kenhou)** | Thuật của người tóc đen ngoài phố, bị cắt ngang chưa kịp phát động. |

→ **Cần chốt: trong video đọc tên thuật theo bản Việt ("Linh Nghiệm"), theo romaji ("Reigen"), hay đọc cả hai?** Bible chưa có quy tắc cho việc này.

**Chi tiết hình chưa chắc chắn:**

8. **P08-a — khuôn mặt quỷ tối sầm hiện sau lưng nữ địch.** Theo mạch (Yojin bị ghì → "Buông... ra..." → cú đấm → nhát chém xé thung lũng → Yojin gọi "Yatsu...") thì **rất nhiều khả năng đây là Yatsuha ở trạng thái mạnh**, nhưng **không có panel nào chỉ rõ**. Không được viết chắc trong lời kể cho tới khi user xác nhận.
9. **P05-a — "Cô đã nhận ra rồi nhỉ."** Nữ địch dùng đại từ **"cô"** trong khi người đối thoại (Yatsuha) được chính cô ta gọi là **"anh"** ở P12-a. **Bản dịch mâu thuẫn đại từ.** Chưa rõ là lỗi dịch hay đang nói với người thứ ba.
10. **P18-a — "Cô gọi là Yojin-sama sao!"** Câu này đứng trong khung có Yojin và Yatsuha; **chưa xác định được ai nói.** Đọc hợp lý nhất là nữ địch vừa học được tên Yojin từ tiếng quát của Yatsuha ở P17-c.
11. **P13-c — Yojin bốc lửa.** Chưa rõ đây là **thuật anh chủ động dùng** hay là trạng thái mất kiểm soát. Bible mục 4 đã ghi "mắt Yojin đỏ ở C1-P01 là hiệu ứng hay trạng thái dùng thuật" vẫn **chưa tiết lộ** — panel này chưa đủ để kết luận, **không được suy đoán**.
12. **P21-a — vài gương mặt học sinh trong đám đông.** Không đủ nét để xác nhận có **Kenta** (bạn cùng lớp Hikari, bible mục 1) hay không. Ghi **KHÔNG ĐỌC ĐƯỢC / không xác nhận**.
13. **Địa điểm hai tuyến.** Tuyến Yojin/Yatsuha ở rừng núi; tuyến Hikari ở một sảnh lát gạch đông người (ga tàu? trung tâm thương mại?). **Chưa rõ tên địa điểm, chưa rõ khoảng cách giữa hai nơi.**

**Khoảng trống quy trình — cần user xử lý:**

14. **C2 → C11 chưa có beat sheet nào** trong repo, và **series-bible mới chỉ lập từ C1**. C12 giả định người xem đã biết Yatsuha, Karikura, Ma Duyên, "giờ hoàng hôn". Nếu video C12 phát độc lập, **phải quyết định giới thiệu lại bao nhiêu** — nhưng bible không cho biết mốc nào đã tiết lộ ở C2–C11, nên **hiện chưa thể biết cái gì là spoiler và cái gì không**.
15. **Bible mục 4 ghi "Hikari chưa biết bất cứ điều nào ở trên" tính đến hết C1.** C12 **không cho biết** tới giờ Hikari đã biết chưa. Lời kể **không được khẳng định theo hướng nào**.
16. **`tts-pronounce.tsv` mới có Yojin.** Thiếu: **Yatsuha, Karikura, Hikari, Akitsugu, Reigen, Haramitsu, Kenhou**. Cần bổ sung trước bước audio.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** 73 panel trên 20 trang nội dung (P01, P22, P23 là quảng cáo — đã bỏ; P02 chỉ dùng phần dưới). Anh soát lại giúp các panel trọng số 3, đặc biệt P08-a (mặt quỷ hiện sau lưng), P13-c (Yojin bốc lửa) và P18-b/c (chỗ cú lật) — em mô tả đúng ảnh chưa?
2. **Tên nhân vật đúng chưa?** Em chỉ dùng **Yojin** và **Hikari** theo bible. **Yatsuha / Karikura / Ma Duyên / Akitsugu** là lấy nguyên chữ trong thoại, chưa có trong bible. Nữ địch chương này **em để không tên**. Anh chốt giúp: giữ nguyên các tên đó, hay gọi khác? Và **Akitsugu là gã ngoài phố hay là một người thứ ba?**
3. **Trọng số hợp lý chưa?** Em để 4 đỉnh: cảm xúc (P07 "Đẹp thật đấy") · hành động (P09→P10→P15) · nghĩa (P13-c) · cú lật (P18-b/c → P20-f → P21-d). Với ngân sách 468 từ / 180 giây, phần rừng (P03→P17, 52 panel) đang chiếm quá nhiều — anh có muốn em hạ trọng số cụm P05–P07 xuống để dành đất cho cú lật không?

**Chưa sang `/manga-narration`. Chờ duyệt.**
