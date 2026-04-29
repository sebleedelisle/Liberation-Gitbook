---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/latency-setting
---

# ✅ Cài đặt độ trễ

Trong panel _Settings_ (_Liberation->Settings_ hoặc CMD/CTRL ,), bạn sẽ thấy một thanh trượt có nhãn _Latency(ms)._ (Trong các phiên bản Liberation cũ hơn, mục này nằm trong panel Laser Overview)

{% hint style="info" %}
Thiết lập độ trễ mặc định 150ms phù hợp với hầu hết trường hợp, nhưng nếu bạn gặp sự cố mạng, bạn có thể thử tăng giá trị này.
{% endhint %}

### Giải thích chi tiết hơn

Thiết lập "độ trễ khung hình" này là khoảng thời gian tối đa từ khi Liberation tạo một khung hình đến khi laser bắt đầu phát khung hình đó. Nếu tăng giá trị này, bạn có thể nhận thấy một độ trễ nhỏ giữa Liberation và đầu ra laser.

Lợi ích của độ trễ khung hình dài hơn là Liberation có thể nạp nội dung vào bộ đệm của laser controller sớm nhất có thể; nếu mạng bị nghẽn, controller sẽ ít có khả năng bị hết điểm hơn.

Thiết lập này thường chỉ áp dụng cho DAC mạng, và giá trị 100ms thường là mức cân bằng tốt giữa tốc độ và khả năng chống chịu với độ trễ mạng. Nếu bạn có mạng thật sự ổn định, bạn có thể giảm xuống 50ms.&#x20;
