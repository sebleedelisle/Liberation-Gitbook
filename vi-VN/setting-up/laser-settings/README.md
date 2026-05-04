# ✅ Bảng cài đặt đầu ra laser

Mở bảng cài đặt _Laser output_ bằng menu _View -> Laser Output Settings._

<figure><img src="../../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Bảng này hiển thị các cài đặt của laser đang được chọn. Bạn có thể đổi laser đang chọn bằng cách:

* dùng nút số tương ứng trong bảng _Laser Overview_
* dùng phím số trên bàn phím; các phím 1 đến 0 mở laser 1 - 10
* dùng phím `Tab` để chuyển lần lượt qua các laser (`Shift + Tab` để chuyển ngược lại).

Ở đầu bảng này, bạn sẽ thấy:

* một nút số - bấm vào nút này để bật/tắt trạng thái sẵn sàng phát của laser này. Nút có màu đỏ khi laser đang ở trạng thái sẵn sàng phát.
* thanh trượt _Brightness_ chỉ dành cho laser này. Lưu ý rằng mức này được kết hợp với độ sáng tổng thể.
* công tắc _Test Pattern_ và bộ chọn mẫu. Các mục này cho phép bạn chọn một mẫu test riêng cho laser này. (Các điều khiển này cũng được phản chiếu trên thanh công cụ của Output view).

### Hướng đầu ra / hiệu chỉnh lật gương

Các mục tiếp theo dùng để hiệu chỉnh cách thiết lập laser để laser hoạt động nhất quán trong Liberation.

* **Flip horizontal / vertical** - các tùy chọn này cho phép bạn hiệu chỉnh đầu ra của laser

{% hint style="info" %}
Bạn không cần thay đổi cài đặt lật ngang/dọc, trừ khi laser bị đấu dây sai hoặc các nút lật X/Y ở mặt sau chưa được đặt đúng. Nếu muốn lật đầu ra cho một Clip cụ thể, bạn có thể thực hiện ngay trên Clip đó.
{% endhint %}

* **Orientation** - nếu laser được treo nghiêng hoặc lắp ngược, bạn có thể hiệu chỉnh góc xoay bằng cài đặt này.
* **Fine position adjustments** - có thể dùng để hiệu chỉnh các sai lệch dịch chuyển/xoay rất nhỏ. Mục này được thiết kế để bù trôi/ổn định vị trí nếu laser được để qua đêm hoặc trong thời gian dài.

{% hint style="info" %}
Lưu ý rằng các hiệu chỉnh hướng/lật gương không thay đổi bất kỳ điều gì trong 3D Visualiser; chúng nên được dùng để hiệu chỉnh đầu ra của laser thật sao cho khớp với nội dung trong 3D Visualiser!
{% endhint %}

### Sao chép cài đặt laser

Xem [Bảng cài đặt đầu ra laser](./#copy-laser-settings "mention").

### Cài đặt scanner

<figure><img src="../../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Cài đặt tốc độ xác định scanner di chuyển nhanh đến mức nào.

{% hint style="danger" %}
Mặc dù các cài đặt mặc định khá thận trọng, bạn vẫn có thể làm hỏng scanner nếu điều khiển chúng chạy quá nhanh. Hãy cẩn thận, đặc biệt khi tăng tốc độ.
{% endhint %}

{% hint style="info" %}
Cài đặt tốc độ này không thay đổi point rate; thay vào đó, nó điều chỉnh mức độ giãn cách giữa các điểm. Để biết thêm thông tin, xem [cách Liberation tạo nội dung laser](../../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Đồng bộ scanner (lệch màu / lệch blanking)**

Chùm tia đổi màu và bật/tắt khi scanner di chuyển nó, và hai việc này thường không hoàn toàn đồng bộ với nhau. Điều chỉnh cài đặt này để đưa chúng khớp lại.

{% hint style="info" %}
Mục này đôi khi được gọi là _blank shift_, nhưng cá nhân tôi thích thuật ngữ _scanner sync_ hơn - chính xác hơn một chút vì nó điều chỉnh thời điểm của tất cả thay đổi màu so với chuyển động của scanner.
{% endhint %}

<div><figure><img src="../../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>“Đuôi” laser - Colour shift chưa được đặt đúng</p></figcaption></figure> <figure><img src="../../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Không còn “đuôi” laser! Colour shift tốt!</p></figcaption></figure></div>

Nếu bạn thấy các “đuôi” nhỏ trên đầu ra laser, nhiều khả năng scanner sync cần được điều chỉnh. Nếu các đuôi vẫn xuất hiện dù bạn chỉnh thế nào, có thể bạn đang điều khiển scanner/driver laser nhanh hơn khả năng xử lý của chúng. Hãy thử giảm tốc độ scanner.

#### Preset scanner

Dùng mục này để chọn một cài đặt scanner được thiết kế sẵn. Tùy chọn mặc định thường là phù hợp, nên bạn không cần thay đổi cài đặt này trừ khi scanner của bạn đặc biệt kém (hoặc đặc biệt tốt). Nếu muốn tìm hiểu sâu hơn, xem [preset scanner](../../advanced/scanner-presets.md "mention")

#### Hiệu chuẩn màu

Bạn có thể dùng hệ thống này để hiệu chỉnh đường cong độ sáng và cân bằng trắng của laser. Xem [hiệu chuẩn màu](../../advanced/colour-calibration.md "mention")

#### Cài đặt nâng cao

Bạn không cần phải chỉnh các mục này, nhưng nếu tò mò, hãy xem [cài đặt laser nâng cao](../../advanced/advanced-laser-settings.md "mention")
