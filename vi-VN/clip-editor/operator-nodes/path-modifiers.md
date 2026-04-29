---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/path-modifiers
---

# 🟩 Bộ sửa đổi đường dẫn

## &#x20;Dotter

node này thay thế nội dung đường và hình bằng các chấm cách đều nhau (các chấm hiện có không thay đổi).

* **Colour** – màu của các chấm. Bị bỏ qua nếu bật _Inherit Colour_, xem bên dưới. _Xem thêm_ [Cài đặt màu và HSB](../fundamentals/colour-settings-and-hsb.md)
* **Spacing** – khoảng cách giữa các chấm, tính bằng pixel. Giá trị nhỏ hơn = nhiều chấm hơn, giá trị lớn hơn = ít chấm hơn.
* **Offset** – dịch vị trí bắt đầu của các chấm theo phần trăm của khoảng cách. Có thể animate (ví dụ bằng Oscillator Node dạng răng cưa) để tạo hiệu ứng chấm “di chuyển”.
* **Keep Original** – nếu bật, các đường/hình gốc được giữ lại và các chấm được vẽ chồng lên trên.
* **Render Profile** – chọn chất lượng render. _Xem_ [Render Profile](../fundamentals/render-profile.md)
* **Length Auto Divisible by Spacing** – tự động điều chỉnh khoảng cách để chiều dài path chia hết đều.
* **Fade Out Ends** – giảm dần độ sáng của các chấm về phía đầu và cuối path. Hữu ích khi animate **Offset** bằng Oscillator Node dạng răng cưa, để các chấm fade in/out mượt mà khi di chuyển đến cuối hình.

## &#x20;Trimmer

node này cắt bớt chiều dài hiển thị của các đường và hình, cho phép bạn làm chúng xuất hiện, ẩn đi hoặc animate theo thời gian.

* **Offset** – điều khiển vị trí bắt đầu của phần hình đang hiển thị. Ngay cả khi _Trim Size_ ở 0%, việc animate Offset từ 0% → 100% sẽ làm hình được vẽ vào, hiển thị đầy đủ ở 50%, rồi biến mất trở lại.
* **Trim Size** – đặt phần hình được giữ lại, tính theo phần trăm tổng chiều dài của hình.
* **Loop** – xử lý hình như một vòng lặp liên tục, để phần cuối nối lại với phần đầu thay vì biến mất.
* **All Shapes** – kết hợp tất cả hình đầu vào và cắt chúng như thể chúng là một path duy nhất. Nếu tắt, từng hình sẽ được cắt riêng.
* **Add Dot at Start / Add Dot at End** – thêm một chấm có màu đã chọn tại các điểm cắt. (Nếu không áp dụng cắt, sẽ không thêm chấm.)
* **Colour** – màu của các chấm tại điểm cắt. _Xem thêm_ [Cài đặt màu và HSB](../fundamentals/colour-settings-and-hsb.md)
* **Render Profile** – chọn render profile cho các chấm. _Xem_ [Render Profile](../fundamentals/render-profile.md)
