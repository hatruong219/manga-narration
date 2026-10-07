# BEAT SHEET — Twilight Blade C5 "Dấu vết bóng tối"

Nguồn ảnh: `series/TWB/C5/pages-clean/` (đã bỏ chrome site)
Cốt truyện: Chiyoko Maruume · Minh hoạ: Tokegoro
Trạng thái: **ĐỦ 21/21 trang** · **81 panel** (P21 BỎ)
Chiều đọc: **phải → trái** (xác nhận ở P03: câu hỏi "Chú đang làm gì thế ạ?" nằm ở khung PHẢI,
câu trả lời "Chú đang làm cơm nắm" nằm ở khung TRÁI).

### A. Kiểm tra đầu vào

21 ảnh `TWB_C5_P01`–`P21`, **liên tục, không thiếu trang**.

| Trang | Kích thước clean | Ghi chú |
|---|---|---|
| P01 | 822×1052 | đã cắt mép trên; vẫn còn watermark `NetTruyen12s` |
| P02 | 822×162 | **dải mỏng nối tiếp P01** — không phải trang thiếu, là phần đáy khung bị tách |
| P03–P19 | 822×1200 | khổ chuẩn |
| P20 | 822×1500 | **clean-pages CHƯA cắt banner quảng cáo đáy** (dải xanh `TRUYENQQQ.COM` + dàn nhân vật lạ) → phải crop tay khi dựng |
| P21 | 822×134 | **quảng cáo thuần, không có nội dung truyện** → **BỎ** |

- Không so được số px đã cắt: file trong `pages/` là JPEG progressive, header không parse ra
  kích thước gốc tin cậy. Chỉ ghi nhận `pages-clean/` đã được re-encode và rộng 822px.
- **Watermark `NetTruyen12s` còn ở góc trên** các trang P01, P04, P06, P08, P09, P10, P11, P12,
  P14, P15, P18 → phải che ở khâu dựng.
- Dải "CÒN TIẾP…" ở P20 vẫn giữ.

### ⚠ Ba điểm phải chốt trước khi viết lời

1. **Chương này KHÔNG có Hikari sau P04.** Hikari chỉ xuất hiện ở đoạn mở (P01–P04) rồi đi ngủ.
   Toàn bộ phần còn lại là Yojin + **chàng trai lạ** (kẻ đã tấn công anh) + mẹ cậu ta.
2. **Chàng trai không phải phản diện** — cậu bị oán hồn ép bằng mạng mẹ mình (P08).
   Nhưng **cú lật P19–P20 lật lại chính điều đó**: việc cứu mẹ cậu chính là cái bẫy.
3. **Từ trong ảnh là "quái vật"**, không phải "oán hồn". Theo bible §2 thì chốt dùng **oán hồn**
   cho nhất quán — cột "Sự việc" dưới đây dùng *oán hồn*, cột thoại giữ nguyên văn *quái vật*.

### B. Beat Sheet

| # | Panel | Sự việc | Câu thoại chốt (trích NGẮN) | Cảm xúc | TS |
|---|---|---|---|---|---|
| 1 | P01-a | Trăng lưỡi liềm sau mây — đêm | — | tĩnh, lạnh | 1 |
| 2 | P01-b | Phòng Hikari, cậu đứng cạnh bàn học. **Băng tiêu đề: Chương 5 — Dấu vết bóng tối** | — | mở chương | 2 |
| 3 | P01-c | Cận Hikari, nhớ lại buổi tư vấn ban ngày, thấy căng thẳng, có nhắc "bị gián đoạn một chút" | "Buổi tư vấn hôm nay làm mình căng thẳng quá" | mệt, còn dư chấn | 2 |
| 4 | P01-d | Hikari mở cửa ra khỏi phòng, mong thầy Shimizu không sao | "Mong là thầy Shimizu sẽ không sao..." | lo cho người khác | 2 |
| 5 | P01-e | Yojin trong bếp, găng đen, đang cầm nắm cơm. Hikari gọi từ ngoài khung | "Chú Yojin? Có chuyện gì sao?" / "À... Hikari..." | bị bắt quả tang | 2 |
| 6 | P02-a | Nắm cơm trong tay Yojin **vỡ vụn** trên bàn; Hikari nghiêng đầu nhìn | SFX ボロ | hài, vụng về | 1 |
| 7 | P03-a | Hikari hỏi chú đang làm gì; Yojin bóp cơm, lại hỏng lần nữa | "A, lại nữa rồi..." | hài | 1 |
| 8 | P03-b | Yojin nói đang nắm cơm cho bữa khuya, than khó kiểm soát lực tay | "Kiểm soát lực tay khó quá." | thú nhận | 2 |
| 9 | P03-c | Hai nắm cơm trên đĩa bị nén chặt cứng, méo | "Bị nén chặt lại luôn rồi...?" | hài, tương phản | 2 |
| 10 | P03-d | Hikari mách dùng cái bát để tạo hình; Yojin sáng mắt | "Ra là vậy. Tạo hình... ra là có cách đó...!" | ấm, thân | 2 |
| 11 | P03-e | Yojin giơ nắm cơm tròn hoàn hảo, cảm ơn Hikari. Cậu bé reo "Yay!" | "Cảm ơn cháu nhé, Hikari-kun!" | vui, gia đình giả | 2 |
| 12 | P04-a | Rót nước; Yojin khen Hikari biết nhiều mẹo, nói khá bất ngờ khi được cháu chỉ | "Cháu biết nhiều mẹo hay thật đấy." | dịu | 1 |
| 13 | P04-b | Hikari uống nước; Yojin dẫn lời thầy giáo khen cậu chăm học | "...vì Hikari lúc nào cũng chăm chỉ học hành mà." | khích lệ | 1 |
| 14 | P04-c | Yojin đứng ở cửa, bưng đĩa, **báo tin thầy Shimizu đã hồi phục hoàn toàn**; Hikari mừng | "Nghe nói thầy ấy đã hồi phục hoàn toàn rồi đấy." | nhẹ gánh | 2 |
| 15 | P04-d | Cửa phòng Hikari — **có dán bùa/phù chú**. Hai chú cháu chúc ngủ ngon | "Cháu cứ yên tâm mà nghỉ ngơi đi nhé." | ấm bề mặt, lạnh bề sâu | 3 |
| 16 | P04-e | Yojin quay ra, khung cửa nứt vỡ và dán bùa. Mặt anh tắt hết vẻ dịu vừa rồi | — | **đổi mặt nạ** | 3 |
| 17 | P05-a | Trong phòng khác: **một chàng trai lạ**, tóc rối, mặt băng, ngồi bệt dưới sàn | "Xin lỗi, để cậu đợi lâu rồi." | kiệt sức, cảnh giác | 3 |
| 18 | P05-b | Cậu ta hỏi đây là nhà Yojin thật à; nội tâm chửi anh điên vì rước kẻ vừa tấn công mình về | "Lại đi rước kẻ vừa tấn công mình về nhà..." | hoang mang | 3 |
| 19 | P05-c | Yojin gạt đi: mấy trò tấn công đó chẳng đánh gục được anh; hỏi cậu ta có đói không | "Quan trọng hơn là cậu đang đói bụng đúng không?" | bình thản áp đảo | 3 |
| 20 | P05-d | Đặt đĩa cơm nắm xuống trước mặt cậu ta | "Ăn đi." | ra lệnh mềm | 2 |
| 21 | P06-a | Yojin ăn trước để chứng minh; bảo không có độc | "Không có độc đâu mà sợ." | trấn an kiểu lạ | 2 |
| 22 | P06-b | Cậu ta nhai, tiếng nghe không giống ăn cơm nắm; vẫn nuốt | "Không sao, vẫn ăn được là tốt rồi." | hài đen | 1 |
| 23 | P06-c | Yojin lập luận: nếu cậu thật sự theo phe oán hồn và muốn giết anh thì đã ra tay dứt khoát hơn | "...thì cậu đã ra tay dứt khoát hơn rồi." | đọc vị | 3 |
| 24 | P06-d | Yojin kể **đã nhìn thấy một kẻ bất động ở rất xa**, rời đi ngay sau khi cậu ta ngất → đó là **kẻ giám sát** cậu. Chú thích khung: *Thị lực 10/10* | "Khả năng cao kẻ đó chính là kẻ giám sát cậu." | tiết lộ lạnh | 3 |
| 25 | P06-e | Cậu ta vỡ ra là mình bị theo dõi lén, chửi kẻ đó | "Lén lút theo dõi sao...?" / "Cái thằng khốn kiếp đó...!" | phẫn nộ, bị phản bội | 3 |
| 26 | P07-a | Yojin cúi xuống, đặt tay lên đầu cậu ta, hỏi con oán hồn ra lệnh gì | "Cậu đã bị con quái vật đó ra lệnh làm gì?" | dồn, dịu | 3 |
| 27 | P07-b | Cận mặt cậu ta, bắt đầu kể: nó đột nhiên xuất hiện | "Nó... đột nhiên xuất hiện." | sợ hồi tưởng | 2 |
| 28 | P07-c | Hồi tưởng: **hình ảnh Hikari đang cười** — "đứa trẻ có vết sẹo ở mắt" | "Đứa trẻ... có vết sẹo ở mắt..." | lạnh sống lưng | 3 |
| 29 | P07-d | Cận mặt oán hồn, mắt trắng trợn: lệnh **bắt đứa trẻ đó** | "Và ra lệnh cho tôi phải bắt đứa trẻ đó đi." | uy hiếp | 3 |
| 30 | P08-a | Hồi tưởng: oán hồn với xúc tu đen, lệnh **giết sạch kẻ cản đường và cả lũ pháp sư**; cấm phản bội dù chỉ là sai sót | "Hãy giết sạch... và cả lũ pháp sư nữa." | tàn bạo | 3 |
| 31 | P08-b | **Miệng khổng lồ thè lưỡi dài xuống người mẹ cậu đang nằm giường bệnh** — lời đe: mày không muốn mất mẹ đúng không | "...không muốn mất đi người mẹ yêu dấu của mình đúng không?" | kinh dị, tống tiền | 3 |
| 32 | P08-c | Về hiện tại: cậu ta cúi rạp, xin nhận mọi hình phạt vì đã tấn công | "Tôi sẽ nhận lấy mọi hình phạt thích đáng..." | nhục, cam chịu | 3 |
| 33 | P09-a | Cậu ta khóc, cầu xin **ít nhất hãy cứu mẹ tôi** | "Xin hãy cứu lấy mẹ tôi...!" | tuyệt vọng | 3 |
| 34 | P09-b | Khung tốc độ — Yojin bật dậy | — | chuyển nhịp | 1 |
| 35 | P09-c | Yojin hỏi mẹ cậu ở đâu; cậu đáp đang nằm viện, **ngất ở nơi làm việc và chưa tỉnh lại** | "Từ sau khi bà ấy ngất xỉu ở nơi làm việc..." | manh mối | 3 |
| 36 | P09-d | Yojin đặt tay lên vai cậu ta: **cậu không có lỗi** | "Cậu không có lỗi." | tha thứ | 3 |
| 37 | P10-a | Cận mặt cậu ta, sững ra | "Tôi hiểu rồi." | được gỡ gánh | 2 |
| 38 | P10-b | Yojin quay lưng bước đi, hứa chắc chắn cứu được mẹ cậu, rồi nói "với cả..." | "Tôi chắc chắn sẽ cứu được mẹ cậu." | cam kết | 3 |
| 39 | P10-c | Cận Yojin trong bóng tối: anh nhất định phải **"nói chuyện" thật dài** với con oán hồn đó | "...tôi nhất định phải 'nói chuyện' thật dài với nó..." | sát khí nén | 3 |
| 40 | P11-a | Ngoại cảnh bệnh viện đêm, trăng lưỡi liềm; biển tên chữ Nhật 岩屋 | — | chuyển cảnh lạnh | 2 |
| 41 | P11-b | Hành lang bệnh viện, một y tá đi tuần cầm đèn pin | — | yên tĩnh gượng | 1 |
| 42 | P11-c | Y tá dừng trước cửa kính mờ **phòng 316** (biển tên chữ Nhật 吉野) | — | thường nhật | 2 |
| 43 | P11-d | **Một bóng đen hiện sau lớp kính mờ** của phòng 316 | — | rợn | 3 |
| 44 | P11-e | Cận mặt y tá hoảng loạn | "!?" | sốc | 3 |
| 45 | P12-a | Nhìn lại thì cửa kính trống trơn; cô tự nhủ chắc tưởng tượng | "Chắc do mình tưởng tượng ra thôi." | tự trấn an | 2 |
| 46 | P12-b | Cô đi tiếp, lau mồ hôi, nhắc mình phải quen đi tuần đêm — **phía sau lưng, bệnh nhân liệt giường đang đứng chân trần ở cửa phòng** | "Chỗ đó là phòng của một bệnh nhân liệt giường mà..." | **rợn tột độ** | 3 |
| 47 | P13-a | Yojin (cầm ô cán móc) và chàng trai chạy tới trước **岩屋病院**; Yojin hỏi phòng mẹ cậu ở đâu | "Phòng bệnh của mẹ cậu ở đâu?" | gấp gáp | 3 |
| 48 | P13-b | Cậu ta hụt hơi đáp "tầng ba"; Yojin chốt: vậy con oán hồn cũng đang quanh đây | "Vậy thì con quái vật đó cũng đang ở quanh đây rồi." | căng | 3 |
| 49 | P13-c | Cậu ta hỏi rốt cuộc quái vật là cái gì, ngoài cậu chẳng ai nhìn thấy nó | "Ngoài tôi ra thì chẳng ai nhìn thấy nó cả..." | hoang mang | 2 |
| 50 | P13-d | Yojin giải thích: chúng không thuộc về thế giới này — **những kẻ bị ruồng bỏ** | "Chúng là những kẻ bị ruồng bỏ." | **thiết lập thế giới** | 3 |
| 51 | P14-a | Cậu ta lặp lại "kẻ bị ruồng bỏ...?" | "Kẻ bị ruồng bỏ...?" | chưa hiểu | 1 |
| 52 | P14-b | Yojin: người **nhìn thấy được** chúng mới là hiếm | "...những người nhìn thấy được chúng mới là hiếm đấy..." | tiết lộ | 3 |
| 53 | P14-c | Chính vì thế nên tên đó mới **lợi dụng** cậu | "Chính vì thế nên tên đó mới lợi dụng cậu." | xót, sáng tỏ | 3 |
| 54 | P14-d | Yojin: loại bầy đàn sức chiến đấu thấp nhưng **trí thông minh rất cao** | "...bù lại chúng có trí thông minh rất cao..." | **gài cho cú lật** | 3 |
| 55 | P14-e | Cậu ta đứng khựng, ngước lên gọi "Mẹ...?"; Yojin: "Hả?" | "Mẹ...?" | đứng tim | 3 |
| 56 | P14-f | Hai người ngước nhìn toà nhà — **một bóng người đứng trên mép mái** | — | báo động | 3 |
| 57 | P14-g | Cận một con mắt trống rỗng dưới lọn tóc dài | — | vô hồn | 3 |
| 58 | P15-a | Toàn cảnh: **mẹ cậu mặc áo bệnh nhân, chân trần, đứng trên lan can mái**, mắt trắng dã | — | **kinh dị đỉnh 1** | 3 |
| 59 | P15-b | Cậu ta gào "KHÔNG!!" | "KHÔNG!!" | vỡ oà | 3 |
| 60 | P15-c | Mắt Yojin nheo lại, đo tình huống | — | tính toán | 2 |
| 61 | P15-d | Cận mặt bà, hoàn toàn vô cảm | — | trống rỗng | 3 |
| 62 | P15-e | Cậu ta hét "LÀM ƠN!" | "LÀM ƠN!" | van xin | 3 |
| 63 | P15-f | Bàn chân trần rời khỏi lan can | — | **điểm không quay lại** | 3 |
| 64 | P16-a | **Bà rơi đầu xuống trước dọc mặt toà nhà**; cậu ta gào "MẸ!!!" | "MẸ!!!" | **cao trào hành động** | 3 |
| 65 | P16-b | Cận mặt cậu ta gào, mắt trợn | — | tuyệt vọng | 3 |
| 66 | P16-c | Yojin bật người lên, **móc ô vào lan can/bờ tường** làm điểm tựa | SFX | phản xạ | 3 |
| 67 | P16-d | Yojin lao ngang mặt đất/tường để cắt đường rơi | — | tốc độ phi nhân | 3 |
| 68 | P17-a | **Yojin đón được bà giữa không trung**, tay bà buông thõng | — | **giải toả** | 3 |
| 69 | P17-b | Cận mặt cậu ta, chưa dám tin | — | nín thở | 2 |
| 70 | P17-c | Yojin tiếp đất, đỡ bà; cậu ta lao tới gọi "Mẹ!"; Yojin trấn an bà không bị thương | "Không sao đâu. Bà ấy không bị thương..." | nhẹ nhõm **giả** | 3 |
| 71 | P17-d | Cận mắt Yojin, tóc bà, SFX ふっ — **một hơi thở lạ phát ra từ bà** | SFX ふっ | gài bẫy | 3 |
| 72 | P18-a | Trên trời: **một khối tóc đen xù có nhiều mắt nhỏ** hiện ra, gọi Yojin là "đại pháp sư", nói biết ngay anh sẽ đến | "Ta biết ngay là ngươi sẽ đến mà... Tên đại pháp sư..." | **chờ sẵn** | 3 |
| 73 | P18-b | Cậu ta hét "Mày!"; Yojin bảo cứ giao hắn cho anh | "Cứ giao hắn cho tôi." | chắn trước | 3 |
| 74 | P18-c | Yojin bảo cậu đưa mẹ đến nơi an toàn — câu bị cắt ngang bằng dấu gạch | "...đến nơi an toàn đi—" | **câu chưa kịp xong** | 3 |
| 75 | P18-d | Cận mặt Yojin, quyết đoán | — | sẵn sàng đánh | 2 |
| 76 | P19-a | Yojin **trao bà cho con trai**, tay vẫn đặt trên vai bà, tay kia cầm ô; mái tóc dài của bà che kín mặt giữa hai người | — | tưởng là an toàn | 3 |
| 77 | P19-b | Cậu ta sững: "Hả...?" | "Hả...?" | linh cảm | 2 |
| 78 | P19-c | **Miệng bà há ra thành miệng quái — oán hồn nói qua bà: "Làm tốt lắm, thằng nhóc. Đến phút cuối cùng thì mày cũng có ích đấy."** | "Đến phút cuối cùng thì mày cũng có ích đấy." | **CÚ LẬT** | 3 |
| 79 | P19-d | Bà cúi gằm mặt xuống, tiếng khục trong cổ | SFX ぐ... | hỏng hết | 3 |
| 80 | P20-a | **Toàn khung là mặt oán hồn khổng lồ**, tóc đen, mắt trắng, răng nhọn, xung quanh lơ lửng những thân người nhỏ: "Bây giờ, đại pháp sư... là của ta." | "Bây giờ, đại pháp sư... là của ta." | **CAO TRÀO CUỐI** | 3 |
| 81 | P20-b | Cận mắt Yojin **có vòng dấu lạ trong tròng**, xúc tu đen bám lấy đầu anh. Dải "CÒN TIẾP…" | — | **hẫng, treo** | 3 |
| — | P21 | Dải quảng cáo thuần | — | — | **BỎ** |

> Tổng: **81 panel có nội dung** (P01→P20), 1 trang BỎ.

### C. Điểm cao trào

Chương này có **bốn đỉnh**, và đỉnh cuối lật ngược ba đỉnh trước:

1. **Đỉnh cảm xúc — P08-b → P09-a.** Miệng oán hồn thè lưỡi xuống người mẹ đang hôn mê, rồi
   cậu trai khóc "Xin hãy cứu lấy mẹ tôi...!". Đây là chỗ nhân vật từ *kẻ tấn công* thành
   *nạn nhân bị tống tiền*. Đòn bẩy cho toàn bộ phần sau.
2. **Đỉnh rợn — P11-d → P12-b.** Bóng đen sau kính mờ phòng 316, rồi y tá tự trấn an "chắc do
   mình tưởng tượng" trong khi **sau lưng cô, bệnh nhân liệt giường đang đứng chân trần**.
   Người xem biết trước nhân vật. Đọc lại sau P19 thì khung này mang hai nghĩa: đó không phải
   bà ấy tỉnh dậy, mà là thứ bên trong bà ấy đi ra.
3. **Đỉnh hành động — P15-f → P17-a.** Chân trần rời lan can, bà rơi đầu xuống trước, Yojin móc
   ô làm điểm tựa, lao ngang và đón được giữa không trung. Câu "Bà ấy không bị thương..." là
   đỉnh giải toả — và là **câu sai nhất chương**.
4. **CÚ LẬT + cao trào cuối — P19-c → P20.** Miệng bà há ra, oán hồn nói qua bà: *"Làm tốt lắm,
   thằng nhóc. Đến phút cuối cùng thì mày cũng có ích đấy."* Rồi mặt oán hồn phủ kín trang P20:
   *"Bây giờ, đại pháp sư... là của ta."* Khung cuối: mắt Yojin có vòng dấu lạ, xúc tu bám đầu.

**Cú lật đổi nghĩa những gì đã đọc — liệt kê để viết lời kể bám vào:**

- **Mục tiêu thật chưa bao giờ là Hikari.** P07–P08 dựng lệnh "bắt đứa trẻ có vết sẹo ở mắt";
  nhưng lệnh đầy đủ ở P08-a là *"giết sạch những kẻ cản đường và cả lũ pháp sư nữa"*.
  Sau P20 mới rõ: món hàng là **Yojin**, đứa trẻ chỉ là mồi để kéo pháp sư ra.
- **"Kẻ giám sát" mà Yojin nhìn thấy từ xa (P06-d) là một suy luận đúng dẫn tới kết luận sai.**
  Anh nghĩ đó là kẻ đứng ngoài canh chừng con mồi. Thật ra nó đã **ở sẵn trong bệnh viện**,
  trong người bà mẹ.
- **"Ngất xỉu ở nơi làm việc, vẫn chưa tỉnh lại" (P09-c) không phải bệnh.** Đó là thời điểm bà
  bị chiếm.
- **Chính lời hứa cứu người biến thành đường dẫn.** P10-b "Tôi chắc chắn sẽ cứu được mẹ cậu" và
  P10-c "tôi nhất định phải 'nói chuyện' thật dài với nó" — oán hồn trông chờ đúng hai câu đó.
- **P14-d là câu gài thẳng vào mặt người đọc**: *"sức chiến đấu thấp, nhưng bù lại chúng có trí
  thông minh rất cao"*. Yojin tự nói ra nguyên lý sẽ hạ chính mình, ngay trước khi sập bẫy.
- **Cứu được mới là thua.** Đỡ được bà giữa không trung là điều kiện để oán hồn chạm vào Yojin.
  Nếu anh không cứu, bẫy không đóng. Hơi thở lạ ở P17-d là dấu báo đã bị sập, 2 trang trước khi
  nhân vật biết.
- **Câu bị cắt ngang ở P18-c** — *"Cậu hãy đưa mẹ... đến nơi an toàn đi—"* — sau P19 đọc lại
  thành ra: nơi an toàn đó không tồn tại, và anh đang tự tay trao vũ khí cho đối phương.
- **Tiêu đề chương "Dấu vết bóng tối"** khớp với bùa/phù chú dán trên cửa phòng Hikari (P04-d, e):
  nhà đã được dựng hàng rào, nhưng đòn đánh không đi vào nhà.

### D. Chưa rõ

**Không đoán bừa — những mục dưới đây KHÔNG được khẳng định trong video.**

| Mục | Hiện trạng trong ảnh | Ghi chú |
|---|---|---|
| **Tên chàng trai** | **CHƯA XUẤT HIỆN** trong toàn chương. Không ai gọi tên cậu | Gọi tạm "chàng trai", "cậu ta". **Không được đặt tên.** |
| **Tên mẹ cậu ta** | Không có trong thoại | — |
| **Biển phòng 316** | Chữ Nhật `316 吉野様` (đọc *Yoshino*) — **chưa được dịch trong bản tiếng Việt** | Rất có thể là họ của hai mẹ con (cậu ta nói mẹ ở "tầng ba", P13-b), **nhưng chưa xác nhận đó là phòng của bà**. Không dùng tên này trong lời kể. |
| **Tên bệnh viện** | Biển chữ Nhật `岩屋病院` (đọc *Iwaya*) | Bản dịch không đưa tên. Gọi là "bệnh viện". |
| **Thầy Shimizu** | Chỉ có họ. "Đã hồi phục hoàn toàn" (P04-c) — **chưa rõ thầy bị làm sao**, chương này không kể | Nếu là sự kiện chương trước thì phải tra C4 rồi mới nhắc. |
| **"Buổi tư vấn hôm nay"** (P01-c) | Hikari nói căng thẳng và "bị gián đoạn một chút" | Tư vấn với ai, gián đoạn vì chuyện gì — **chương này không cho biết**. |
| **Bùa dán trên cửa phòng Hikari** (P04-d, e) | Thấy rõ phù chú và khung cửa nứt | Không có lời giải thích. Không được gọi tên loại thuật. |
| **Con oán hồn ở P18/P20 có phải kẻ ra lệnh ở P07–P08 không** | Hình dạng khác nhau: P07-d là mặt người tái mắt trắng, P08 là xúc tu đen, P18-a là khối tóc nhiều mắt, P20 là mặt khổng lồ | Có thể cùng một thứ đổi dạng, có thể là hai. **Không kết luận.** |
| **Những thân người nhỏ lơ lửng quanh mặt oán hồn** (P20-a) | Thấy rõ 4–5 hình người trắng, mỗi hình gắn một khối tròn | Không có lời giải. |
| **Vòng dấu trong mắt Yojin** (P20-b) | Thấy rõ | Bible đã ghi "mắt Yojin đỏ ở C1-P01 là hiệu ứng hay trạng thái dùng thuật" là **chưa rõ** — mục này vẫn để mở, không nối hai chi tiết. |
| **Yojin có bị chiếm thật không** | Oán hồn tuyên bố "là của ta", nhưng chương dừng ngay đó | **Không được nói anh đã bị chiếm.** Chỉ kể đến đúng khung cuối. |
| **"Đại pháp sư"** | Từ mới, oán hồn gọi Yojin (P18-a, P20-a) | Bible mới có "pháp sư trừ tà". Cần chốt: giữ **đại pháp sư** làm cách oán hồn gọi, hay quy về "pháp sư trừ tà". |
| **"Kẻ bị ruồng bỏ"** (P13-d) | Yojin dùng để định nghĩa loài oán hồn | Từ mới, nên bổ sung vào bible §2 sau khi user duyệt. |
| **Từ "quái vật" vs "oán hồn"** | Chương 5 **chỉ dùng "quái vật"**, không dùng "oán hồn" lần nào | Bible §2 chốt dùng "oán hồn". Cần user xác nhận có giữ chuẩn đó cho C5 không. |

---

## DỪNG Ở ĐÂY — 3 câu hỏi duyệt

1. **Panel có thật không?** — 81 panel ở mục B có khớp với ảnh không, đặc biệt thứ tự đọc
   **phải → trái** ở P01 (trăng → phòng → cận Hikari → ra cửa → gặp Yojin) và ở P14 (3 khung
   thoại hàng trên)?
2. **Tên nhân vật đúng chưa?** — Chàng trai và mẹ cậu **chưa có tên trong truyện**; tôi để trống
   thay vì suy từ biển phòng `吉野`. Có duyệt cách gọi "chàng trai / cậu ta" không, hay muốn
   chờ chương sau mới dựng lời kể?
3. **Trọng số hợp lý chưa?** — Tôi để TS 3 khá dày ở P15–P20 (cả đoạn cứu người + cú lật).
   Có muốn hạ bớt đoạn rơi/đón (#64–#70) xuống 2 để dồn ngân sách 468 từ cho cú lật P19–P20 không?

**Chưa viết lời kể. Chưa sang `/manga-narration`.**
