---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/transformations
---

# 🟩 Transformations

## &#x20;Translate

Di chuyển toàn bộ nội dung theo trục x, y và/hoặc z. Lưu ý rằng hệ tọa độ được đặt tâm ở giữa và trải từ +/-200 trên trục x và y. Xem [Hệ tọa độ](../fundamentals/co-ordinate-system.md "mention").

* **x** - khoảng cách di chuyển theo trục x (trái - phải).
* **y** - khoảng cách di chuyển theo trục y (trên - dưới).

#### Tùy chọn 3D (có sẵn khi chọn 3D)

* **z** - khoảng cách di chuyển theo trục z (lùi và tiến vào trong màn hình).

## <img src="../../.gitbook/assets/image (3).png" alt="" data-size="line"> Rotate

Xoay toàn bộ nội dung. Giá trị được tính bằng độ. Xem [Hệ tọa độ](../fundamentals/co-ordinate-system.md "mention").

* **rotation** - mức xoay nội dung theo chiều kim đồng hồ, tính bằng độ. Mọi thứ được xoay quanh gốc tọa độ (0,0), tức là tâm.
* **pivot point x / pivot point y** - Dùng các giá trị này để dịch điểm gốc xoay.

#### Tùy chọn 3D (có sẵn khi chọn 3D)

* **rotation x** - xoay quanh trục x (pitch).
* **rotation y** - xoay quanh trục y (yaw).
* **pivot point z** - vị trí dịch điểm xoay theo trục z.

## <img src="../../.gitbook/assets/image (4).png" alt="" data-size="line"> Scale

Thay đổi tỷ lệ toàn bộ nội dung.

* **scale** - tỷ lệ phần trăm thu phóng.
* **scale x / scale y** - nếu bạn muốn thay đổi tỷ lệ theo chiều ngang và/hoặc chiều dọc, hãy dùng các tùy chọn này.

{% hint style="warning" %}
Bất cứ khi nào một nội dung được thu phóng về 0% trên bất kỳ trục nào, nội dung đó sẽ biến mất!
{% endhint %}
