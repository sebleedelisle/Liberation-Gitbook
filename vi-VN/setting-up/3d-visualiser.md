---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/3d-visualiser
---

# ✅ 3D Visualiser

### Giới thiệu

3D visualiser của Liberation là một tính năng cực kỳ hữu ích — bạn có thể thiết kế và tinh chỉnh show mà không cần bất kỳ thiết bị laser nào! Với tôi, đây là một công cụ rất giá trị, đặc biệt trong các hệ thống phức tạp với số lượng lớn thiết bị laser.

### Di chuyển trong không gian 3D

<figure><img src="../.gitbook/assets/White.png" alt=""><figcaption><p>Giao diện 3D Visualiser</p></figcaption></figure>

* Nhấp và kéo để xoay góc nhìn quanh điểm orbit
* Dùng con lăn chuột để di chuyển tiến/lùi về phía điểm orbit
* Nhấp và kéo trong khi giữ phím shift để di chuyển camera theo phương ngang (strafe) sang trái, phải, lên và xuống trên mặt phẳng XY
* Nhấp đúp vào bất kỳ đâu trong visualiser để đặt lại vị trí camera

### Cài đặt

Mở panel _3D Visualiser Settings_ từ menu _Window_.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-22 at 10.33.17.png" alt="" width="375"><figcaption><p>Panel 3D Visualiser Settings</p></figcaption></figure>

* **Visualiser size** - thay đổi kích thước visualiser tương đối với phần còn lại của ứng dụng
* **Brightness Adjustment** - thay đổi độ sáng hiển thị của laser
* **Show laser numbers** - hiển thị số tương ứng phía trên mỗi thiết bị laser
* **Show zone names** - hiển thị tên zone tương ứng phía dưới mỗi thiết bị laser

### Cài đặt camera

Các cài đặt này chủ yếu liên quan đến camera ảo trong không gian 3D. Bạn sẽ thấy một menu thả xuống chứa các preset cho những cài đặt này để có thể lưu và tải lại.

* **Camera distance -** Camera luôn hướng về _Orbit point_ của nó. Camera distance là khoảng cách từ camera đến điểm này. Bạn cũng có thể điều chỉnh cài đặt này bằng con lăn chuột.
* **FOV -** Field of view - xác định camera có góc nhìn rộng hay đang zoom vào gần đến mức nào.
* **Orbit position** - mô tả góc xoay hiện tại quanh điểm orbit. Giá trị đầu tiên là góc xoay quanh trục X (pitch), và giá trị thứ hai là góc xoay quanh trục Y (yaw).
* **Orbit centre point** - vị trí của điểm orbit trong không gian 3D, theo x, y, z.
* **Grid height** - chiều cao của lưới so với “mặt đất” (tức là nơi y = 0).

### Cài đặt nội dung

Các cài đặt này xác định vị trí đặt các thiết bị laser (và Canvas) trong môi trường 3D. Bạn sẽ thấy một menu thả xuống chứa các preset cho những cài đặt này để có thể lưu và tải lại.

#### Thiết bị laser

Mỗi thiết bị laser có nhóm cài đặt riêng, bạn có thể mở rộng bằng hình tam giác nhỏ màu trắng.

<figure><img src="../.gitbook/assets/Camera Visualiser Laser Settings.png" alt="" width="375"><figcaption><p>Cài đặt laser trong 3D visualiser</p></figcaption></figure>

* **3D Position** - vị trí x, y và z của thiết bị laser.
* **3D Orientation** - góc xoay của thiết bị laser quanh từng trục x, y và z.
* **Flip X / Flip Y** - lật Output ảo của thiết bị laser - LƯU Ý rằng thao tác này thường không cần thiết; tốt hơn là dùng các cài đặt lật / hướng của thiết bị laser để sửa các điểm không nhất quán với phần cứng của bạn.
* **Output Range horizontal / vertical** - liên quan đến góc tối đa / tối thiểu của scanner trên thiết bị laser. 60º là giá trị tiêu chuẩn, nhưng bạn có thể điều chỉnh nếu thiết bị laser của bạn khác.

#### Canvas

Nếu đang dùng hệ thống Canvas, bạn cũng có thể chọn đưa hình ảnh Canvas vào 3D view. Bật checkbox để render Canvas trong đó, rồi dùng các cài đặt vị trí, hướng và tỷ lệ để xác định Canvas sẽ hiển thị như thế nào trong 3D view.

<figure><img src="../.gitbook/assets/Camera Visualiser Canva Settings.png" alt="" width="375"><figcaption><p>Cài đặt Canvas trong 3D visualiser</p></figcaption></figure>

{% hint style="info" %}
Thấy các laser “ma”? 3D Visualiser hoạt động khá độc lập với cấu hình laser, nên có thể trong visualiser có nhiều thiết bị laser hơn số lượng bạn có trong Liberation. Khi bạn thêm một thiết bị laser vào project, một đối tượng laser mới bên trong visualiser cũng sẽ được thêm vào. Nhưng nếu bạn xóa một thiết bị laser, vẫn sẽ còn lại một đối tượng laser “ma” trong visualiser.

Để loại bỏ tất cả laser “ma”, hãy nhấp nút _Remove extra 3D laser objects_ (ở cuối panel cài đặt 3D Visualiser).

<img src="../.gitbook/assets/Remove extra 3D laser.png" alt="" data-size="original">
{% endhint %}
