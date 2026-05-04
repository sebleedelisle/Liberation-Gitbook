---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Thay đổi màu

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Thay đổi màu

Thay đổi màu của toàn bộ nội dung đầu vào. Bạn có thể đặt các giá trị HSB cố định, hoặc chuyển sang hệ thống gradient và lấy mẫu màu từ một gradient tùy chỉnh.

* **hue, saturation, brightness** - các giá trị màu, xem [thiết lập màu và HSB](../fundamentals/colour-settings-and-hsb.md "mention")
* **hue mode** -
  * OFF - không thay đổi hue
  * FIXED - hue của các phần tử được đặt theo giá trị hue
  * SHIFT - hue của các phần tử được dịch theo giá trị này, vì vậy các phần tử có màu khác nhau vẫn giữ sự khác biệt, chỉ được dịch chuyển theo giá trị hue.
* **saturation mode** -
  * OFF - không thay đổi saturation
  * FIXED - saturation được cố định ở giá trị đã chỉ định.
* **brightness mode** -
  * OFF - không thay đổi brightness
  * FIXED - brightness của các phần tử được đặt theo giá trị brightness
  * MULTIPLY - brightness của các phần tử được kết hợp với giá trị brightness, vì vậy nếu chúng đang nhấp nháy thì vẫn sẽ nhấp nháy, nhưng chỉ sáng tối đa đến mức brightness được chỉ định tại đây.
* **gradient mode** - chuyển từ các thanh trượt HSB cố định sang trình chỉnh sửa gradient. node lấy mẫu một màu từ gradient, rồi áp dụng màu đó bằng các chế độ hue, saturation và brightness ở trên.
* **gradient position** - chọn điểm trong gradient sẽ được lấy mẫu. Tạo chuyển động cho giá trị này từ 0% đến 100% bằng Sawtooth Oscillator để duyệt qua gradient theo thời gian.
* **blend** - mức độ áp dụng colour changer, 0% là không áp dụng, 100% là áp dụng hoàn toàn, và 50% là sự kết hợp giữa màu hiện có và các giá trị mới.

{% hint style="info" %}
node Colour Change lấy mẫu một màu từ gradient cho toàn bộ đầu vào. Nếu bạn muốn gradient chạy dọc theo hình dựa trên vị trí, hãy dùng [các bộ thay đổi theo vị trí](position-based-changers.md "mention") thay thế.
{% endhint %}

### Trình chỉnh sửa gradient

Khi bật **gradient mode**, trình chỉnh sửa gradient sẽ xuất hiện bên dưới các điều khiển chính.

* Nhấp vào thanh gradient để thêm một điểm dừng màu.
* Nhấp chuột trái vào một điểm dừng để chọn, rồi kéo sang ngang để di chuyển điểm đó.
* Kéo điểm dừng đang chọn xuống dưới, ra khỏi thanh, hoặc nhấn Delete/Backspace để xóa điểm đó. Một gradient luôn giữ lại ít nhất hai điểm dừng.
* Nhấp chuột phải vào một điểm dừng để chỉnh sửa bằng bộ chọn màu.
* Dùng **Position**, **Hue**, **Saturation** và **Brightness** để chỉnh sửa chính xác điểm dừng đang chọn.
* **interpolation** chọn cách pha trộn màu giữa các điểm dừng:
* **HSB** - pha trộn hue, saturation và brightness. Cách này phù hợp nhất cho chuyển động kiểu cầu vồng mượt quanh vòng màu.
* **RGB** - pha trộn trực tiếp các giá trị đỏ, lục và lam. Cách này thường cho cảm giác giống hiệu ứng chuyển màu trên màn hình hoặc bàn điều khiển ánh sáng hơn.
* **NONE** - nhảy từ điểm dừng này sang điểm dừng tiếp theo mà không pha trộn.
* **hue direction** có sẵn khi dùng nội suy HSB:
* **AUTO** - đi theo đường ngắn nhất quanh vòng hue.
* **FORWARDS** - luôn di chuyển tiến qua các giá trị hue.
* **BACKWARDS** - luôn di chuyển lùi qua các giá trị hue.
