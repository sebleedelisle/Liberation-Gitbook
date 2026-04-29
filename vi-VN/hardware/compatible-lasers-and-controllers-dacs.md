---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/hardware/compatible-lasers-and-controllers-dacs
---

# ✅ Laser và bộ điều khiển tương thích (DAC)

### Laser nào tương thích với Liberation?

Nếu laser của bạn có đầu vào ILDA tiêu chuẩn, bạn có thể dùng nó với Liberation (cùng với một bộ điều khiển laser tương thích như Ether Dream hoặc Helios DAC - [xem danh sách đầy đủ bên dưới](compatible-lasers-and-controllers-dacs.md#compatible-laser-controllers)).

<figure><img src="../.gitbook/assets/helios-dac.png" alt="" width="563"><figcaption><p>Helios DAC - lựa chọn rẻ nhất cho sử dụng tại nhà</p></figcaption></figure>

Bạn không cần bộ điều khiển ngoài hoặc đầu vào ILDA nếu:

* Laser của bạn đã tích hợp Ether Dream bên trong; hoặc
* Bạn có LaserCube của Wicked Lasers; hoặc
* Bạn có thiết bị X-Laser tích hợp Mercury; hoặc
* Bạn có laser Laser Animation Sollinger tích hợp bộ điều khiển AVB (hiện chỉ đang thử nghiệm trên macOS)

{% hint style="info" %}
**Bộ điều khiển laser là gì?**

Bộ điều khiển laser (hay DAC) là một thiết bị phần cứng có thể nhận dữ liệu số từ Liberation và chuyển đổi thành tín hiệu tương tự cần thiết để điều khiển scanner và đầu ra của laser. (Vì vậy mới gọi là DAC: Digital to Analog Converter - bộ chuyển đổi số sang tương tự.)

Bộ điều khiển kết nối với máy tính qua USB hoặc qua mạng máy tính tiêu chuẩn; nó có thể là thiết bị rời bên ngoài, hoặc được lắp bên trong laser.

Nếu là thiết bị rời, bạn kết nối nó với laser qua cổng ILDA. ILDA là một tiêu chuẩn trong ngành, sử dụng đầu nối 'D' 25 chân kiểu cũ. Hãy chuẩn bị một cáp ILDA, cắm một đầu vào bộ điều khiển và đầu còn lại vào laser.
{% endhint %}

<figure><img src="../.gitbook/assets/etherdream-ilda.png" alt="" width="375"><figcaption><p>Đầu ra ILDA trên một Ether Dream rời</p></figcaption></figure>

<figure><img src="../.gitbook/assets/opt-laser-rear.jpg" alt="" width="317"><figcaption><p>Mặt sau của laser, hiển thị các cổng kết nối khác nhau, bao gồm đầu vào ILDA</p></figcaption></figure>

<figure><img src="../.gitbook/assets/ilda-cable.jpg" alt="" width="375"><figcaption><p>Một cáp ILDA tiêu chuẩn</p></figcaption></figure>

### Bộ điều khiển nào phù hợp nhất với tôi?

Nếu bạn là người dùng tại nhà, hoặc chạy các show nhỏ với 4 laser trở xuống và các laser ở gần máy tính, thì bộ điều khiển USB như **Helios DAC** là lựa chọn **tiết kiệm nhất**.

DAC dùng mạng như **Ether Dream** là **lựa chọn tốt nhất cho chuyên viên laser chuyên nghiệp** nếu bạn sẵn sàng thiết lập mạng và muốn vận hành số lượng lớn laser; cho đến nay, tất cả các show Liberation quy mô lớn đều chạy bằng Ether Dream.

Nếu bạn có **LaserCube** thì hoàn toàn không cần bộ điều khiển laser riêng - Liberation tương thích với mọi LaserCube. Các mẫu đời đầu kết nối bằng cáp USB, còn các mẫu mới hơn kết nối qua mạng.

Nếu bạn là người dùng chuyên nghiệp và muốn lựa chọn dễ triển khai nhất, hãy cân nhắc thiết bị X-Laser tích hợp Mercury hoặc laser Laser Animation Sollinger dùng AVB.

### Bộ điều khiển laser tương thích

#### Ether Dream (Mạng)

[Ether Dream](https://ether-dream.com) đã có mặt hơn mười năm và hiện ở phiên bản 4 (dù Liberation cũng hoạt động với Ether Dream phiên bản 1, 2 và 3). Chúng cực kỳ đáng tin cậy.

Bạn kết nối với chúng qua mạng tiêu chuẩn. Có thể mua dưới dạng thiết bị độc lập, hoặc tốt hơn nữa là lắp sẵn bên trong laser.

#### Helios (USB)

[Helios](https://bitlasers.com/helios-laser-dac/) là lựa chọn tốt nhất cho người mới bắt đầu và rẻ hơn Ether Dream, nhưng vì kết nối qua USB nên không khuyến nghị dùng với đường cáp dài. Ngoài ra, bạn có thể gặp vấn đề về dữ liệu USB và driver khi kết nối nhiều hơn 4 thiết bị (đặc biệt trên Windows).

Nhưng nếu bạn chỉ muốn chạy vài laser tại nhà, đây là lựa chọn rẻ nhất và đơn giản nhất.

#### Mercury (Tích hợp trong thiết bị X-Laser)

[**Mercury**](https://x-laser.com/pages/mercury-laser-control-system) là hệ thống điều khiển laser DMX mạnh mẽ của X-Laser, được thiết kế cho các nhà thiết kế ánh sáng muốn chạy laser trực tiếp từ bàn điều khiển ánh sáng truyền thống. Với bản cập nhật firmware mới nhất, Mercury cũng có **mô phỏng Ether Dream**, nghĩa là giờ đây nó hoạt động liền mạch với Liberation - cũng như mọi phần mềm khác hỗ trợ Ether Dream.

#### AVB (Tích hợp trong thiết bị Laser Animation Sollinger)

**AVB** là một giao thức mở dựa trên mạng dành cho truyền phát âm thanh và dữ liệu hiệu năng cao, độ trễ thấp. Nhiều máy chiếu LaserAnimation Sollinger có hỗ trợ AVB trực tiếp trong phần cứng, cho phép Liberation kết nối với chúng qua mạng mà không cần DAC rời. Hỗ trợ AVB trong Liberation hiện **chỉ có trên macOS và đang trong giai đoạn thử nghiệm**, đồng thời yêu cầu **thiết bị mạng tương thích có hỗ trợ AVB**. Khi được thiết lập đúng cách, AVB mang lại quy trình làm việc đơn giản hơn, ít thiết bị rời hơn và độ tin cậy cao cho các show chuyên nghiệp.

#### Các bộ điều khiển sẽ được hỗ trợ trong tương lai:

* [IDN](http://www.ilda-digital.com) (một giao thức mạng mở của ILDA, có thể được bất kỳ nhà sản xuất nào triển khai)

### Gợi ý đi cáp

Để đạt hiệu năng tối ưu, hãy đặt DAC USB gần máy tính và kết nối chúng tới laser bằng cáp ILDA dài hơn. (Tuy nhiên hãy cẩn thận, vì cáp ILDA có thể trở thành “móc kéo” khi tháo dỡ hệ thống!)

Nếu dùng Ether Dream, bạn vẫn có thể đặt tất cả chúng cùng một chỗ và kết nối tới laser bằng cáp ILDA dài, hoặc treo/lắp chúng gần laser và dùng cáp mạng dài hơn.

Cách thiết lập lý tưởng là lắp Ether Dream (hoặc các bộ điều khiển khác) trực tiếp bên trong laser của bạn (Rob tại Stanwax Laser có thể làm việc này cho bạn ở Vương quốc Anh).
