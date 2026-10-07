# BEAT SHEET — Twilight Blade C9 「子の父」

Nguồn ảnh: `series/TWB/C9/pages-clean/`
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **ĐỦ 21/21 trang** · 70 panel ghi nhận · 1 trang BỎ hoàn toàn
Tên chương: 第9話「子の父」 — tạm dịch **"Cha của đứa con"**. Bản dịch Việt trong ảnh KHÔNG dịch tên chương → **chưa chốt, đừng đưa bản dịch này lên video như tên chính thức.**

> **Chiều đọc: PHẢI → TRÁI.** Đã kiểm chứng ở P03 (bấm chuông hình → mở cửa → Yukina) và P09
> (Hikari đưa đĩa → Yamato cảm ơn → "cứ coi anh như anh trai"). Panel được đánh `-a`, `-b`…
> theo thứ tự đọc phải-sang-trái, trên-xuống-dưới.

---

### A. Kiểm tra đầu vào

21 ảnh `TWB_C9_P01`–`P21`, **liên tục, không thiếu trang.**

`clean-pages.py` đã chạy nhưng **làm chưa sạch** — ba chỗ còn quảng cáo, phải xử lý ở khâu dựng:

| Trang | Gốc | Sau clean | Ghi chú |
|---|---|---|---|
| P01 | 822×1500 | 822×1052 (cắt 448px) | **VẪN CÒN banner FoxTruyen màu ở hàng 0–460.** Nội dung truyện chỉ bắt đầu từ y≈461 → phải crop thêm ~461px mép trên |
| P02–P19 | 822×1200 (P02 610) | không đổi | sạch, không có vùng màu |
| P20 | 822×1500 | 822×1500 (0px) | **CÒN banner FoxTruyen ở đáy, hàng 1202–1499** → crop ~298px mép dưới. Trang này có khung truyện + omake 4 khung + dòng báo chương sau, đều nằm trên y=1202 |
| P21 | 822×610 | 822×582 (cắt 28px) | **BỎ TOÀN TRANG** — 100% quảng cáo (FoxTruyen + TruyenQQQ), không có nội dung truyện |

Watermark site tổng hợp: không thấy trên các trang truyện của chapter này (chỉ có 2 banner nói trên).

⚠ **Cảnh báo nghiêm trọng về ngữ cảnh, KHÔNG phải về ảnh:**
`tracker.csv` cho thấy **chỉ C1 đã có beat sheet; C2–C8 chưa đọc.** Beat sheet này đọc C9 độc lập.
Bốn thiết lập dưới đây C9 coi như người xem đã biết, nhưng `series-bible.md` (lập từ C1) **chưa có**:
Yamato là đệ tử của Yojin · Hikari đã dọn về sống chung · Yukina đã tồn tại từ trước · tổ chức có tên.
→ Trước khi viết lời kể phải đọc C2–C8, nếu không sẽ giới thiệu nhân vật sai mốc.

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P01-a | Khung mở: một chiếc hamburger **cháy đen thui** trên đĩa, kèm súp lơ và khoai tây. Nét vẽ trang trọng như ảnh ẩm thực. Tên chương đặt cạnh | "Sau bao nỗ lực vất vả và… đã hoàn thành rồi!" | tự hào lệch tông | 2 |
| 2 | P01-b | Dải mặt: Hikari và Yojin nhìn xuống đĩa, câu nói bị cắt ngang giữa trang | "LÀ…" | nín thở, hài | 1 |
| 3 | P02-a | Hikari mắt sáng rực, reo lên gọi tên món | "HAMBURGER…!" | háo hức | 2 |
| 4 | P02-b | Yamato đứng bếp, cầm xẻng lật, đẩy công sang Yojin | "Người làm là sư phụ mà~" | vui vẻ | 2 |
| 5 | P02-c | Yojin giơ hai tay đẩy lại; chú thích nhỏ thú nhận súp lơ và khoai tây là **đồ đông lạnh** | "Tôi chỉ giúp đoạn nướng thôi mà~~" | ngượng, đùn đẩy | 2 |
| 6 | P03-a | Chuông cửa reo lúc tối muộn. Yamato lo lại là quái vật; Yojin đứng dậy ra cửa | "Chắc không phải lại là yêu quái đâu nhỉ…?" | cảnh giác ngầm | 2 |
| 7 | P03-b | Yojin bấm màn hình chuông cửa, giật mình một nhịp | "!" | bất ngờ | 1 |
| 8 | P03-c | Cửa mở. Yojin nhận ra người đứng ngoài | "Ồ, là cô à." | quen biết | 2 |
| 9 | P03-d | Khung đứng cả trang: **một cô gái tóc đen buộc cao, vest đen, xách vali**, cúi chào | "Anh đã vất vả rồi…, Đại pháp sư Odaki." | trang trọng | 3 |
| 10 | P04-a | Cận mặt — cô tự giới thiệu và báo mình **vừa đi công tác về** | "Tôi là Yukina Kitsutsuki. Tôi vừa mới trở về!" | dứt khoát | 3 |
| 11 | P04-b | Hành lang: Yojin cảm ơn cô vì **nhiệm vụ điều tra**; cô xin nói chuyện riêng ngay | "Bây giờ ngài có rảnh không ạ?" | công vụ | 2 |
| 12 | P04-c | Yukina truyền lời: **Tổng soái Himorogi** nhờ gửi lời nhắn cho Yojin — **cài đặt cho toàn bộ nửa sau chương** | "Tổng soái Himorogi… có nhờ tôi gửi lời nhắn đến ngài…" | nặng, mở nút | 3 |
| 13 | P05-a | Cắt về bàn ăn: Hikari và Yamato ngồi chờ, thức ăn nguội dần | "Họ đang nói chuyện gì mà lâu thế nhỉ…" | sốt ruột | 1 |
| 14 | P05-b | Yamato lấp liếm bằng chuyện "dự án ở công ty"; Yojin thò đầu ra ra hiệu im lặng | (chú thích) "Giữ bí mật với Hikari-kun nhé." | **Yojin vẫn đang giấu Hikari** | 3 |
| 15 | P05-c | Hikari đổi chủ đề, hỏi thẳng Yamato: **làm cách nào mà anh được chú Yojin nhận làm đệ tử** | "…làm cách nào…?" | dò hỏi, ganh tị | 3 |
| 16 | P05-d | Hikari cúi mặt, lộ vết thương thật: cậu **đã xin và bị từ chối** | "Rõ ràng là chú ấy đã từ chối em…" | tủi | 3 |
| 17 | P06-a | Yamato ngớ ra rồi cười vỡ lẽ; Hikari giật mình vì bị đọc vị | "Hóa ra là vậy… thảo nào…" | nhẹ nhõm, hài | 2 |
| 18 | P06-b | Yamato kể **chính anh ban đầu cũng bị Yojin từ chối**, vì nghề này cực kỳ nguy hiểm | "Ban đầu anh cũng bị từ chối mà." | đồng cảm | 2 |
| 19 | P06-c | Yamato nhắc lại điều Hikari đã biết: cậu có **thể chất dễ bị yêu quái thu hút** | "Nghe bảo em ấy có thể chất dễ bị thu hút yêu quái…" | lạnh, thực tế | 2 |
| 20 | P06-d | **Khung lớn — mắt Hikari mở trừng.** Yamato diễn giải lý do Yojin từ chối: đó không phải chê, mà là **tình cha con** | "…kiểu như tình cha con ấy." / "Nên anh ấy mới lo lắng đặc biệt như thế, không phải sao?" | vỡ oà | 3 |
| 21 | P07-a | Yamato bồn chồn, tự hỏi mình nói vậy cậu bé đã hiểu chưa | "Người cha…" | hồi hộp | 2 |
| 22 | P07-b | Cận mặt Hikari đỏ bừng, môi run — cậu lắp lại hai chữ đó cho chính mình | "Chú Yojin…, đối với em là…" | nghẹn | 3 |
| 23 | P07-c | Hikari bật ra thành lời: **cậu chưa từng biết mình được nhìn theo hướng đó** | "Em không biết là…, chú ấy đối với em theo hướng đó!" | xúc động | 3 |
| 24 | P07-d | Cửa mở đúng lúc; Yamato thở phào. Yojin quay lại bàn ăn | "Suýt nữa thì nguy~" / "Để mọi người chờ lâu rồi…" | hạ nhiệt | 1 |
| 25 | P08-a | **Khung lớn, lạnh:** Yojin và Yukina đứng cạnh nhau, mặt không cười. Yojin xin lỗi hai đứa nhỏ | "Xin lỗi hai đứa nhé…" | báo tin xấu | 2 |
| 26 | P08-b | Yojin (ngoài khung) mở lời về **chuyện ngày mai**; Yamato quay lại, chưa biết Yukina là ai | "Về chuyện ngày mai thì…" / "Ai kia…?" | chuyển màn | 2 |
| 27 | P09-a | **Sáng hôm sau.** Ngoại cảnh toà nhà, nắng | "Trời ơi, hôm nay là thứ Bảy rồi…" | chuyển cảnh | 1 |
| 28 | P09-b | Chảo trứng ốp la và thịt hun khói đang xèo. Lời than xác nhận **Yojin đã bị gọi đi làm** | "…mà lại bị gọi đi làm cơ đấy~" | thường ngày | 2 |
| 29 | P09-c | Hikari chủ động lấy đĩa ra; Yamato cảm ơn rối rít | "Yoshino-san, em lấy đĩa ra rồi." | ấm | 1 |
| 30 | P09-d | Yamato đề nghị bỏ họ, gọi tên cho thân — hôm nay chỉ hai anh em trông nhà | "Cứ gọi anh là Yamato đi cho thân thiết!" | kéo gần | 2 |
| 31 | P09-e | **Yamato tự nhận vai thứ hai trong nhà** — không phải cha, mà là anh trai | "Cứ coi anh như anh trai của em cũng được nhé." | ấm, cài motif | 3 |
| 32 | P10-a | Hikari đáp lại lời mời; hai bên chốt cách gọi tên nhau | "Vậy thì… anh Yamato!" / "Anh cũng gọi em là Hikari nha~" | thân | 2 |
| 33 | P10-b | Hikari chợt nhìn ra phía cửa | "Ờ mờ…, đằng kia…" | khựng | 1 |
| 34 | P10-c | **Yukina đứng sẵn ở khung cửa, im lặng, mặt lạnh** — đã có mặt từ lúc nào không rõ | "…" | gợn | 2 |
| 35 | P10-d | Hikari nhận ra cô, gọi đúng tên, mời ăn sáng. Yukina từ chối khéo, bảo hai người cứ dùng bữa | "Cô là Yukina-san…, đúng không nhỉ? Cấp dưới của sư phụ…" | lễ phép / cứng | 2 |
| 36 | P11-a | Yamato nài thêm; Yukina gạt phắt | "Không cần đâu!" | cự tuyệt | 1 |
| 37 | P11-b | **Yukina nói ra nhiệm vụ của mình: làm người giám hộ đại diện cho Hikari.** Không được lơ là cảnh giác | "…làm người giám hộ đại diện cho Hikari-kun." | nghiêm, tiết lộ | 3 |
| 38 | P11-c | Yukina dằn mặt Yamato: biết anh mới thành đệ tử, **nhưng phó quan là cô** — tị nạnh thứ bậc | "Nhưng phó quan chính là tôi đây." | gằn | 3 |
| 39 | P11-d | Bụng Yukina kêu rõ to giữa lúc đang lên gân | (tượng thanh) ぐるるる | vỡ trận, hài | 2 |
| 40 | P12-a | Yukina chối quanh, bảo đó là tiếng **đau bụng** — bị vặn lại ngay | "Thế thì lại càng đáng lo hơn đấy chứ!?" | cuống | 2 |
| 41 | P12-b | Yamato thông cảm bằng kinh nghiệm bản thân; Yukina nổi đoá không cho xếp chung | "Đừng có đánh đồng tôi với anh!?" | quạu | 1 |
| 42 | P12-c | **Yukina lỡ nói hết suy nghĩ thật thành tiếng:** cô sợ không thân nổi với một **cậu bé 14 tuổi** | "…không biết có thể thân thiết với một cậu bé 14 tuổi hay không…" | lộ tẩy, đáng yêu | 3 |
| 43 | P12-d | **Hikari chủ động phá băng** — đề nghị cả ba cùng ăn | "Cả 3 chúng ta… cùng ăn chung được không ạ?" | mở lòng | 3 |
| 44 | P13-a | Hikari cười rạng rỡ, nói thẳng điều cậu muốn | "Em… cũng muốn trở nên thân thiết với cả hai người!" | sáng | 3 |
| 45 | P13-b | Yukina đỏ mặt, mồ hôi, không biết đáp sao | "Thế thì…" | lúng túng | 2 |
| 46 | P13-c | **Khung lớn:** Hikari cười hết cỡ; câu hỏi rất đời thường về trứng ốp la được đưa ra và Yukina trả lời — **băng tan** | "Lòng đào hay chín hẳn, cô thích loại nào hơn?" / "…cho tôi lòng đào…" | ấm, đỉnh cảm xúc | 3 |
| 47 | P13-d | Chim bay, hoa anh đào rụng — chuyển sang tuyến khác | — | lặng | 1 |
| 48 | P14-a | Hành lang gỗ kiểu Nhật ở **trụ sở**. Một nữ nhân viên mới đi lạc, than trụ sở quá rộng | "Trụ sở rộng quá đi mất~" | hài, nhẹ | 1 |
| 49 | P14-b | Cô đâm sầm vào Yojin. **Yojin đỡ cô và xin lỗi trước** | "Ôi trời, xin lỗi em nhé. Em không sao chứ?" | điềm đạm | 2 |
| 50 | P14-c | Tiền bối tóc đỏ của cô nhìn thấy, mặt biến sắc | "OÁI!" | hoảng | 1 |
| 51 | P15-a | Tiền bối rạp người xin lỗi thay; Yojin gạt đi, nhận lỗi về mình | "Là tôi đâm vào cô ấy mà. Không sao đâu." | khiêm nhường | 2 |
| 52 | P15-b | Yojin chào rồi đi tiếp, vẫy tay | "Chà, tôi nên đi đây." | bình thản | 1 |
| 53 | P15-c | Lính mới vẫn ngơ ngác, chỉ biết đó là "Đại pháp sư Odaki" | "Ồ~ người đó là 'Đại pháp sư Odaki' ạ…" | ngây | 2 |
| 54 | P15-d | **Tiền bối gào lên — lần đầu tiên tổ chức được gọi tên: "Bát Giới"**, và Yojin là bậc cao nhất của nó | "Đó là bậc cao nhất của 'Bát Giới' đấy!!" | chấn động, tiết lộ | 3 |
| 55 | P16-a | **Khung lớn cả trang:** Yojin đi dưới hoa anh đào, áo khoác đen khuy huy hiệu. Danh xưng đầy đủ được xướng lên | "Đại pháp sư 'Hãm Ma Giới'…, Đại pháp sư Odaki Yojin…!" | uy nghi | 3 |
| 56 | P16-b | Tiền bối thú nhận đây cũng là lần đầu anh nói chuyện với Yojin; lính mới khen ngược lại anh | "Đây cũng là lần đầu tiên tôi nói chuyện với ngài ấy đó…!" | hài, hạ nhiệt | 1 |
| 57 | P17-a | **Khung lớn, lặng ngắt:** Yojin đứng quay lưng trước một cánh cửa gỗ chạm khắc khổng lồ | — | nén | 3 |
| 58 | P17-b | Hai khung cận liền nhau: **anh thở ra, rồi hít vào** — chỉnh lại nét mặt trước khi vào | (tượng thanh) ふぅ / すぅ | căng, chuẩn bị | 3 |
| 59 | P17-c | Anh xin phép; bên trong vọng ra một tiếng ngắn cho vào | "Xin phép ngài." / "Vào đi." | ngưỡng cửa | 3 |
| 60 | P18-a | Yojin xưng danh và báo cáo có mặt — **giọng của cấp dưới thuần tuý** | "Tôi là Odaki Yojin, hiện đã có mặt." | cứng nhắc | 2 |
| 61 | P18-b | **Người trong phòng lộ diện:** đàn ông lớn tuổi, ria mép, vest sọc, đeo huy hiệu — nói với Yojin bằng giọng thân mật | "Ừ, ta chờ cậu mãi…, Yojin." | quyền lực, ấm lạ | 3 |
| 62 | P18-c | Ông xin lỗi vì gọi Yojin về gấp **giữa lúc đang thực hiện nhiệm vụ giám sát** — xác nhận Yojin vẫn đang giám sát Hikari | "…lúc đang thực hiện nhiệm vụ giám sát nhé." | xác nhận mốc C1 | 3 |
| 63 | P19-a | Ông bảo Yojin ngồi xuống, đừng đứng nói chuyện | "Ngồi xuống đi, đứng nói chuyện làm gì." | xuề xoà | 1 |
| 64 | P19-b | **Khung lớn cái bàn:** ấm trà, cupcake, bánh quy, pretzel, madeleine, hộp sô-cô-la — **toàn đồ ngọt dọn cho trẻ con.** Yojin im lặng | "…" | lệch pha, buồn cười | 3 |
| 65 | P19-c | Yojin cuối cùng cũng lên tiếng — câu thoại tiết lộ **anh đã 32 tuổi** | "Ngài đã quên rằng…, tôi đã 32 tuổi rồi sao." | mệt mỏi | 3 |
| 66 | P19-d | Tổng soái hoàn toàn không hiểu vấn đề, tưởng anh chê món | "Sao thế? Cậu muốn ăn món khác à?" / "Có sao đâu chứ…" | vô tư | 2 |
| 67 | P20-a | **CÚ LẬT.** Cận mặt Tổng soái, cười hiền: ông tự nhận mình là **cha nuôi** của Yojin | "Với một người cha nuôi như ta, chuyện đó chẳng có gì đáng bận tâm cả, Yojin." | lật nghĩa toàn chương | 3 |
| 68 | P20-b | Ông gọi Yojin bằng **"con"** và hỏi vì sao tuổi tác lại là vấn đề. Yojin cụp mắt, không đáp | "Sao con lại thấy nó là vấn đề…, rằng con bao nhiêu tuổi." | nghẹn, ấm | 3 |
| 69 | P20-c | **Omake 4 khung** (ngoài mạch chính): Yamato mời thêm thịt hun khói; Hikari và Yukina chibi đua nhau giành phần nấu | "Trưa nay chính tay tôi sẽ nấu bữa trưa…!" | hài, kết ngọt | 1 |
| 70 | P20-d | Dòng báo chương sau: 「陽刃の父、登場!!」— **"Cha của Yojin xuất hiện!!"**, phát hành 26/8 (thứ Tư) | 陽刃の父、登場!! | mở nút cho C10 | 2 |
| — | P21 | Trang quảng cáo FoxTruyen + TruyenQQQ | — | — | **BỎ** |

---

### C. Điểm cao trào

Chương này có **ba đỉnh**, và đỉnh thứ ba làm đổi nghĩa hai đỉnh đầu.

**1. Đỉnh cảm xúc — P06-d → P07-c (beat 20–23).**
Yamato gọi tên thứ mà Hikari không dám gọi: lý do Yojin từ chối nhận cậu làm đệ tử không phải
là chê, mà là **tình cha con**. Khung lớn mắt Hikari mở trừng ở P06-d là đỉnh thị giác; câu
"Em không biết là… chú ấy đối với em theo hướng đó!" ở P07-c là đỉnh lời. Nối thẳng với mốc
C1: Yojin cố ý giấu Hikari mọi chuyện — ở đây cái Hikari nhận được lại chính là thứ Yojin
không nói ra.

**2. Đỉnh ấm — P12-d → P13-c (beat 43–46).**
Hikari, chứ không phải người lớn nào, là người phá băng. Yukina lỡ để lộ rằng cô sợ không
thân nổi với một cậu bé 14 tuổi; cậu bé mời cả ba cùng ăn. Câu chốt là một câu hỏi tầm thường
đến mức đó mới là điểm: "lòng đào hay chín hẳn". Đây là đỉnh của tuyến "gia đình chắp vá":
Yojin = người cha, Yamato = anh trai (P09-e), Yukina = người giám hộ đại diện (P11-b).

**3. CÚ LẬT CUỐI — P19-b → P20-b (beat 64–68).**
Nửa đầu chương dựng Yojin thành **người cha**: người che chắn, người giấu sự thật, người mà
một đứa trẻ 14 tuổi phải đoán mới hiểu. Nửa sau đưa anh vào phòng Tổng soái với tư cách cấp
dưới cứng nhắc nhất — và rồi bàn đầy bánh kẹo, câu "tôi đã 32 tuổi rồi", và ông già gọi anh
là **"con"**, tự nhận là **cha nuôi**.

**Cái bị đổi nghĩa:** người cha của C9 hoá ra cũng là đứa con của ai đó. Tên chương 「子の父」
và dòng báo chương sau 「陽刃の父、登場!!」 xác nhận đây mới là chủ đề thật, không phải bữa
hamburger cháy ở P01. Đọc lại, mọi chi tiết nửa đầu mang hai nghĩa: Yojin từ chối nhận đệ tử
vì nghề nguy hiểm — nhưng chính anh đã được ai đó nhận về; anh thở ra hít vào trước cửa như
một nhân viên — sau cánh cửa là cha anh.

**Khoảnh khắc lạnh đáng giữ nguyên:** P17-b, hai khung anh thở ra rồi hít vào. Không có thoại.
Sau cú lật, khung đó không còn là sự căng thẳng nghề nghiệp nữa.

---

### D. Chưa rõ

**Không được đoán bừa trong lời kể.**

*Về tổ chức — bible hiện ghi "CHƯA RÕ, không được bịa". C9 đã hé nhưng vẫn KHÔNG đủ:*
1. **"Bát Giới"** (P15-d) — tên tổ chức, xuất hiện lần đầu. Tám "giới" là gì, cơ cấu ra sao: **không giải thích trong chương.**
2. **"Hãm Ma Giới"** (P16-a) — danh hiệu của Yojin. Là một trong tám giới hay là cấp bậc riêng: **không nói.**
3. **"Tổng soái"** — chức của Himorogi. Quan hệ giữa Tổng soái và Bát Giới: **không nói.**
4. **"Phó quan"** — Yukina tự nhận (P11-c). Phó quan **của ai** (của Yojin hay của Tổng soái): **không nói.**
5. **"Đại pháp sư"** — C9 dùng từ này cho Yojin. Bible C1 chốt nghề anh là **"pháp sư trừ tà"** (tự nhận ở C1-P34). Hai từ này là một chức danh hay hai, chưa xác định được → khi viết lời kể nên dùng "pháp sư trừ tà" theo bible và chỉ trích "Đại pháp sư Odaki" như **thoại gốc**.

*Về từ vựng — MÂU THUẪN VỚI BIBLE, cần chốt trước khi viết:*
6. Bản dịch C9 dùng **"yêu quái"** (P03-a, P06-c) cho loại sinh vật mà bible §2 đã chốt gọi là **"oán hồn"** (bible cũng đã gộp "ác linh" vào "oán hồn"). Không xác định được từ gốc tiếng Nhật từ ảnh. → **Đề xuất: giữ "oán hồn" theo bible cho nhất quán toàn kênh, ghi chú lại; KHÔNG đưa "yêu quái" làm từ thứ ba.**

*Về nhân vật:*
7. **Himorogi** — chỉ có một tên gọi duy nhất, không rõ đó là họ hay tên. **Tên đầy đủ: chưa có.**
8. Quan hệ cha nuôi Himorogi–Yojin: **nhận nuôi từ khi nào, vì sao, cha mẹ ruột Yojin là ai — chương không nói một chữ.** Dòng báo chương sau nói "cha của Yojin xuất hiện" ở C10 → **để dành, không suy đoán trước.**
9. **Yukina Kitsutsuki** — "vừa mới trở về" từ một **nhiệm vụ điều tra** (P04-a/b). Điều tra vụ gì: **không nói.** Có liên quan vụ cháy căn hộ Fujino hay không: **không có căn cứ.**
10. **Lời nhắn của Tổng soái** mà Yukina chuyển ở P04-c có phải chính là lệnh triệu tập dẫn tới cuộc gặp P17–P20 không — truyện **không nối rõ**, chỉ đặt cạnh nhau.
11. **Nữ nhân viên mới và tiền bối tóc đỏ** (P14–P16): **không có tên**, không rõ vai. Gọi là "một nhân viên mới" và "tiền bối của cô".
12. **Yamato trở thành đệ tử bằng cách nào** — Hikari hỏi thẳng ở P05-c nhưng Yamato **né, không trả lời**; chỉ nói "ban đầu anh cũng bị từ chối". Câu hỏi của chương bị bỏ ngỏ.
13. **Vì sao Yojin từ chối Hikari** — chỉ có cách giải thích của **Yamato** (P06-d), không phải lời Yojin. Là suy diễn của nhân vật, **không phải sự thật đã xác lập.**

*Về đọc ảnh:*
14. **P02**, khung "Thôi nào thôi nào, sao hai người lại ngạc nhiên thế?" — **không chắc người nói** (đuôi bong bóng chỉ ra ngoài khung). Ba người có mặt: Yojin, Yamato, Hikari.
15. **P13-c**, câu "Trứng ốp la… lòng đào hay chín hẳn, cô thích loại nào hơn?" — **không chắc do Yamato hay Hikari hỏi.** Người trả lời chắc chắn là Yukina ("cho tôi lòng đào").
16. **P06-a**, khung nhỏ bên phải ("…" / "À,…") — nhận là Yamato dựa vào tóc và nốt ruồi dưới mắt, **độ chắc trung bình.**
17. **Tên chương 「子の父」** — bản dịch Việt bỏ trống. "Cha của đứa con" là bản tạm của beat sheet này, **chưa chốt.**

*Về mốc cốt truyện:*
18. **C2–C8 chưa đọc.** Không xác định được chi tiết nào của C9 là mới và chi tiết nào đã lộ ở các chương giữa: Yamato là đệ tử · Hikari sống cùng Yojin · Yukina đã có mặt từ trước. **Rủi ro cao là lời kể sẽ giới thiệu nhân vật sai mốc.**
19. **Vụ cháy, mẹ Hikari, oán hồn có tổ chức** — C9 **không nhắc đến một lần nào.** Đừng kéo về nếu không phục vụ cú lật.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** Đặc biệt xin soát 3 chỗ tôi tự đánh giá là chưa chắc chắn: người nói ở **P02** (beat 5), người hỏi trứng ở **P13-c** (beat 46), và nhận dạng Yamato ở **P06-a** (beat 17).
2. **Tên nhân vật đúng chưa?** C9 thêm 3 tên mới chưa có trong `series-bible.md`: **Yukina Kitsutsuki** · **Yoshino Yamato** (Hikari gọi "anh Yoshino", tự xưng "Yamato") · **Tổng soái Himorogi**. Cùng 2 thuật ngữ mới: **"Bát Giới"** · **"Hãm Ma Giới"**. Và một xung đột cần anh chốt: **"yêu quái" (C9) vs "oán hồn" (bible)** — dùng từ nào?
3. **Trọng số hợp lý chưa?** Tôi đặt TS3 cho cả ba đỉnh, nhưng dồn nhiều nhất vào cụm cú lật **P17–P20** (beat 57–68, 9 panel TS3 liên tiếp). Nếu anh muốn video 180 giây nghiêng về tuyến ấm ở nhà (P06–P13) thay vì tuyến trụ sở, nói tôi hạ trọng số cụm P14–P16 xuống.

**Chưa sang `/manga-narration`. Chờ duyệt.**
