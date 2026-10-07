# VOICE PROFILE — FRN

> Tích luỹ qua từng chapter. Đây là thứ giữ giọng đồng nhất qua 50 chapter.
> `/manga-qc` cập nhật sau mỗi vòng. **Bỏ bước này thì chapter sau mắc đúng lỗi cũ.**
> Đợt đầu (20–21/09/2026): 5 subagent mắt mới, mỗi con chỉ đọc đúng 1 chương, không
> biết bible/beat-sheet/chương khác. C1–C5 đã ĐĂNG NGUYÊN TRẠNG (điểm QC thấp, xem
> dưới) — không sửa lại 5 chương đó, áp dụng hết các luật này từ C6 trở đi.

## Kinh nghiệm QUY TRÌNH (rút ra sau 20 chương, chốt 07/10/2026)

Khác với các mục dưới (về VĂN PHONG), mục này ghi lại bài học về CÁCH LÀM để pipeline
chạy mượt hơn — đọc trước khi bắt đầu một chương mới.

- **Không dispatch Agent-tool hàng loạt/song song cho việc viết nội dung.** Từng thử
  11 subagent song song cho C20-C30, cả 11 đều chết giữa chừng vì chạm rate limit tuần
  của Claude API — tốn sạch một đợt mà không ra được gì. User chốt: làm TUẦN TỰ, từng
  chương một, trực tiếp trong hội thoại chính, không qua Agent tool cho bước nội dung/
  shots-cutting. (Agent tool vẫn dùng được cho việc khác như search/research không tốn
  quota API riêng, nhưng không dùng cho batch content work nữa.)
- **Cắt shots: luôn xác minh lại bằng file thật, đừng tin riêng contact-sheet thumbnail.**
  Nhiều lần thumbnail nhỏ trông sai (quá hẹp/lệch) nhưng file gốc kích thước thật lại
  đúng — và ngược lại, có lần ước lượng tọa độ sai be bét (C20 panel P08, lệch cả
  500px) mà chỉ phát hiện ra khi mở trực tiếp file `.jpg` đã cắt, không phải khi nhìn
  contact sheet. Quy trình chuẩn: đọc trang gốc → ước lượng tọa độ → chạy `build-shots.py
  --sheet` → soi contact sheet → **mở riêng từng shot khả nghi (mờ, lệch, quá hẹp) bằng
  Read trực tiếp** trước khi kết luận đúng/sai.
- **`shots.tsv` cột "trang" phải là mã trang trần (`P08`), không phải tên file đầy đủ**
  (`FRN_C20_P08.jpg`) — `build-shots.py` tự ghép tên file, đưa cả tên file vào sẽ vỡ
  `int()` parse. Lỗi này tốn một vòng sửa ở C20, kiểm tra ngay từ dòng đầu khi viết
  shots.tsv chương mới.
- **Vbee hết quota API → có lối thoát hợp lệ: tự tay dán text lên web Vbee (tài khoản
  trả phí của user, dùng point-pool lớn hơn sub-cap API).** Vbee web tự tách khối theo
  dòng trống — khớp đúng thứ tự `narration-plain.txt`/`tts-lines/Sxx.txt` nếu paste theo
  đúng thứ tự gốc. Xuất từng khối riêng (không gộp) thành zip, file trả về tên dạng
  `{số thứ tự}_{slug}_{uuid}.mp3.mp3` — đổi tên về `S{NN}.mp3` bằng
  `grep -oE '^[0-9]+'` lấy số đầu rồi copy vào `results/C<n>/audio/`, sau đó chạy tiếp
  pipeline bình thường từ `concat-audio.py`. Đã chạy thành công toàn bộ C20 bằng cách
  này — xem chi tiết lệnh ở `CHAY-VBEE.md`. Đây không phải "lách luật", là dùng tay đúng
  quota đã mua của chính user — không tự động hoá bước dán/export (vẫn cần user làm tay
  trên web), chỉ tự động hoá bước đổi tên/ghép sau khi có file.
- **Cấu trúc release giờ CHỐT**: mỗi bộ truyện một thư mục phẳng `release/<BỘ>/`, chứa
  toàn bộ `C<n>-video-final.mp4` + đúng MỘT file `note.md` liệt kê tiêu đề/mô tả/tag
  từng chương theo mẫu `N, <tiêu đề>\n<mô tả>\n<tag>`. `scripts/release.sh` đã tự động
  hoá việc này qua `scripts/extract-package-info.py` (luôn lấy Phương án 1 trong
  package.md) — không cần tự tay chép lại nữa, chỉ cần `package.md` viết đúng khuôn
  "## Phương án 1" ở đầu.

## Hook đã dùng — tránh lặp mô-típ

| Chapter | Hook thật đang dùng | Mô-típ | Điểm QC (Hook) |
|---|---|---|---|
| C1 | Xe ngựa về đô thành sau khi hạ Quỷ Vương | tổng kết bối cảnh sau chiến thắng | 2/5 |
| C2 | "20 năm đã trôi qua…" + caption bản đồ Strahl | thẻ thời gian + địa lý | 2/5 |
| C3 | Cảnh quán ăn mơ hồ ("cắn dở quả gì đó tròn") + "26 năm…" | thẻ thời gian, mòn | 2/5 |
| C4 | Con phố lát đá + bình bố cục trang + "27 năm…" | mô tả bố cục trang | 2/5 |
| C5 | Mô tả trang màu mở chương + "27 năm…" | mô tả bố cục trang, không có hook | 2/5 |
| C6 | Đêm giao thừa, Frieren thức trắng vì nụ cười của Fern | khoảnh khắc thân mật ban đêm | — |
| C7 | Lời hẹn kéo dài đúng một ngàn năm | lời hẹn/con số thời gian lớn | — |
| C8 | Hành trình này chưa tốn nổi 1% cuộc đời Frieren | tỉ lệ phần trăm cuộc đời | — |
| C9 | Frieren bắn hạ ảo ảnh Himmel không chút do dự | hành động quyết đoán trước ảo ảnh | — |
| C10 | Gã thỏ đế bí mật bổ rìu suốt ba năm dưới vách đá | bí mật luyện tập, lật bằng hình ảnh | — |
| C12 | Một ly kem bị thu nhỏ, Stark nhận ra mình đã lớn | vật nhỏ làm gương soi thời gian | — |
| C13 | Ông lão khen tượng "giống hệt Frieren-sama" ngay trước mặt cô | nghịch lý kịch tính, người trong cuộc không biết | — |
| C14 | "Mẹ ơi" lúc hấp hối — một lời nói dối để sinh tồn | tiếng gọi sinh tồn bị vạch trần | — |
| C11 | Thì ra sư phụ cũng từng sợ — cú đánh ngày xưa không phải thất vọng | nỗi sợ được thừa kế, không phải thất vọng | — |
| C15 | Đao phủ tới lấy mạng cô gái bị giam — và mất mạng trước | thợ săn hoá con mồi | — |
| C16 | Lính gác mất đầu, kẻ bị giam lại ung dung bước ra ngoài | bí ẩn treo mở + thái độ lệch pha hiện trường | — |
| C17 | Bị treo ngược, đánh gục — hoá ra lại là kế hoạch | thất bại giả làm mồi nhử | — |
| C18 | Lần đầu lộ diện — "Máy chém Aura" đối mặt Frieren | kẻ phản diện chờ đợi bấy lâu xuất hiện | — |
| C19 | Một câu nói đứng riêng — "Là Aura-sama" | lời nói bí ẩn không rõ chủ đích | — |
| C20 | "Ngươi đã đào tạo những gì cho con bé này vậy?" | đối thủ phải tự hỏi về người thầy vắng mặt | — |

**LUẬT MỚI — bắt buộc từ C6:**
- **Cấm mở chương bằng "X năm đã trôi qua kể từ lúc Himmel qua đời."** 4/5 chương C1–C5
  dính câu này trong 3 dòng đầu. Mốc thời gian vẫn cần (bible §4a) nhưng đẩy xuống sau
  khi đã có ít nhất một hình ảnh/tình huống cụ thể, không đặt làm dòng 1–2.
- **Cấm mở bằng mô tả bố cục trang / mô tả cảnh mơ hồ không rõ đang tả gì** ("cắn dở quả
  gì đó tròn", "bụi trắng rơi chậm", "Bố cục ấy đã nói trước cả chương"). Hook phải mở
  bằng MỘT tình huống hoặc MỘT câu thoại cụ thể, có sức nặng ngay từ dòng đầu.
- Vật liệu hook tốt thường đã có sẵn trong beat sheet nhưng bị chôn giữa/cuối chương —
  QC C3 chỉ ra pho tượng phủ rêu (đỉnh chương) đáng lẽ là mở đầu, không phải dòng 25.
  QC C5 chỉ ra con số "40%/70% pháp sư bị giết" nên lên đầu thay vì chôn ở dòng 57.
  **Đọc hết mục C (điểm cao trào) của beat sheet TRƯỚC khi viết 3 dòng mở**, chọn hook
  từ đó thay vì từ dòng đầu của trang P03.

## Viết TIÊU ĐỀ video (khác luật viết lời kể — đọc kỹ trước khi đóng gói)

Tiêu đề đứng một mình trên YouTube, người xem chưa hề có ngữ cảnh nào — khác hẳn
lời kể, nơi người xem đã theo dõi từ đầu video. Ba lỗi đã mắc và sửa ở 5 tiêu đề
đầu, tránh lặp lại:

- **Không dùng đại từ ("cô", "ông", "anh") làm chủ ngữ tiêu đề.** Lời kể dùng "cô"
  cho Frieren vì người xem đã biết từ phút đầu; người lướt qua tiêu đề trên feed
  thì không. Luôn gọi thẳng tên nhân vật trong tiêu đề, kể cả khi tên đó đã lặp ở
  phần "| Frieren Chap N" phía sau — lặp tên vì mục đích rõ nghĩa không phải lỗi.
- **Không dùng đại từ mơ hồ để ép tò mò** ("thứ này", "một người", "điều này",
  hay bọc câu hỏi trong ngoặc kép kiểu rao giảng). Nói thẳng danh từ cụ thể có
  thật trong chương — quan tài, phong ấn, loài hoa, tên nhân vật.
- **Không dùng cấu trúc "làm X để Y"** (giải thích nguyên nhân–mục đích quá gọn,
  quá logic, đọc lên nghe như văn quảng cáo AI viết). Thay bằng hai mệnh đề tách
  rời bằng dấu phẩy, hoặc chỉ nêu tình huống rồi dừng, để người xem tự tò mò vì
  sao — không giải thích hộ.
- **Khuôn tiêu đề CHỐT (28/09/2026, theo yêu cầu user)**: `Pháp Sư Tiễn Táng
  Frieren Chap <N>: <hook>` — tên bộ đứng TRƯỚC "Chap N:", hook đi SAU dấu hai
  chấm. Không còn dùng khuôn cũ "<hook> | Frieren Chap N". Ví dụ mẫu user cho:
  "Pháp Sư Tiễn Táng Frieren Chap 3: Loài Hoa Không Còn Tồn Tại, Nhưng Frieren
  Vẫn Đi Tìm". Áp dụng cho MỌI package.md từ giờ trở đi, kể cả khi viết lại tiêu
  đề các chương đã release trước đó.

## Kỹ thuật VERBALIZED SAMPLING cho các đỉnh cảm xúc (chốt 29/09/2026)

Chốt sau phản hồi gay gắt của user: *"khoan task này không phải là bảo kể lại rồi
né các từ cấm là xong, mà nó là telling cơ mà, phải thu hút người xem chứ."* Gốc
bệnh không phải là dùng nhầm từ bị cấm — mà là **mode collapse**: khi viết một
lần duy nhất cho một câu quan trọng, người viết (kể cả AI) luôn rơi vào phiên bản
"phổ biến nhất/an toàn nhất" — chính là bản kể lể, hiền lành mà rubric đang chê là
telling. (Nguồn: paper "Verbalized Sampling: How to Mitigate Mode Collapse and
Unlock LLM Diversity", Stanford 10/2026, arxiv.org/abs/2510.01171 — tăng đa dạng
sáng tác 1.6-2.1x khi bắt buộc sinh nhiều phương án thay vì chấp nhận bản đầu.)

**Áp dụng bắt buộc cho MỖI đỉnh cảm xúc đã đánh dấu trong mục C beat sheet (và
câu hook mở đầu)**, KHÔNG áp dụng tràn lan cho toàn bộ 100+ dòng (tốn token vô
ích — chỉ áp dụng ở đúng chỗ có trọng số cao nhất):
1. Viết ra 3-4 phương án khác hẳn nhau về góc tiếp cận cho cùng một khoảnh khắc
   (vd: góc âm thanh/im lặng — góc nhịp tim/thể chất — góc thời gian chững lại —
   góc đối lập quy mô). Không phải đổi từ đồng nghĩa, mà đổi hẳn GÓC NHÌN.
2. Chọn hoặc ghép bản mạnh nhất — ưu tiên bản neo cảm xúc vào một chi tiết vật
   lý/giác quan cụ thể, KHÔNG chọn bản nào chỉ đổi cách gọi tên cảm xúc.
3. Không dừng lại ở lần sinh đầu tiên dù nó "nghe ổn" — bản đầu tiên gần như luôn
   là bản mode-collapsed, đúng bản mà rubric strict sẽ chê.

## LUẬT QUAN TRỌNG NHẤT — mạch văn phải LIỀN, không phải liệt kê từng khung

Chốt 26/09/2026, phản hồi trực tiếp của user sau khi đọc C6: *"nội dung đang chưa
hay lắm, có vẻ đang đọc từng khung hình chứ không liền mạch về 1 câu chuyện."* Đây
là lỗi NẶNG NHẤT, ưu tiên sửa trước mọi lỗi câu chữ khác.

**Gốc bệnh:** mỗi dòng narration.tsv ứng với một đoạn ảnh, nên người viết có xu
hướng coi mỗi dòng là MỘT SỰ KIỆN ĐỘC LẬP — kể xong thì dừng, dòng sau kể sự kiện
tiếp theo mà không nối gì với dòng trước. Đọc liền một mạch 5-10 dòng thì nghe như
một danh sách "việc này xảy ra. việc kia xảy ra." chứ không phải một câu chuyện.

**Ví dụ lỗi thật, ba dòng liền của C6 (đã viết, đang sửa):**
> "Ông lão giao việc dẫn hai người men theo bờ, giải thích đây từng là lối đi của
> du thuyền, nên rác trôi vào rất nhiều."
> "Frieren hỏi lại. Dân làng trước có dọn bờ biển này, giờ bỏ vì thiếu người, đúng
> chứ."
> "Ông lão nhìn ra khơi. "Trước đây nơi này đã từng là một vùng biển trong vắt
> đấy." Fern đứng lặng giữa đống gỗ dạt, không nói gì."

Ba câu này có quan hệ nhân-quả thật (ông kể → Frieren vặn lại → ông né câu hỏi
bằng một câu tiếc nuối) nhưng bị tách rời hoàn toàn, đọc như ba tin nhắn không
liên quan.

**Sửa thành mạch liền** (gộp còn hai dòng, có nối):
> "Ông lão giao việc dẫn hai người men theo bờ biển ngổn ngang rác dạt, kể rằng
> nơi này từng là lối tàu bè qua lại — Frieren hỏi thẳng liệu dân làng bỏ mặc
> nơi này chỉ vì thiếu nhân lực, đúng không."
> "Ông chỉ đáp bằng một câu tiếc nuối, mắt nhìn ra khơi: "Trước đây nơi này đã
> từng là một vùng biển trong vắt đấy." Fern đứng lặng giữa đống gỗ mục, không nói
> gì thêm."

**Cách làm cụ thể, áp dụng cho MỌI chương từ giờ:**

1. **Đừng viết từ beat sheet theo kiểu 1 dòng beat sheet → 1 dòng narration.** Đọc
   một CỤM 3-6 panel liên quan (cùng một cảnh/hội thoại) rồi mới viết — quyết định
   cụm đó cần mấy dòng narration dựa trên nhịp thật cần cho video, không phải theo
   số panel có sẵn.
2. **Câu trước phải tạo ra lý do cho câu sau xuất hiện.** Tự hỏi trước khi viết mỗi
   dòng: "vì sao điều này xảy ra NGAY SAU điều vừa kể?" Nếu không trả lời được,
   thường là thiếu một mệnh đề nối.
3. **Dùng liên từ phụ thuộc thật** (khi, vì, dù, sau khi, trong lúc, dù cho, mệnh
   đề quan hệ) để một câu ôm được 2 sự kiện có quan hệ nhân quả — KHÔNG phải liên
   từ mở đầu câu kiểu tic ("Rồi", "Và") mà linter đã cấm. Khác nhau: liên từ tic là
   ghép hai câu ĐỘC LẬP bằng một từ thừa ở đầu; liên từ phụ thuộc là làm cho MỘT
   câu chứa cả nguyên nhân lẫn kết quả.
4. **Không phải 1 panel = 1 dòng.** Panel chuyển tiếp/đồng nhất một hành động thì
   gộp vào cùng dòng với panel trước hoặc sau. Ngược lại, một panel nặng có thể
   cần 2 dòng để đủ chỗ thở — nhưng cả 2 dòng đó vẫn phải nối liền ý, không phải
   tách đôi một câu đơn thành hai câu cụt.
5. **Đọc thử 5 dòng liền một lượt sau khi viết xong mỗi cụm cảnh** — nếu nghe như
   danh sách sự kiện rời thì viết lại ngay, đừng đợi tới bước tự kiểm cuối.

## Giới hạn độ dài dòng khi làm liền mạch — HAI CONSTRAINT PHẢI THOẢ CÙNG LÚC

Chốt 26/09/2026, phát hiện khi sửa C6: viết liền mạch (mục trên) rất dễ overcorrect
thành GỘP QUÁ TAY — một dòng ôm 3 sự việc hình ảnh khác nhau bằng câu dài đẹp, nhưng
mỗi dòng narration.tsv = MỘT SHOT = MỘT KHUNG ẢNH TĨNH. Dòng 60-84 từ ở tốc độ 4,15
từ/giây là 14-20 giây một ảnh đứng yên — nghe mượt nhưng nhìn rất chán.

**Giới hạn cứng: tối đa ~50 từ/dòng (~12 giây), lý tưởng 15-30 từ/dòng (~4-7 giây).**
Nếu một dòng đang gộp nhiều hơn 2 sự việc hình ảnh khác nhau (2 hành động/biểu cảm/
khung cảnh riêng biệt) → BẮT BUỘC tách thành 2 dòng.

**Tách nhưng KHÔNG được quay lại kiểu liệt kê rời.** Tách bằng cách: dòng sau tiếp
nối ý dòng trước bằng liên từ phụ thuộc hoặc đại từ quy chiếu ngược ("Nghe vậy…",
"Chưa kịp đáp thì…", "Đúng lúc đó…") — không phải cắt đôi câu dài thành hai câu SVO
độc lập không còn liên quan gì nhau.

Ví dụ SAI (quá dài, 1 dòng ôm 3 việc):
> "Frieren chìa ra một cuốn sách cũ, hỏi liệu vậy đã đủ tính làm thù lao chưa vậy ạ,
> rồi lật sách xoèn xoẹt, reo lên vì thấy tên Flamme trên bìa, trong khi Fern chỉ
> gọi đúng một tiếng như đã đoán trước chuyện gì sắp xảy ra."  (60 từ, ~14s)

Sửa đúng (2 dòng, vẫn nối, mỗi dòng một hình):
> "Frieren chìa ra một cuốn sách cũ, hỏi liệu vậy đã đủ tính làm thù lao chưa."
> "Cô lật sách xoèn xoẹt rồi reo lên vì thấy tên Flamme trên bìa — Fern chỉ đáp lại
> đúng một tiếng, như đã đoán trước chuyện gì sắp xảy ra."

Trước khi báo cáo xong một chương: chạy nhanh script đếm từ/dòng, dòng nào >50 từ
phải tách lại theo đúng nguyên tắc trên.

## Tra cứu ngoài (Google) — CHỈ để xác nhận, KHÔNG để lấy nội dung chưa vẽ

Chốt 26/09/2026, theo yêu cầu user: khi beat sheet/lời kể gặp một tên riêng hoặc
chi tiết chưa rõ, được phép tra Google để hiểu rõ hơn — nhưng có ranh giới cứng:

- **ĐƯỢC:** tra để xác nhận danh tính/bối cảnh của thứ **ĐÃ xuất hiện trên trang đang
  đọc** — ví dụ: tên "Aura" ở C15 có đúng là một trong "bảy ma thuật sư huỷ diệt" mà
  bible từng nhắc không, cách phiên âm chuẩn một địa danh, nghĩa gốc một thuật ngữ.
  Việc tra chỉ để KHỚP NỐI dữ kiện đã có trong bible với dữ kiện mới trên trang, không
  phải để biết thêm.
- **CẤM:** tra để biết chuyện gì xảy ra ở **chương sau** chưa đọc tới, tra tiểu sử/kết
  cục nhân vật vượt quá những gì trang hiện tại đã vẽ. Bộ này là kênh kể theo đúng
  mạch, tiết lộ trước là hỏng cả cấu trúc "chưa tiết lộ" mà bible đang giữ.
- Bất cứ gì tra được mà **trang hiện tại chưa tự xác nhận** thì vẫn ghi ở mục D "Chưa
  rõ" kèm chú "gợi ý từ tra cứu ngoài, chưa được trang xác nhận" — KHÔNG được nâng
  thẳng lên thành sự thật trong bảng B hay đưa vào lời kể như dữ kiện chắc chắn.

## Mô tả hình ảnh mơ hồ — khác với suy diễn cốt truyện, đừng lẫn hai thứ

Chốt 26/09/2026, theo phản hồi user: "quả gì đó tròn" (C3) đọc lên nghe như người
kể **không nhìn ra ảnh**, giảm uy tín kênh — dù đúng luật "không suy diễn" theo nghĩa
đen. Cần tách hai loại mơ hồ, xử lý khác nhau:

- **Chi tiết hình ảnh không ảnh hưởng cốt truyện** (một loại quả, màu áo, hình dạng
  một vật nhỏ trong tay) → **cứ chọn một từ cụ thể hợp lý** ("táo", "quả cam") dù
  không chắc 100%. Sai một quả táo thành quả cam không làm hỏng nội dung, nhưng nói
  "quả gì đó tròn" thì hỏng cả câu — nghe như không đọc được tranh.
- **Sự kiện/quan hệ/động cơ ảnh hưởng cốt truyện** (ai nói câu đó, hai người có quan
  hệ gì, vì sao nhân vật làm vậy) → GIỮ NGUYÊN luật cũ: không suy diễn, không đoán,
  kể trung tính hoặc bỏ trống chủ ngữ nếu ảnh không xác nhận được.
- Quy tắc phân biệt nhanh: tự hỏi "đoán sai chỗ này có làm người xem hiểu sai truyện
  không?" — không thì cứ chọn một từ cụ thể; có thì phải trung tính/bỏ trống.

## Sửa mâu thuẫn: "không thoại"/"khoảng lặng" — chỉ được MÔ TẢ, cấm GỌI TÊN

Một số QC trước khen "Một khung lớn, không thoại. Mặt ông nghiêng đi, cười." là hay,
nhưng nửa đầu câu đó ("không thoại") lại đúng loại ngôn ngữ storyboard đã bị cấm ở
mục dưới. Chốt lại cho hết mâu thuẫn:

- **Muốn tạo khoảng lặng: chỉ mô tả HÀNH ĐỘNG/BIỂU CẢM, KHÔNG được nói "không thoại",
  "không một lời", "không lời thoại nào" dưới bất kỳ hình thức nào.** Viết "Mặt ông
  nghiêng đi, cười." là đủ — im lặng đã nằm sẵn trong việc không có câu thoại nào
  được trích, không cần tuyên bố nó ra.
- Đúng: "Cô mỉm cười, và không hỏi thêm gì nữa." (đây là kể một HÀNH ĐỘNG — "không
  hỏi thêm" — không phải tuyên bố về khung tranh).
  Sai: "Một khung lớn, không thoại." (đây là mô tả cái KHUNG TRANH, thuộc nhóm bị cấm).

## Cách diễn đạt ĐÃ ĂN (giữ lại, tái dùng)

- **Mở chương bằng flash-forward + lặp nguyên văn**: trích thẳng câu neo của cả
  chương (lấy từ mục C beat sheet) làm 3 dòng mở, để chương tự trả lời/lặp lại câu đó
  ở cao trào — làm tốt ở C6 ("Bởi vì cậu là một người như thế mà." — mở đầu, rồi lặp
  lại đúng lúc hồi tưởng, rồi giải ở cú lật cuối). Mạnh hơn hẳn kiểu mở tả cảnh.
## Cách diễn đạt ĐÃ ĂN (giữ lại, tái dùng)

- **Lặp nguyên văn một câu ở ngữ cảnh mới, không bình luận thêm** — kỹ thuật chính của
  cả bộ, làm tốt nhất ở: "Có lẽ thế." (C1, lúc trẻ ↔ bên quan tài) · "Đồ tư tế thúi." /
  "HAHAHA." (C1, đêm hội ↔ lần cuối tiễn Heiter) · "…Thế à." (C1) · cặp "Cậu đâu phải là
  Himmel." ↔ "Nếu là Anh hùng Himmel, thì cậu ấy cũng sẽ làm vậy thôi." (C2).
- **Đếm chữ thay vì tả cảm xúc**: "Frieren buông đúng ba tiếng." / "Ông chỉ đáp hai
  tiếng." — đúng giọng lạnh của bộ. **NHƯNG bắt buộc đếm lại bằng mắt trước khi khoá
  file**: C1 dòng 5/72 và C2 dòng 34 đều nói sai số so với câu trích thật (ví dụ nói
  "hai tiếng" nhưng câu trích có ba). Xem mục "Đã bị QC gạch".
- **Chốt đoạn bằng một hành động nhỏ, không phải bằng cảm xúc gọi tên**: "Cô mỉm cười,
  và không hỏi thêm gì nữa." (C4) · "Frieren nhìn cô bé, không đáp ngay." (C5).
- **Để người ngoài phán thay vì người kể phán**: "Đúng thật là vô cảm." (lời đám đông ở
  C1, không phải nhận xét của người kể) — dùng lại mỗi khi cần một phán xét về nhân vật
  chính, đừng để người kể tự phán.
- **Đối chiếu mốc thời gian trần trụi**: "Lời hẹn 50 năm, giữ trọn." (C1) — mẫu câu nên
  lặp lại về cấu trúc cho các lời hứa dài hạn khác của bộ.
- **"Cận mặt [tên]. [một hành động, không tính từ]."** — công thức tốt để tạo khoảng
  lặng (C1 dòng 75, C4 dòng 86 "Chiếc trâm đã nằm trên tóc"). **Nhưng chỉ 1–2 lần mỗi
  chương** — 5 chương đầu lạm dụng thành ~50 lần cộng dồn, xem mục dưới.
- **Con số đi kèm rất lạnh, không tô màu**: "Con số đi kèm rất lạnh." / "Hắn không
  hoảng." (C5) — nói sự thật rồi dừng, không thêm tính từ.

## Chấm "bịa trích dẫn" — BẮT BUỘC đối chiếu ảnh trang thật, không chỉ tin beat-sheet.md

Chốt 07/10/2026, sự cố thật ở C21: hai vòng chấm liên tiếp (vòng 5, vòng xác minh) kết
luận 3 dòng narration là "bịa trích dẫn hoàn toàn, không có trong beat-sheet" — tôi tin
theo, XOÁ MẤT 3 dòng đó. Khi tự tay mở lại ảnh trang gốc (`pages-clean/FRN_C21_P15.jpg`)
để cắt shots, phát hiện cả 3 câu trích đó **có thật 100%, đúng nguyên văn** trên trang —
beat-sheet.md chỉ đơn giản là ĐÃ KHÔNG GHI những beat đó (beat sheet luôn là bản tóm tắt
rút gọn, không phải bản chép đủ mọi khung/mọi câu thoại) và lệch số trang P so với file
ảnh thật (beat sheet ghi "P15-a/b" cho nội dung thực ra nằm ở file `P16.jpg`).

**Gốc bệnh:** giám khảo (và cả tôi) coi `beat-sheet.md` là nguồn sự thật DUY NHẤT và
ĐẦY ĐỦ, trong khi nó chỉ là bản tóm tắt — "không tìm thấy trong beat-sheet" KHÔNG đồng
nghĩa với "bịa". Nguồn sự thật thật sự là ẢNH TRANG GỐC.

**Luật mới bắt buộc:** trước khi kết luận một câu trích/sự kiện là "bịa thêm, vượt quá
beat sheet" (mục A3/D1 của `manga-litscore`) và xoá nó đi, BẮT BUỘC mở trực tiếp file
ảnh trang tương ứng (`pages-clean/`) ra xem bằng mắt để xác nhận — không được kết luận
chỉ bằng cách grep/đối chiếu với beat-sheet.md. Nếu không có quyền truy cập ảnh (vd.
subagent chấm điểm không được giao công cụ đọc ảnh), phải hạ mức độ chắc chắn của phán
quyết đó xuống "nghi ngờ, cần người có ảnh xác minh lại" thay vì chấm thẳng điểm 0 và
yêu cầu xoá. Áp dụng từ C21 trở đi, và áp dụng ngay khi kiểm tra điểm "bịa trích dẫn" ở
mọi chương cũ nếu nghi ngờ tương tự.

## Phạm vi áp dụng bảng "Đã bị QC gạch" — chỉ tính lời NGƯỜI KỂ, không tính lời THOẠI trích dẫn

Chốt 07/10/2026, sau khi hai lượt chấm C21 không đồng nhất về việc có trừ điểm cụm cấm
nằm TRONG dấu ngoặc kép hay không (lượt 1 không trừ, lượt 2 trừ dù cùng một câu thoại
trích nguyên văn khớp beat sheet). Quy tắc chốt: **bảng cụm cấm dưới đây chỉ áp dụng cho
câu văn NGƯỜI KỂ (phần ngoài dấu ngoặc kép)** — đây là nơi phản ánh thói quen/tic của
người viết lời kể. Lời THOẠI nhân vật trích nguyên văn từ beat sheet (trong ngoặc kép)
GIỮ NGUYÊN bản dịch gốc dù trúng cụm cấm, không được sửa để né linter — sửa lời thoại
trích dẫn để né cụm cấm chính là VI PHẠM luật "không bịa trích dẫn" (mục A/D của
`manga-litscore`). Áp dụng luôn khi chấm điểm các chương từ C21 trở đi.

## Đã bị QC gạch (đừng dùng lại)

| Cụm / lỗi | Lý do | Chapter |
|---|---|---|
| "Cận mặt", "Khung rộng", "Khung lớn", "Toàn cảnh", "Hồi tưởng mở ra/trải ra" dùng làm CHỦ NGỮ MỞ ĐẦU câu | Ngôn ngữ storyboard — người xem xem video, không lật trang. Đếm được 92 dòng/5 chương, tăng dần C1(5)→C3(36). Giới hạn: tối đa 1–2 lần MỖI CHƯƠNG, không dùng làm từ mở câu | C1–C5 |
| "trang giấy không chỉ rõ ai nói câu nào", "chương này không nói" (dùng >1 lần/chương), "bóng thoại", "không một lời thoại trong khung" | Người kể tự thú trước khán giả là mình không đọc được tranh. Không ai xem truyện muốn nghe điều đó. Chỗ không rõ ai nói: kể trống chủ ngữ và im lặng, đừng giải thích lý do | C1, C3, C4, C5 |
| "Và phần cay nhất nằm ở vế sau.", "hạ xuống câu chốt của cả chương", "Logic của cô rất gọn:", "Hai câu ở đầu trận, nghe lại một lần nữa." | Người kể tự khen/báo trước câu sắp tới sẽ hay → phá cú đấm khi nó tới thật. Vi phạm luật "kể lạnh, để người xem tự thấy đau" | C3, C4, C5 |
| Đếm chữ ("đúng hai/ba tiếng") không khớp số âm tiết thật của câu trích | Lỗi máy đếm được — BẮT BUỘC kiểm bằng script trước khi khoá file, không chỉ đọc bằng mắt | C1 (2 chỗ), C2 (1 chỗ) |
| Gán câu thoại cho sai người đứng cạnh (vd tả hành động của A rồi đưa lời thoại của B vào ngay sau, không đổi chủ ngữ) | Nghe lên gây loạn nhân vật ngay lập tức | C4 dòng 67 |
| Hai đại từ sắc thái giống nhau ("hắn") trỏ hai nhân vật khác nhau trong 2 dòng liền kề | Người nghe (không có hình cố định) không có cách phân biệt. "hắn" chỉ mở cho MỘT phản diện/chương, ghi rõ trong bible ai được dùng | C5 dòng 73–76 |
| Dấu gạch cắt lời giữa chừng ("ng-…", "đ-…") để nguyên trong câu trích | TTS đọc sẽ đánh vần chữ cái hoặc nuốt âm. Viết lại thành câu trọn, dùng mẫu "Câu ấy không kịp hết." để diễn tả bị ngắt lời | C3 (4 chỗ) |
| Lỗi ngữ pháp/chính tả thật lọt qua (thiếu chữ "chưa", dùng sai "ngạt ngào", cụm không phải tiếng Việt) | Nghe ra ngay, không cần biết truyện gốc | C3 (4 chỗ) |
| Từ khoá lặp dày trong một chương: "mà thôi" (9 lần/C3), "hẳn là" (6 lần/C2), "quả thật/quả là" (5 lần/C1), "mổ xẻ" (3 lần/C5), "rút ra kết luận" (2 lần/C5) | Tai nghe ra sự lặp dù linter không bắt (dưới ngưỡng tic) — tự kiểm bằng grep trước khi khoá file, không chỉ tin linter | rải rác |
| Thành ngữ/sáo lệch tông lạnh: "dội một gáo nước lạnh", "bão đạn", "gieo rắc tàn bạo", "cùng hội cùng thuyền", "phủi đi hết" | Lên gân hoặc sáo, lệch giọng trầm-lạnh của bible §3 | C1, C2, C5 |
| Suy diễn nội tâm đóng khung như sự thật: "chưa bao giờ...", "thật lòng", "chính là", "thật ra là một câu hỏi dành cho chính mình" | Bịa quan hệ nhân quả/tâm lý không có căn cứ trong ảnh — đúng loại lỗi mà bible cấm suy diễn | rải rác cả 5 chương |
| **"Tên chương hiện lên: ..."/"Trang màu tên chương hiện lên: ..."/"Ngay khi đó, trang màu tên chương hiện lên..."** — bất kỳ câu nào tường thuật việc TRANG TIÊU ĐỀ/SPLASH PAGE xuất hiện, thay vì kể nội dung câu chuyện | Ngôn ngữ giới thiệu trang/sản phẩm, không phải kể chuyện — user chốt 28/09/2026: "đã bảo review truyện chứ có phải giới thiệu trang nào, trang đó có gì đâu". LỌT QUA CẢ 5 CHƯƠNG ĐẦU (C6-C10) vì không ai liệt kê nó vào danh sách cấm trước đó — đây chính là bài học: mọi câu tường thuật về TRANG/KHUNG/BẢNG TÊN thay vì SỰ KIỆN đều phải bị cấm, không chỉ những cụm đã từng bắt được. Khi viết panel loại "trang tên chương" (thường là P02/P03 đầu chương, chỉ có chữ tên chương + 1 hình nền): nếu panel đó có nội dung hình ảnh thật (nhân vật, bối cảnh) thì chỉ kể đúng nội dung hình ảnh đó, bỏ hẳn vế "tên chương hiện lên"; nếu panel đó KHÔNG có nội dung nào ngoài chữ tên chương thì bỏ hẳn dòng đó khỏi narration.tsv, không cần thay thế. Đã sửa quy tắc, KHÔNG re-làm 5 chương cũ (tốn token Claude + Vbee vô ích) — chỉ áp dụng cho chương mới từ C11 trở đi | C6, C7, C8, C9, C10 (toàn bộ 5 chương đã release) |

## Nhịp đang chạy (đo thật từ audio Vbee, 5 chương đầu)

- đoạn / phút: **~11,8** (dao động 9,8–13,0 — C1 chậm nhất do đoạn dài hơn)
- từ / đoạn: **~19** (dao động 17–23)
- giây / đoạn: **~5,1** (dao động 4,6–6,1)
- Giọng Vbee `hn_female_ngochuyen_full_48k-fhg` @ `VBEE_SPEED=1.0` đọc thật **4,15
  từ/giây** — nhanh hơn dự toán README 3,5 khoảng 19%. Dùng 4,15 cho `--wps`, đo lại
  nếu đổi giọng/tốc độ.
- Độ dài chương theo số panel thật, không ép ngân sách: C1 166 panel→10:20 · C2 163
  panel→11:35 · C3 185 panel→14:36 (dài nhất, QC chê dư 15–20%, nên CÓ ngân sách mềm
  ~13–14 phút cho chương dày, cắt bớt montage/đoạn nối thay vì giữ hết) · C4 99
  panel→8:48 · C5 118 panel→10:10.

## Điểm QC 5 chương đầu (Hook / Nhịp / Giọng / Mạch / Đọc-lên, thang 5)

| | Hook | Nhịp | Giọng | Mạch | Đọc lên | Tổng/25 |
|---|---|---|---|---|---|---|
| C1 | 2 | 3 | 3 | 3 | 3 | 14 |
| C2 | 2 | 3 | 3 | 2 | 3 | 13 |
| C3 | 2 | 2 | 2 | 3 | 2 | 11 |
| C4 | 2 | 2 | 3 | 2 | 3 | 12 |
| C5 | 2 | 3 | 3 | 2 | 2 | 12 |

**Yếu nhất toàn cục: Hook (2/5 cả 5 chương) và ngôn ngữ storyboard trong Giọng kể.**
Ưu tiên sửa hai điểm này trước khi lo các mục còn lại.
