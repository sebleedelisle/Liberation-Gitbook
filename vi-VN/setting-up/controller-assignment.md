---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/controller-assignment
---

# ✅ Controller Assignment

Sau khi đã thiết lập các laser trong Liberation, bạn có thể gán từng laser với một bộ điều khiển laser ngoài thực tế. (Xem [các laser và bộ điều khiển/DAC tương thích](../hardware/compatible-lasers-and-controllers-dacs.md) để kiểm tra phần cứng có thể sử dụng). Các bộ điều khiển sẽ được kết nối qua USB hoặc qua mạng.

* Mở panel _Controller Assignment_ bằng tùy chọn menu _View -> Controller Assignment_. (Hoặc bạn cũng có thể dùng nút _ASSIGN LASER CONTROLLERS_ trong panel _Laser Overview_.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.30.18.png" alt="Panel Controller Assignment"><figcaption></figcaption></figure>

* Panel được chia làm hai phần: danh sách laser ở bên trái và danh sách các bộ điều khiển hiện có ở bên phải. Nếu bạn không thấy bộ điều khiển laser của mình trong danh sách, hãy nhấn nút _REFRESH_. Nếu vẫn gặp vấn đề, xem [khắc phục sự cố](../troubleshooting/).
* Để gán một bộ điều khiển cho một laser, hãy nhấp và kéo từ bên phải sang một vị trí laser còn trống ở bên trái. Thao tác này cho Liberation biết bộ điều khiển nào sẽ được dùng cho laser nào. (Nếu đổi ý, bạn có thể tự do kéo bộ điều khiển lên xuống để chuyển từ laser này sang laser khác.)

<figure><img src="../.gitbook/assets/Screenshot 2024-12-31 at 14.33.23.png" alt="Danh sách bộ điều khiển" width="375"><figcaption></figcaption></figure>

* Nếu bạn thấy một ô vuông màu xanh lá bên cạnh bộ điều khiển, điều đó có nghĩa là Liberation đã kết nối thành công với bộ điều khiển đó.

<figure><img src="../.gitbook/assets/controller-assignment-laser-list" alt="" width="338"><figcaption><p>Một Ether Dream và một Helios DAC lần lượt được gán cho laser 2 và 3</p></figcaption></figure>

{% hint style="info" %}
Lưu ý rằng mỗi khi bạn kết nối với một bộ điều khiển, laser sẽ tự động được chuyển sang trạng thái không armed.
{% endhint %}

* Ô vuông màu cam 🟧 nghĩa là bộ điều khiển đang gặp sự cố kết nối chập chờn. Nguyên nhân thường là do vấn đề mạng, xem [khắc phục sự cố](../troubleshooting/).
* Ô vuông màu đỏ 🟥 nghĩa là không thể kết nối tới bộ điều khiển, xem [khắc phục sự cố](../troubleshooting/).
* _Nút ngắt kết nối_ (X) sẽ ngắt kết nối bộ điều khiển nhưng không xóa bộ điều khiển khỏi phần gán laser. Sau đó, bạn có thể dùng _nút kết nối lại_ (biểu tượng mũi tên làm mới) để kết nối lại, hoặc nhấp lại vào _nút ngắt kết nối_ để xóa phần gán.
* _Tính năng nâng cao:_ Mở panel phân tích bộ điều khiển bằng cách nhấp vào nút có biểu tượng giống biểu đồ. Đây là tính năng nâng cao, cung cấp thông tin chi tiết về luồng dữ liệu và có thể giúp khắc phục sự cố. (Tùy chọn này có thể không khả dụng với một số loại bộ điều khiển.)
* Bạn có thể dùng _nút đổi tên_ (biểu tượng bút chì) để đổi tên bộ điều khiển này thành bất cứ tên nào bạn muốn. Nên đặt tên sao cho dễ liên hệ với phần cứng cụ thể. Nếu bộ điều khiển được tích hợp trong một laser, bạn có thể đặt tên tương ứng, ví dụ _LaserCube Ultra #1_ hoặc _Triton T5 #3._ Các tên này sẽ được lưu cùng bản cài đặt Liberation của bạn và sẽ xuất hiện từ bây giờ trở đi; điều này rất hữu ích để nhanh chóng nhận diện các laser.

{% hint style="info" %}
Mẹo - **nhấp đúp** vào một bộ điều khiển ở bên phải để tự động gán nó cho laser khả dụng tiếp theo ở bên trái. Cách này có thể tiết kiệm rất nhiều thời gian nếu bạn có nhiều laser cần gán!
{% endhint %}

Bạn có thể dùng các nút _DISCONNECT ALL_ và _RECONNECT ALL_ để nhanh chóng đặt lại toàn bộ kết nối. Điều này hữu ích khi bạn gặp sự cố mạng.
