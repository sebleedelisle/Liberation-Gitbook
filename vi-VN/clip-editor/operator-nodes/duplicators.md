---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/duplicators
---

# 🟩 Duplicators

## <img src="../../.gitbook/assets/image (5).png" alt="" data-size="line"> Mirror

Tạo một bản sao phản chiếu của toàn bộ nội dung. Theo mặc định, trục phản chiếu là một đường thẳng đứng ở giữa.

* **angle** - góc của đường trục phản chiếu.
* **offset position** - dịch chuyển trục phản chiếu (di chuyển vuông góc với trục)
* **delay** - độ trễ thời gian của nội dung được phản chiếu. Lưu ý rằng mục này chỉ có tác dụng nếu nội dung có một dạng animation nào đó.

#### Tùy chọn 3D (có sẵn khi chọn 3D)

* **angle X / angle Y** - trục phản chiếu trở thành một mặt phẳng, và bạn có thể dùng các thiết lập này để xoay mặt phẳng trong 3D.

## <img src="../../.gitbook/assets/image (6).png" alt="" data-size="line"> Circular Pattern

Nhân bản nội dung theo dạng vòng tròn.

* **radius** - khoảng cách từ điểm trung tâm mà nội dung được dịch chuyển trước khi xoay.
* **count** - số lượng bản sao của đối tượng cần tạo.
* **use each objects pivot point** - khi được chọn, mỗi phần tử sẽ được dịch chuyển và xoay quanh điểm trung tâm riêng của nó. (Chỉ có tác dụng khi có nhiều phần tử đang được nhân bản)
* **delay** - thêm độ trễ thời gian tăng dần cho từng phần tử được nhân bản. Lưu ý rằng nội dung cần có một dạng animation nào đó để hiệu ứng này thấy rõ.
* **rotation** - một giá trị xoay bù được thêm vào các phần tử.

#### Tùy chọn 3D (có sẵn khi chọn 3D)

* **rotation x / rotation y** - xoay toàn bộ mẫu vòng tròn quanh các trục x và y.

## <img src="../../.gitbook/assets/image (7).png" alt="" data-size="line"> Grid Pattern

Nhân bản nội dung theo dạng lưới gồm các hàng và cột.

* **spacing** - khoảng cách giữa các phần tử
* **count X**- số lượng bản sao theo chiều ngang (cột)
* **count Y**- số lượng bản sao theo chiều dọc (hàng)
* **horizontal alignment** - điểm bắt đầu của các cột: LEFT, CENTRE hoặc RIGHT
* **vertical alignment** - điểm bắt đầu của các hàng: TOP, MIDDLE hoặc BOTTOM
* **delay** - thêm độ trễ thời gian tăng dần cho từng phần tử được nhân bản. Lưu ý rằng nội dung cần có một dạng animation nào đó để hiệu ứng này thấy rõ.
