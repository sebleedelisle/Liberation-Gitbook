---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/graphics-and-the-canvas-system/canvas-overview
---

# 🟩 Tổng quan về Canvas

Hệ thống Canvas của Liberation tương đối đơn giản, nhưng lúc đầu có thể hơi khó hiểu. Dưới đây là phần tổng quan về khái niệm để bạn bắt đầu.

{% hint style="info" %}
**Khoan đã, tôi có cần dùng hệ thống Canvas không?**

Có thể là không! Nếu bạn chỉ chiếu một hình đồ họa duy nhất lên một máy laser duy nhất, bạn có thể làm việc đó dễ dàng bằng beam zone (mặc dù theo mặc định nội dung beam zone bị lật ngang, vì vậy bạn sẽ cần X flip Clip).

Nhưng nếu bạn muốn phân bổ nội dung đồ họa trên nhiều máy laser, hoặc tách nội dung thành nhiều phần khác nhau để mapping lên kiến trúc, thì hệ thống Canvas sẽ đáp ứng việc đó!
{% endhint %}

### Canvas

Trước hết là chính Canvas. Đây là phần bạn thấy trong view _CANVAS_, đại diện cho một Canvas lớn, và bạn có thể vẽ nội dung ở bất kỳ đâu trong không gian này.

### Vùng đích Canvas

Các vùng này được hiển thị dưới dạng hình chữ nhật viền xanh dương trong Canvas view, và đây là các khu vực mà bạn có thể gửi nội dung tới. Bạn gửi nội dung của một Clip tới một vùng đích Canvas, giống như cách bạn gửi một Clip tới beam zone. Bạn sẽ thấy các nút vùng đích Canvas ở bên phải các nút beam zone trong Clip Deck.

{% hint style="info" %}
Nếu bạn không thấy các nút Canvas trong Clip Deck, hãy thử cuộn các nút beam zone bằng `Shift + Left / Right Arrow`. Bạn sẽ thấy một nút cho mỗi vùng đích Canvas, được gắn nhãn _CANVAS 1, CANVAS 2_, v.v.
{% endhint %}

### Canvas zones

Canvas zones là các khu vực trong Canvas mà bạn chọn để gửi tới một máy laser. Chúng được biểu diễn dưới dạng hình chữ nhật viền hồng trong Canvas view. Bạn có thể nhấp chuột phải vào từng zone và chọn các máy laser mà bạn muốn gán zone đó vào. Nếu bây giờ bạn chuyển sang view _OUTPUT_ của máy laser đó, bạn sẽ thấy một zone mới đã xuất hiện.

{% hint style="danger" %}
CẢNH BÁO - nếu máy laser đang ở trạng thái armed, bạn có thể đột ngột bắt đầu chiếu nội dung trong một canvas zone mặc định. Tốt nhất là disarm máy laser trước khi gán canvas zones cho nó.
{% endhint %}

{% hint style="info" %}
Bạn cũng có thể gán một canvas zone cho máy laser bằng cách nhấp nút _add canvas zone_ trong view _OUTPUT_. Xem [Zones](../output-view/zones.md "mention").
{% endhint %}

### Ảnh tham chiếu

Bạn có thể thêm một ảnh tham chiếu vào Canvas và dùng ảnh này làm mẫu cho đồ họa của mình. Bạn nên điều chỉnh sắc độ màu trên ảnh tham chiếu (menu nhấp chuột phải) và làm ảnh tối xuống để dễ nhìn thấy nội dung của bạn phủ lên trên hơn.

{% hint style="info" %}
Với mapping kiến trúc, tôi thấy hữu ích khi tạo một hình ảnh “trải phẳng” của tòa nhà, trong đó tất cả các bề mặt của tòa nhà được biểu diễn dưới dạng một ảnh phẳng không bị méo. Việc hiệu chỉnh phối cảnh cho các phần khác nhau có thể được thực hiện bằng canvas zone trong view _OUTPUT_.
{% endhint %}

<figure><img src="../.gitbook/assets/SaltwellHallFlat2.jpg" alt=""><figcaption><p>Một ảnh tham chiếu “làm phẳng” cho Saltwell Hall ở Gateshead, Vương quốc Anh</p></figcaption></figure>

<figure><img src="../.gitbook/assets/SaltwellHallZones.png" alt=""><figcaption><p>Các canvas zones trong một phiên bản Liberation còn rất sơ khai (khoảng 2017!) Lưu ý rằng các hình chữ nhật màu hồng chọn phần nào của Canvas sẽ được hiển thị, còn các Output views bên dưới cho biết các zone đó sẽ đi tới phần nào của từng máy laser.</p></figcaption></figure>

### Canvas trong trình hiển thị 3D

Việc tái tạo hệ thống chiếu nhiều máy laser phức tạp của bạn trong trình hiển thị 3D có lẽ sẽ khá lắt léo (nói nhẹ là vậy)! Vì thế, thay vào đó, bạn có tùy chọn đặt Canvas của mình trong không gian 3D. Bật checkbox _Show canvas_ trong panel _3D visualiser settings_. (Bất kỳ ảnh tham chiếu nào bạn có trong Canvas cũng sẽ xuất hiện trong trình hiển thị.)

{% hint style="info" %}
Lưu ý rằng trình hiển thị vẫn sẽ hiển thị các phép chiếu Canvas dưới dạng hiệu ứng khí quyển phát ra từ các máy laser. Bạn có thể chỉ cần di chuyển chúng ra khỏi khung nhìn, hoặc nếu muốn làm kỹ hơn, bạn có thể căn chúng thẳng hàng với Canvas!
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 2025-01-17 at 10.36.49.png" alt=""><figcaption><p>Sẽ rất thỏa mãn khi bạn căn thẳng các chùm tia từ máy laser với hình ảnh Canvas trong trình hiển thị 3D!</p></figcaption></figure>
