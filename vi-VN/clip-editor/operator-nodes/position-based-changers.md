---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Bộ thay đổi dựa trên vị trí

Nhóm node này chỉnh sửa nội dung theo vị trí. Theo mặc định, hiệu ứng được áp dụng dọc theo trục ngang (từ trái sang phải), nhưng bạn có thể xoay trục này đến bất kỳ góc nào. Mỗi node cũng có chế độ _radial_, trong đó hiệu ứng được điều khiển bởi góc của từng điểm so với tâm.

* **Colour Changer by Position** – áp dụng một gradient dọc theo trục đã chọn hoặc quanh góc radial.\
  \&#xNAN;_Ví dụ: Tạo gradient cầu vồng quét qua một đường thẳng, hoặc dùng chế độ radial trên một vòng tròn để tạo hiệu ứng bánh xe màu._
* **Wave Shift by Position** – áp dụng biến dạng dạng sóng sin, dịch chuyển nội dung theo chiều dọc (hoặc vuông góc với trục đã chọn).\
  \&#xNAN;_Ví dụ: Làm một đường gợn như mặt nước, hoặc dùng chế độ radial để làm vòng tròn phồng ra từ tâm._
* **Noise Shift by Position** – áp dụng biến dạng nhiễu simplex, dịch chuyển nội dung theo chiều dọc (hoặc vuông góc với trục đã chọn).\
  \&#xNAN;_Ví dụ: tương tự ví dụ Wave Shift, nhưng có cảm giác tự nhiên và ngẫu nhiên hơn, rất phù hợp để thêm biến thiên tự nhiên._

## &#x20;Đổi màu theo vị trí

Node này áp dụng thay đổi màu trên nội dung của bạn dựa theo vị trí. Theo mặc định, trục là trục ngang (0°), nhưng bạn có thể xoay trục hoặc chuyển sang chế độ radial.

* **wavelength** – đặt kích thước của chu kỳ màu lặp lại.
  * _Chế độ Linear:_ ở 100%, một chu kỳ đầy đủ trải hết toàn bộ chiều rộng của nội dung.
  * _Chế độ Radial:_ ở 100%, một chu kỳ đầy đủ trải hết toàn bộ vòng tròn (360°). Giá trị là phần trăm của vòng tròn: ví dụ 50% = nửa vòng tròn (180°).
* **offset** – dịch chuyển điểm bắt đầu của chu kỳ màu, tính theo phần trăm của wavelength. Bạn có thể modulation giá trị này (ví dụ bằng sawtooth oscillator) để chuyển màu mượt mà liên tục.
* **repeat** – khi bật, chu kỳ sẽ lặp lại trên nội dung. Nếu tắt, gradient chỉ được áp dụng một lần: mọi phần trước điểm bắt đầu sẽ là màu bắt đầu, mọi phần sau điểm kết thúc sẽ là màu kết thúc.
* **pingpong** – khi bật, mỗi lần lặp sẽ đảo chiều, tạo hiệu ứng phản chiếu. Nếu tắt _Repeat_, gradient sẽ đi tới rồi quay lại một lần. _Lưu ý: trong chế độ Pingpong, wavelength bao gồm cả lượt đi và lượt về._
* **linear angle** – xoay trục của hiệu ứng. 0° = ngang.
* **radial** – chuyển sang chế độ radial, áp dụng màu dựa trên góc tính từ tâm.
* **radial smooth loop** – tự động điều chỉnh wavelength để nó chia đều 100% vòng tròn, tránh đường nối nhìn thấy được tại điểm chu kỳ quay vòng.
* **legacy mode** – chuyển về các thanh trượt HSB start/end cũ hơn. Tắt tùy chọn này để dùng trình chỉnh sửa gradient mới.

**Chế độ màu**

Các mục này xác định những thành phần nào của phần chỉnh màu được áp dụng lên nội dung. Xem thêm: [Thiết lập màu và HSB](../fundamentals/colour-settings-and-hsb.md "mention").

* **hue mode**
  * _OFF_ – hue không thay đổi.
  * _FIXED_ – hue bị đặt thành một giá trị cố định.
  * _SHIFTED_ – hue được dịch theo lượng đã chỉ định (các phần tử có màu khác nhau vẫn phân biệt được, nhưng được dịch quanh bánh xe màu cùng nhau).
* **saturation mode**
  * _OFF_ – saturation không thay đổi.
  * _FIXED_ – saturation được đặt thành giá trị đã chỉ định.
* **brightness mode**
  * _OFF_ – brightness không thay đổi.
  * _FIXED_ – brightness được đặt thành giá trị đã chỉ định.
  * _MULTIPLY_ – brightness được nhân theo giá trị đã chỉ định. Cách này giữ lại động thái gốc (ví dụ các phần tử nhấp nháy vẫn nhấp nháy, nhưng trong phạm vi brightness đã giới hạn).

**Trình chỉnh sửa gradient**

Sử dụng cùng trình chỉnh sửa gradient như [Thay đổi màu](colour-changer.md "mention"), nhưng ánh xạ gradient lên nội dung theo vị trí.

* Nhấp vào thanh gradient để thêm một điểm dừng màu.
* Nhấp chuột trái vào một điểm dừng để chọn, rồi kéo ngang để di chuyển điểm đó.
* Kéo điểm dừng đã chọn xuống, ra xa khỏi thanh, hoặc nhấn Delete/Backspace để xóa điểm đó. Một gradient luôn giữ lại ít nhất hai điểm dừng.
* Nhấp chuột phải vào một điểm dừng để chỉnh sửa bằng bộ chọn màu.
* Dùng **Position**, **Hue**, **Saturation** và **Brightness** để chỉnh sửa chính xác điểm dừng đã chọn.
* **interpolation** chọn cách pha trộn màu giữa các điểm dừng:
* **HSB** – pha trộn hue, saturation và brightness. Cách này phù hợp nhất cho chuyển động kiểu cầu vồng mượt quanh vòng màu.
* **RGB** – pha trộn trực tiếp các giá trị đỏ, lục và lam. Cách này thường cho cảm giác giống hiệu ứng fade màu trên màn hình hoặc bàn điều khiển ánh sáng hơn.
* **NONE** – nhảy từ điểm dừng này sang điểm dừng kế tiếp, không pha trộn.
* **hue direction** có sẵn khi dùng nội suy HSB:
* **AUTO** – đi theo đường ngắn nhất quanh vòng hue.
* **FORWARDS** – luôn đi tiến qua các giá trị hue.
* **BACKWARDS** – luôn đi lùi qua các giá trị hue.
* **blend** – trộn phần đổi màu với màu gốc. Ở 100%, hiệu ứng thay thế hoàn toàn màu gốc.

**Giá trị start / end kiểu cũ**

Nếu bật **legacy mode**, trình chỉnh sửa gradient sẽ được thay bằng các điều khiển cũ hơn:

* **start hue / end hue** – hue ở đầu và cuối dải.
* **start saturation / end saturation** – saturation ở đầu và cuối dải.
* **start brightness / end brightness** – brightness ở đầu và cuối dải.

**Ví dụ 1: Gradient cầu vồng trượt**

Bắt đầu từ thiết lập mặc định:

1. Giữ node ở chế độ **Linear** (góc 0° = ngang).
2. Giữ **wavelength** ở 100% (trải hết toàn bộ chiều rộng, và đây thường là giá trị mặc định).
3. Giữ nguyên gradient mặc định.
4. Bật **repeat**.
5. Thêm **Sawtooth Oscillator** vào thiết lập **offset**, chạy từ 0% đến 100%.

***

**Ví dụ 2: Gradient Đen–Trắng–Đen (Pingpong)**

Bắt đầu từ thiết lập mặc định:

1. Giữ node ở chế độ **Linear** (góc 0° = ngang).
2. Giữ **wavelength** ở 100% (trải hết toàn bộ chiều rộng, và đây thường là giá trị mặc định).
3. Tắt **repeat**.
4. Đặt điểm dừng gradient đầu tiên thành màu đen.
5. Đặt điểm dừng gradient cuối cùng thành màu trắng.
6. Đặt **hue mode** thành OFF.
7. Đặt **saturation mode** thành FIXED nếu bạn muốn ép kết quả thành thang xám.
8. Đặt **brightness mode** thành FIXED.
9. Bật **pingpong**.

_Kết quả: gradient chuyển dần từ đen sang trắng, rồi quay lại đen theo chiều rộng._\
Lưu ý rằng nếu bạn muốn nội dung giữ nguyên hue và saturation, hãy tắt Saturation mode. \\

***

**Ví dụ 3: Bánh xe cầu vồng xoay (Radial)**

1. Bật chế độ **radial**.
2. Đặt **wavelength** thành 100% (một vòng quét đầy đủ 360°).
3. Bật **repeat**.
4. Thêm **Sawtooth Oscillator** vào thiết lập **offset**, chạy từ 0% đến 100%.

_Kết quả: một bánh xe màu liền mạch xoay liên tục quanh vòng tròn._

## &#x20;Dịch sóng theo vị trí

Node này áp dụng biến dạng dạng sóng trên nội dung, dịch chuyển các điểm vuông góc với trục đã chọn (hoặc theo hướng radial từ tâm).

* **Wavelength** – đặt độ dài của chu kỳ sóng.
  * _Chế độ Linear:_ ở 100%, một chu kỳ đầy đủ trải hết toàn bộ chiều rộng của nội dung.
  * _Chế độ Radial:_ ở 100%, một chu kỳ đầy đủ trải hết 360°. (Giá trị là phần trăm của vòng tròn: 50% = nửa vòng, 25% = một phần tư vòng, v.v.)
* **Size** – điều khiển biên độ của sóng (nội dung bị dịch chuyển bao xa).
* **Offset** – dịch chuyển sóng dọc theo trục (hoặc quanh vòng tròn trong chế độ radial). Đây là phần trăm của wavelength, nên bạn có thể animate nó bằng **Oscillator Node** để làm sóng di chuyển.
* **Radial** – chuyển từ chế độ linear sang radial, để độ dịch chuyển dựa trên góc tính từ tâm.
* **Radial Smooth Loop** – điều chỉnh wavelength để nó chia đều 100% vòng tròn, tránh đường nối nhìn thấy được tại điểm quay vòng.
* **Triangle** – đổi dạng sóng từ sin sang tam giác.
* **Absolute** – lấy giá trị tuyệt đối của sóng, tạo ra chỉ các dịch chuyển hướng lên (gập phần âm sang phía dương).
* **Angle** – xoay trục của sóng. 0° = ngang.

## &#x20;Dịch nhiễu theo vị trí

Node này làm biến dạng nội dung bằng một trường nhiễu (giống như nhiễu động), dịch chuyển các điểm vuông góc với trục đã chọn (hoặc theo hướng radial từ tâm). So với _Wave Shift_, kết quả tự nhiên và ngẫu nhiên hơn.

* **Detail** – điều khiển độ mịn/chi tiết của nhiễu. Giá trị cao hơn = biến thiên sắc nét và nhiều chi tiết hơn. Giá trị thấp hơn = biến thiên mượt hơn.
* **Wavelength** – đặt thang kích thước của mẫu nhiễu.
  * _Chế độ Linear:_ ở 100%, một chu kỳ nhiễu đầy đủ trải hết chiều rộng của nội dung.
  * _Chế độ Radial:_ ở 100%, một chu kỳ đầy đủ trải hết 360°.
* **Size** – điều khiển lượng dịch chuyển (biên độ của biến dạng nhiễu).
* **Offset** – dịch chuyển mẫu nhiễu dọc theo trục (hoặc quanh vòng tròn). Đây là phần trăm của wavelength, nên bạn có thể animate nó bằng **Oscillator Node** để làm nhiễu “chảy.”
* **Depth Offset** – di chuyển xuyên qua trường nhiễu 3D, tạo biến thiên theo thời gian. Mục này đặc biệt hiệu quả khi được animate bằng Oscillator Node.
* **Depth Detail** – điều khiển mức chi tiết của biến thiên theo chiều depth.
* **Absolute** – lấy giá trị tuyệt đối của nhiễu, gập các giá trị âm thành dương (tạo ra chỉ dịch chuyển một phía).
* **Angle** – xoay trục của noise trong chế độ tuyến tính. 0° = nằm ngang.
* **Radial** – chuyển từ chế độ linear sang radial, để độ dịch chuyển dựa trên góc tính từ tâm.
* **Radial Smooth Loop** – điều chỉnh wavelength để nó chia đều 100% vòng tròn, tránh đường nối nhìn thấy được trong chế độ radial.
