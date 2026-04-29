---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/using-liberation-with-capture
---

# 🟩 Sử dụng Liberation với Capture

Liberation hỗ trợ [Capture](https://capture.se) làm trình trực quan hóa bên ngoài (từ phiên bản 1.0.3 trở đi). Nếu bạn đã dùng Capture trong quy trình làm việc, bạn có thể dùng nó để xem trước output laser trực tiếp của Liberation trong cảnh 3D.

### Cách hoạt động

Không cần quy trình kết nối đặc biệt hay liên kết thủ công.

Miễn là:

* Liberation và Capture nằm trên cùng một mạng
* Tường lửa của bạn cho phép kết nối

…thì mọi laser bạn đã thiết lập trong Liberation sẽ tự động xuất hiện trong Capture dưới dạng nguồn media. Bạn không cần cấu hình địa chỉ IP hay bật tùy chọn đặc biệt nào - chúng sẽ tự hiển thị.

### Xem laser trong Capture

Tất cả laser đã cấu hình trong Liberation sẽ xuất hiện trong Capture dưới dạng các nguồn media khả dụng.

Để thực sự thấy output:

* Laser phải ở trạng thái armed trong Liberation
* Nguồn phải được gắn vào một fixture laser trong Capture

Sau khi được armed, Capture sẽ trực quan hóa luồng output trực tiếp từ Liberation. Nếu một laser ở trạng thái disarmed trong Liberation, nó vẫn sẽ hiển thị trong Capture như một nguồn, nhưng sẽ không xuất bất kỳ nội dung nào.

Xem tài liệu tại [capture.se](https://www.capture.se/) để biết thêm hướng dẫn và hỗ trợ khi thiết lập laser trong Capture. <br>

### Giới hạn giấy phép và laser ở trạng thái armed

Kết nối Capture được xử lý giống hệt như các output laser vật lý.

Điều này có nghĩa là:

* Bạn chỉ có thể arm số lượng laser tối đa mà cấp giấy phép của bạn cho phép
* Chỉ các laser ở trạng thái armed mới chủ động gửi dữ liệu tới Capture

### Tôi có cần Capture không?

Hoàn toàn không.

Liberation có sẵn trình trực quan hóa 3D tích hợp, luôn khả dụng và không phụ thuộc vào cấp giấy phép của bạn. Bạn có thể thiết kế và xem trước show trực tiếp trong Liberation mà không cần phần mềm bên ngoài.

Capture chỉ đơn giản là một tùy chọn bổ sung nếu bạn đã dùng nó cho thiết kế ánh sáng hoặc show.

### Khắc phục sự cố

Nếu laser không xuất hiện trong Capture:

* Kiểm tra để đảm bảo cả hai ứng dụng nằm trên cùng một mạng
* Kiểm tra cài đặt tường lửa
* Đảm bảo laser ở trạng thái armed trong Liberation
