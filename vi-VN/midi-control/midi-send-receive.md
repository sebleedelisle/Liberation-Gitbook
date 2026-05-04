---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-send-receive
---

# 🟩 MIDI Send/Receive

Hệ thống MIDI Send/Receive tách biệt với các điều khiển APC40, và là cách để đưa dữ liệu MIDI vào cũng như ra khỏi Liberation. Các chức năng như bắt đầu và dừng Clips, điều chỉnh thiết lập toàn cục, hiệu ứng và tham số của Clip đều có lệnh MIDI tương ứng.

{% hint style="info" %}
Hệ thống MIDI Send/Receive ban đầu được xây dựng trước khi Liberation có bất kỳ chức năng Timeline nào; đây là một giải pháp tạm thời để bạn có thể ghi và phát lại một show trong phần mềm âm nhạc như Logic Pro hoặc Cubase.

Hệ thống này cho phép bạn điều khiển trực tiếp Clips, hiệu ứng và thiết lập, không phụ thuộc vào màn hình hiển thị hay vị trí cuộn của Clip Deck. Các khả năng điều khiển live mang tính hệ thống hơn như tap tempo, gán zones, và arm/disarm chưa được triển khai.
{% endhint %}

### Thiết lập MIDI Send/Receive

Mở panel _MIDI Send/Receive_ (bằng menu _View -> MIDI Send/Receive_). Bạn sẽ thấy các tùy chọn _SEND, RECEIVE,_ hoặc _BOTH_ để gửi và nhận, cùng với khả năng chọn các giao diện MIDI muốn sử dụng.

{% hint style="danger" %}
Hãy thận trọng khi dùng thiết lập _BOTH_. Thiết bị và phần mềm MIDI có thể được cấu hình để gửi lại dữ liệu mà chúng nhận vào; điều này có thể tạo vòng lặp phản hồi dữ liệu MIDI, và đó là điều không tốt!
{% endhint %}

### Ánh xạ MIDI

Xem [Ánh xạ mặc định gửi/nhận MIDI](../reference/midi-send-receive-default-mapping.md "mention")

Tôi dự định bổ sung khả năng ánh xạ MIDI tùy chỉnh linh hoạt hơn trong tương lai, nhưng hiện tại bạn có thể dùng các ứng dụng như [BOME](https://www.bome.com/products/miditranslator) và [Chetaigne](http://benjamin.kuperberg.fr/chataigne/en) để chuyển đổi giữa Liberation và phần cứng tùy chỉnh của bạn.
