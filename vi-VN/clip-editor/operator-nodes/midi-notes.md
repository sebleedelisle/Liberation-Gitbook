---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/midi-notes
---

# 🟩 MIDI notes

## MIDI notes

Tạo các hiệu ứng kiểu “đàn hạc laser”, trong đó các nốt MIDI đầu vào kích hoạt tia hoặc hình dạng trên một dải giá trị. node sử dụng bất kỳ nội dung nào bạn đưa vào làm _nguồn_ cho từng nốt - đưa vào một điểm, bạn sẽ có một hàng các điểm. Đưa vào một hình như hình tròn, bạn sẽ có một hàng các hình tròn; các hình phức tạp hơn cũng sẽ được nhân bản theo cách tương tự.

Bạn có thể chọn MIDI interface mà Liberation lắng nghe trong **Liberation → Settings** (`Cmd / Ctrl + ,`)

* **midi channel** – kênh MIDI cần lắng nghe (0 = tất cả kênh, 1–16 = kênh cụ thể)
* **width** – tổng chiều rộng mà các nốt sẽ trải ra.
* **midi note min / max** – giá trị nốt MIDI thấp nhất và cao nhất trong dải.
* **ignore out of range notes** – lọc bỏ mọi nốt nằm ngoài dải đã đặt. Nếu tắt, các nốt ngoài dải sẽ được “kẹp” vào nốt khả dụng gần nhất (nốt cao kích hoạt phần trên của dải, nốt thấp kích hoạt phần dưới).
* **auto extend range** – tự động mở rộng dải nếu có nốt được chơi nằm ngoài dải hiện tại.

{% hint style="info" %}
Không chắc bạn đang nhận được dải nốt nào? Bật **auto extend range**, đặt **midi note min** thật cao và **midi note max** thật thấp, rồi chơi qua các nốt của bạn. Hệ thống sẽ bắt tất cả và tự mở rộng dải cho bạn. Khi đã có đủ, chỉ cần tắt **auto extend range** để khóa dải lại.
{% endhint %}

* **leave all notes visible** – tạo tia hoặc hình dạng cho tất cả nốt trong dải, dù chúng có đang được chơi hay không, tạo hiệu ứng “đàn hạc laser”.
* **hit colour** – màu xuất hiện khi một nốt được kích hoạt.
* **hit colour hold time** – thời gian màu hit giữ nguyên ở độ sáng tối đa trước khi mờ dần. Giá trị tính bằng giây (0–1). _100% = 1 giây._
* **hit colour decay time** – thời gian để màu hit mờ trở lại sau thời gian giữ. Giá trị tính bằng giây (0–1). _100% = 1 giây._

{% hint style="info" %}
Nếu nội dung của bạn đã là màu trắng thuần, đặt hit colour thành trắng sẽ không tạo khác biệt. Để có kết quả tốt nhất, hãy dùng màu bão hòa cho nội dung và đặt hit colour thành trắng - cách này tạo hiệu ứng lóe sáng rất đẹp khi nốt được kích hoạt.
{% endhint %}

* **note off fade out time** – thời gian để nốt mờ dần sau khi được nhả. Giá trị tính bằng giây (0–1). _100% = 1 giây._
* **hit scale factor** – mức độ nốt phóng to khi được kích hoạt (ví dụ: 2 = gấp đôi kích thước).
* **hit scale hold time** – thời gian nốt giữ kích thước phóng to trước khi thu nhỏ lại. Giá trị tính bằng giây (0–1). _100% = 1 giây._
* **hit scale decay time** – thời gian để nốt trở về kích thước ban đầu. Giá trị tính bằng giây (0–1). _100% = 1 giây._
* **note off shrink time** – thời gian để thu nhỏ về kích thước ban đầu sau khi nốt được nhả. Giá trị tính bằng giây (0–1). _100% = 1 giây._ (Không có tác dụng khi bật **leave all notes visible**.)

{% hint style="info" %}
Scaling - Lưu ý rằng nếu nội dung của bạn chỉ là một điểm đơn lẻ thì việc scale sẽ không có tác dụng!
{% endhint %}
