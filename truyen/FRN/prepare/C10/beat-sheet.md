# BEAT SHEET — FRN Chapter 10 · "Rồng thái dương"

Nguồn: `truyen/FRN/prepare/C10/pages-clean/` · 26 file · đọc hết P01→P26, không nhảy cóc.
Tên và thuật ngữ theo `truyen/FRN/series-bible.md`. **CHƯA viết lời kể.**

---

## A. Kiểm tra đầu vào

### A1. Danh sách ảnh đã nhận

| File | Kích thước sạch | Gốc | Bị cắt | Phân loại |
|---|---|---|---|---|
| FRN_C10_P01.jpg | 900×585 | 900×1075 | **490px** (y0–460, y460–490) | **BỎ** — banner quảng cáo các bộ + logo 7 Fingers Team |
| FRN_C10_P02.jpg | 900×720 | 900×720 | 0 | **BỎ** — trang credit 7 Fingers Team (TRANSLATOR/EDITOR/PROOFREADER/QC: Credemoe, Yahari) |
| FRN_C10_P03.jpg | 900×1291 | 900×1291 | 0 | Nội dung — trang tên chương |
| FRN_C10_P04 … P24 (21 file) | 900×1291 | 900×1291 | 0 | Nội dung |
| FRN_C10_P25.jpg | 900×470 | 900×470 | 0 | **BỎ** — banner "12 FINGERS TEAM" |
| FRN_C10_P26.jpg | 900×1351 | 900×1857 | **506px** (đáy) | **GIỮ** — tranh màu minh hoạ, có chữ ký hoạ sĩ ở góc phải dưới |

**Không thiếu trang nào.** P01→P26 liên tục, đánh số đều. Không cần CẢNH BÁO/DỪNG.

**Số trang in trên ảnh = số thứ tự file − 2** (P04 in "2", P24 in "22") — đúng như bible ghi.
→ **22 trang truyện: P03–P24.**

### A2. Vụ clean-pages cắt 1026px — đã kiểm, KHÔNG mất nội dung truyện

Chạy lại `clean-pages.py --dry-run` cho ra:

```
FRN_C10_P01.jpg  bỏ  490px / 1075  [y0-460 y460-490]
FRN_C10_P26.jpg  bỏ  536px / 1857  [y1351-1857 y1811-1841]
26 trang · sửa 2 · bỏ tổng 1026px
```

**Con số 1026 là số đếm trùng.** Hai khoảng của P26 **chồng nhau** (y1811–1841 nằm trong
y1351–1857) nên script cộng dồn 536px, còn chiều cao thật chỉ giảm 506px.
Tổng cắt thật = 490 + 506 = **996px**.

**Vì sao gấp đôi các chương khác (~520px):** các chương trước chỉ có **một** trang dính banner
đồ hoạ lớn. C10 dính **hai** — P01 (banner truyenqqq.com nền hồng, nằm TRÊN dòng promo → luật B)
và P26 (banner truyenqqq.com nền xanh ở đáy → luật `bottom_banner`). Không phải layout chrome lạ,
chỉ là hai trang cùng bị bắt.

**Đã mở ảnh gốc `pages/` để đối chiếu từng vùng bị cắt:**

- P01, vùng y0–490: banner "CẬP NHẬT CHƯƠNG MỚI SỚM NHẤT TẠI WEBSITE / TRUYENQQQ.COM" (nền
  hồng, dàn nhân vật Naruto/Deku/…) + dòng "TRUY CẬP NGAY TRUYENQQQ.COM ĐỂ ỦNG HỘ NHÓM DỊCH".
  → **rác site, cắt đúng.**
- P26, vùng y1351–1857: đúng banner đó phiên bản nền xanh + dòng promo.
  → **rác site, cắt đúng.**

**Kết luận: không trang nào bị cắt lố mất nội dung truyện.**

### A3. Lệch khuôn so với ghi chú "P01, P02 và trang CUỐI là banner"

Khuôn lặp được nêu (900×585, 900×720, 900×946) **đúng 2/3 ở C10**:

- P01 = 900×585 ✅ banner · P02 = 900×720 ✅ credit → **BỎ cả hai, đã kiểm mắt.**
- Trang banner cuối **KHÔNG phải P26 và KHÔNG phải 900×946**. Ở C10 nó là **P25 = 900×470**
  ("12 FINGERS TEAM", cùng mẫu bảng đen/Komi-san như C1-P38 và C2-P37). → **BỎ P25.**
- **P26 (900×1351) KHÔNG phải banner** — là **tranh màu minh hoạ ngoài truyện**: Frieren ngồi
  trên bệ cửa sổ một thành cổ, nhìn ra tháp mái đỏ, chiếc va-li đặt dưới sàn; góc phải dưới có
  chữ ký của hoạ sĩ. Không có chữ nhóm dịch, không có logo site.
  → **GIỮ.** Đây là trang màu duy nhất của chương, ưu tiên làm thumbnail (bible mục 5).
  → **Cần sửa bảng "trang phải bỏ" trong series-bible: C10 bỏ P01, P02, P25 — không bỏ P26.**

### A4. Chiều đọc: PHẢI → TRÁI (manga Nhật) — bằng chứng

1. **Số trang in luân phiên theo gáy phải.** Trang in số CHẴN (P04="2", P06="4", P08="6",
   P10="8", P12="10"…) đặt ở mép **TRÁI** dưới; trang in số LẺ (P05="3", P07="5", P09="7",
   P11="9", P13="11"…) đặt ở mép **PHẢI** dưới. Đây là kiểu đóng gáy bên phải.
2. **SFX katakana không bị lật:** プス (P06), しゅぱーん (P18), ドォーン (P22), パチパチ (P22–P23)
   đều đọc xuôi → bản scan chưa bị mirror.
3. **P03 còn nguyên tiêu đề dọc tiếng Nhật** 葬送のフリーレン, cột chữ xếp từ phải sang.
4. **Logic hỏi–đáp chỉ chạy được khi đọc phải→trái:**
   - P05 khung trên: bong bóng PHẢI "Nhưng mà sao một nơi như thế này mà lại…" → bong bóng TRÁI
     "Loài rồng thường sử dụng các vật phẩm chứa ma lực để làm tổ ấy mà."
   - P17 cột phải: "Nếu cậu có thể giữ chân được nó trong 30 giây…" → khung dưới "Ra vậy. 30 giây à."
     → sang khung TRÁI "…kinh nghiệm chiến đấu với quái vật của cậu là bao nhiêu vậy?"
     → lật trang P18: "**LÀ KHÔNG!!!**". Đọc ngược thì chuỗi này vô nghĩa.

### A5. Ai là ai trong chương này (dễ nhầm — đã soi kỹ)

- **Frieren**: **tai nhọn**, áo khoác trắng cổ kẻ sọc, tóc bạc buộc hai túm. Trong C10 cô
  **thấp hơn Fern**.
- **Fern**: đã lớn, **cao hơn Frieren**, tóc dài thẫm màu, áo choàng đen, **cầm gậy phép** và
  luôn xách một chiếc **va-li**. Người bắn phép ở P05 là Fern, không phải Frieren.
- Nhầm hai người này là lỗi chí mạng của chương — kiểm bằng tai nhọn, không bằng chiều cao.

---

## B. Beat Sheet

Ký hiệu: `P{file}-{a,b,c…}` theo thứ tự đọc **phải→trái, trên→dưới**.
TS = trọng số (3 = khoảnh khắc quyết định · 1 = panel chuyển tiếp).

| # | Panel | Sự việc | Câu thoại chốt | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P03-a | Trang tên chương. Toàn cảnh hẻm núi phủ cây; Frieren và Fern đi trên lối mòn nhìn lên vách đá. | "Chương 10 · Rồng thái dương" | tĩnh, mở màn | 2 |
| 2 | P04-a | Khung toàn cảnh hẻm núi có suối chảy. Hai ô dẫn truyện định vị thời gian và nơi chốn. | "28 năm đã trôi qua kể từ lúc Anh hùng Himmel qua đời." | trầm, mốc thời gian | 3 |
| 3 | P04-b | Frieren và Fern nép bên mép vách, nhìn xuống lòng hẻm núi. | — | rình, thận trọng | 1 |
| 4 | P04-c | Dưới đáy hẻm: một con rồng nằm cạnh cái tổ. Fern lần đầu thấy rồng. | "Là rồng kìa…" / "Lần đầu tiên em thấy đấy." | ngạc nhiên | 2 |
| 5 | P04-d | Cận cảnh cái tổ: chất đầy vật phẩm, trong đó có một cuốn sách. Frieren nhận ra đúng thứ mình tìm. | "Có một cuốn sách phép thuật ha. Cũng là cái mà ta đang tìm kiếm đó." | hớn hở kiểu Frieren | 3 |
| 6 | P05-a | Hai người đi trong rừng đá. Fern thắc mắc, Frieren giải thích tập tính làm tổ của rồng. | "Loài rồng thường sử dụng các vật phẩm chứa ma lực để làm tổ ấy mà." | giảng giải, thong thả | 2 |
| 7 | P05-b | Cận cảnh đầu con rồng — vảy dày, sừng cong. | — | uy hiếp | 2 |
| 8 | P05-c | Frieren gọi đúng tên loài; Fern đề xuất diệt luôn. | "Rồng thái dương à. Là loại mà sẽ nuốt chửng tất cả những mạo hiểm giả mà nó bắt gặp đấy." | tỉnh bơ | 3 |
| 9 | P05-d | Frieren dặn Fern đừng làm hỏng cái tổ; Fern đáp gọn. | "Cố đừng để cái tổ dính đòn theo nhé." / "Vâng ạ." | công việc, khô | 2 |
| 10 | P05-e | Fern bắn một luồng phép xuyên qua hẻm núi. | — | dứt khoát | 3 |
| 11 | P06-a | Con rồng đứng nguyên, chỉ bốc khói lèo tèo. Đòn phép không ăn thua. | SFX プス プス | hụt | 3 |
| 12 | P06-b | Fern báo cáo, Frieren bình luận nhẹ tênh. | "…Frieren-sama, hình như là không hiệu quả lắm ạ…" / "Loài rồng quả là cứng cáp thật đấy nhỉ." | tréo ngoe, hài | 2 |
| 13 | P06-c | Frieren tuyên bố rút lui — và bỏ chạy trước, để Fern đứng lại. | "Thôi thì chẳng còn cách nào khác nữa rồi, chạy thôi." | hài, trắng trợn | 3 |
| 14 | P06-d | Con rồng dựng thẳng người, đổ bóng xuống Fern đang đứng một mình. | — | nguy cấp | 3 |
| 15 | P06-e | Cận mặt Fern, tóc bay, nắm tay siết lại — vừa nhận ra mình bị bỏ lại. | "Ơ?" | chưng hửng | 3 |
| 16 | P07-a | Khung rừng rộng, chim bay — đã thoát. | — | hạ nhiệt | 1 |
| 17 | P07-b | Frieren đứng phân tích, Fern ngồi bệt thở dốc. | "Nó bay cũng lẹ nữa, nên có lẽ đánh trên không sẽ chỉ tổ tốn sức đấy." | kiệt sức vs. thản nhiên | 2 |
| 18 | P07-c | Fern nghiêng mặt, nói khẽ. | "Em cứ ngờ là mình đã chết rồi chứ…" | hờn, mệt | 2 |
| 19 | P07-d | Frieren rủ quay lại thử tiếp, lý luận rằng cứ thế sớm muộn cũng hạ được. | "Vậy giờ chúng ta quay lại nhé?" | lì lợm | 2 |
| 20 | P07-e | Cận mặt Fern, gân giận nổi lên, nhìn thẳng. | — | giận nín | 3 |
| 21 | P07-f | Frieren lùi bước, tự nhận cách làm sai. | "…Đúng rồi ha. Chơi đuổi bắt với loài rồng đâu phải là cách của một pháp sư chứ nhỉ." | chịu thua | 2 |
| 22 | P08-a | Hai người nhìn sang ngôi làng bên kia hẻm núi. Frieren kết luận cần thêm người. | "Có lẽ là phải nhẫn nại và cần tiếp nhận thêm bạn đồng hành rồi…" | chuyển hướng | 3 |
| 23 | P08-b | **Hồi tưởng — đêm cắm trại.** Bên đống lửa: Frieren ngồi, một **người lùn đội mũ sừng** ngồi đối diện, một người ngủ trong túi ngủ. | "Tiên phong à?" | đêm, trầm | 2 |
| 24 | P08-c | Người lùn xác nhận đúng thứ Frieren đang cần. | "Cô đang muốn tìm một người như thế, đúng chứ?" / "Phải." | thống nhất | 2 |
| 25 | P08-d | Người lùn mách tên và chỗ ở. **Lần đầu cái tên Stark xuất hiện.** | "Có một chiến binh tên là Stark sống trong một ngôi làng ở gần hẻm núi Riegel đấy." | giới thiệu | 3 |
| 26 | P08-e | Người lùn nói rõ quan hệ. | "Đó là học trò của tôi đấy." | gọn, có sức nặng | 3 |
| 27 | P08-f | Cận mặt nghiêng Frieren, lắng nghe. | — | ghi nhận | 1 |
| 28 | P09-a | Frieren đứng bên lửa trại hỏi tiếp về Stark. | "Hừm, cậu ta là một chiến binh tốt chứ?" | thăm dò | 2 |
| 29 | P09-b | Cận mặt người lùn — mắt nghiêm, không đáp ngay. Cắt cảnh ở đây. | — | treo lửng | 3 |
| 30 | P09-c | Hiện tại: quảng trường làng, dân làng đi lại, hàng quán, trẻ con. | — | yên bình | 1 |
| 31 | P09-d | Fern nhận xét làng quá yên so với việc có rồng ở gần; Frieren ậm ừ. | "Nơi đây yên bình đến mức khó có thể tin rằng lại có một con rồng sống gần đây đấy ạ." | nghi hoặc | 2 |
| 32 | P09-e | Fern hỏi sách trong tổ rồng chép phép gì; Frieren trả lời thật. | "Phép thuật làm cho quần áo trong suốt ấy mà." | tấu hài khô | 3 |
| 33 | P09-f | Fern chốt hạ về gu sưu tầm của Frieren; Frieren không chối. | "Frieren-sama chỉ toàn thu thập những phép thuật kỳ quái không thôi nhỉ?" / "Thì đó là thú vui của ta mà." | ngán ngẩm | 2 |
| 34 | P09-g | Cận mặt Fern, vô cảm nhìn thẳng. | — | bất lực | 2 |
| 35 | P10-a | Frieren còn đang biện hộ cho món phép đó thì một dân làng cắt ngang. | "Du khách à, các vị có thể dành ra chút thời gian được không?" | cắt ngang | 2 |
| 36 | P10-b | Một bà lão nhỏ người nhắc tới Stark. | "Stark-sama có chuyện muốn nói với các vị đấy." | mở nút | 3 |
| 37 | P10-c | Frieren thấy khỏi phải đi tìm nữa. | "…Có vẻ như là chúng ta không cần phải tốn sức tìm kiếm cậu ta nữa rồi nhỉ?" | may mắn | 2 |
| 38 | P10-d | Ba người đi trong rừng, bà lão dẫn đường. | — | chuyển cảnh | 1 |
| 39 | P10-e | Bà lão bắt đầu kể chuyện làng. | "Con rồng đó đã tấn công ngôi làng này gần 3 năm nay rồi." | kể, nặng | 3 |
| 40 | P10-f | **Hồi tưởng của làng:** con rồng khổng lồ đứng giữa làng trong mưa, cúi đầu xuống mái nhà. | — | kinh hoàng | 3 |
| 41 | P10-g | Một người phụ nữ ôm chặt đứa trẻ, ngồi bệt dưới mưa. | — | sợ, bất lực | 3 |
| 42 | P11-a | Stark xuất hiện giữa mưa, vác rìu lớn, đứng chắn giữa rồng và dân làng. | "Vào lúc đó, Stark-sama đã xuất hiện trước mặt chúng tôi." | anh hùng | 3 |
| 43 | P11-b | Lưng Stark bất động trước con rồng; nhìn nhau một hồi rồi rồng bỏ đi. | "Ngài ấy không rời một bước trước con rồng đó," / "Và sau khi nhìn chằm chằm một hồi, thì con rồng đã bỏ đi." | sững sờ, tôn kính | 3 |
| 44 | P11-c | Bà lão kết chuyện: nhờ Stark ở lại mà làng yên tới giờ. | "…nhờ vào việc ngài ấy quyết định sống ở đây, mà chúng tôi không còn bị rồng tấn công…" | biết ơn | 2 |
| 45 | P11-d | Frieren và Fern im lặng nghe. | "……" | dè dặt | 2 |
| 46 | P11-e | Fern suy ra kết luận hiển nhiên. | "Thế nếu chúng ta chiêu mộ được Stark-sama, thì sẽ có thể hạ gục được con rồng đó phải không ạ?" | hy vọng | 2 |
| 47 | P11-f | Frieren đáp một câu không cam kết. | "Mong là vậy." | ngờ vực ngầm | 3 |
| 48 | P12-a | Khung lớn: lòng hẻm núi, vách đá dựng đứng; Stark ngồi với hai đứa trẻ, cây rìu cắm bên cạnh. | — | đời thường | 2 |
| 49 | P12-b | Một đứa trẻ hỏi có thể mạnh như Stark không; Stark khẳng định được. | "Cậu có nghĩ là tớ sẽ trở thành một chiến binh hùng mạnh như anh Stark đây không vậy?" / "Tất nhiên là được rồi." | ấm áp | 2 |
| 50 | P12-c | Cận mặt Stark, cười buồn, nói thêm một câu tự hạ. | "Cơ mà chiến binh cũng không hẳn là tuyệt vời đến thế đâu." | chua chát — **gieo mầm** | 3 |
| 51 | P13-a | Stark thấy bà lão dẫn khách tới, đứng dậy gọi. | "Bà ơi!" | thân mật | 1 |
| 52 | P13-b | Khung rộng: cả nhóm gặp nhau trong rừng. | — | chuyển | 1 |
| 53 | P13-c | Stark đoán ra hai người là thủ phạm chọc con rồng, và trách. | "Vậy ra hai người là kẻ đã tấn công con rồng à." / "Không khéo lại gây nguy hại cho ngôi làng này thêm lần nữa mất." | bực, lo | 3 |
| 54 | P13-d | Stark lên giọng đàn anh, khoe vết sẹo trên trán làm bằng chứng kinh nghiệm. | "Tôi bị một vết sẹo trên trán này là do chạm mặt với rồng hắc ám trước đây đấy nh-…" | ra vẻ | 2 |
| 55 | P13-e | Frieren gạt phăng giữa chừng. | "Giờ cái vết sẹo đó đâu có quan trọng chứ?" | phũ | 3 |
| 56 | P13-f | Cận mặt Stark cụt hứng. | "……" | quê | 2 |
| 57 | P14-a | Stark đoán hai người do sư phụ mình phái tới, rồi hỏi tên. | "…Hai người chắc hẳn là được sư phụ tôi phái tới nhỉ." / "Tên là gì vậy?" | dò xét | 2 |
| 58 | P14-b | Frieren xưng tên và nghề. | "Tôi là pháp sư Frieren." | điềm nhiên | 3 |
| 59 | P14-c | Cận mặt Stark — đứng hình khi nghe cái tên. | — | chấn động ngầm | 3 |
| 60 | P14-d | Stark xin bà lão cho nói chuyện riêng. | "Bà à, cho chúng cháu chút riêng tư nhé." | nghiêm lại | 2 |
| 61 | P14-e | Bà lão và hai đứa trẻ đứng nhìn theo, lo lắng. | — | lo | 1 |
| 62 | P14-f | Stark trấn an bọn trẻ. | "Không sao đâu. Họ là người quen của sư phụ anh mà." | vỗ về | 2 |
| 63 | P14-g | Khung rộng dưới chân vách đá: ba người nói chuyện, cây rìu dựng bên. | — | chuyển | 1 |
| 64 | P14-h | Stark đoán sư phụ đang giận vì mình bỏ đi không nói. | "Chắc hẳn sư phụ đang giận lắm nhỉ?" / "Do bỗng dưng tôi lại bỏ đi và lén lút tới nơi này mà." | áy náy | 3 |
| 65 | P15-a | Frieren vào thẳng vấn đề: sao không diệt con rồng, sao còn ở lại. | "Stark này, tại sao cậu lại không hạ con rồng đó vậy?" / "Cậu đâu có lí do gì để ở lại đây, đúng chứ?" | truy | 3 |
| 66 | P15-b | Cận mặt Stark, im. | — | né | 2 |
| 67 | P15-c | Stark đòi biết mục đích của Frieren trước, và rào trước là sẽ từ chối nếu chỉ để gọi về. | "Cô có thể nói cho tôi nghe về mục đích của bản thân mình trước được không?" | phòng thủ | 2 |
| 68 | P15-d | Frieren ngỏ lời mời thẳng, kèm điều kiện đổi chác. | "Chúng tôi muốn cậu làm tiên phong cho mình." / "…cũng đang tính tới việc giúp cậu loại bỏ con rồng đó nữa." | chào mời | 3 |
| 69 | P15-e | Stark hỏi lý do; Frieren nói thật là vì quyển sách trong tổ. | "Sao lại thế?" / "Do là tụi tôi muốn quyển sổ phép thuật ở trong tổ của nó ấy mà." | thật thà đến lố | 2 |
| 70 | P15-f | Frieren thừa nhận không có động cơ cao cả nào. | "Đó chỉ là thú vui của tôi mà thôi." / "Không có lí do đặc biệt nào đâu." | phẳng lì | 3 |
| 71 | P15-g | Stark cảnh báo đây là rồng thái dương, không phải thứ muốn đánh là đánh. | "Không phải là loại cứ thích là tấn công được đâu." | nghiêm | 2 |
| 72 | P16-a | Cận Frieren nghiêng mặt, đồng tình. | "Đúng vậy nhỉ." | lặng | 2 |
| 73 | P16-b | **Hồi tưởng:** một tảng đá lớn lơ lửng giữa không trung. Frieren cầm gậy đứng bên trái; bên phải là người đeo kính mặc áo tu đang chỉ trỏ hào hứng, người lùn đội mũ sừng, và một người cao đứng sát mép khung. (Ảnh KHÔNG in tên ai — xem mục D.) | — | ấm, xa xăm | 3 |
| 74 | P16-c | Frieren nói về lý do mình sưu tầm phép thuật kỳ quặc. | "Có một vài tên ngốc từng tán dương phép thuật mà tôi thu thập được ấy mà." / "Có lẽ đó là lí do chăng." | hoài niệm giấu kín | 3 |
| 75 | P16-d | Cận Stark, chưa hiểu. | — | ngơ | 1 |
| 76 | P16-e | Ba người đi, Stark lặp lại từ đó như không tin nổi. | "'Tán dương'… ấy hà?" | ngờ vực | 2 |
| 77 | P16-f | Cận mặt Stark; một bàn tay chìa tới sát trán cậu (KHÔNG RÕ của ai). | "……" | khựng | 2 |
| 78 | P17-a | Cả ba đứng đối diện; Stark buột miệng chê, rồi bị hỏi vặn. | "Ngớ ngẩn thật đấy." / "Đúng chứ?" | châm chọc | 2 |
| 79 | P17-b | Stark chấp nhận làm tiên phong, viện cớ lệnh sư phụ — nhưng ra điều kiện. | "Tôi không phiền nếu trở thành tiên phong cho cô đâu." / "Nhưng trước hết thì cô cần phải hạ được rồng thái dương đã." | ra giá | 3 |
| 80 | P17-c | Cận Stark, thú nhận một mình đối phó thì quá sức, rồi hỏi ngược. | "Nhưng mà Frieren đây có thể đánh bại được nó đúng chứ?" | cầu cứu giấu kín | 3 |
| 81 | P17-d | Frieren ra điều kiện của riêng mình. | "Nếu cậu có thể giữ chân được nó trong 30 giây, thì chắc chắn sẽ được." | lạnh, chắc nịch | 3 |
| 82 | P17-e | Stark nhắc lại con số. | "Ra vậy. 30 giây à." | nuốt khan | 2 |
| 83 | P17-f | Stark hỏi lại cho chắc; Fern quay sang thắc mắc. | "Tôi… cần phải làm vậy sao?" / "Cậu ta đang nói cái gì thế ạ?" | lấn cấn | 2 |
| 84 | P17-g | Frieren mỉm cười, nói phán đoán của mình đã đúng, rồi hỏi câu then chốt. | "Stark này, kinh nghiệm chiến đấu với quái vật của cậu là bao nhiêu vậy?" | gài bẫy xong | 3 |
| 85 | P18-a | **CÚ LẬT 1.** Stark gào lên, nước mắt nước mũi. | "**LÀ KHÔNG!!!**" | vỡ trận | 3 |
| 86 | P18-b | Stark bám lấy Frieren van xin, thú nhận mình chỉ làm quá lên. | "Giúp tôi với, Frieren ơi!!!" / "Chỉ là tôi đã quá muốn đối đầu với nó ngay từ đầu mà thôi!!" | thảm hại, hài | 3 |
| 87 | P18-c | **Hồi tưởng đêm mưa:** con rồng xén ngang dãy nhà; Stark đứng chết trân, một đứa trẻ nép sau lưng. | "Nhưng mà tôi đã sợ đến độ chẳng thể nào nhấc nổi một bước nữa là!!" | khiếp đảm | 3 |
| 88 | P18-d | **Sự thật:** con rồng tự bỏ đi vì tính khí thất thường, còn Stark bị dân làng tung hô thành người hùng giữa đám đông reo mừng. | "…tôi đã được tôn lên làm người hùng!" | mỉa mai, tội nghiệp | 3 |
| 89 | P19-a | Stark khóc tu tu, kể thêm: dân làng quá tốt nên không nỡ bỏ trốn. Khung phụ: bữa cơm ở quán, đứa trẻ đòi xem tuyệt kĩ, ông đầu bếp giục ăn nhiều. | "Trước tình cảnh đó làm tôi chẳng thể bỏ chạy đi đâu được cả!!" | day dứt | 3 |
| 90 | P19-b | Fern lạnh mặt đề nghị bỏ Stark; Stark níu áo Frieren. | "Frieren-sama, tên này vô dụng rồi. Chúng ta tìm người khác đi ạ." / "ĐỪNG BỎ TÔI LẠI MÀ!!" | phũ vs. hoảng | 3 |
| 91 | P19-c | Frieren bác lại Fern, khẳng định Stark đánh được rồng. | "Không, cậu ta có thể chiến đấu với rồng đấy." / "Nên là thế." | quả quyết | 3 |
| 92 | P19-d | Fern nói móc rằng Frieren coi Stark như con nít. | "Ngài cứ coi cậu ta như thể là con nít, chỉ cần cố gắng là sẽ làm được đấy nhỉ…" | mỉa | 2 |
| 93 | P19-e | Khung dọc: Frieren và Fern đứng dưới một **vết chém dọc khổng lồ xẻ đôi vách hẻm núi**, ngước nhìn. | "……?" | ngờ ngợ — **gieo mầm cú lật cuối** | 3 |
| 94 | P20-a | Frieren dừng lại bên một thân cây khổng lồ, đưa tay chạm vào. | — | quan sát | 2 |
| 95 | P20-b | Hai người bỏ đi, Frieren để lại cho Stark một đêm suy nghĩ. | "Stark, tôi sẽ cho cậu một đêm, hãy suy nghĩ cẩn thận nhé." / "Chắc chắn cậu không thể tiếp tục nếu cứ như thế này được đâu." | ra đề bài | 3 |
| 96 | P20-c | Đêm xuống. Stark ngồi một mình dưới gốc cây lớn, cây rìu dựng bên cạnh. | — | cô độc | 2 |
| 97 | P20-d | Cận mặt Stark, bàn tay quấn băng đưa lên trán, nghĩ ngợi. | — | dằn vặt | 3 |
| 98 | P20-e | Ngoại cảnh quán trọ đêm, biển hiệu "INN". | — | chuyển | 1 |
| 99 | P20-f | Trong bếp quán: ông đầu bếp và cô bé phụ bếp khen Stark. | "Hai vị đã gặp Stark-sama rồi à? Đó quả là một chàng trai tốt nhỉ." | ấm | 2 |
| 100 | P21-a | Frieren và Fern ăn tối; Frieren nhận xét cả làng sùng bái Stark. | "Nơi đây tôn thờ Stark-sama quá nhỉ?" / "Mà, có vẻ là một người tốt mà." | nhẩn nha | 2 |
| 101 | P21-b | Fern phản bác bằng một chữ. | "Đối với em thì chỉ là một gã thỏ đế thôi ạ." | khinh | 3 |
| 102 | P21-c | Frieren công nhận Stark nhát, rồi đem chuyện cũ của Fern ra so. | "Nhưng mà cả Fern cũng thế thôi mà, như lần đầu em chạm trán với quái vật ấy-…" | trêu | 3 |
| 103 | P21-d | Fern trừng mắt; Frieren rút lời ngay. | "Hừm" / "…Thôi được rồi. Ta sẽ quên vụ đó vậy." | hài, quen thuộc | 2 |
| 104 | P21-e | Hai người đi về trên phố đêm; Frieren tiếc thời Fern còn bé. | "Khi còn nhỏ thì em ngoan ngoãn và dễ thương đến thế cơ mà…" | bùi ngùi pha đùa | 2 |
| 105 | P21-f | Fern hỏi câu mấu chốt: vì sao con rồng thôi tấn công làng. Frieren bỏ lửng. | "…tại sao con rồng đó lại không tấn công ngôi làng nữa vậy ạ?" / "Ai mà biết… Hoặc là…" | treo | 3 |
| 106 | P22-a | Một tiếng nổ trầm vọng trong đêm. Fern giật mình nhìn quanh. | SFX ドォーン… / "…Tiếng gì vậy nhỉ?" | hiếu kỳ | 3 |
| 107 | P22-b | Frieren đoán ngay là Stark, đẩy Fern đi xem, còn mình đi ngủ. | "Chắc hẳn là của Stark đấy." / "Nếu mà hiếu kì, thì sao em không thử kiểm tra xem?" / "Còn ta đi ngủ đây." | thả câu | 3 |
| 108 | P22-c | Cận mặt Fern, ngập ngừng. | — | do dự | 2 |
| 109 | P22-d | Ngoại cảnh quán trọ đêm. | — | chuyển | 1 |
| 110 | P22-e | Frieren ngồi một mình trên giường trong phòng trọ tối. | — | tĩnh | 2 |
| 111 | P22-f | **Hồi tưởng — trở lại đêm cắm trại.** Lặp nguyên câu hỏi đã bỏ lửng ở P09. | "Hừm, cậu ta là một chiến binh tốt chứ?" | nối mạch | 3 |
| 112 | P23-a | Cận mặt người lùn, tiếng lửa nổ lép bép, vẫn chưa đáp. | SFX パチパチ | nặng | 2 |
| 113 | P23-b | **CÚ LẬT 2.** Người lùn kể: làng cũ của Stark từng bị quỷ dữ tấn công, và Stark đã bỏ chạy. | "…thì cậu ta đã tháo chạy như một gã thỏ đế." | phơi bày | 3 |
| 114 | P23-c | Khung mưa: một bóng nhỏ đội mũ sừng đứng chôn chân cạnh cây rìu rơi dưới đất. Người lùn tự nhận mình cũng vậy. | "Giống như tôi vậy." | tự thú, nặng | 3 |
| 115 | P23-d | Người lùn giải thích vì thế mới truyền hết những gì mình biết cho Stark. | "Vì lẽ ấy, nên tôi đã truyền đạt lại cho cậu ta những gì mà mình biết." / "Chắc chắn giờ cậu ta sẽ có thể chiến đấu vì người khác đấy." | tin tưởng | 3 |
| 116 | P23-e | Frieren mỉm cười, chốt lại. | "Ra vậy. Thế tức là một chiến binh tốt rồi." | ấm, nhẹ nhõm | 3 |
| 117 | P24-a | Khung xa: vách hẻm núi với một vết xẻ dọc chạy suốt từ đỉnh xuống. | — | tò mò | 2 |
| 118 | P24-b | **CÚ LẬT CUỐI.** Khung lớn: nhát rìu của Stark nổ tung vào chân vách đá, đá vụn bắn tung; Fern đứng bên chứng kiến. | SFX ドォォン / ドカーン | choáng | 3 |
| 119 | P24-c | Fern hiểu ra những vết chém khổng lồ khắp hẻm núi là gì. | "…Vậy ra đây là dấu vết luyện tập của cậu à." | vỡ lẽ | 3 |
| 120 | P24-d | Stark quay đầu nhìn lại, cây rìu còn cắm trong đá. | — | lặng, kết chương | 3 |

**Ngoài truyện:** P26 — tranh màu, Frieren ngồi trên bệ cửa sổ thành cổ nhìn ra tháp mái đỏ,
va-li đặt dưới sàn. Không có thoại. Dùng làm thumbnail/ảnh đóng video, **không đưa vào mạch kể**.

**Tổng: 120 panel truyện (P03–P24) + 1 tranh màu (P26). Ba trang bỏ: P01, P02, P25.**

---

## C. Điểm cao trào

Chương này có **bốn đỉnh**, và đỉnh cuối mới là cái đổi nghĩa toàn bộ phần trước.

**1. Đỉnh hài — Frieren bỏ chạy trước (P06-c → P06-e).**
Frieren nói "chạy thôi" rồi chạy thật, bỏ Fern đứng một mình dưới bóng con rồng. Khung cận
"Ơ?" của Fern là nhịp cười lớn nhất nửa đầu chương, đồng thời thiết lập rằng **chạy trốn
không phải điều Frieren coi là nhục**. Chi tiết này về sau cộng hưởng với chuyện Stark bỏ chạy.

**2. Đỉnh cảm xúc ngầm — hồi tưởng tảng đá bay (P16-b → P16-c).**
Frieren giải thích vì sao mình sưu tầm phép thuật vô dụng: "Có một vài tên ngốc từng tán dương
phép thuật mà tôi thu thập được ấy mà." Khung hồi tưởng bốn người không có một chữ thoại.
Đây là mạch bộ truyện nằm dưới mạch Stark — và là chỗ duy nhất chương này chạm vào tổ đội cũ.

**3. Cú lật 1 — Stark không hề là người hùng (P17-g → P18-d).**
Chuỗi bắc cầu qua trang: Frieren hỏi "kinh nghiệm chiến đấu với quái vật của cậu là bao nhiêu
vậy?" → lật trang → "**LÀ KHÔNG!!!**". Rồi vỡ ra: đêm đó Stark **sợ đến mức không nhấc nổi
chân**, con rồng bỏ đi do tính khí thất thường, và cậu bị tung hô nhầm thành người hùng. Toàn
bộ câu chuyện đẹp đẽ bà lão kể ở P11 bị lật ngược.

**4. Cú lật 2 — "Giống như tôi vậy" (P23-b → P23-e).**
Câu hỏi bỏ lửng từ P09 được trả lời sau 14 trang. Người lùn kể Stark từng tháo chạy khi làng cũ
bị tấn công — rồi tự nhận mình cũng từng như thế, và chính vì vậy mới truyền hết võ cho cậu:
"Chắc chắn giờ cậu ta sẽ có thể chiến đấu vì người khác đấy." Đây là **định nghĩa lại thế nào
là một chiến binh tốt**: không phải kẻ không sợ, mà là kẻ vẫn đứng lại.

**5. Cú lật cuối — vết chém trên vách đá (P19-e → P24).**
Khung "……?" ở P19-e (Frieren và Fern ngước nhìn vết xẻ dọc suốt vách hẻm núi) được cài từ
trước, đến P24 mới trả: đó là **dấu vết luyện tập hằng đêm của Stark**. Người bị Fern gọi là
"gã thỏ đế", người khóc lóc xin đừng bỏ lại, là người ba năm nay đêm nào cũng bổ rìu vào đá.
Và nó giải thích luôn câu Frieren bỏ lửng ở P21-f ("Hoặc là…") lẫn câu cô khẳng định ở P19-c
("cậu ta **có thể** chiến đấu với rồng đấy") — Frieren đã đọc ra điều đó từ vết chém, trước cả
khi Fern kịp hiểu.

> Khi viết lời kể: **thứ tự tiết lộ là tài sản của chương này.** Đừng nói trước ở đoạn P11 rằng
> Stark không thật sự đánh nhau, và đừng nói trước ở P19 vết chém là gì.

---

## D. Chưa rõ

**Nhân vật chưa có tên trong ảnh — KHÔNG được tự đặt:**

1. **Người lùn đội mũ sừng** (P08-b→f, P09-a/b, P22-f, P23-a→e). Chương 10 **không in tên**
   người này ở bất kỳ khung nào. Những gì ảnh cho biết: là **người lùn**, đội mũ sắt hai sừng,
   để râu dài, ngồi cạnh lửa trại cùng Frieren, xưng "tôi" và gọi Frieren là "cô"; **là sư phụ
   của Stark** ("Đó là học trò của tôi đấy"); từng bỏ chạy khi quê mình bị tấn công.
   → Ngoại hình và vai trò **khớp Eisen** trong bible (chiến binh, tộc người lùn, dùng rìu, đồng
   đội cũ của Frieren), nhưng đây là **suy luận từ bible, không phải chữ in trong C10**.
   **Cần user chốt**: gọi thẳng "Eisen" hay gọi "sư phụ của Stark" trong lời kể.
2. **"Sư phụ" mà Stark nhắc tới** (P14-a, P14-f, P14-h, P15-c) — cùng một người ở mục 1, nhưng
   bản dịch không bao giờ gọi tên.
3. **Bà lão dẫn đường / người kể chuyện làng** (P10-b, P10-e, P11, P13-a, P14-e). Chưa có tên.
4. **Ông đầu bếp và cô bé phụ bếp ở quán trọ** (P19-a khung phụ, P20-f). Chưa có tên.
5. **Hai đứa trẻ trong làng** (P12-b, P14-e, P19-a). Chưa có tên.
6. **Người phụ nữ ôm con dưới mưa** (P10-g). Chưa có tên; chưa rõ có phải bà lão hồi trẻ không.
7. **Ngôi làng** — chưa có tên. Chỉ biết nằm **gần hẻm núi Riegel**, thuộc **các vùng trung tâm**.
8. **Bốn người trong khung hồi tưởng P16-b** — ảnh **không in tên ai**. Nhận dạng được: Frieren
   (tai nhọn, cầm gậy); một người **đeo kính, mặc áo tu có hình thánh giá trên ngực**, đang chỉ
   trỏ hào hứng; **người lùn đội mũ sừng**; một người cao đứng sát mép phải khung, chỉ thấy
   nửa mặt nghiêng. Khớp lần lượt với Heiter, Eisen, Himmel trong bible — nhưng **là suy luận**.
9. **Người đang ngủ trong túi ngủ ở khung trại P08-b.** Mặt bị khuất, tóc bắt sáng trắng nên
   nhìn thoáng dễ tưởng là một nhân vật khác. Căn cứ để nói đó là **Fern**: khung toàn cảnh
   cùng cảnh (P08-c) có **chiếc va-li** mà Fern xách suốt chương. Vẫn xếp vào "chưa chắc".

**Chi tiết mơ hồ khác:**

10. **Bàn tay chìa tới trước trán Stark ở P16-f** — không rõ là tay ai (Frieren hay Fern), và
    không rõ có phải đang chỉ vào vết sẹo hay không. Không có thoại kèm theo.
11. **Tuổi, họ, quá khứ của Stark**: chưa nói. Chỉ biết cậu **bỏ sư phụ mà đi**, **lén** tới
    làng này, đã ở đây **khoảng 3 năm**, và có **một vết sẹo trên trán** mà cậu khoe là do
    **rồng hắc ám** — nhưng lời khoe đó bị cắt ngang giữa chừng và chương không xác nhận.
12. **"Quỷ dữ" tấn công làng cũ của Stark** (P23-b) — không nói là loại gì, ở đâu, khi nào.
13. **Nội dung cuốn sách trong tổ rồng** — Frieren chỉ nói đó là thứ cô đang tìm và rằng
    "thú vui của ta". Ở P09-e cô nói cuốn sách chép **"phép thuật làm cho quần áo trong suốt"**,
    nhưng khung ngay trước đó cho thấy đó là câu trả lời cho món phép **cô đang bàn**, không
    chắc là nội dung của đúng cuốn trong tổ. **Đừng khẳng định là một.**
14. **Frieren có thật hạ được rồng thái dương trong 30 giây hay không** — chương chưa chứng minh.
    Cô mới chỉ nói "nếu cậu giữ chân được nó 30 giây thì chắc chắn sẽ được".
15. **Stark đã nhận lời làm tiên phong chưa** — tới hết P24 vẫn chưa có câu đồng ý dứt khoát.
    Frieren mới cho cậu "một đêm để suy nghĩ" (P20-b).
16. **Vì sao con rồng thật sự ngừng tấn công làng** — Stark nói là do tính khí thất thường của
    nó (P18-d), Frieren bỏ lửng "Hoặc là…" (P21-f). **Chương không chốt.** Không được suy diễn
    rằng con rồng sợ Stark.
17. **Thân cây khổng lồ Frieren chạm vào ở P20-a** — không có thoại, không rõ cô thấy gì ở đó.

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** 120 panel ở mục B đều đọc từ 22 trang P03–P24 theo chiều
   phải→trái. Có chỗ nào anh thấy tôi ghép nhầm thứ tự khung hoặc gán nhầm bong bóng thoại
   (nghi nhất: P15-e và P17-e/f) không?
2. **Tên nhân vật đúng chưa?** Frieren / Fern / Stark là chữ in trong ảnh. **Người lùn đội mũ
   sừng và bốn người trong hồi tưởng P16-b KHÔNG được in tên** — anh muốn lời kể gọi thẳng
   "Eisen / Himmel / Heiter" theo bible, hay gọi mô tả ("sư phụ của Stark", "tổ đội cũ")?
3. **Trọng số hợp lý chưa?** Tôi để TS 3 cho cả bốn cú lật (P18, P23, P24) và cho khung hồi
   tưởng P16-b. Nếu video 7–8 phút thì mạch Stark sẽ nuốt gần hết thời lượng — anh muốn giữ
   khung hồi tưởng tổ đội cũ ở mức 3, hay hạ xuống để dồn cho cú lật cuối?
