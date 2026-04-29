---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/introduction
---

# ✅ Giới thiệu

Liberation có hệ thống DMX linh hoạt và mạnh mẽ, cho phép bạn tạo hiệu ứng ánh sáng và điều khiển các laser tương thích DMX qua Art-Net. Hệ thống này được thiết kế để giúp bạn dễ dàng đồng bộ ánh sáng với chương trình laser mà không cần bàn điều khiển ánh sáng riêng.

{% hint style="info" %}
**Art-Net là gì, và liên quan thế nào đến DMX?**

**DMX** là hệ thống đã được dùng nhiều năm để điều khiển đèn, laser, máy tạo khói và các hiệu ứng sân khấu khác. DMX gửi tín hiệu điều khiển qua cáp chuyên dụng, thường dùng đầu nối XLR, và mỗi thiết bị sẽ lắng nghe một nhóm kênh cụ thể để biết cần làm gì.

**Art-Net** là cách mới hơn để gửi cùng dữ liệu DMX đó qua mạng máy tính thông thường. Thay vì dùng cáp chuyên dụng, Art-Net gửi mọi thứ qua Ethernet, giống như lưu lượng internet hoặc mạng nội bộ.

Trong Liberation, toàn bộ tín hiệu DMX output được gửi bằng Art-Net. Bạn có thể dùng Art-Net để điều khiển trực tiếp các thiết bị tương thích Art-Net, hoặc kết nối một **Art-Net node** – một hộp nhỏ chuyển đổi Art-Net trở lại DMX tiêu chuẩn. Nhờ vậy, bạn vẫn có thể điều khiển đèn và hiệu ứng DMX truyền thống, kể cả khi chúng không tự hỗ trợ Art-Net.
{% endhint %}

Bạn cũng có thể dùng hệ thống này để điều khiển nhiều loại thiết bị sân khấu khác nhau như máy tạo khói, máy haze, vòi phun CO₂, máy phun tia lửa lạnh, v.v. Nếu thiết bị hỗ trợ DMX, bạn có thể thiết lập nó dưới dạng một DMX zone và kích hoạt trực tiếp từ Liberation, ngay cùng với nội dung laser của bạn.

Các thiết bị DMX được thêm dưới dạng **DMX zone**, xuất hiện trong danh sách zone cùng với các beam zone laser và vùng mục tiêu canvas. Mỗi DMX zone sử dụng một **DMX preset**, cho Liberation biết cách ánh xạ các thuộc tính từ Clip laser của bạn – như vị trí, màu sắc và độ sáng – sang giá trị kênh DMX.

Khi bạn gửi một Clip tới một DMX zone, Liberation sẽ đọc phần tử đầu tiên trong Clip và chuyển đổi các thuộc tính của phần tử đó dựa trên preset. Cách này giúp bạn dễ dàng điều khiển đèn và hiệu ứng DMX trực tiếp từ chính các Clip mà bạn đã dùng cho laser.

#### Liberation tại Glastonbury

<figure><img src="../.gitbook/assets/show-arcadia-spider-2023.jpg" alt=""><figcaption></figcaption></figure>

Bài thử nghiệm thực tế đầu tiên của hệ thống DMX trong Liberation diễn ra tại Glastonbury 2023, nơi Reach Lasers lắp đặt tổng cộng 90 nguồn beam trong sân khấu Arcadia “spider”.

18 laser được điều khiển bằng Ether Dreams tích hợp bên trong, và thêm 12 thanh beam 6 đầu được điều khiển qua Art-Net và DMX.
