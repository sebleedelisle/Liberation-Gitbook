---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/setting-up/laser-settings
---

# ✅ Bảng cài đặt đầu ra laser

Mở bảng cài đặt _Laser output_ bằng menu _View -> Laser Output Settings._

<figure><img src="../.gitbook/assets/Copy Laser Setting in Laser Output.png" alt="" width="326"><figcaption></figcaption></figure>

Bảng này sẽ hiển thị các cài đặt cho laser đang được chọn. Bạn có thể thay đổi laser đang chọn:

* bằng nút số của laser đó trong bảng _Laser Overview_
* bằng phím số trên bàn phím; các phím 1 đến 0 mở laser 1 - 10
* bằng phím `Tab` để chuyển lần lượt qua các laser (`Shift + Tab` chuyển ngược lại).

Ở đầu bảng này, bạn sẽ thấy:

* một nút số - bấm vào đây để bật/tắt trạng thái sẵn sàng phát của laser này. Nút có màu đỏ khi laser đang ở trạng thái sẵn sàng phát.
* một thanh trượt _Brightness_ chỉ dành cho laser này. Lưu ý rằng giá trị này được kết hợp với độ sáng tổng.
* công tắc _Test Pattern_ và bộ chọn mẫu. Các mục này cho phép bạn chọn một mẫu thử cụ thể chỉ cho laser này. (Các điều khiển này cũng được phản chiếu trên thanh công cụ của Output view).

### Hướng đầu ra / hiệu chỉnh lật gương

Các mục tiếp theo dùng để hiệu chỉnh cách thiết lập laser, để laser hoạt động nhất quán trong Liberation.

* **Flip horizontal / vertical** - các tùy chọn này cho phép bạn hiệu chỉnh đầu ra của laser

{% hint style="info" %}
Bạn thường không cần thay đổi các cài đặt lật ngang / lật dọc, trừ khi laser được đấu dây sai hoặc các nút lật X/Y ở mặt sau chưa được đặt đúng. Nếu bạn muốn lật đầu ra cho một Clip cụ thể, hãy thực hiện trực tiếp trên Clip đó.
{% endhint %}

* **Orientation** - nếu laser được treo nghiêng hoặc lộn ngược, bạn có thể hiệu chỉnh góc xoay bằng cài đặt này.
* **Fine position adjustments** - có thể dùng để hiệu chỉnh các dịch chuyển/xoay rất nhỏ. Tính năng này được thiết kế để bù trôi/lún vị trí nếu laser được để qua đêm hoặc trong thời gian dài.

{% hint style="info" %}
Lưu ý rằng các hiệu chỉnh hướng / lật gương không thay đổi gì trong 3D Visualiser. Chúng nên được dùng để hiệu chỉnh đầu ra của laser thực tế sao cho khớp với nội dung trong 3D Visualiser!
{% endhint %}

### Sao chép cài đặt laser

Xem [Sao chép cài đặt laser](laser-settings.md#copy-laser-settings "mention").

### Cài đặt scanner

<figure><img src="../.gitbook/assets/Laser output scanner settings.png" alt=""><figcaption></figcaption></figure>

#### **Speed**

Cài đặt tốc độ xác định scanner di chuyển nhanh đến mức nào.

{% hint style="danger" %}
Mặc dù các cài đặt mặc định khá thận trọng, bạn vẫn có thể làm hỏng scanner nếu điều khiển chúng chạy quá nhanh. Hãy cẩn thận, đặc biệt khi tăng tốc độ.
{% endhint %}

{% hint style="info" %}
Cài đặt tốc độ này không thay đổi tốc độ điểm; thay vào đó, nó điều chỉnh mức độ giãn cách giữa các điểm. Để biết thêm thông tin, xem [Cách Liberation tạo nội dung laser](../advanced/how-liberation-generates-laser-content.md "mention")
{% endhint %}

#### **Scanner sync (Colour shift / blank shift)**

Chùm tia đổi màu và bật/tắt khi scanner di chuyển nó xung quanh, và hai việc này thường không đồng bộ hoàn hảo với nhau. Điều chỉnh cài đặt này để đưa chúng về đúng nhịp.

{% hint style="info" %}
Cài đặt này đôi khi được gọi là _blank shift_, nhưng cá nhân tôi thích thuật ngữ _scanner sync_ hơn - chính xác hơn một chút, vì nó điều chỉnh thời điểm của tất cả các thay đổi màu so với chuyển động của scanner.
{% endhint %}

<div><figure><img src="../.gitbook/assets/Colour shift tails.jpeg" alt="" width="320"><figcaption><p>“Đuôi” laser - Colour shift chưa được đặt đúng</p></figcaption></figure> <figure><img src="../.gitbook/assets/Colour shift no tails.jpeg" alt="" width="320"><figcaption><p>Không còn “đuôi” laser! Colour shift đã tốt!</p></figcaption></figure></div>

Nếu bạn thấy các “đuôi” nhỏ trên đầu ra laser, nhiều khả năng scanner sync cần được điều chỉnh. Nếu các đuôi vẫn xuất hiện dù bạn chỉnh thế nào, có thể bạn đang điều khiển scanner/trình điều khiển laser nhanh hơn khả năng xử lý của chúng. Hãy thử giảm tốc độ scanner.

#### Preset scanner

Dùng mục này để chọn một cài đặt scanner được thiết kế sẵn. Tùy chọn mặc định thường là phù hợp, nên bạn không cần thay đổi cài đặt này trừ khi scanner của bạn đặc biệt kém (hoặc đặc biệt tốt). Nếu muốn tìm hiểu sâu hơn, xem [Preset scanner](../advanced/scanner-presets.md "mention")

#### Hiệu chuẩn màu

Bạn có thể dùng hệ thống này để hiệu chỉnh đường cong độ sáng và cân bằng trắng của laser. Xem [Hiệu chuẩn màu](../advanced/colour-calibration.md "mention")

#### Cài đặt nâng cao

Bạn không cần chỉnh các mục này, nhưng nếu muốn tìm hiểu, xem [Cài đặt laser nâng cao](../advanced/advanced-laser-settings.md "mention")
