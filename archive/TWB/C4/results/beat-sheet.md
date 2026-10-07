# BEAT SHEET — Twilight Blade C4 "Trận chiến tại cánh cửa"

Nguồn ảnh: `series/TWB/C4/pages-clean/`
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **ĐỦ 38/38 trang** · **70 panel có nội dung**
Chiều đọc: **phải → trái** (xác nhận: câu loa "XIN CHÚ Ý," ở P01 nối sang panel PHẢI của P02)

---

### A. Kiểm tra đầu vào

38 ảnh `TWB_C4_P01`–`P38`, đánh số liên tục, **không thiếu trang**.

**⚠ `clean-pages.py` chưa cắt gì ở chapter này.** Đối chiếu `pages/` với `pages-clean/`,
kích thước **trùng khít từng trang** — chưa có trang nào bị cắt px:

- `P01` **còn nguyên banner quảng cáo TruyenQQQ + dòng promo ở ĐẦU trang** (~630px trên cùng của ảnh 1125×1500) → cần cắt trước khi dựng.
- `P38` **còn nguyên banner quảng cáo TruyenQQQ + dòng promo ở ĐÁY trang** (~640px dưới cùng của ảnh 1125×776) → cần cắt; dải **"CÒN TIẾP!"** phải giữ lại.
- Watermark `NetTruyen12s` ở góc **trên-trái** của hầu hết trang cao (P01, P05, P07, P09, P11, P17, P19, P21, P23, P27, P29, P33, P35) → che ở khâu dựng.

**Cấu trúc file lạ — phải biết trước khi cắt khung:**
ảnh nguồn là webtoon dạng dải dọc bị cắt xen kẽ. Trang **lẻ** (P01…P37) cao 1500px là trang
nội dung; trang **chẵn** (P04…P36) chỉ cao **140–147px** — đó là **rìa dưới của panel trang
trước bị cắt rời**, chứa nốt phần chữ bị đứt. 17 trang này đánh dấu **NỐI**, không phải panel
riêng, nhưng **không được bỏ** vì giữ vế sau của thoại.
(P02 cao 779px và P38 cao 776px là hai ngoại lệ — P02 là trang nội dung thật, P38 là trang cuối.)

Độ phân giải 1125px rộng — **gấp gần 2× chapter 1** (587px), chữ đọc rất rõ.

---

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| — | P01-a | Banner quảng cáo TruyenQQQ đầu trang | — | — | **BỎ** |
| 1 | P01-b | Hikari ngồi một mình ở bàn học, tay nghịch cây bút, mặt lo; khối tiêu đề đè lên nền cửa sổ: **Chương 4 — "Trận chiến tại cánh cửa"** | "Hy vọng thầy Shimizu không sao…" | lo âm ỉ | 3 |
| 2 | P01-c | Loa gắn tường bật lên | "Xin chú ý," | trung tính | 1 |
| 3 | P02-a | Lớp học nhìn từ trên: bàn ghế trống trơn, chỉ còn Hikari ngồi giữa. Loa báo đóng cửa sớm, yêu cầu rời khuôn viên | "…trường học hôm nay sẽ đóng cửa sớm" | bất thường | 2 |
| 4 | P02-b | Cắt sang hành lang tối: giáo viên và nhân viên mắt trắng dại, miệng há, lê bước; một người kéo cây lau nhà. Tiền cảnh hai trụ đen lớn choán khung. Một giọng ngoài khung buông câu hỏi | "Nghe rõ rồi chứ, thầy trừ tà?" | lạnh gáy | 3 |
| 5 | P03-a | Yojin đứng giữa vòng vây hàng chục người bị chiếm xác đang chìa tay về phía anh; tay anh cầm một con dao ngắn | — | bị dồn | 3 |
| 6 | P03-b | Một thanh niên tóc nâu ló ra ở mép dưới, giục Yojin rút lui | "Ông anh biến đi nhanh được không hả?!" | sốt ruột, hỗn | 2 |
| — | P04 | **NỐI** — rìa dưới panel P03 | — | — | — |
| 7 | P05-a | Cận hai đôi mắt khoá vào nhau qua một vệt tối | — | đối đầu | 2 |
| 8 | P05-b | Ba người bị chiếm xác gào lên, tay chìa tới | — | ghê rợn | 2 |
| 9 | P05-c | Đám đông cầm chổi, cầm cào, dồn từ phía sau | — | vây kín | 2 |
| 10 | P05-d | Yojin bẻ quặt một người bị chiếm xác xuống | "Urrr!" | dứt khoát | 2 |
| 11 | P05-e | Nhìn từ sau lưng thanh niên tóc nâu: đám đông đang nuốt lấy hai người | — | ngộp | 1 |
| 12 | P05-f | Thanh niên tóc nâu càu nhàu, như đã cảnh báo từ trước | "Tôi đã bảo rồi cơ mà?" | bực, quen thuộc | 2 |
| — | P06 | **NỐI** — rìa dưới panel P05 | — | — | — |
| 13 | P07-a | **Trang toàn khung**: Yojin túm tóc một người bị chiếm xác giơ lên, thân người văng tung toé quanh anh; tay áo đen, huy hiệu tròn trắng trên ve áo | (SHWP) | áp đảo | 3 |
| — | P08 | **NỐI** — rìa dưới panel P07 | — | — | — |
| 14 | P09-a | Mái tóc dài của một người bị chiếm xác bay xoã, lao tới | — | dồn dập | 1 |
| 15 | P09-b | Thanh niên tóc nâu giật mình; Yojin bắt đầu một câu dài | "Nếu cậu đã biết tôi là ai…" | chững lại | 3 |
| 16 | P09-c | Bàn tay Yojin bẻ gãy đôi cán chổi; câu nói vế hai | "…mà vẫn chọn cách giúp đỡ những linh hồn tà ác này…" | lạnh | 3 |
| — | P10 | **NỐI** — "…này…" | — | — | — |
| 17 | P11-a | Cận mặt nghiêng Yojin, tay còn cầm mảnh gãy. Anh chốt vế cuối — **đây là lời tuyên chiến, không phải lời hỏi** | "…thế thì cậu chính là kẻ thù của tôi." | lạnh, dứt | 3 |
| 18 | P11-b | Thanh niên tóc nâu toát mồ hôi, nghĩ thầm về Yojin | "Tên này bị cái quái gì vậy?" | hoang mang | 2 |
| 19 | P11-c | Đám bị chiếm xác vung chổi bổ xuống; thanh niên tóc nâu buông một câu đùa nhưng nghe như cảnh báo thật | "Tôi không phải là kẻ thù duy nhất của anh đâu!" | đùa mà nặng | 3 |
| — | P12 | **NỐI** — rìa dưới panel P11 | — | — | — |
| 20 | P13-a | Yojin vung cán chổi gãy, quật ngã cả mảng người bị chiếm xác | "Nào nào, thưa ông." | bạo liệt | 3 |
| 21 | P13-b | Một người bị chiếm xác lãnh đòn | "Urk?" | — | 1 |
| 22 | P13-c | Thanh niên tóc nâu sững ra | "Cái quái gì thế?" | choáng | 1 |
| 23 | P13-d | Hai người bị chiếm xác đứng ngây giữa nền hoa hồng (khung vẽ kiểu shoujo, lệch tông cố ý) | — | hài, lệch tông | 2 |
| 24 | P13-e | Một giọng dỗ dành người bị chiếm xác | "Tôi không muốn làm ông bị thương đâu…" | dịu bất ngờ | 2 |
| 25 | P13-f | Cận một con mắt Yojin qua khe tóc | — | sắc | 2 |
| — | P14 | **NỐI** — rìa dưới panel P13 | — | — | — |
| 26 | P15-a | Yojin phóng cây chổi lên cầu thang, trúng người bị chiếm xác đang xông xuống | (SHP) | quyết liệt | 2 |
| 27 | P15-b | Thanh niên tóc nâu hét lên — **hét vì lo cho người bị chiếm xác, không phải lo cho mình** | "Cẩn thận đi!" / "Oa!" | hoảng, vị tha | 3 |
| — | P16 | **NỐI** — rìa dưới panel P15 | — | — | — |
| 28 | P17-a | Hành lang dài ngổn ngang người nằm gục; vài người lờ mờ tỉnh lại, ngơ ngác; một phụ nữ cầm điện thoại. Trận đánh đã xong | (KRMPL) | tàn cuộc | 3 |
| 29 | P17-b | Yojin kề mũi dao vào cổ thanh niên tóc nâu, ra lệnh | "Không được cử động." | lạnh, áp chế | 3 |
| — | P18 | **NỐI** — rìa dưới panel P17 | — | — | — |
| 30 | P19-a | Dao vẫn kề cổ; Yojin cấm cậu ta mở miệng ngoài việc trả lời | "Chỉ được mở mồm khi trả lời câu hỏi của tôi." | thẩm vấn | 3 |
| 31 | P19-b | Thanh niên tóc nâu nghĩ thầm, đã hết cả đùa | "Thằng cha này bị cái gì vậy?!" | sợ thật | 2 |
| 32 | P19-c | Một thứ trắng, dài, có vuốt đang trườn đi trong hành lang; Yojin hỏi thẳng | "Cậu là ai, và mục đích của cậu là gì?" | truy vấn | 3 |
| 33 | P19-d | Thanh niên tóc nâu nhắm mắt chịu trận | — | cam chịu | 1 |
| 34 | P19-e | Cậu ta cười gượng, xin hàng cho qua chuyện | "Biết rồi màaaaa," | né tránh | 2 |
| — | P20 | **NỐI** — rìa dưới panel P19 | — | — | — |
| 35 | P21-a | Mũi dao chĩa vào một sinh vật trắng lông lá; thanh niên tóc nâu chịu thua | "Anh bắt thóp tôi rồi…" | bị lột mặt | 3 |
| 36 | P21-b | Sinh vật trắng bị xuyên thủng ngực, bật ngửa | (BSH) | dứt điểm | 3 |
| 37 | P21-c | Thanh niên tóc nâu kêu lên tiếc | "Ôi thôi nào!" / "Tôi thấy rồi…" | tiếc, lộ | 2 |
| 38 | P21-d | Cận mắt Yojin: anh chốt rằng cần một buổi nói chuyện khác | "…xem ra cậu quyết tâm muốn gây khó dễ đây mà." | đe doạ ngầm | 3 |
| — | P22 | **NỐI** — "…cần một cuộc thảo luận 'sâu sắc' hơn rồi…" | — | — | — |
| 39 | P23-a | **Cửa lớp bật mở — Hikari đứng đó.** Cậu nhận ra người đang kề dao vào cổ người khác và reo lên. **Khung này xác nhận người áo đen tóc sáng suốt chapter là Yojin** | "Ô, chú Yojin!" | lật tông tức thì | 3 |
| 40 | P23-b | Yojin xoay người trong nháy mắt, đổi tư thế thành thân thiện; thanh niên tóc nâu chữa cháy | "Thầy ấy hoàn toàn khỏi rồi!" | diễn, hài căng | 3 |
| 41 | P23-c | Hikari hỏi về thầy chủ nhiệm — **mối lo mở đầu chapter quay lại** | "Thầy Shimizu ổn chứ chú?" | ngây thơ | 3 |
| — | P24 | **NỐI** — "…rồi!" | — | — | — |
| 42 | P25-a | Yojin ghé sát tai thanh niên tóc nâu thì thầm đề nghị "hợp tác" (chữ viết tay = nói nhỏ), miệng vẫn nói to cho Hikari nghe, rồi bảo Hikari đợi thêm | thầm: "Hợp tác đi, rồi chúng ta có thể tránh được bất kỳ chuyện không hay nào." | hai mặt, lạnh | 3 |
| 43 | P25-b | Thanh niên tóc nâu cười xoà qua ô cửa, bịa một lời giải thích trơn tru cho Hikari | "Anh chỉ là một trong những nhân viên hậu cần thôi!" | bịa trơn tru | 3 |
| 44 | P25-c | Hikari đáp ngoan, rồi nói lý do cậu ra khỏi lớp: mãi không thấy thầy quay lại | "Em cứ thắc mắc không biết có chuyện gì xảy ra…" | thật thà | 2 |
| 45 | P25-d | Hai người lớn liếc nhau | "À!" / "Ừm…" | gượng | 1 |
| — | P26 | **NỐI** — "…ấy quay lại." | — | — | — |
| 46 | P27-a | Thầy Shimizu tỉnh lại giữa hành lang, ôm đầu, không nhớ gì | "Mình đang làm gì ở đây thế này?" | trống rỗng | 3 |
| 47 | P27-b | Yojin siết cổ tay thanh niên tóc nâu, nói sẽ không lâu | "Chuyện này không mất nhiều thời gian đâu." | ép | 2 |
| 48 | P27-c | Thanh niên tóc nâu liếc, gợi ý rằng cảnh này trông rất khó coi | "Anh chắc trông thế này ổn chứ?" | dò dẫm | 2 |
| 49 | P27-d | Cận Yojin mỉm cười — **nụ cười này là câu trả lời, không phải sự đồng tình** | "Đúng vậy." | lạnh, nguy hiểm | 3 |
| 50 | P27-e | Cậu ta nói nốt: nếu giáo viên nào phát hiện thì phiền lắm | "…thì sẽ phiền phức lắm đấy…" | lo | 2 |
| — | P28 | **NỐI** — rìa dưới panel P27 | — | — | — |
| 51 | P29-a | **Một cú quật đen giáng thẳng vào mặt thanh niên tóc nâu**, máu bắn ra | (WHAM) | thẳng tay | 3 |
| 52 | P29-b | Cắt sang toàn cảnh thành phố ban đêm, trăng lưỡi liềm; (ghi chú người dịch chèn ngoài truyện) | — | hạ nhiệt, lạnh | 2 |
| 53 | P29-c | Khung đen đặc, tiếng lạch cạch, hai bóng thoại rỗng | "…" / "…" | bất an | 2 |
| — | P30 | **NỐI** — khung đen | — | — | — |
| 54 | P31-a | Trong bóng tối, Yojin búng tay bật sáng | (FWK) | chủ động | 2 |
| 55 | P31-b | Thanh niên tóc nâu tỉnh dậy, mặt bầm tím, sưng; Yojin nói tỉnh bơ | "Có vẻ tôi lỡ tay đánh cậu mạnh hơn dự tính rồi." | tàn nhẫn nhẹ nhàng | 3 |
| 56 | P31-c | Cậu ta nhìn quanh căn phòng lạ, hoảng; Yojin chặn lại | "Tôi mới là người đặt câu hỏi ở đây." / "Giờ thì nói đi." | áp đảo | 3 |
| 57 | P31-d | Hai mặt sát nhau; Yojin hỏi thẳng cậu ta được gì khi hợp tác với các linh hồn | "Cậu hy vọng sẽ đạt được điều gì…" | truy đến cùng | 3 |
| — | P32 | **NỐI** — "…với các linh hồn?" | — | — | — |
| 58 | P33-a | Thanh niên tóc nâu mở lời rồi tắc lại | "Tôi…" | nghẹn | 2 |
| 59 | P33-b | Yojin đứng lặng, chờ | — | kiên nhẫn lạnh | 1 |
| 60 | P33-c | Cậu ta quay mặt đi | — | trốn | 2 |
| 61 | P33-d | Yojin đứng cạnh cửa có dán một lá bùa: căn phòng đã được lập **kết giới** | "Căn phòng này đã được thiết lập kết giới…" | lạnh, có chuẩn bị | 3 |
| 62 | P33-e | Thanh niên tóc nâu bị trói dây thừng, ngồi dựa tường, đầu cúi — và nói câu quyết định | "…không thể nói được." | bất lực | 3 |
| 63 | P33-f | Yojin giải thích kết giới chặn âm thanh: hét đến mấy cũng không ai ngoài phòng nghe thấy | "Cho dù cậu có hét lớn đến mức nào…" | ép tới cùng | 3 |
| — | P34 | **NỐI** — "…này nghe thấy đâu." | — | — | — |
| 64 | P35-a | Mũi dao cắt phăng dây thừng; Yojin nói nốt vế còn lại của kết giới | "Chưa kể, các linh hồn cũng sẽ không nghe thấy cậu đâu." | mở khoá | 3 |
| 65 | P35-b | Yojin ngồi xuống ngang tầm, đưa tay đỡ mặt cậu ta — **cả cuộc tra khảo lật thành một lối thoát** | "Nó đang lợi dụng cậu…" | dịu đột ngột | 3 |
| 66 | P35-c | Cận hai gương mặt sát nhau, Yojin chốt câu hỏi | "…phải không?" | căng, thương | 3 |
| — | P36 | **NỐI** — rìa dưới panel P35 | — | — | — |
| 67 | P37-a | **CÚ LẬT.** Cắt sang một nơi tối: một thân người trần, nhiều cánh tay dang rộng, lơ lửng. Giọng nó nhắc tới "thằng nhóc đó" | "Thằng nhóc đó đã làm hỏng việc của ta." | rợn | 3 |
| 68 | P37-b | Cận cái miệng khổng lồ nhe răng cười của sinh vật nhiều tay; nó tuyên án | "…những đứa trẻ hư hỏng và vô dụng… thì phải bị trừng phạt." | ác, khoái trá | 3 |
| 69 | P37-c | Cận hai con mắt to, con ngươi hình lục giác trắng; nó nói nốt phần đe doạ | "Và cả những thứ mà nó yêu thương nữa." | lạnh sống lưng | 3 |
| 70 | P38-a | Dải kết chapter | "CÒN TIẾP!" | — | 1 |
| — | P38-b | Banner quảng cáo TruyenQQQ cuối trang | — | — | **BỎ** |

---

### C. Điểm cao trào

Chapter này có **bốn đỉnh** và **một cú lật cuối**. Không dồn hết vào một chỗ.

**Đỉnh 1 — hành động (P07, TS 3).** Trang toàn khung, Yojin một mình phá vòng vây.
Hình mạnh nhất chapter, nhưng chỉ là nền cho ba đỉnh sau.

**Đỉnh 2 — tuyên chiến (P09 → P11, TS 3).** Câu dài của Yojin bị bẻ làm ba panel:
*"Nếu cậu đã biết tôi là ai… mà vẫn chọn cách giúp đỡ những linh hồn tà ác này…
thế thì cậu chính là kẻ thù của tôi."* Đây là lần đầu nghề của Yojin được đối chiếu
trực tiếp với một con người, không phải một con quái.

**Đỉnh 3 — cánh cửa (P23, TS 3).** Hikari mở cửa đúng lúc dao đang kề cổ. **Đây là "cánh
cửa" trong tên chương.** Trận chiến thật không nằm ở hành lang mà ở chỗ Yojin phải giấu
tất cả trong một giây — đúng mạch "Yojin cố ý giấu Hikari" đã chốt ở bible C1.

**Đỉnh 4 — cảm xúc (P35, TS 3).** Yojin cắt dây trói rồi hỏi *"Nó đang lợi dụng cậu…
phải không?"* Toàn bộ cuộc tra khảo từ P17 đến P33 lật nghĩa: kết giới không phải để tra tấn
mà **để cậu ta nói được mà không bị nghe thấy**.

**CÚ LẬT CUỐI (P37) — đổi nghĩa toàn bộ phần đầu.**
Một sinh vật nhiều tay ở nơi khác gọi thanh niên tóc nâu là *"thằng nhóc đó"*, nói cậu ta
*"làm hỏng việc của ta"*, rồi phán: *"những đứa trẻ hư hỏng và vô dụng thì phải bị trừng phạt.
Và cả những thứ mà nó yêu thương nữa."*

Đọc lại từ đầu thì ba chi tiết mang nghĩa khác hẳn:
1. **P03 "Ông anh biến đi nhanh được không hả?!"** — không phải cản đường Yojin, mà là đuổi anh
   đi trước khi anh thấy quá nhiều.
2. **P11 "Tin tôi đi, tôi không phải là kẻ thù duy nhất của anh đâu!"** — nghe như câu đùa,
   thực ra là lời cảnh báo về thứ ở P37.
3. **P15 "Cẩn thận đi!"** và **P13 "Tôi không muốn làm ông bị thương đâu…"** — cậu ta lo cho
   những người bị chiếm xác, nghĩa là cậu **không đứng cùng phe với thứ đang sai khiến mình**.
4. **P33 "…không thể nói được."** — không phải ngoan cố, mà là **không dám**, vì sợ bị trừng phạt.

Nói cách khác: vai của thanh niên tóc nâu chuyển từ **kẻ đồng loã** sang **con tin**, và câu
hỏi của Yojin ở P35 hoá ra đã đúng trước khi người xem kịp tin.

---

### D. Chưa rõ

**Không đoán, không đặt tên thay.**

- **Tên thanh niên tóc nâu — CHƯA XUẤT HIỆN.** Suốt 38 trang không ai gọi tên cậu ta. Cậu tự
  nhận *"chỉ là một trong những nhân viên hậu cần thôi"* (P25) nhưng đó là lời bịa để lừa Hikari.
  Trong video phải gọi bằng mô tả (ví dụ "thanh niên tóc nâu"), **không được đặt tên**.
- **Sinh vật nhiều tay ở P37 — CHƯA CÓ TÊN.** Không gọi là "trùm", "cấp trên", "thủ lĩnh".
  Chỉ biết: ở một nơi tối, nhiều tay, miệng lớn, mắt có con ngươi lục giác, và nó coi thanh niên
  tóc nâu là "thằng nhóc" của nó.
- **Quan hệ giữa hai kẻ đó — CHƯA RÕ.** Bị cưỡng ép, bị mua chuộc, hay ràng buộc gì khác: truyện
  chưa nói. Yojin mới chỉ *hỏi* "nó đang lợi dụng cậu, phải không?" — cậu ta **chưa trả lời**.
- **"Những thứ mà nó yêu thương" là ai — CHƯA RÕ.** Không có khung nào chỉ ra.
- **Ai nói câu "Nghe rõ rồi chứ, thầy trừ tà?" (P02)** — giọng ngoài khung, không thấy người nói.
  Hai trụ đen ở tiền cảnh **chưa rõ là chân người hay cột/bàn**.
- **Người nói "Nào nào, thưa ông." và "Tôi không muốn làm ông bị thương đâu…" (P13)** —
  đuôi bong bóng không chỉ rõ; nhiều khả năng là thanh niên tóc nâu nói với người bị chiếm xác,
  nhưng **không chắc**.
- **Sinh vật trắng lông lá (P19, P21) có phải cùng loại "oán hồn" ở C1 hay không — CHƯA RÕ.**
  Truyện không gọi tên nó.
- **Thầy Shimizu** — tên mới, giáo viên ở trường Hikari, bị chiếm xác rồi tỉnh lại và **không nhớ
  gì** (P27). Chưa rõ bị chiếm từ khi nào, do ai, và vì sao lại là ông.
- **Căn phòng có kết giới ở P31–P35 nằm ở đâu, của ai — CHƯA RÕ.** Chỉ thấy một lá bùa dán cửa.
- **Vì sao cả trường bị chiếm xác cùng lúc — CHƯA RÕ.** Không có khung nào giải thích.
- **Hikari có liên quan gì tới vụ này không — CHƯA RÕ.** Chapter này không nhắc "thể chất đặc biệt".
  **Không được kéo mốc C1 vào để suy diễn.**
- **Chưa có beat sheet cho C2 và C3** (`series/TWB/C2/results/` và `C3/results/` chỉ có thư mục rỗng).
  Vì vậy **chưa rõ thanh niên tóc nâu và thầy Shimizu đã xuất hiện ở C2–C3 hay chưa**, và chưa rõ
  chapter này nối tiếp tình huống nào. Nên đọc C2–C3 trước khi viết lời kể.

**Ghi chú thuật ngữ — cần chốt trước khi viết lời:**
bản dịch C4 dùng **"linh hồn"** và **"linh hồn tà ác"** (P09, P31, P35) cho thứ mà bible đã chốt
gọi là **"oán hồn"**. Bible yêu cầu dùng **một từ duy nhất** → giữ **"oán hồn"** khi kể, chỉ trích
nguyên văn "linh hồn tà ác" nếu cho nghe thoại gốc.
Thuật ngữ **mới** của chapter này: **kết giới** (P33) — giữ nguyên, bible chưa có mục này.

---

## DỪNG Ở ĐÂY — chờ duyệt

Ba câu hỏi cần trả lời trước khi sang `/manga-narration`:

1. **Panel có thật không?** — 70 panel ở mục B có khớp với ảnh không, đặc biệt cụm P13
   (khung hoa hồng lệch tông) và P19–P21 (sinh vật trắng)?
2. **Tên nhân vật đúng chưa?** — Yojin và Hikari lấy từ bible; **thầy Shimizu** là tên mới của
   chapter này; thanh niên tóc nâu và sinh vật ở P37 **cố ý để trống**. Duyệt cách gọi thay thế?
3. **Trọng số hợp lý chưa?** — bốn đỉnh (P07 · P11 · P23 · P35) cộng cú lật P37 có đúng là chỗ
   cần dồn thời lượng trong ngân sách 180 giây không, hay cắt bớt đỉnh 1 để dành cho P23 và P37?
