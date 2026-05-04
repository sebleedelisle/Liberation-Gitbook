---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/live-control-with-the-apc40
---

# 🟩 Bộ điều khiển MIDI live

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

### **APC40 controller**

Đây là controller phần cứng mặc định cho Liberation; rất nên dùng thiết bị này, và có thể nói Liberation đã được thiết kế xoay quanh phần cứng này ngay từ đầu. Ngay khi bạn cắm APC40, Liberation sẽ tự động kết nối với thiết bị.

{% hint style="warning" %}
_Ôi không! Đầu cắm USB của tôi bị tuột giữa chừng trong buổi diễn!_

Đừng hoảng — chỉ cần cắm lại, Liberation sẽ tự động kết nối lại, không có gì phức tạp.
{% endhint %}

### APC40 Mark 1 hay Mark 2?

Nói ngắn gọn, nên dùng Mark 2 vì thiết bị có các nút đủ màu, khớp hơn với giao diện Clip Deck của Liberation. Phiên bản Mark 1 vẫn dùng được khi cần, nhưng sẽ hơi dễ nhầm hơn vì bố cục hơi khác so với trên màn hình, và các nút chỉ có thể hiển thị đỏ, cam hoặc xanh lá, nên sẽ không khớp với màu của Clip.

{% hint style="info" %}
APC40 Mark 1 đời đầu ra mắt từ năm 2009(!) và một số người vẫn thích phiên bản này vì thân kim loại và kiểu dáng chắc chắn giống một bàn điều khiển. Phiên bản Mark 2 cập nhật ra mắt năm 2014; dù đã ngừng sản xuất vào năm 2024, thiết bị sẽ được sản xuất trở lại vào năm 2025 do nhu cầu từ các nghệ sĩ trình diễn hình ảnh (Resolume, v.v.) và người làm laser.
{% endhint %}

Để xem danh sách đầy đủ các điều khiển có trên APC40, hãy xem [Tham khảo APC40](../reference/apc40-reference.md "mention")

### APC Mini

Liberation 1.0.3 cũng bao gồm một cấu hình cho APC Mini. Cấu hình này ánh xạ lưới Clip 8x5, các nút zone, điều khiển lật X/Y của zone, các nút group, dừng tất cả Clip, di chuyển trang Clip, di chuyển trang zone, tap tempo, đặt lại ô nhịp và chỉnh nhẹ tempo. Các fader điều khiển mức effect, còn fader khi giữ Shift điều khiển tham số effect. Fader cuối cùng điều khiển Global Brightness.

### MIDI Fighter Twister

Cấu hình MIDI Fighter Twister dành cho kiểu điều khiển chủ yếu bằng encoder, thay vì khởi chạy Clip. Một hàng encoder điều khiển tham số 1 cho các khe effect 1-8, và một hàng khác bám theo tám điều khiển theo ngữ cảnh trong Parameters panel, bao gồm dịch Clip, độ trễ zone, xoay/tỷ lệ global và fade group.
