# BEAT SHEET — Twilight Blade C8 "Điềm báo"

Nguồn ảnh: `series/TWB/C8/pages-clean/`
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **ĐỦ 21/21 file ảnh** (= 20 trang truyện, vì P02 và P21 chỉ là dải cắt rời của trang trên nó)

> **Chiều đọc: PHẢI → TRÁI** (bản gốc Nhật giữ nguyên layout). Đã kiểm chứng ở P05 (ô caption
> "Khoảng 2 tiếng trước…" nằm góc trên **phải**) và ở mạch hỏi–đáp P05 hàng dưới, P11 hàng 1–2.
> Mọi thứ tự panel dưới đây theo chiều này.

### A. Kiểm tra đầu vào

21 ảnh `TWB_C8_P01`–`P21`, liên tục, **không thiếu trang**.

Số đo trước → sau khi `clean-pages.py` chạy (gốc rộng 822px, cao hơn hẳn C1):

| File | pages/ | pages-clean/ | Đã cắt |
|---|---|---|---|
| P01 | 822×1500 | 822×1052 | **−448px** (banner + promo đầu chương) |
| P02 | 822×162 | 822×162 | không cắt |
| P03–P19 | 822×1200 | 822×1200 | không cắt |
| P20 | 822×1500 | 822×1500 | **không cắt** |
| P21 | 822×162 | 822×134 | −28px |

**⚠ Ba cảnh báo cho khâu dựng:**

1. **P20 chưa được làm sạch.** Khoảng 300px đáy trang vẫn là **banner quảng cáo TRUYENQQQ.COM**
   với hình nhân vật của bộ khác. Đây đúng là trang chứa cú lật cuối chương → **bắt buộc crop
   đáy trước khi lên khung**, nếu không banner sẽ nằm ngay dưới câu thoại quan trọng nhất.
2. **P21 = phần còn lại của chính banner đó**, không có nội dung truyện → **BỎ**.
3. **P02 không phải một trang.** Nó là dải đáy 162px bị cắt rời của **P01** (chứa đuôi ba bong
   bóng thoại của P01 hàng 3). Khi dựng phải ghép P01+P02 mới đọc đủ câu. Tương tự, P21 là dải
   đáy của P20.

**Trang bỏ:**
- `P04` — trang tiêu đề: tranh Yamato cỡ lớn, Hikari nhỏ phía sau, logo `あわいの焔刃`,
  dòng **"CHƯƠNG 8 · ĐIỀM BÁO"**, và ô quảng cáo phát hành tập 1 ngày 4/9. **BỎ nội dung, giữ
  lại tên chương.** (Ảnh này đẹp, dùng làm thumbnail được.)
- `P21` — dải quảng cáo. **BỎ.**

**Lưu ý đối chiếu series-bible:** bible hiện mới lập từ C1, và tracker cho thấy **C2–C7 chưa
qua bước beat sheet**. Vì vậy C8 xuất hiện một loạt nhân vật và thuật ngữ mà bible chưa có
(Yoshino Yamato, Gaihou-shi, Kairyouku, Hakkai, nhóm người ở P20). Dưới đây **chỉ ghi đúng
những gì có chữ trong ảnh C8**, không suy ra bối cảnh từ các chương chưa đọc — xem mục D.

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P01-a | Trong nhà, Hikari ngồi cầm cốc nước, nghe Yojin dẫn chuyện | "…chú xin giới thiệu nhé, Hikari-kun" | chờ đợi | 2 |
| 2 | P01-b | Yojin đứng cạnh một thanh niên tóc sáng rối, áo khoác sáng màu; giới thiệu cậu ta là thực tập sinh dưới tay mình. Thanh niên tự xưng tên | "Tên anh là **Yoshino Yamato**!" | ra mắt nhân vật mới | 3 |
| 3 | P01-c + P02 | Yamato nói đã **bỏ việc làm thêm trên trường** để làm thực tập sinh, mong được phụ chăm sóc Hikari. Yojin nghĩ thầm: ra chuyện của cậu là vậy | "rất mong được mọi người giúp đỡ ạ!" | nhiệt tình, hơi quá đà | 2 |
| 4 | P03-a | Cận Hikari nghe tiếp: vì "một số lý do", Yamato cũng sẽ làm **công việc giống của Yojin** | "…cũng sẽ làm công việc giống của chú…" | dò xét | 3 |
| 5 | P03-b | Yamato cười; Yojin dặn từ giờ cậu ta sẽ ra vào nhà, hãy hoà thuận với nhau | "hãy hoà thuận với nhau nhé" | sinh hoạt | 1 |
| 6 | P03-c | Hikari lặp lại chậm rãi "làm cùng công việc… với chú Yojin…". Hai người lớn giật nảy, nghĩ mình bị nghi | "Bị nghi ngờ rồi sao…!?" | hoảng ngầm | 3 |
| 7 | P03-d | Yojin cận mặt, nói một câu đóng cửa vấn đề | "Cháu **không cần** phải trở thành một người giống như chú đâu." | lạnh, chốt hạ | 3 |
| 8 | P03-e | Cận mắt Hikari. Không trả lời, chỉ im lặng | "⋮" | giấu ý nghĩ | 3 |
| 9 | P03-f | Chữ "SAFE" bung ra; hai người lớn thở phào. Hikari quay sang Yamato, nói câu chào xã giao | "…mong anh giúp đỡ…" | né được, nhưng gượng | 2 |
| — | **P04** | **Trang tiêu đề — "CHƯƠNG 8 · ĐIỀM BÁO"**. Tranh Yamato lớn, Hikari nhỏ phía sau | — | — | **BỎ** |
| 10 | P05-a | Ô caption đổi thời gian | "Khoảng **2 tiếng trước**…" | lùi mốc | 2 |
| 11 | P05-b | Tranh tư liệu: một đoàn người bịt mắt, mặt nạ chấm tròn, áo lễ truyền thống, gậy phép, quạ bay. Lời dẫn giải thích **Gaihou-shi (ngoại pháp sư)** là thuật sĩ dùng "ngoại pháp", đã bảo vệ con người khỏi **yêu ma** suốt nhiều thời đại | "họ là những người đã bảo vệ con người khỏi yêu ma suốt nhiều thời đại" | mở rộng thế giới | 3 |
| 12 | P05-c | Yamato hỏi ngoại pháp là gì; được trả lời đó là một dạng ma thuật, và **không dùng ngoại pháp thì không thể tiêu diệt yêu ma** | "không dùng ngoại pháp thì không thể tiêu diệt được" | giảng giải | 3 |
| 13 | P05-d | Yojin: muốn học ngoại pháp thì bắt buộc phải kiểm soát **"Kairyouku" (giới lực)**, và đó là thứ phải rèn trước. Yamato than thở | "Lại là 'giới lực' nữa à!" | uể oải, hài | 2 |
| 14 | P06-a | Siêu thị. Yamato ôm đồ than nặng, lẩm bẩm về chuyện luyện năng lượng; Yojin dò danh sách mua sắm trên điện thoại | "Thịt xay với… sữa tươi nhỉ." | thường ngày | 1 |
| 15 | P06-b | Yojin xin lỗi vì lại kéo Yamato đi chợ; Yamato nói đã nghỉ làm thêm nên rảnh, rồi hỏi nấu gì cho Hikari | "Anh định nấu đồ ăn cho Hikari-kun à?" | thân thiện | 1 |
| 16 | P06-c | Hình món hamburg sốt demi-glace lấp lánh; Yojin tuyên bố hôm nay làm hamburg vì "trẻ con chắc là thích" | "Hôm nay… tôi định làm hamburg." | ấm, ngây ngô | 2 |
| 17 | P07-a | Yojin cho biết **dạo này Hikari không khoẻ**; ăn đồ ngon may ra vui lên. Yamato ngạc nhiên | "Thấy bảo dạo này thằng bé không khoẻ lắm…" | lo ngầm | 3 |
| 18 | P07-b | Cận bàn tay Yojin. Nội tâm: những đứa trẻ như thế **chẳng bao giờ chịu yếu đuối hay than thở với ai** | "…chẳng bao giờ chịu yếu đuối hay than thở với ai…" | xót, bất lực | 3 |
| 19 | P07-c | Yojin tự hỏi mình lo kiểu này có thái quá không | "…có vẻ hơi thái quá đúng không?" | tự ngờ | 3 |
| 20 | P07-d | Yamato gạt đi, bảo lo vậy là bình thường | "Thế này thì cũng bình thường mà." | trấn an | 2 |
| 21 | P07-e | Yamato vỗ vai Yojin, quả quyết Hikari sẽ vui lắm; Yojin lúng túng | "Tuyệt quá còn gì!" | hào hứng | 2 |
| 22 | P07-f | Yojin (vẽ chibi) nhớ lại hồi bé: ngày có chuyện buồn mà **mẹ nấu món mình thích** là sướng phát điên — nhất là hamburger | "mẹ tôi mà làm món tôi thích là tôi sướng phát điên luôn ấy" | ký ức ấm, hiếm | 3 |
| 23 | P08-a | Yamato buột miệng từng làm hamburger rồi. Yojin hét lên, sốc thật sự | "Cậu **từng làm hamburger rồi sao**!!?" | sốc, hài | 2 |
| 24 | P08-b | Yamato nói chỉ vài lần thôi; Yojin gọi cậu ta là "người có kinh nghiệm" | "ra cậu là 'người có kinh nghiệm' sao…!!" | hài | 1 |
| 25 | P08-c | Yamato tỉnh bơ: làm thử mới thấy dễ không tưởng, chỉ trộn – nặn – rán | "Mấy khoản trộn, nặn rồi rán thôi mà!" | vô tư | 1 |
| 26 | P08-d | Cận mặt Yojin méo mó vì kinh hoàng trước ba động tác đó. Yamato đành nhận phụ một tay | "Lại còn **dễ** sao!?" | hài đen | 2 |
| 27 | P09-a | Về tới bếp nhà. Bàn tay găng đen bóc hành tây; Yamato trêu anh là gà mờ nấu ăn | "Không ngờ anh lại là gà mờ nấu ăn đấy~" | ấm, đùa | 1 |
| 28 | P09-b | Yamato hỏi sao vẫn cố tự làm; Yojin đáp người mới bắt đầu không có nghĩa là không được làm. Yamato thầm khen ngầu — dù chỉ là chuyện hamburg | "Người mới bắt đầu thì đâu có nghĩa là không được làm." | lì lợm dễ mến | 2 |
| 29 | P09-c | Yamato nhận xét Hikari nhát gan / dè chừng người lạ | "Hikari-kun đúng là bị nhát gan thật đấy…" | quan sát | 2 |
| 30 | P09-d | Hikari vụt chạy khỏi bếp, viện cớ đi làm bài tập | "Em đi làm bài tập đây ạ!" | lảng tránh | 2 |
| 31 | P09-e | **Yojin nhận phần lỗi về mình**: bị đề phòng cũng phải thôi, vì dù không cố ý thì anh vẫn là kẻ xấu — kể cả khi Hikari không hề biết | "Thì **tôi vẫn là kẻ xấu**, kể cả em ấy không có biết đi chăng nữa." | tự kết án | 3 |
| 32 | P10-a | Hai người đứng cạnh nhau ở bếp. Yojin nói một câu như tín điều | "**Hối hận** không phải là thứ để níu kéo, mà là thứ để đối mặt và chấp nhận." | lạnh, nặng | 3 |
| 33 | P10-b | Yojin quay sang Yamato: cậu cũng không ngoảnh mặt làm lơ mãi được. Yamato im một nhịp rồi đáp gọn | "Vâng!" | ràng buộc | 3 |
| 34 | P10-c | Đang thái hành, Yojin dặn thêm: **đừng kể chuyện pháp sư ngoại đạo cho mẹ cậu nghe** | "Đừng có kể cho mẹ cậu nghe…" | cảnh giác | 3 |
| 35 | P10-d | Lý do: **tổ chức của họ không công khai với công chúng**. Yamato dạ vâng | "tổ chức của chúng ta là một tổ chức **không công khai**" | hé lộ | 3 |
| 36 | P11-a | Ra ban công nướng đồ. Yamato hỏi "tổ chức" nghĩa là còn nhiều người khác; Yojin xác nhận, và nói **có những pháp sư ngoại đạo mạnh hơn anh rất nhiều** | "Có những pháp sư ngoại đạo mạnh hơn tôi rất nhiều." | khiêm tốn | 3 |
| 37 | P11-b | Yamato hỏi thẳng anh xếp thứ mấy. Yojin ậm ừ, nhắc tới **Hakkai (Bát Giới)** — nơi pháp sư ai cũng mạnh. Yamato ngơ ngác trước cái tên | "Bát Giới?" | tò mò, cài cắm | 3 |
| 38 | P11-c | Lửa bếp nướng bất ngờ bùng to; Yamato nhảy dựng vì sắp cháy đồ ăn | "Chờ chút chờ chút! Cháy mất!" | hài, xả hơi | 1 |
| 39 | P11-d | Giữa lúc nhốn nháo, Yojin trả lời câu hỏi thứ hạng — rồi bị ngắt giữa chừng | "Tôi chắc cỡ **vừa vừa tầm trung** thôi." | tưởng vô hại | 3 |
| 40 | P12-a | Một tiếng thét xé không khí. Cận mặt hai người, nụ cười tắt ngấm | (chữ tượng thanh) | chuyển tông gắt | 3 |
| 41 | P12-b | Yamato bật dậy, không hiểu chuyện gì | "C… cái gì thế!?" | hoảng | 2 |
| 42 | P12-c | Yojin xác định hướng: từ bên ngoài. Gọi tên Yamato | "Từ bên ngoài…" | lạnh, vào việc | 3 |
| 43 | P12-d | Yojin rút **lưỡi kiếm** ra, giao lại củ hành tây cho Yamato rồi lao đi | "Tôi **giao hành tây** lại cho cậu đấy." | chuyển vai chớp nhoáng | 3 |
| 44 | P13-a | Một **oán hồn** hình đàn bà tóc dài, tay chân dài ngoẵng, miệng há toác, đang bò qua cửa vào ban công | "Chẳng lẽ lại là…" | kinh dị bung | 3 |
| 45 | P13-b | Cận miệng nó há rộng bất thường, áp vào kính | — | ghê rợn | 2 |
| 46 | P13-c | Cận con mắt lồi của nó; nó phát ra tiếng ê a như đang dò tìm | "Ừm… ừm…" | ám | 3 |
| 47 | P14-a | Yojin quật ngang, tóc con quái văng tung | (chữ tượng thanh) | dứt khoát | 3 |
| 48 | P14-b | Cận mắt Yojin sau mái tóc — không một gợn cảm xúc | — | lạnh | 3 |
| 49 | P14-c | Yojin ghì đầu nó xuống sàn ban công, lưỡi kiếm trong tay, buông một câu gần như **hài lòng** | "Được đấy chứ." | máu lạnh | 3 |
| 50 | P15-a | Thân con quái rữa ra, **đẻ / nhả ra thêm nhiều oán hồn nhỏ** bám trần, bám tường; tiếng "KEE KEE KEE" | "KEE KEE KEE…" | leo thang | 3 |
| 51 | P15-b | Cận mắt Yojin giữa dịch nhầy. Anh khen cái trò đó **hay** | "Hay đấy… với thứ đó." | khoái chiến | 3 |
| 52 | P15-c | Yamato bám cửa kính nhìn ra, chết lặng | "Không thể nào…" | choáng | 3 |
| 53 | **P16** | **SPLASH cả trang.** Yojin đứng giữa một bầy oán hồn khổng lồ phủ kín khung, một tay lưỡi kiếm, một tay **xách cái đầu vừa chặt**. Yamato thốt lên câu đá thẳng vào lời "tầm trung" ở P11 | "Thế… thế này mà bảo là **tầm trung bình** thôi sao…?" | bùng nổ / lật vai | 3 |
| 54 | P17-a | Yojin nhảy bổ, chém nát một con; xác nổ tung thành mảng nhầy | (chữ tượng thanh) | tàn sát | 3 |
| 55 | P17-b | Cận Yojin **ngậm lưỡi kiếm trong miệng**, tay rút thêm vũ khí | — | thú tính | 3 |
| 56 | P17-c | Cắt về trong nhà: Yamato thò đầu ra, **cố nói át tiếng chém** bằng chuyện lửa bếp | "…tôi không nghĩ anh có vấn đề khi để lửa lớn để làm món hamburg đâu." | hài đen, che đậy | 3 |
| 57 | P17-d | Ngoài ban công, một **quả cầu lửa đen** bùng lên trên nền phố đêm | (chữ tượng thanh) | thuật của Yojin | 3 |
| 58 | P18-a | Cửa phòng mở: **Hikari đứng đó cầm cốc**, gọi tên Yojin | "Ơ? Chú Yojin…" | báo động | 3 |
| 59 | P18-b | Yamato bật dậy chặn ngay, hỏi dồn chuyện bài tập; Hikari vẫn hỏi chú Yojin đâu | "Hikari-kun! Em làm bài tập xong chưa!?" | cuống | 3 |
| 60 | P18-c | Yamato bịa: anh ấy đang nghe **một cuộc điện thoại quan trọng** nên mới ra ngoài | "nghe một cuộc điện thoại quan trọng ấy mà~" | nói dối trơn tru | 3 |
| 61 | P18-d | Hikari đáp "là vậy sao ạ". Sau lưng hai người, **Yojin vẫn đang vung kiếm trên ban công** trong cùng một khung hình | "chắc chú ấy sắp vào lại ngay thôi!" | mỉa mai thị giác | 3 |
| 62 | P19-a | Yamato hỏi Hikari có muốn uống thêm nước không | "Em có muốn uống thêm nước không??" | lảng chuyện | 1 |
| 63 | P19-b | Cận mắt Hikari. Cậu bắt đầu hỏi ngược lại Yamato | "…còn anh Yoshino" | dò hỏi | 3 |
| 64 | P19-c | **Hikari hỏi làm thế nào mà anh với chú Yojin…** — câu hỏi bị cắt đúng lúc cửa kéo mở | "…mà anh với chú Yo-" | hụt, treo | 3 |
| 65 | P19-d | Yojin bước vào, quần áo chỉnh tề như không có gì xảy ra | "Ah… …Hikari-kun." | bình thản giả | 3 |
| 66 | P19-e | Yojin hỏi cháu đói chưa, xin lỗi vì bắt đợi thêm chút nữa. Hikari dạ. Yamato đứng nhìn, không nói gì | "Xin lỗi nha, đợi chú thêm một chút nữa." | ấm — và giả tạo | 3 |
| 67 | P20-a | **Đổi cảnh hoàn toàn**: cận mặt một người đàn ông đang cười; cận mặt một cô gái tóc đen. Cánh hoa bay, chim sẻ. Không ai trong số này từng xuất hiện ở C1 | — | mở mặt trận mới | 3 |
| 68 | P20-b | Một cô gái tóc đen buộc đuôi dài, mặc đồng phục sẫm, **kết thúc một bản báo cáo** | "…**Báo cáo** đến đây là hết ạ." | lạnh, hành chính | 3 |
| 69 | P20-c | Chim sẻ đậu trên vai người nghe; người đó cảm ơn cô gái | "Cảm ơn vì đã vất vả." | lịch thiệp, rợn | 3 |
| 70 | P20-d | Người đàn ông lưng rộng áo đen quay đi, kết luận rằng **chuyện này phải trực tiếp nói chuyện mới được** — rồi gọi đích danh | "Hùm… phải trực tiếp nói chuyện mới được." → "**Yojin.**" | cú lật / cliffhanger | 3 |
| — | **P21** | Dải quảng cáo còn sót | — | — | **BỎ** |

**Tổng: 70 panel có nội dung** (P04 và P21 loại, không tính).

---

### C. Điểm cao trào

Chương này có **ba đỉnh**, và cái sau lần lượt đánh sập cái trước.

**1. Đỉnh hành động — P16 (splash), dựng từ P11 và trả bài ngay.**
Ở P11 Yamato hỏi Yojin xếp thứ mấy trong tổ chức, Yojin trả lời `"Tôi chắc cỡ vừa vừa tầm trung
thôi."` Năm trang sau, cả trang P16 là Yojin đứng giữa một bầy oán hồn, tay xách cái đầu vừa
chặt, và Yamato nói đúng cái câu khán giả đang nghĩ: `"Thế này mà bảo là tầm trung bình thôi
sao…?"` Đây là một cú **setup–payoff khép kín trong cùng chương**, không cần biết chương trước
cũng hiểu. Chuỗi P14→P17 còn đẩy thêm: Yojin ghì đầu quái xuống sàn rồi nói `"Được đấy chứ."`,
khen con quái `"Hay đấy"` khi nó đẻ thêm bầy con, và ngậm lưỡi kiếm trong miệng ở P17-b. Người
đàn ông vụng về không biết nặn hamburger ở P08 và cái thứ trên ban công ở P16 là **cùng một
người, cách nhau tám trang**.

**2. Đỉnh cảm xúc — P09-e → P10-d, và nó là chỗ nặng nhất chương.**
Hikari vừa viện cớ bài tập để chuồn khỏi bếp, Yamato nhận xét cậu bé nhát; Yojin đáp lại bằng
câu tự kết án: `"Thì tôi vẫn là kẻ xấu, kể cả em ấy không có biết đi chăng nữa."` Ngay sau đó là
`"Hối hận không phải là thứ để níu kéo, mà là thứ để đối mặt và chấp nhận."` Đọc cùng **C1 P52**
(Yojin được lệnh giám sát Hikari như nhân tố có nguy cơ gây thảm hoạ), câu này không còn là lời
răn dạy đàn em nữa — nó là lời một người **biết rõ mình đang làm gì với đứa trẻ đang ngồi cách
đó một bức tường**. Toàn bộ nửa đầu nấu ăn — đi chợ, chọn hamburg, nhớ món mẹ nấu ở P07-f — vì
thế mang hai nghĩa cùng lúc, đúng như trục đã dựng ở C1.

**3. Cú lật cuối — P20, và nó đổi nghĩa gần như toàn bộ phần đầu.**
Chương đột ngột cắt sang một nơi khác, người khác, không ai từng thấy ở C1: một cô gái vừa
**kết thúc một bản báo cáo**, một người cảm ơn cô `"vì đã vất vả"`, rồi một người đàn ông áo
đen kết luận `"Cái này xem ra phải trực tiếp nói chuyện mới được."` — và gọi tên: `"Yojin."`
Tức là **suốt lúc Yojin đi chợ, nấu hamburg, nói dối Hikari và chém oán hồn trên ban công, có
người đang theo dõi và báo cáo về anh.** Ba chi tiết ở nửa đầu bỗng đổi màu khi đọc lại:
- `P03-d` "Cháu không cần phải trở thành một người giống như chú đâu" — Yojin nói câu đó với
  Hikari, nhưng chính anh mới là người sắp bị gọi ra chất vấn.
- `P10-d` "tổ chức của chúng ta là một tổ chức không công khai với công chúng" — chính cái tổ
  chức đó vừa lập hồ sơ về anh.
- `P11-b` "các pháp sư trong Hakkai (Bát Giới) ai cũng mạnh" — cái tên vừa được thả ra ở trang
  11 gần như chắc chắn là nơi những người ở P20 thuộc về.

**Mạch phụ đáng dùng:** P17-c → P19-c là một đoạn **hài đen rất sạch** — Yamato che tiếng chém
bằng chuyện lửa bếp, bịa ra "cuộc điện thoại quan trọng", còn Yojin thì bước vào phòng chỉnh tề
hỏi `"Cháu đói chưa?"`. Và ngay trước đó, **Hikari đã bắt đầu hỏi** `"Làm thế nào… mà anh với
chú Yo-"` — câu hỏi bị cửa kéo cắt ngang. Cậu bé đang tiến rất gần tới sự thật, và chương đóng
lại đúng lúc đó.

---

### D. Chưa rõ

**Nhân vật mới, chưa đủ dữ kiện:**
- **Yoshino Yamato** — tên đầy đủ có trong ảnh (P01-b), chắc chắn. Nhưng **chưa rõ** vì sao cậu
  ta được nhận làm thực tập sinh, "một số lý do" ở P03-a là lý do gì, quan hệ trước đó với Yojin
  ra sao, và cậu ta đã biết những gì về Hikari. C8 không trả lời. **Chưa rõ cách gọi trong video**
  — ảnh có cả "Yamato-kun" (Yojin gọi) và "anh Yoshino" (Hikari gọi); cần user chốt.
- **Mẹ của Yamato** — chỉ được nhắc một lần ở P10-c (`"đừng kể cho mẹ cậu nghe"`). Không tên,
  không mặt.
- **Ba người ở P20** — một cô gái tóc đen buộc đuôi dài đang báo cáo; một người đeo kính ở góc
  trái; một người đàn ông lưng rộng áo đen có chim sẻ đậu quanh, là người gọi tên Yojin. **Không
  ai được gọi tên trong ảnh.** Không rõ ai thuộc cấp ai, không rõ đây có phải Hakkai hay không.
  **Không được đặt tên hay gán vai cho họ.**
- **Hai gương mặt cận ở P20-a** (một người đàn ông đang cười, một cô gái tóc đen) — chưa rõ có
  phải chính hai người ở panel dưới hay là người khác nữa.
- **"Yojin." ở P20-d** — chưa chắc chắn ai nói. Bong bóng nằm giữa người đàn ông áo đen và người
  đeo kính ở mép trái, đuôi bong bóng bị thân người che. Khi viết lời kể **nên để trung tính**
  ("một cái tên được gọi ra"), đừng gán cho ai.

**Thuật ngữ mới — bible chưa có, cần user chốt bản dịch trước bước narration:**
- **Gaihou-shi / ngoại pháp sư** (P05-b, P10-c). Bản dịch C8 dùng **hai cách** cho cùng một từ:
  "ngoại pháp sư" (P05) và "pháp sư ngoại đạo" (P10, P11). Bible C1 lại chốt là **"pháp sư trừ
  tà"**. Ba cách gọi cho một nghề → **phải chọn một** trước khi viết lời.
- **Ngoại pháp** (P05-c) — "một dạng ma thuật", điều kiện bắt buộc để tiêu diệt yêu ma.
- **Kairyouku / giới lực** (P05-d) — thứ phải kiểm soát được mới học được ngoại pháp. Chưa rõ
  bản chất.
- **Hakkai / Bát Giới** (P11-b) — chưa rõ là **tên tổ chức**, một **cấp bậc**, hay một **nhóm
  tám người mạnh nhất**. Trong ảnh chỉ có đúng một câu: "các pháp sư trong Hakkai ai cũng mạnh".
  **Không được suy ra là tổ chức của Yojin.**
- **Yêu ma** (P05-b, P05-c) — bible C1 đã chốt dùng **"oán hồn"** cho loại sinh vật này. C8 dùng
  "yêu ma" / "yêu ma quỷ quái". Chưa rõ đây là cùng một loại hay hai loại khác nhau → cần chốt.

**Chi tiết cốt truyện còn mờ:**
- **"Dạo này Hikari không khoẻ"** (P07-a) — Yojin nói "thấy bảo", tức là nghe từ người khác.
  **Chưa rõ nghe từ ai**, và cũng chưa rõ Hikari không khoẻ thế nào. Chương không nói tiếp.
- **Vì sao Hikari dè chừng** (P09-c/P09-e) — Yamato bảo cậu nhát gan, Yojin thì cho là mình đáng
  bị đề phòng. Chưa rõ Hikari thật sự nghi điều gì, hay chỉ ngại người lạ.
- **Câu hỏi bỏ dở của Hikari ở P19-c** — "Làm thế nào… mà anh với chú Yo-". Chưa rõ vế sau là
  "quen nhau", "làm cùng nhau" hay gì khác. **Không được đoán nốt câu này.**
- **Xuất xứ con oán hồn ở P13** — không có khung nào nói nó từ đâu tới, có liên quan gì tới thể
  chất của Hikari hay không. C1 đã chốt Hikari thu hút oán hồn, nhưng **C8 không nhắc lại**, nên
  đừng nối hộ tác giả.
- **Ngọn lửa đen ở P17-d** — chưa rõ có phải cùng loại thuật với ngọn lửa ở C1 P42 hay không;
  trong C8 không có câu thoại nào xác nhận.
- **C2–C7 chưa đọc.** Rất nhiều thứ ở trên có thể đã được giải thích trong bảy chương ở giữa.
  Beat sheet này **chỉ dựa trên C1 + C8**.

---

## DỪNG Ở ĐÂY — chờ duyệt

Chưa viết một chữ lời kể nào. Ba câu hỏi cần user xác nhận trước khi sang `/manga-narration`:

1. **Panel có thật không** — đặc biệt: P07-f (người nhớ món mẹ nấu là **Yojin**, vẽ chibi tóc
   sáng áo đen có khuy tròn — không phải Yamato) và P20-d (ai là người nói "Yojin."). Xem lại
   giúp hai chỗ này.
2. **Tên nhân vật đúng chưa** — chốt cách gọi **Yoshino Yamato** trong video ("Yamato" hay
   "Yoshino"?), và chốt **một** bản dịch cho nghề của Yojin giữa ba cách đang có: "pháp sư trừ
   tà" (bible C1) / "ngoại pháp sư" / "pháp sư ngoại đạo" (C8). Cùng đó: dùng "oán hồn" hay
   "yêu ma"?
3. **Trọng số hợp lý chưa** — chương này có tới ba đỉnh (P16 hành động, P10 cảm xúc, P20 cú
   lật) trong ngân sách 180 giây. Nếu giữ cả ba thì phần siêu thị (#14–#26) phải nén rất mạnh.
   User muốn giữ đủ ba, hay bỏ bớt một?
