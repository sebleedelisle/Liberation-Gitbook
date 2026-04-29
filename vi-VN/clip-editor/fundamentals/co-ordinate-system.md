---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/co-ordinate-system
---

# 🟩 Hệ tọa độ

Nội dung Clip sử dụng hệ tọa độ x/y, trong đó gốc tọa độ (0,0) nằm ở giữa màn hình.

* Trên trục ngang x, bên trái là giá trị âm, bên phải là giá trị dương.
* Trên trục dọc y, phía trên là giá trị âm, phía dưới là giá trị dương.

Clip có chiều rộng và chiều cao là 400 pixel, nên tọa độ của vùng hiển thị nằm trong khoảng từ -200 đến 200.

{% hint style="info" %}
Clip editor tạo các hình dạng _vector_. Điều này có nghĩa là chúng không được lưu dưới dạng pixel, mà dưới dạng các tập hợp tọa độ xác định cách vẽ hình. Cách này tương tự như Inkscape hoặc Illustrator định nghĩa nội dung, khác với Photoshop.
{% endhint %}

### 3D

Ngoài ra, bạn có thể di chuyển trong không gian 3D, tiến và lùi dọc theo trục z. Theo mặc định, mọi thứ đều ở vị trí z bằng 0.

* Trên trục z, lùi ra xa bạn là giá trị âm, tiến về phía bạn là giá trị dương.
