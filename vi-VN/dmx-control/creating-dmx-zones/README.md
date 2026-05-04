---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/creating-dmx-zones
---

# 🟩 Tạo DMX zone

1. Kết nối Art-Net node và thiết lập theo hướng dẫn trong [Kết nối với Art-Net node](../connecting-to-an-artnet-node.md "mention").
2. Mở **DMX Zones** và nhấp **ADD DMX ZONE**.
3. Đặt **Node**, **Universe** và **Address** của zone khớp với thiết bị.
4. Chọn **Preset** cho thiết bị. Preset xác định các kênh DMX nào sẽ nhận giá trị cố định, giá trị bật/tắt nội dung, màu RGB, vị trí X/Y, độ sáng hoặc đầu vào DMX Value rõ ràng.
5. Nhấp **Edit DMX profile/channel mapping** (biểu tượng thanh trượt) để chỉnh sửa ánh xạ kênh. Preset mặc định bắt đầu với một kênh bật/tắt nội dung và các kênh màu RGB.
6. Gán các Clip cho DMX zone giống như cách bạn gán chúng cho beam zone hoặc canvas zone.
7. Nhấn **ARM** khi bạn đã sẵn sàng để zone xuất DMX.

{% hint style="warning" %}
Chỉ các DMX zone đã được kích hoạt mới gửi giá trị trực tiếp. Các DMX zone chưa được kích hoạt sẽ xóa các kênh đã ánh xạ về 0, an toàn hơn khi thiết lập thiết bị.
{% endhint %}

Đầu ra DMX cũng bị giới hạn bởi cấp giấy phép của bạn. Nếu nút **ARM** bị tắt, hãy kiểm tra xem cấp giấy phép của bạn có bao gồm đầu ra DMX hay không, hoặc số lượng DMX zone được kích hoạt tối đa đã đạt giới hạn chưa.
