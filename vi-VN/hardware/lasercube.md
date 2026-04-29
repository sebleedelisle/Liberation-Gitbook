---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/lasercube
---

# ✅ LaserCube

<figure><img src="../.gitbook/assets/main-image-4.jpg.webp" alt=""><figcaption><p>Ảnh quảng bá LaserCube do Wicked Lasers cung cấp</p></figcaption></figure>

[LaserCube](https://www.laseros.com/lasercube/) của Wicked Lasers là một thiết bị laser chạy pin cực kỳ nhỏ gọn, có nhiều cấu hình công suất khác nhau. Sản phẩm này được cộng đồng người dùng hobby ưa chuộng nhờ ứng dụng điện thoại dễ dùng, nhưng các mẫu gần đây đã đủ khả năng dùng trong các show chuyên nghiệp.

Ứng dụng trên điện thoại (tên là LaserOS, cũng có phiên bản desktop) được tải miễn phí, rất thú vị để dùng thử và đủ tốt cho hầu hết người dùng. Nhưng nếu bạn chạy các show lớn hơn với nhiều laser, bạn sẽ cần một công cụ chuyên dụng và mạnh mẽ hơn — và đó là lúc Liberation phát huy tác dụng.

### Kết nối với LaserCube

Các LaserCube đời đầu được điều khiển qua USB, nhưng các mẫu hiện nay đều có bộ điều khiển mạng tích hợp. Những thiết bị được điều khiển qua mạng này được gọi là “LaserCube Wifi”. Liberation hỗ trợ cả hai loại LaserCube\*, dù kết nối qua USB hay qua mạng.

\*(Hỗ trợ giao thức mạng LaserCube được giới thiệu từ phiên bản 0.7.3)

### USB LaserCube

Kết nối LaserCube với máy tính bằng cáp micro USB, sau đó tìm thiết bị trong panel _Controller Assignment_ (xem [Controller Assignment](../setting-up/controller-assignment.md)). Nếu thiết bị không tự động xuất hiện, hãy nhấn nút _REFRESH_.

### Network LaserCube "Wifi"

{% hint style="danger" %}
Mặc dù các thiết bị “Wifi” được thiết kế để vận hành qua mạng không dây, cách này không được khuyến nghị vì bạn rất có thể sẽ gặp tình trạng mất kết nối hoặc lỗi giật. Thay vào đó, hãy dùng cổng RJ45 để kết nối LaserCube vào mạng có dây, giống như khi dùng Ether Dream.
{% endhint %}

Kết nối LaserCube vào mạng có dây của bạn.

Đặt LaserCube ở chế độ “LAN Client” và đảm bảo trong mạng có router. LaserCube sẽ nhận địa chỉ IP từ router, sau đó thiết bị sẽ xuất hiện trong panel _Controller Assignment_. (Xem [Controller Assignment](../setting-up/controller-assignment.md)).

{% hint style="info" %}
Bạn có thể thiết lập mạng không cần router và gán địa chỉ IP tĩnh cho tất cả thiết bị; cách này rất phổ biến trong ngành sự kiện. Cá nhân tôi vẫn thích thêm một router vào mạng và khuyến nghị lựa chọn này cho những ai chưa có nhiều kinh nghiệm về mạng.

Router sẽ tự động cấp phát địa chỉ IP cho mọi thiết bị; theo tôi cách này đơn giản hơn và ít dễ lỗi hơn.
{% endhint %}

{% hint style="danger" %}
Khác với Ether Dream, _**LaserCube KHÔNG TẮT TIA LASER**_ nếu gặp lỗi thiếu dữ liệu trong bộ đệm, mất gói tin hoặc dữ liệu bị hỏng / không đúng.

Thay vào đó, thiết bị chỉ tiếp tục từ điểm đang dừng, và trong một số trường hợp điều này có thể khiến tia laser đang phát quét qua các khu vực không nằm trong zones; tệ hơn nữa là có thể cắt xuyên qua các mask trong phần mềm.

Tôi đang trao đổi với đội ngũ thiết kế/lập trình của LaserCube và hy vọng họ sẽ xử lý vấn đề này trong tương lai bằng bản cập nhật firmware. Nhưng trong thời gian chờ đợi, bạn phải đảm bảo che chắn vật lý ở mọi nơi mà bạn không muốn tia laser đi tới.

Công bằng mà nói, có lẽ bạn vẫn nên làm việc này trong mọi trường hợp, nhưng bản thân tôi có dùng mask trong phần mềm để bảo vệ camera và máy chiếu. Vì vậy hãy lưu ý rằng làm việc này bằng giao thức mạng LaserCube nguy hiểm hơn so với Ether Dream (thiết bị sẽ chuyển sang chế độ dừng an toàn ngay khi có bất kỳ lỗi hoặc dữ liệu bị thiếu nào).

Ngoài ra, tôi đã nói rồi nhưng vẫn nhắc lại: **hãy dùng kết nối có dây cho LaserCube**. Wifi sẽ không đủ ổn định và sẽ làm vấn đề này nghiêm trọng hơn.
{% endhint %}
