# BEAT SHEET — FRN Chapter 1: "Hồi kết của cuộc hành trình"

> Bước ĐỌC HIỂU. **Chưa viết lời kể.** Dừng chờ duyệt.
> Nguồn ảnh: `truyen/FRN/prepare/C1/pages-clean/` · Đối chiếu `truyen/FRN/series-bible.md`.
> Thuật ngữ dùng theo bible: **Quỷ Vương** (không dùng "Ma Vương"), **ma lực** (không dùng "mana"),
> **elf**, **tộc người lùn**, **Kỷ Nguyên Sao Băng**, **rồng hắc ám**, **tà khí**, **tiên phong**, **giám mục**.

---

## A. Kiểm tra đầu vào

### A1. Ảnh đã nhận — 38/38 file, đã xem HẾT, theo thứ tự P01→P38

Đọc theo 7 lô nhỏ (P01–05 · P06–10 · P11–15 · P16–20 · P21–25 · P26–30 · P31–35 · P36–38),
ghi chép xong từng lô mới sang lô sau. **Không trang nào bị nhảy cóc, không trang nào bị
`[media removed: request limit]`.**

| File | Kích thước (pages-clean) | Gốc (pages) | clean-pages cắt | Tình trạng |
|---|---|---|---|---|
| FRN_C1_P01 | 900×585 | 900×1075 | **−490 px** | **BỎ** — banner quảng cáo bộ khác + logo 7 Fingers Team |
| FRN_C1_P02 | 900×720 | 900×720 | 0 | **BỎ** — trang credit nhóm dịch (TRANSLATOR Credemoe / EDITOR Yahari / PROOFREADER + QC Credemoe) |
| FRN_C1_P03 | 836×1200 | 836×1200 | 0 | Nội dung — **trang màu** |
| FRN_C1_P04 | 900×646 | 900×646 | 0 | Nội dung — **trang màu, SPREAD 2 trang nằm ngang**, có tên chương |
| FRN_C1_P05 … P25 | 836×1200 | 836×1200 | 0 | Nội dung (đen trắng) |
| FRN_C1_P26 | 900×646 | 900×646 | 0 | Nội dung — **SPREAD 2 trang nằm ngang**, khung mưa sao băng tràn trang |
| FRN_C1_P27 … P37 | 836×1200 | 836×1200 | 0 | Nội dung (đen trắng) |
| FRN_C1_P38 | 900×946 | 900×976 | **−30 px** | **BỎ** — banner 12 Fingers Team + quảng cáo truyenqqq.com |

- **Không thiếu trang liên tiếp.** File chạy liền P01→P38, không đứt số. → Không cảnh báo, không dừng.
- `clean-pages.py` chỉ động vào **2 file** (P01 cắt 490 px, P38 cắt 30 px) — cả hai đều là trang bị loại,
  nên **không trang nội dung nào bị cắt mất tranh**.
- **35 trang nội dung thật: P03 → P37.**

### A2. Xác minh 3 trang bị loại (P01, P02, P38)

Xem tận mắt, không suy từ kích thước:
- **P01**: dải ảnh bìa các bộ khác (Hatsukoi Zombie, Komi-san, Shinigami Bocchan…) + khung đỏ
  "7 FINGERS TEAM" + link facebook. Không có một khung truyện nào.
- **P02**: trang credit — bìa tập 7 + tên staff + "Tất cả các sản phẩm đều phi lợi nhuận / Giữ nguyên credit khi reup".
  Đây là **trang có giá trị tra cứu** (tên tác giả, tên nhóm dịch) nhưng **không phải trang truyện**.
- **P38**: bảng đen "12 FINGERS TEAM (4/5/2020)" + băng-rôn xanh "CẬP NHẬT CHƯƠNG MỚI SỚM NHẤT TẠI WEBSITE TRUYENQQQ.COM"
  + dàn nhân vật Naruto/Deku/Tanjiro. Không có một khung truyện nào.

Khớp đúng với mục 5 của series-bible (ba file này đã được chốt là phải loại tay).

### A3. Chiều đọc — ĐÃ XÁC MINH LÀ **PHẢI → TRÁI** (manga Nhật, nhiều panel/trang)

Đây **không phải webtoon cuộn dọc**. Bằng chứng trong chính ảnh, không suy đoán:

1. **P05, khung đáy trang (nhà vua tuyên dương).** Bong bóng bên **phải** kết bằng dấu phẩy —
   *"CÁC NGƯƠI ĐÃ ĐÁNH BẠI ĐƯỢC QUỶ VƯƠNG,"* — và bong bóng bên **trái** mới là vế sau —
   *"VÀ MANG TỚI CHO THẾ GIỚI NÀY MỘT KỶ NGUYÊN HÒA BÌNH."* Một câu bị cắt làm hai, phải trước trái sau.
2. **P05, cụm 4 panel giới thiệu tổ đội.** Panel phải trên "ANH HÙNG HIMMEL." → phải dưới "CHIẾN BINH EISEN."
   → giữa "TƯ TẾ HEITER." → panel **trái cùng** "**VÀ** PHÁP SƯ FRIEREN." Chữ "**và**" nằm ở phần tử **cuối**
   của một danh sách, mà nó ở panel trái cùng → trái là chỗ đọc sau cùng.
3. **P08, hàng dưới (gag bị cắt lời).** Panel **phải**: Frieren khoe *"VỀ MẶT ĐÓ THÌ TÔI NỔI TRỘI H-…"*
   (gãy giữa chừng) — panel **trái** là câu chen ngang của Himmel *"TỤI TÔI ĐÃ PHÂN VÂN KHÔNG BIẾT CÓ NÊN
   BỎ CÔ LẠI KHI BỊ MIMIC NGẤU NGHIẾN ĐẤY."* Cú cắt lời chỉ có nghĩa khi phải đọc trước trái.
4. **P33.** Phải: Heiter dặn *"hãy biểu cho mộ của tôi chút rượu nhé."* → trái: Frieren hỏi lại
   *"…cậu không e sợ cái chết sao, Heiter?"* → trang dưới mới là câu trả lời. Hỏi–đáp chạy phải sang trái.

→ **Toàn bộ số panel dưới đây đánh theo chiều PHẢI → TRÁI, trên xuống dưới.** Trong một băng ngang,
cột phải đọc hết (trên rồi dưới) mới sang panel trái.

### A4. Số trang in trên ảnh — quy tắc của C1 KHÁC bible

Bible mục 5 ghi "số trang in = số file − 2" (kiểm trên C2). **C1 không theo công thức đó.**
Hai số in đọc được trong C1: file **P11 in số "10"**, file **P37 in số "37"**.
Giải thích khớp hoàn toàn: **P04 và P26 mỗi file là một spread = 2 trang in**.
→ P03 = trang 1 · P04 = trang 2–3 · P05 = trang 4 · … · P11 = trang 10 ✓ · … · P25 = trang 24 ·
P26 = trang 25–26 · P27 = trang 27 · … · P37 = trang 37 ✓.
**Beat sheet này dùng SỐ FILE (P03…P37) cho khỏi lệch**, đúng như bible dặn.

### A5. Ghi chú sản xuất phát hiện thêm

- **P13, panel b**: có **một ô thoại để TRẮNG, chưa dịch** (nhóm dịch bỏ sót). Không đoán nội dung.
- **P03, panel c**: bản dịch trang này in "**Ma Vương**"; các trang khác (P04, P05, P16) in "quỷ vương".
  Beat sheet + lời kể **chỉ dùng "Quỷ Vương"**; chữ "Ma Vương" chỉ giữ khi trích nguyên thoại.
- Thuật ngữ "**ma lực**" **không xuất hiện lần nào trong C1** — đây là từ của C2. Không được đưa vào C1.
- **Watermark site: không có.** Tranh sạch, chữ bong bóng đọc rõ ở 836px.
- Khung cần **HOLD, cấm cắt nhỏ**: **P26** (spread mưa sao băng) và **P11-b** (khung lớn tràn trang).
- Ứng viên hook/thumbnail: **P04** (màu, có tên chương), **P03** (màu), **P26** (spread).

### A6. Tổng kết đếm

**35 trang nội dung · 166 panel.**

---

## B. Beat Sheet

Trọng số: **3** = khoảnh khắc quyết định · **2** = có sức nặng · **1** = panel chuyển tiếp.

### Khúc 1 — Khải hoàn (P03–P06)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Xe ngựa chở tổ đội bốn người men đường rừng, đô thành hiện ra cuối đường. Trang màu, logo tựa đề nằm ngay đây. | "Đô thành đang ở trước mắt rồi nhỉ." | thảnh thơi, mở màn | 2 |
| 2 | P03-b | Himmel nhắc Frieren vẫn đang nghĩ ngợi; ai đó lo chuyện kiếm việc sau khi về. | "Cậu vẫn còn đang suy nghĩ về chuyện đó đấy à?" | đời thường | 1 |
| 3 | P03-c | Himmel ngồi bó gối, nói đánh bại kẻ thù xong thì cuộc đời vẫn chưa hết, còn nhiều việc phải làm. **Bản dịch trang này in "Ma Vương"** — cùng một đối tượng với Quỷ Vương. | "thì cuộc đời vẫn chưa chấm dứt hẳn đâu" | nhen chủ đề | 2 |
| 4 | P03-d | Cả nhóm nhao nhao chuyện nghề nghiệp; Heiter mơ một công việc vừa làm vừa uống được rượu. | "Nếu đó là công việc mà tôi có thể uống rượu trong khi làm…" | hài, ấm | 1 |
| 5 | P03-e | Himmel quay sang Frieren, nói chặng đường phía trước của cô sẽ rất dài, dài quá sức tưởng tượng của cả nhóm. | "Chặng đường phía trước của cậu hẳn sẽ còn rất dài," | **gieo mầm cả chương** | 3 |
| 6 | P03-f | Frieren ôm cuốn sách bìa đỏ, đáp hai tiếng gọn lỏn, không bận tâm. | "Có lẽ thế." | dửng dưng | 2 |
| 7 | P04-a | **Spread màu, trang tên chương.** Bốn người rẽ đám đông ăn mừng. Dòng dẫn in ngay trên tranh: đây là "kết thúc" của một tổ đội anh hùng. | "Đây là 'kết thúc' của một tổ đội anh hùng" | hoành tráng pha buồn | 3 |
| 8 | P05-a | Lâu đài trắng trên đồi, cờ bay. | — | trang nghiêm | 1 |
| 9 | P05-b | Nhìn từ trên xuống: dân chúng chật hai bên phố, tổ đội đi giữa trong mưa hoa. | — | khải hoàn | 2 |
| 10 | P05-c | Nhà vua xướng danh Himmel. | "Anh hùng Himmel." | vinh danh | 2 |
| 11 | P05-d | Xướng danh Eisen. | "Chiến binh Eisen." | vinh danh | 1 |
| 12 | P05-e | Xướng danh Heiter. | "Tư tế Heiter." | vinh danh | 1 |
| 13 | P05-f | Xướng danh Frieren — người cuối cùng, khung lớn nhất, mặt lạnh. | "Và pháp sư Frieren." | vinh danh, lặng | 2 |
| 14 | P05-g | Toàn cảnh ngai vàng: bốn người quỳ, vua tuyên công trạng hạ Quỷ Vương và mở kỷ nguyên hòa bình. | "Các ngươi đã đánh bại được Quỷ Vương," | đỉnh của phần mở | 3 |
| 15 | P06-a | Đêm hội ở quảng trường. Himmel khoe đức vua sẽ cho tạc tượng cả nhóm ngay tại đây. | "sẽ cho tạc tượng của chúng ta ở ngay quảng trường này" | phấn khích | 2 |
| 16 | P06-b | Himmel tạo dáng, lo thợ tạc không ra nổi vẻ đẹp trai của mình; Frieren cạnh khoé nhà vua keo kiệt, đưa đúng 10 đồng lúc khởi hành. | "cho chúng ta có đúng 10 đồng khi bắt đầu cuộc hành trình này" | hài | 1 |
| 17 | P06-c | Heiter ôm thùng rượu, dỗ Frieren: được uống chùa là đủ rồi. | "Chúng ta có thể uống rượu miễn phí mà" | hài | 1 |
| 18 | P06-d | Frieren buông một câu chửi yêu; Heiter cười xoà. **Chú thích của nhóm dịch: ý nói nồng nặc mùi rượu.** | "Đồ tư tế thúi." / "HAHAHA." | thân mật — **sẽ lặp lại ở P34** | 2 |

### Khúc 2 — "Kết thúc rồi" và lời hẹn 50 năm (P07–P13)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 19 | P07-a | Cận mũ sừng của Eisen, giọng trầm buông lửng. | "…Kết thúc rồi nhỉ?" | hụt hẫng | 2 |
| 20 | P07-b | Trước quầy rượu, Himmel xác nhận: đây là dấu chấm hết cho cuộc hành trình. | "Đây là dấu chấm hết cho cuộc hành trình của chúng ta." | **chốt khúc** | 3 |
| 21 | P07-c | Heiter cầm vại, Frieren cầm kẹo, đứng cạnh nhau, không ai nói gì. | — | khoảng lặng | 1 |
| 22 | P07-d | Phố đêm; ai đó nhẩm lại con số. | "10 năm à…?" / "Đã có nhiều thứ xảy ra trong suốt khoảng thời gian đó nhỉ?" | hoài niệm | 2 |
| 23 | P08-a | Kể lại chuyện cũ: trước khi khởi hành, Himmel và Eisen suýt bị xử tử vì phỉ báng nhà vua. Hồi tưởng chen vào: "Làm luôn đi.", "Hay là để tôi liếm giày người nhé?" | "còn suýt nữa thì bị xử tử vì phỉ báng nhà vua" | hài | 1 |
| 24 | P08-b | Chuyện thứ hai: Heiter say xỉn là thành đồ bỏ đi — và mỗi tuần một lần. Hồi tưởng: mặt Heiter như xác sống. | "Và còn xảy ra mỗi lần một tuần nữa chứ." | hài | 1 |
| 25 | P08-c | Frieren liếm kẹo mút, định khoe mình hơn hẳn khoản đó. | "Về mặt đó thì tôi nổi trội h-…" | tự mãn | 1 |
| 26 | P08-d | Bị cắt lời ngay: hồi tưởng Frieren bị **mimic** ngoạm, cả nhóm đứng ngoài cân nhắc có nên bỏ cô lại. | "Tụi tôi đã phân vân không biết có nên bỏ cô lại" | hài, đánh úp | 2 |
| 27 | P09-a | Toàn cảnh dân chúng trong lễ hội, tổ đội lẫn trong đám đông. | — | ấm | 1 |
| 28 | P09-b | Frieren cười khẽ: kỷ niệm của cả nhóm toàn là chuyện lố bịch. | "toàn là những kỉ niệm lố bịch không à" | dịu | 2 |
| 29 | P09-c | Himmel đối lại: lố bịch nhưng vui, và anh thấy mình may mắn. | "Thật là may mắn khi tôi được phiêu lưu cùng với các cậu." | **ấm, sẽ dội lại ở P30** | 3 |
| 30 | P09-d | Heiter đáp một tiếng; Frieren mỉm cười. | "Ừm." | lặng | 1 |
| 31 | P10-a | Frieren buột miệng: mười năm ấy hơi ngắn. | "Mặc dù là có hơi ngắn ngủi chút ha." | **lệch thang thời gian** | 3 |
| 32 | P10-b | Nhìn từ sau: cả nhóm đứng giữa phố. | — | chuyển | 1 |
| 33 | P10-c | Himmel sững lại, không hiểu nổi: mười năm mà ngắn? | "Ngắn á?" / "Tận 10 năm lận cơ mà." | ngỡ ngàng | 3 |
| 34 | P10-d | Frieren chỉ Heiter làm ví dụ: anh bạn này đã già khú rồi. Heiter: thô lỗ thật đấy. | "Anh bạn đây đã đến cái tuổi già khú đế rồi đấy nhé." | hài mà lạnh sống lưng | 2 |
| 35 | P10-e | Himmel bồi thêm: cậu ta vốn đã thế từ đầu. Heiter lặp lại y hệt. | "Thô lỗ thật đấy." | hài | 1 |
| 36 | P10-f | Bốn người ngồi trên bờ tường đêm. Frieren nói về quãng đời người: nó sẽ không kéo dài đâu. | "Nó sẽ không diễn ra lâu đâu nhỉ?" | **lạnh, định nghĩa cả bộ** | 3 |
| 37 | P11-a | Heiter chỉ trời: người đời gọi đây là **Kỷ Nguyên Sao Băng** — mưa sao băng 50 năm mới có một lần. | "50 năm một lần" | mở ra mốc thời gian | 3 |
| 38 | P11-b | **KHUNG LỚN TRÀN TRANG.** Bốn tấm lưng trên bờ tường, cả bầu trời kẻ vạch sao băng. Himmel: khởi đầu hoàn hảo cho kỷ nguyên hoà bình. | "Một khởi đầu hoàn hảo cho một kỷ nguyên hòa bình nhỉ." | **choáng ngợp — HOLD** | 3 |
| 39 | P12-a | Himmel ngửa mặt, mắt sáng. | "Tráng lệ thật đấy." | rung động | 2 |
| 40 | P12-b | Frieren dội gáo nước lạnh: ngắm trong thị trấn thì hơi khó. Himmel nhắc cô giữ ý, ai nấy đang xúc động. | "Cậu phải biết giữ ý tứ chứ." | hài | 1 |
| 41 | P12-c | Frieren quay mặt lại, bắt đầu một câu. | "Vậy thì lần tới," | chuyển | 2 |
| 42 | P12-d | **LỜI HẸN.** Frieren nói có một nơi ngắm được rõ hơn hẳn, và 50 năm nữa cô sẽ dẫn cả nhóm tới đó. | "Sau 50 năm nữa," / "khi ấy tôi sẽ dẫn tới đó nhé." | **trục xoay của chương** | 3 |
| 43 | P12-e | Himmel bật cười khe khẽ; Frieren không hiểu, hỏi lại. | "…Haha." / "Sao vậy?" | ấm | 2 |
| 44 | P12-f | Himmel chối, mắt vẫn cười. | "À không." / "Không có gì đâu." | **ấm, thương** | 3 |
| 45 | P13-a | Trời hửng, lâu đài trong sương, sao băng còn vạch cuối. Himmel nhận lời. | "Hãy cùng nhau ngắm nhìn nó nhé." | **chốt giao kèo** | 3 |
| 46 | P13-b | Ngoài cổng, đến lúc chia tay. *(Panel này còn một ô thoại để TRẮNG, nhóm dịch bỏ sót — KHÔNG ĐỌC ĐƯỢC.)* | "Vậy giờ tôi đành phải nói lời từ biệt ở đây rồi." | bịn rịn | 2 |
| 47 | P13-c | Himmel hỏi Frieren định làm gì tiếp. | "Từ giờ cậu tính làm gì vậy?" | chuyển | 1 |
| 48 | P13-d | Frieren nói sẽ học thêm phép thuật, và vốn đã định dành một thập kỉ đi khám phá **các vùng trung tâm**. | "đi khám phá các vùng trung tâm trong một thập kỉ" | bình thản | 2 |
| 49 | P13-e | Cô bước qua cầu gỗ, tay xách va li, buông lại một câu nhẹ như không. | "thỉnh thoảng thì tôi cũng sẽ ló mặt trở về đây thôi" | **nhẹ tênh — chính là chỗ đau** | 3 |

### Khúc 3 — 50 năm của Frieren (P14–P17)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 50 | P14-a | Himmel và Heiter đứng nhìn theo. Hai người tự nhận không đo nổi cảm xúc của **elf**, không biết cô sẽ sống bao lâu. | "Chúng ta vẫn chẳng thể nào cảm nhận được hết cảm xúc của Elf nhỉ." | **hé lộ khoảng cách** | 3 |
| 51 | P14-b | Ô chữ nền xám, không có người: với cô, 50 năm có lẽ chỉ là một ngày thoáng qua. | "chỉ là một ngày thoáng qua đối với cậu ấy mà thôi" | **lạnh, chốt luật chơi** | 3 |
| 52 | P14-c | Frieren một mình đi về căn nhà gỗ giữa rừng. | — | cô độc | 1 |
| 53 | P14-d | Cô đặt giỏ và sách xuống bên gốc cây. | — | chuyển | 1 |
| 54 | P14-e | Trong tiệm, cô nói chuyện với **ông lão bán đồ đeo kính một mắt**. | — | đời thường | 1 |
| 55 | P15-a→i | **Montage 50 năm, CÂM HOÀN TOÀN, 9 panel:** lội tuyết vào thị trấn · ngồi trên phế tích ngửa mặt · đứng giữa hang thạch anh · thả phép thuật hoa cho lũ trẻ trong đồng · trẻ con chơi ngoài quảng trường · câu cá cạnh người tuyết · ngủ gục dưới gốc cây · chúi đầu vào một hòm đá · đứng nhìn xuống vực. | — (không một chữ) | **thời gian trôi — nhịp nghỉ dài** | 2 |
| 56 | P16-a | Căn nhà gỗ trong rừng, cũng cây cũng cửa ấy. Không một chữ. | — | tuần hoàn | 1 |
| 57 | P16-b | Ông lão bán đồ nghe hỏi mua **sừng rồng hắc ám**, lắc đầu, tiệm không bán thứ đó. | "Sừng của rồng hắc ám ấy hà?" | hụt | 1 |
| 58 | P16-c | Ông nói đã 20–30 năm rồi không thấy con rồng hắc ám nào; Frieren lẩm bẩm rắc rối thật, cô định dùng nó làm vật triệu hồi. | "Rắc rối thật ha." | bế tắc | 2 |
| 59 | P16-d | Frieren sực nhớ: cái sừng cô nhặt trong lâu đài Quỷ Vương đã đưa cho Himmel giữ hộ. Hồi tưởng chen vào — có người hỏi thứ đó toả **tà khí**, hại cơ thể người không; Frieren đáp gọn: "Không biết!" | "Có đưa cho Himmel giữ hộ thì phải…" | **kích hoạt cả nửa sau** | 3 |
| 60 | P16-e | Cô tính thêm: Kỷ Nguyên Sao Băng cũng sắp tới, tiện thể ghé lấy luôn. | "Mà kỷ nguyên sao băng cũng sắp tới rồi nhỉ…" | **tiện đường — không phải vì nhớ** | 3 |
| 61 | P17-a | Toàn cảnh lâu đài và mái ngói thị trấn, đã khác đi. | — | thời gian | 2 |
| 62 | P17-b | Frieren đứng giữa phố lát đá, xách va li, ngước nhìn. | "Thị trấn này đã thay đổi đáng kể rồi nhỉ…?" | bỡ ngỡ | 2 |
| 63 | P17-c | Cô đi tìm, nghĩ chắc anh ở quanh đây. Phía xa có một ông già chống gậy. | "Hình như cậu ta ở quanh đây thì phải." | chuyển | 2 |
| 64 | P17-d | Cận mặt Frieren. Một giọng gọi tên cô từ phía sau. | "…Frieren đấy à?" | **khựng lại** | 3 |

### Khúc 4 — Himmel đã già (P18–P21)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 65 | P18-a | Frieren quay lại. Trước mặt là một **ông lão hói, râu bạc dài, chống gậy**. Cô gọi tên anh. | "Himmel…" | **CÚ LẬT LỚN NHẤT NỬA ĐẦU** | 3 |
| 66 | P18-b | Frieren bật ra câu thật thà đến tàn nhẫn; Himmel chibi kêu chua cay. | "Sao trông lọm khọm thế này…" | sốc pha hài | 2 |
| 67 | P18-c | Himmel già cãi lại y như 50 năm trước: già rồi vẫn đẹp trai ngời ngời. | "Chẳng phải tôi vẫn đẹp trai ngời ngời dù cho là đã già đi hay sao?" | **thương — anh không đổi** | 3 |
| 68 | P18-d | Hai người đứng cách nhau trên phố vắng. Himmel: 50 năm rồi, cô chẳng già đi chút nào; anh đã tưởng không còn gặp lại. | "…Tôi cứ ngỡ là mình sẽ không còn được gặp lại cậu nữa ấy chứ." | **nhói** | 3 |
| 69 | P19-a | Trong nhà Himmel: anh ngồi ghế bập bênh bên lò sưởi, Frieren đứng. Nghe chuyện Kỷ Nguyên Sao Băng, anh khen tráng lệ. | "Kỷ nguyên sao băng ấy à…? Thật là tráng lệ nhỉ." | ấm | 2 |
| 70 | P19-b | Frieren hỏi tới thứ cô nhặt trong lâu đài Quỷ Vương; Himmel đọc vanh vách trước khi cô nói hết: sừng rồng hắc ám. | "Là sừng của rồng hắc ám chứ gì." | **anh nhớ, cô không** | 3 |
| 71 | P19-c | Himmel trên ghế: anh chưa từng quên, dù chỉ một chi tiết nhỏ. | "Tôi vẫn chưa từng quên cái đó đâu, dù chỉ là một chi tiết nhỏ đấy." | **nặng** | 3 |
| 72 | P19-d | Cái tủ ngăn kéo đen kịt, **tà khí** rỉ ra thành khói (sfx モワ) — suốt 50 năm. Frieren chibi rụt cổ xin lỗi. | "Do là tà khí nó cứ rỉ ra từ trong ngăn kéo suốt từng ấy năm cơ mà." | hài đen, xót | 3 |
| 73 | P19-e | Frieren quay lưng lại phía tủ, bảo lẽ ra cứ quẳng nó vào nhà kho. | "Mà cậu cứ ném nó vào trong nhà kho, rồi sau đó…" | thực dụng | 2 |
| 74 | P19-f | Himmel cắt ngang, dứt khoát. | "Tôi không thể làm thế được." | **bản lề** | 3 |
| 75 | P20-a | Himmel nói thẳng: với cô nó chỉ là món để lại cho anh mà chẳng nghĩ ngợi gì — nhưng với anh, đó là **báu vật đồng đội thân yêu gửi gắm**. | "một báu vật mà đồng đội thân yêu đã trao cho tôi giữ gìn cẩn thận" | **đỉnh cảm xúc khúc này** | 3 |
| 76 | P20-b | Anh trao lại cái sừng. Rốt cuộc anh cũng trả được. | "Cuối cùng thì tôi cũng đã có thể trả lại cho cậu vật này rồi." | **nhẹ nhõm mà buốt** | 3 |
| 77 | P20-c | Mái ngói thị trấn dưới nắng. Không một chữ. | — | khoảng lặng | 1 |
| 78 | P20-d | Ngoài sân, một con chim lớn vỗ cánh bay khỏi tay Frieren. Giọng lửng: chuyện đó có gì lớn lao đâu. | "Đó có phải là một điều lớn lao gì đâu cơ chứ…" | **chưa hiểu ra** | 3 |
| 79 | P20-e | Frieren đứng trong quảng trường. Giữa quảng trường là một **bệ tượng** có người đứng trên. | — | **đối chiếu P06** | 2 |
| 80 | P21-a | Cô đứng nhỏ xíu dưới chân bệ, ngước lên. | — | lặng | 2 |
| 81 | P21-b | **Cận bức tượng: đúng bốn người.** Frieren cầm trượng, Himmel giơ kiếm, Heiter, Eisen. Đá đã loang lổ vệt thời gian. Lời hứa tạc tượng ở P06 đã thành sự thật — và đã kịp cũ. | — (không một chữ) | **cú đối chiếu lạnh người** | 3 |
| 82 | P21-c | Khung lớn: mặt Frieren nhìn nghiêng, không biểu cảm. | — | trống | 2 |
| 83 | P21-d | Mái nhà thị trấn, trời mây. | — | chuyển | 1 |

### Khúc 5 — Chuyến đi một tuần (P22–P26)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 84 | P22-a | Frieren giục Himmel sửa soạn. | "Vẫn chưa xong à Himmel?" | đời thường | 1 |
| 85 | P22-b | Himmel soi gương; Frieren trêu anh hói rồi thì chải chuốt làm gì. Anh cãi: hói cũng có thanh danh. | "Kể cả người hói thì cũng có thanh danh của mình đấy nhé." | hài, ấm | 2 |
| 86 | P22-c | Ra tới cửa: giờ thì đi ngắm Kỷ Nguyên Sao Băng thôi. | "…Giờ thì cùng đi ngắm kỷ nguyên sao băng thôi nhỉ?" | háo hức | 2 |
| 87 | P22-d | Dưới cổng vòm thành, một bóng người xách hành lý bước vào. | — | chờ đợi | 1 |
| 88 | P22-e | **Heiter và Eisen tới.** Heiter giơ tay chào, Eisen đứng cạnh. | — | tái hợp | 3 |
| 89 | P22-f | Frieren nhận xét Heiter trông chững chạc hẳn. Heiter đáp: giờ đang làm **giám mục trong thánh thành**. | "Thì bởi giờ tôi đang làm giám mục trong thánh thành mà." | **thăng chức — 50 năm của ông** | 3 |
| 90 | P23-a | Heiter xoa đầu Frieren (sfx ぐしぐし), cười ha hả: cô chẳng đổi chút nào. Cô gắt bảo đừng xoa. | "Còn cậu thì vẫn chẳng thay đổi một chút nào nhỉ?" | thân mật | 2 |
| 91 | P23-b | Frieren quay sang Eisen: ông cũng gần như y nguyên — **tộc người lùn** mà. | "Quả là tộc người lùn nhỉ." | **thang thời gian thứ ba** | 2 |
| 92 | P23-c | Heiter hỏi cái nơi ngắm đẹp ấy ở đâu, và có phải khởi hành ngay không — Kỷ Nguyên Sao Băng còn khá lâu mới tới. | "Thế nơi mà chúng tôi có thể ngắm được cảnh đẹp mà cô nói ở đâu đây hà?" | thắc mắc | 2 |
| 93 | P23-d | Frieren: phải đi, vì tới đó mất **một tuần**. | "đi đến đó thì cũng sẽ phải mất đến một tuần đấy…" | **con số then chốt** | 3 |
| 94 | P23-e | Ba ông già méo mặt. | "Xa thật nhỉ." / "Ôi trời…" | hài | 1 |
| 95 | P23-f | Một câu vọng lên từ phía sau mái nhà. | "Đây là ngược đãi người cao tuổi rồi đó." | hài | 1 |
| 96 | P24-a | Bốn người leo đường núi, ba người già lọ mọ phía sau. | — | lên đường | 2 |
| 97 | P24-b | Himmel nhìn quanh, nói thấy như đang sống lại những tháng ngày xưa cũ. | "Cứ như thể là chúng ta đang sống lại những tháng ngày xưa cũ vậy." | **hoài niệm** | 3 |
| 98 | P24-c | Frieren đứng ở biển chỉ đường, cả nhóm quanh cô. | — | đường xa | 1 |
| 99 | P24-d | Bốn người tựa bờ tường đá nhìn dãy núi. Đã từng mạo hiểm qua bao nhiêu nơi. | "Chúng ta đã từng mạo hiểm qua rất nhiều nơi rồi nhỉ?" | ấm | 2 |
| 100 | P24-e | Đi qua một cầu dẫn nước đổ nát phủ cây. | — | chuyển | 1 |
| 101 | P25-a | Lửa trại đêm, nồi treo trên bếp, cả nhóm quây quanh. | — | ấm | 2 |
| 102 | P25-b | Hồi tưởng: trận đánh với một con quái đầu sói. Ký ức vẫn như mới. | "Mọi thứ lập lờ qua mắt tôi giờ cứ như mới vậy." | hào hùng | 2 |
| 103 | P25-c | Bốn người ngồi nghỉ giữa rừng lá đổ. Trong ký ức đẹp ấy luôn có đồng đội. | "Và luôn có cả những đồng đội trong ký ức đẹp đẽ đó nữa." | **ấm sâu** | 3 |
| 104 | P25-d | **Himmel cảm ơn Frieren.** Anh nói đã hằng mong một ngày cả nhóm tụ lại; nhờ có cô mà họ mới có được chuyến phiêu lưu thú vị đến thế. | "Cảm ơn cậu nhé, Frieren." | **lời cảm ơn cuối đời** | 3 |
| 105 | P26-a | **SPREAD TRÀN TRANG.** Bốn tấm lưng trên đỉnh núi tuyết, cả bầu trời là mưa sao băng. Lời hẹn 50 năm đã giữ trọn. Himmel: quả thật là tráng lệ. | "Quả thật là tráng lệ mà." | **CAO TRÀO ĐẸP — HOLD, CẤM CẮT NHỎ** | 3 |

### Khúc 6 — Tang lễ (P27–P31)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 106 | P27-a | Lâu đài và mái ngói dưới trời mây. Không một chữ. | — | chuyển cảnh lạnh | 2 |
| 107 | P27-b | Tháp chuông ba quả chuông. | — | điềm báo | 3 |
| 108 | P27-c | Nhìn từ trên cao: đại sảnh, một **cỗ quan tài** đặt giữa, dân chúng kín hai bên. | — | **cú lật câm** | 3 |
| 109 | P27-d | Heiter mặc lễ phục trắng, ôm sách, chủ lễ. | — (không một chữ cả trang) | trang nghiêm | 3 |
| 110 | P28-a | **Himmel nằm trong quan tài**, phủ hoa hồng trắng, hai tay đặt trên chuôi kiếm. | — | **tang** | 3 |
| 111 | P28-b | Frieren đứng lẫn giữa đoàn người đưa tang, mặt không đổi. | — | trống rỗng | 3 |
| 112 | P28-c | Heiter bên cạnh: chắc hẳn Himmel đã thấy rất vui. | "Chắc hẳn là Himmel đã thấy rất vui đấy." | dịu | 2 |
| 113 | P28-d | Frieren đáp đúng hai chữ cô từng dùng ở P03. | "Có lẽ thế…" | **lặp nguyên văn — đổi nghĩa** | 3 |
| 114 | P29-a | Cận đám đông: người khóc nấc, người che miệng, người đỏ mắt. | — | tang thương | 2 |
| 115 | P29-b | Một người nhận ra Frieren giữa đám đông. | "Cô gái đó là một trong những đồng đội của Himmel-sama à?" | xì xào | 2 |
| 116 | P29-c | Hai người đàn bà thì thầm: không lộ chút thương tiếc nào, đúng là vô cảm. | "Đúng thật là vô cảm mà." | **cáo buộc** | 3 |
| 117 | P29-d | Cận mặt Frieren, mắt mở, không một biểu cảm. | — | **trống** | 3 |
| 118 | P30-a | Heiter đỡ lời giùm cô: bọn tôi cũng có khóc gì đâu. | "Nào nào, chúng tôi cũng có khóc thương gì đâu." | bênh vực | 2 |
| 119 | P30-b | Eisen phang Heiter một phát (sfx カーン) mắng ông giám mục phải nghiêm túc; Heiter cười ha hả khen dữ dội. | "Giám mục à, hãy nghiêm túc hơn đi chứ!" / "Cái đồ vô cảm này!" | hài giữa đám tang | 2 |
| 120 | P30-c | Mặt Frieren chìm trong bóng tối, giọng vỡ ra. | "…Nhưng mà tôi… không hề biết một chút gì về người này hết…" | **CAO TRÀO CẢM XÚC** | 3 |
| 121 | P30-d | Heiter nghiêng mặt, mỉm cười, không nói gì. | — | thấu hiểu | 2 |
| 122 | P30-e | **Khung lớn: Frieren bật khóc**, nước mắt rơi. Mười năm phiêu lưu — chỉ có thế. | "Tôi chỉ đơn thuần là phiêu lưu cùng với người ấy trong 10 năm mà thôi…" | **ĐỈNH CỦA CHƯƠNG** | 3 |
| 123 | P31-a | Cận mặt Frieren đẫm nước mắt, ký ức tràn về. | — | vỡ | 3 |
| 124 | P31-b | Mảnh ký ức: Himmel đứng, Heiter phía sau. | — | ký ức | 2 |
| 125 | P31-c | Mảnh ký ức: cả nhóm giáp mặt một con quái khổng lồ. | — | ký ức | 2 |
| 126 | P31-d | Mảnh ký ức: trong quán, Himmel và Heiter cười với cô. | — | ký ức ấm | 2 |
| 127 | P31-e | Mảnh ký ức: lửa trại trong rừng, cả nhóm quây quần. | — | ký ức ấm | 2 |
| 128 | P31-f | Ô nhỏ, nền trắng: tấm lưng Himmel đi xa dần rồi nhạt đi. | — | **mất** | 3 |
| 129 | P31-g | Khung lớn cuối trang: Frieren gục đầu, nước mắt nhỏ xuống. Cô biết đời người ngắn — mà chưa từng nghĩ tới chuyện thân thiết hơn với anh. | "…nhưng cớ sao tôi lại chưa hề nghĩ đến chuyện thân thiết hơn với cậu ấy chứ..?" | **CÂU LUẬN ĐỀ CỦA CẢ BỘ** | 3 |

### Khúc 7 — Chia tay Heiter, chia tay Eisen (P32–P37)

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 130 | P32-a | Heiter đặt tay lên đầu Frieren, Eisen đứng bên, ba người ở khung cửa. | — | chở che | 2 |
| 131 | P32-b | Frieren để yên cho xoa, chỉ càu nhàu. | "Đừng có xoa đầu tôi nữa mà…" | **mềm hơn trước** | 3 |
| 132 | P32-c | Bên cỗ xe ngựa, Heiter nói sẽ về lại thánh thành. | "Thế thì giờ chắc là tôi sẽ trở về thánh thành vậy." | chia tay | 2 |
| 133 | P32-d | Heiter bảo hai người chịu khó ló mặt thăm nhau — có thể đây là cơ hội cuối cùng. | "Có thể đây sẽ là cơ hội cuối cùng đấy." | **báo trước cái chết** | 3 |
| 134 | P32-e | Frieren hỏi thẳng ông có bệnh gì không. | "Cậu bị đau yếu gì à?" | lo | 2 |
| 135 | P32-f | Heiter nhận: mấy chục năm rượu chè đã bào mòn ông. Cười, gọi đó là hình phạt dành cho Frieren. | "những năm tháng uống rượu triền miên đã làm tôi suy yếu mất rồi" | **cười mà đắng** | 3 |
| 136 | P33-a | **LỜI DẶN.** Quay lưng bước đi, Heiter dặn nếu có ngày cô ghé thánh thành thì rót cho mộ ông chút rượu. | "thì hãy biểu cho mộ của tôi chút rượu nhé" | **gieo hạt cho C2** | 3 |
| 137 | P33-b | Frieren hỏi lại: ông không sợ chết sao. | "…Cậu không e sợ cái chết sao, Heiter?" | thẳng thắn | 3 |
| 138 | P33-c | Khung lớn, không thoại: mặt Heiter nghiêng, cười. | — | **khoảng lặng có trọng lượng** | 3 |
| 139 | P33-d | Heiter đáp: nhóm anh hùng cứu cả thế giới thì sang bên kia chắc chắn được sống xa hoa trên thiên đàng. | "Chúng ta là một nhóm anh hùng mà đã giải cứu thế giới này mà." | đùa mà thật | 3 |
| 140 | P33-e | Ông nhắm mắt cười: đó chính là cái lợi ích ông đã chọn khi đi đánh nhau cùng họ. | "Đây chính là lợi ích mà tôi đã chọn khi chiến đấu cùng với mấy cậu đấy." | **định nghĩa đức tin của ông** | 3 |
| 141 | P34-a | Từ cửa sổ xe ngựa, Frieren buông lại đúng câu cũ; Heiter cười đúng tiếng cười cũ. | "Đồ tư tế thúi." / "HAHAHA." | **LẶP NGUYÊN VĂN P06** | 3 |
| 142 | P34-b | Cận mặt Heiter qua ô cửa: thế thì giờ, tôi đi trước nhé. | "Thế thì giờ," / "tôi đi trước nhé." | **câu từ biệt hai nghĩa** | 3 |
| 143 | P34-c | Cỗ xe nhỏ dần rồi khuất vào thung lũng. Frieren và Eisen đứng nhìn theo. | — | chia lìa | 2 |
| 144 | P34-d | Còn lại hai người trên con đường đất, xa xa là một thành trì. | "Giờ thì." | chuyển | 1 |
| 145 | P34-e | Frieren nói cô cũng nên đi ngay. | "Tôi cũng nên đi ngay vậy." | chuyển | 2 |
| 146 | P35-a | Lội qua suối, Eisen hỏi có phải lại lên đường học phép thuật. Frieren: ừm, đó là một chuyện, và còn nữa… | "Ừm. Đó là một chuyện, và ngoài ra thì…" | chuyển | 2 |
| 147 | P35-b | **QUYẾT ĐỊNH CỦA CHƯƠNG.** Frieren ngước lên, mặt sáng: cô sẽ cố gắng hiểu thêm về con người hơn trước kia. | "Tôi nghĩ là mình sẽ cố gắng hiểu thêm về con người hơn trước kia vậy." | **cú lật chủ đề** | 3 |
| 148 | P35-c | Eisen nghe, đáp hai chữ. | "Vậy à." | điềm nhiên | 1 |
| 149 | P35-d | Frieren ngoái lại rủ Eisen: cô là pháp sư, có một **tiên phong** mạnh đi cùng thì tiện — và còn muốn nhờ ông **một chuyện nữa**. | "tôi cũng muốn nhờ cậu một chuyện nữa…" | **gieo hạt chưa gặt** | 3 |
| 150 | P36-a | Eisen quay lưng về phía núi, xin lỗi. | "Xin hãy thứ lỗi cho tôi nhé." | **từ chối** | 3 |
| 151 | P36-b | Cận mặt Eisen, râu trắng phủ kín: ông không còn ở độ tuổi vung nổi rìu như xưa. | "Tôi không còn ở cái độ tuổi mà có khả năng vung rìu như trước nữa rồi." | **già — kể cả tộc người lùn** | 3 |
| 152 | P36-c | Frieren ngoái đầu nhìn, không nói. | — | hụt hẫng | 2 |
| 153 | P36-d | Eisen bảo cô đừng ngạc nhiên thế. | "Xin đừng ngạc nhiên như thế, Frieren à." | điềm tĩnh | 2 |
| 154 | P36-e | Ông khoanh tay: bất ngờ là về già thì cuộc sống lại trôi chậm hơn. | "cuộc sống này lại trôi chậm hơn sau khi già đi đấy" | **đối trọng với thời gian của elf** | 3 |
| 155 | P36-f | Frieren đáp đúng hai chữ cũ. | "…Thế à." | **lặp lại — cô vẫn chưa hiểu hết** | 3 |
| 156 | P37-a | Frieren chào tạm biệt, gọi tên ông. | "Vậy thì hẹn gặp lại nhé." / "Eisen." | chia tay | 3 |
| 157 | P37-b | Eisen đáp lại y hệt. *(Trang in số "37" ở góc dưới.)* | "Ừm." / "Hẹn gặp lại." | chia tay | 2 |
| 158 | P37-c | **KHUNG CUỐI, CÂM.** Con đường đất chạy giữa đồi. Frieren đã đi xa, nhỏ dần. Lưng Eisen đứng nguyên ở tiền cảnh, nhìn theo. | — (không một chữ) | **cú chốt lạnh — bắt đầu chuyến đi mới** | 3 |

---

## C. Điểm cao trào

Chương này có **nhiều đỉnh**, không phải một. Xếp theo sức nặng:

**C1. Đỉnh cảm xúc — Frieren bật khóc ở tang lễ (P30-c → P31-g).**
Dân chúng gọi cô vô cảm (P29-c). Cô không cãi. Rồi giọng vỡ ra:
*"…nhưng mà tôi… không hề biết một chút gì về người này hết…"* → khung lớn nước mắt:
*"Tôi chỉ đơn thuần là phiêu lưu cùng với người ấy trong 10 năm mà thôi…"* →
và câu luận đề của cả bộ ở P31-g: *"…nhưng cớ sao tôi lại chưa hề nghĩ đến chuyện thân thiết hơn
với cậu ấy chứ..?"* Đây là điểm dừng dài nhất nên để cho lời kể.

**C2. Đỉnh hình ảnh — spread mưa sao băng trên đỉnh núi (P26).**
Lời hẹn 50 năm ở P12-d được giữ trọn. Một câu duy nhất: *"Quả thật là tráng lệ mà."*
Khung tràn hai trang → **HOLD, không cắt nhỏ**.

**C3. Cú lật giữa chương — Himmel đã già (P18-a).**
Cô quay lại đúng như đã nói ở P13-e ("thỉnh thoảng thì tôi cũng sẽ ló mặt trở về đây thôi").
Người đứng đó là một ông lão hói chống gậy. Toàn bộ khúc 1–2 bị đổi nghĩa từ khung này trở đi.

**C4. Cú lật câm — tang lễ (P27).**
Cả trang **không một chữ nào**: tháp chuông → đại sảnh nhìn từ trên với cỗ quan tài → Heiter chủ lễ.
Truyện không báo trước một câu nào. Đây là chỗ lời kể phải im.

**C5. Đỉnh ngầm — cái sừng trong ngăn kéo (P19-d → P20-b).**
Với Frieren đó là món đồ bỏ quên; với Himmel là *"báu vật mà đồng đội thân yêu đã trao cho tôi
giữ gìn cẩn thận"* — giữ 50 năm trong nhà, chịu **tà khí** rỉ ra suốt từng ấy năm. Hai thang giá trị
va vào nhau, và chỉ một bên biết.

**C6. Cú lật cuối — quyết định + lời từ chối (P35-b → P37-c).**
Frieren chốt: *"Tôi nghĩ là mình sẽ cố gắng hiểu thêm về con người hơn trước kia vậy."*
Cô rủ Eisen làm **tiên phong** và nói còn *"muốn nhờ cậu một chuyện nữa"* — rồi Eisen từ chối
vì đã quá già để vung rìu. Chương đóng bằng khung câm: cô đi xa dần, ông đứng nhìn theo.
**Chuyện nhờ vả ấy là gì thì chương không nói.**

**Ba cú lặp nguyên văn cần giữ khi viết lời kể (đây là kỹ thuật chính của chương):**
- *"Có lẽ thế."* — Frieren nói với Himmel lúc còn trẻ (P03-f) → nói bên quan tài anh (P28-d).
- *"Đồ tư tế thúi." / "HAHAHA."* — đêm ăn mừng (P06-d) → lần cuối tiễn Heiter (P34-a).
- *"Chẳng phải tôi vẫn đẹp trai ngời ngời…"* — Himmel trẻ khoe tạc tượng (P06-a/b) → Himmel già nói y hệt (P18-c),
  rồi bức tượng ấy đứng loang lổ ở P21-b.

---

## D. Chưa rõ — KHÔNG ĐOÁN

**D1. Chữ không đọc được / bản dịch thiếu**
- **P13, panel b**: một ô thoại **để trắng hoàn toàn**, nhóm dịch bỏ sót. **KHÔNG ĐỌC ĐƯỢC** — không được điền.
- **P16-c**, dòng chữ viết tay nhỏ cạnh Frieren: đọc được là *"Tôi tính dùng nó để làm vật triệu hồi ấy mà…"*
  nhưng chữ mờ, độ chắc trung bình. **Nếu lời kể cần dùng, phải soi lại ảnh gốc.**
- **P08**, các bong bóng hồi tưởng chữ nhỏ viết tay ("Làm luôn đi.", "Hay là để tôi liếm giày người nhé?",
  "Oáiiiii!", "Đáng sợ quá!", "Tôi quá!"): đọc được nhưng **không rõ câu nào của ai**.

**D2. Ai nói câu nào — chưa chắc chắn**
- **P06-b**, câu *"Lão ta quả là một kẻ toan tính mà, cho chúng ta có đúng 10 đồng khi bắt đầu cuộc hành trình này"*:
  bong bóng không có đuôi chỉ rõ người nói. Suy theo mạch (Heiter dỗ *"Nào nào, Frieren"* ngay sau đó)
  thì là **Frieren**, nhưng **chưa chắc 100%**.
- **P07-b**, hai bong bóng *"Ừm, kết thúc rồi."* và *"Đây là dấu chấm hết cho cuộc hành trình của chúng ta."*:
  nhiều khả năng **cùng của Himmel**, nhưng có thể một câu là của Heiter. **Đừng gán tên trong lời kể.**
- **P10-f**, câu *"Nó sẽ không diễn ra lâu đâu nhỉ?"*: ngữ cảnh chỉ về đời người, người nói gần như chắc là
  **Frieren**, nhưng khung vẽ cả bốn người từ sau lưng nên **không xác minh được bằng hình**.
- **P25-b**, *"Mọi thứ lập lờ qua mắt tôi giờ cứ như mới vậy."*: chữ "tôi" là ai — **chưa rõ**.

**D3. Nhân vật / quan hệ chưa lộ trong C1**
- **Tên nhà vua** và **tên vương quốc**: không có. **Tên đô thành** cũng không có.
- **Ông lão bán đồ** (P14-e, P16-b/c): **không tên**. Đừng đặt biệt danh.
- **Quỷ Vương**: **không lên hình một khung nào trong C1**, không thoại, không tên riêng. Chỉ được nhắc.
  **Lâu đài Quỷ Vương** cũng chỉ được nhắc (P16-d, P19-b), không có khung nào vẽ nó.
- **Tuổi Frieren**, tuổi thọ elf, quê quán, ai dạy cô phép thuật: **không có**.
- **Họ của cả bốn người**: **không có**.
- **Fern chưa xuất hiện** trong C1 (ra mắt ở C2-P04). Không được nhắc trước.
- **Ewig**, **sách ma thuật**, **Thánh Thành Strahl** (tên riêng), **ma lực**, **pháp sư tập sự**:
  **không xuất hiện trong C1** — đều là từ của C2. Không được kéo ngược vào lời kể C1.
  C1 chỉ có "thánh thành" viết thường (P22-f, P32-c, P33-a).

**D4. Chi tiết mơ hồ trong chính C1**
- **Himmel chết vì gì, chết lúc nào**: truyện **không nói**. Giữa P26 (mưa sao băng) và P27 (tang lễ)
  **không có một khung chuyển nào** — không rõ cách bao lâu. Không được đoán.
- **Himmel cười gì ở P12-e/f** (*"…Haha." / "À không. Không có gì đâu."*): **chương không giải thích.**
- **"Một chuyện nữa" Frieren muốn nhờ Eisen** (P35-d): **không nói ra**. Chương đóng lại mà vẫn treo.
- **Nơi ngắm mưa sao băng** ở P12-d / P26: **không có tên**, chỉ biết đi mất một tuần và ở trên núi tuyết.
- **Con chim lớn ở P20-d**: không rõ là chim gì, của ai, có ý nghĩa gì. Chỉ mô tả "một con chim lớn".
- **Bức tượng ở P20-e / P21-b**: thấy rõ **bốn người** (Frieren cầm trượng, Himmel giơ kiếm, Heiter, Eisen)
  nhưng **không đọc được chữ trên bệ**. Không được bịa dòng chữ khắc.
- **Con quái ở P25-b** (đầu như sói) và **con quái ở P31-c**: **không có tên** trong truyện.
- **Frieren định làm gì với sừng rồng hắc ám**: chỉ có một dòng chữ nhỏ mờ ở P16-c về "vật triệu hồi".
  Không rõ triệu hồi cái gì, để làm gì. **Không suy diễn.**
- **Tương quan tuổi Eisen**: P23-b nói ông "không thay đổi gì mấy" vì là tộc người lùn, nhưng P36-b
  ông lại nói đã quá già để vung rìu. **Hai chi tiết này truyện để cạnh nhau mà không giải thích** —
  giữ nguyên cả hai, đừng gộp thành một kết luận.

**D5. Kỹ thuật, cần người quyết**
- **P04** và **P26** là **spread ngang 900×646**. Dựng khung dọc 9:16 phải **cắt theo panel/vùng và zoom**,
  hoặc pan ngang. Thả nguyên trang là không nhìn được gì.
- **P15** (9 panel câm) và **P21** (4 panel câm) là hai chỗ có thể **nén mạnh hoặc giãn mạnh** tuỳ ngân sách
  1.470–1.680 từ. Cần chốt trước khi viết lời.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** 166 panel trên 35 trang nội dung, đánh số theo chiều **phải → trái**
   (bằng chứng ở mục A3). Có panel nào anh thấy tôi đọc sai vị trí hoặc gộp/tách nhầm không?
2. **Tên nhân vật đúng chưa?** Toàn bộ dùng Frieren · Himmel · Heiter · Eisen theo bible; **Quỷ Vương**
   thay cho "Ma Vương" của bản dịch P03; **không** nhắc Fern, Ewig, sách ma thuật, ma lực, Strahl
   (đều là của C2). Ổn chưa?
3. **Trọng số hợp lý chưa?** Tôi để **C1 (Frieren khóc, P30-c→P31-g)** và **C2 (spread mưa sao băng, P26)**
   là hai đỉnh lớn nhất, và **P27 (tang lễ câm)** là chỗ lời kể phải im hẳn. Anh có muốn đổi trọng số
   khúc nào không — nhất là khúc **P15** (montage 50 năm) hiện chỉ để TS 2?

**Chưa viết lời kể. Chưa sang `/manga-narration`.**
