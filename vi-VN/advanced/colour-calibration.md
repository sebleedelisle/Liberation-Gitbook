---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/advanced/colour-calibration
---

# 🟩 Hiệu chuẩn màu

Hiệu chuẩn màu đảm bảo các tia laser đỏ, xanh lá và xanh dương của máy chiếu phát sáng một cách mượt mà, dễ dự đoán ở mọi mức độ sáng. Các máy chiếu khác nhau có thể có đường cong độ sáng không tuyến tính, nghĩa là mức đỏ 50% có thể trông sáng hơn hoặc tối hơn nhiều so với một nửa cường độ của mức đỏ 100%. Hiệu chuẩn sẽ điều chỉnh điều này để màu được pha trộn sạch hơn, gradient mượt hơn và màu trắng được cân bằng.

#### Làm nóng máy chiếu

Diode laser thay đổi đặc tính khi nóng lên. Luôn để máy chiếu ổn định trước khi hiệu chuẩn:

* Chiếu một khung sáng, chẳng hạn như **White rectangle test pattern (11)**, trong ít nhất **15–20 phút**.
* Việc này giúp cân bằng màu bạn thiết lập được giữ ổn định trong suốt buổi diễn.

#### Cách hoạt động của bài kiểm tra hiệu chuẩn

Sử dụng các test pattern để hiệu chuẩn (xem [test pattern](../output-view/test-patterns.md))

* **5** – Đỏ
* **6** – Xanh lá
* **7** – Xanh dương
* **8** – Trắng

Mỗi test pattern này hiển thị bốn đường chuyển động:

* **Đường trên cùng** – độ sáng 100% ở tốc độ tối đa
* **Đường thứ hai** – độ sáng 75% ở tốc độ 75%
* **Đường thứ ba** – độ sáng 50% ở tốc độ 50%
* **Đường thứ tư** – độ sáng 25% ở tốc độ 25%

Vì cả độ sáng _và tốc độ_ đều được giảm theo cùng tỷ lệ, các đường này sẽ trông có cùng độ sáng. Nếu một đường trông sáng hơn hoặc tối hơn, hãy điều chỉnh thanh trượt tương ứng cho đến khi chúng khớp nhau.

Mỗi test pattern cũng có một đường thứ năm ở **độ sáng 0%**, đường này không được hiển thị. Đường này dùng để hiệu chỉnh các laser không phát sáng ở mức rất thấp. Nếu laser của bạn vẫn không nhìn thấy ở độ sáng thấp, hãy tăng dần **thiết lập 0%** cho đến khi đường vừa xuất hiện, rồi giảm nhẹ cho đến khi nó biến mất lần nữa. Mục tiêu là tìm ngưỡng laser bắt đầu phát sáng, sau đó giữ ngay dưới ngưỡng đó - để các hiệu ứng fade bắt đầu tự nhiên mà không bị cắt mất dải thấp nhất.

#### Sử dụng panel Colour Calibration

Panel này cung cấp các điều khiển độc lập cho từng kênh (đỏ, xanh lá, xanh dương) ở các mức 100, 75, 50, 25 và 0%.

1. **Chọn một test pattern** (bắt đầu với màu đỏ).
2. **Điều chỉnh các thanh trượt** để các đường 100, 75, 50 và 25% trông có cùng độ sáng.
3. **Tinh chỉnh thanh trượt 0%** nếu đường “tắt” vẫn còn hơi nhìn thấy.
4. **Lặp lại cho màu xanh lá và xanh dương.**
5. Chuyển sang **White test pattern (8)**. Cả bốn đường phải trông bằng nhau và màu trắng phải trung tính (không bị ám màu).

#### Điều chỉnh cân bằng trắng

Bạn cũng có thể dùng hệ thống này để điều chỉnh **cân bằng trắng**. Sau khi hiệu chuẩn từng kênh riêng lẻ, hãy chuyển sang **White test pattern (8)**. Nếu ánh sáng phát ra bị ám màu (ví dụ quá xanh lá hoặc quá xanh dương), hãy điều chỉnh mức tương đối của các kênh đỏ, xanh lá và xanh dương cho đến khi các đường hiển thị màu trắng trung tính. Ngay cả khi công suất các laser của bạn chênh lệch khá nhiều, việc hiệu chuẩn vẫn giúp đưa chúng gần nhau hơn và tạo ra hỗn hợp màu sạch hơn, cân bằng hơn.

#### Lưu hiệu chuẩn

* Dùng **Store** để ghi đè preset hiện tại.
* Dùng **Store As** để tạo preset mới (hữu ích nếu bạn làm việc với nhiều laser).
