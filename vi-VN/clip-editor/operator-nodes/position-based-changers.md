---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/position-based-changers
---

# 🟩 Bộ thay đổi dựa trên vị trí

Nhóm node này chỉnh sửa nội dung theo vị trí. Theo mặc định, hiệu ứng được áp dụng dọc theo trục ngang (từ trái sang phải), nhưng bạn có thể xoay trục này đến bất kỳ góc nào. Mỗi node cũng có chế độ _radial_, trong đó hiệu ứng được điều khiển bởi góc của từng điểm so với tâm.

* **Colour Changer by Position** – dịch chuyển màu trên trục đã chọn hoặc quanh góc radial.\
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

**Chế độ màu**

Các mục này xác định những thành phần nào của phần chỉnh màu được áp dụng lên nội dung. Xem thêm: [Thiết lập màu và HSB](../fundamentals/colour-settings-and-hsb.md).

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

**Giá trị Start / End**

Các thanh trượt này xác định dải màu được áp dụng dọc theo trục đã chọn (hoặc vòng quét radial).

* **start hue** – hue ở đầu gradient.
* **end hue** – hue ở cuối gradient.
* **start saturation** – saturation ở đầu.
* **end saturation** – saturation ở cuối.
* **start brightness** – brightness ở đầu.
* **end brightness** – brightness ở cuối.
* **blend** – trộn phần đổi màu với màu gốc. Ở 100%, hiệu ứng thay thế hoàn toàn màu gốc.

**Ví dụ 1: Gradient cầu vồng trượt**

Bắt đầu từ thiết lập mặc định:

1. Giữ node ở chế độ **Linear** (góc 0° = ngang).
2. Giữ **wavelength** ở 100% (trải hết toàn bộ chiều rộng, và đây thường là giá trị mặc định).
3. Giữ các giá trị bắt đầu và kết thúc như mặc định.
4. Bật **repeat**.
5. Thêm **Sawtooth Oscillator** vào thiết lập **offset**, chạy từ 0% đến 100%.

***

**Ví dụ 2: Gradient Đen–Trắng–Đen (Pingpong)**

Bắt đầu từ thiết lập mặc định:

1. Giữ node ở chế độ **Linear** (góc 0° = ngang).
2. Giữ **wavelength** ở 100% (trải hết toàn bộ chiều rộng, và đây thường là giá trị mặc định).
3. Tắt **repeat**.
4. Đặt **start brightness** thành 0 (đen).
5. Đặt **end brightness** thành 100 (trắng).
6. Đặt **start saturation** và **end saturation** thành 0 (chuyển sang thang xám).
7. **hue mode** OFF
8. **saturation mode** FIXED
9. **brightness mode** FIXED
10. Bật **pingpong**.

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
* **Radial** – chuyển từ chế độ linear sang radial, để độ dịch chuyển dựa trên góc tính từ tâm.
* **Radial Smooth Loop** – điều chỉnh wavelength để nó chia đều 100% vòng tròn, tránh đường nối nhìn thấy được trong chế độ radial.
