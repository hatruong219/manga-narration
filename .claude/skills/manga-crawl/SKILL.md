---
name: manga-crawl
description: Tải ảnh một chapter từ URL trang đọc truyện và bỏ banner quảng cáo của site. Bước đầu tiên của mọi chapter. Dùng khi user đưa link chapter, nói "crawl", "tải chapter", "lấy ảnh".
---

# Tải và làm sạch ảnh chapter

```bash
python3 scripts/crawl-chapter.py '<url chapter>' --bo <MÃ_BỘ>
python3 scripts/clean-pages.py truyen/<MÃ_BỘ>/prepare/C<n>/pages
```

`crawl-chapter.py` tự dựng scaffold cấp bộ (`series-bible.md`, `voice-profile.md`,
`tracker.csv`) nếu chưa có, tự suy mã bộ và số chapter từ URL, và tự nhận host CDN ảnh
(lấy host chiếm đa số trong `data-src`) nên chạy được với nhiều site cùng kiểu.

## Bắt buộc kiểm sau khi chạy

1. **Mở trang đầu và trang cuối bằng mắt.** `clean-pages.py` bỏ banner theo luật vị trí +
   độ bão hoà; chapter có panel màu ở đúng vùng đó sẽ bị cắt lố hoặc sót.
2. **Xem chiều rộng ảnh.** Script báo nếu dưới 1200px. Đọc được hay không tuỳ kiểu trang:
   webtoon cuộn dọc chữ to thì ~580px vẫn rõ; manga nhiều panel nhỏ thì không. Mở một ảnh
   xem chữ trong bong bóng có đọc được không trước khi làm cả chapter.
3. **Watermark của site tổng hợp** thường nằm mép trên và `clean-pages.py` không xử được
   (nó chồng lên tranh, không phải một dải riêng). Ghi nhớ để crop mép trên khi dựng.

## Khi site nạp ảnh bằng JS

`data-src` rỗng → script báo lỗi. Mở DevTools, xem request ảnh thật, rồi lấy URL mẫu.

## Xong thì
Dùng `pages-clean/`, **không dùng `pages/`**. Sang `/manga-beat-sheet`.
