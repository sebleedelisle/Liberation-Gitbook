---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/output-view/zones
---

# 🟩 Zones

Loại zone chính bạn sẽ dùng cho hầu hết dự án là _Beam zone_. Đây là zone được thiết kế cho các hiệu ứng tia sáng trong không khí. Loại zone còn lại là _Canvas zone_ (Xem [Đồ họa và hệ thống Canvas](../graphics-and-the-canvas-system/ "mention")).

{% hint style="danger" %}
**CẢNH BÁO - Hãy cực kỳ thận trọng khi di chuyển zones trong lúc máy laser đang chạy** và giảm độ sáng xuống mức thấp nhất có thể. Xem [Thiết lập laser](../setting-up/setting-up-lasers.md "mention") để biết hướng dẫn đầy đủ về cách kích hoạt và phân vùng laser an toàn
{% endhint %}

Bạn có thể nhấp và kéo zones bằng chuột. Bật một test pattern để xem zone đó sẽ đi tới đâu.

{% hint style="info" %}
Dùng các phím mũi tên để **dịch nhẹ** zone/điểm đang được chọn. Nhấn phím `Shift` để dịch theo bước lớn hơn.
{% endhint %}

{% hint style="info" %}
Mẹo hay: bạn có thể nhanh chóng sao chép thiết lập zone sang nhiều laser! Xem [Sao chép Laser Settings](../setting-up/copy-laser-settings.md "mention")
{% endhint %}

### Thêm beam zone mới

Nhấp nút _Add a new beam zone_ ở đầu thanh công cụ và một zone mới sẽ xuất hiện. Lưu ý rằng beam zones được sắp xếp theo thứ tự bạn thêm, nhưng bạn có thể sắp xếp lại chúng. Xem [Sắp xếp lại beam zones](re-ordering-beam-zones.md "mention")

### Thêm canvas zone hiện có

Nhấp vào nút _Add existing canvas zone_ và bạn sẽ thấy danh sách các canvas zones có sẵn; bạn có thể bật hoặc tắt chúng cho laser này. Xem [Đồ họa và hệ thống Canvas](../graphics-and-the-canvas-system/ "mention")

### Các kiểu hình dạng zone

Có 3 kiểu hình dạng zone:

* **Quad** - hình dạng zone chữ nhật mặc định, có thể đều (thẳng theo trục) hoặc bị biến dạng. Phù hợp nhất cho các zone hình chữ nhật lớn hơn hoặc canvas zones cần hiệu chỉnh phối cảnh.
* **Line/Curve** - Zone được xác định bằng 2 điểm trở lên và độ dày. Lý tưởng cho các zone mỏng hoặc để giới hạn trên ban công, cầu hoặc các hình dạng cong khác.
* **Segmented** - Zone có thể được chia nhỏ thành các quad nhỏ hơn. Lý tưởng cho mapping kiến trúc.

Nhấp chuột phải vào bất kỳ zone nào để mở cài đặt của zone đó. Từ menu nhấp chuột phải này, bạn có thể:

* Đổi tên zone (việc này hữu ích để nhận diện zone trong Clip Deck, đặc biệt khi bạn có nhiều zones!)
* Bật/tắt zone
* Khóa vị trí của zone
* Thay đổi kiểu hình dạng
* Đặt lại về vị trí mặc định
* Truy cập các cài đặt riêng cho từng kiểu hình dạng
* Xóa zone
* Thêm _Alt Zone_ (Xem [Hệ thống Alt Zone](alt-zone-system.md "mention"))

{% hint style="danger" %}
**CẢNH BÁO -** hãy rất cẩn thận khi thay đổi kiểu zone trong lúc laser đang hoạt động. Zone sẽ quay về vị trí / kích thước gần nhất của hình dạng đó, nên đầu ra có thể thay đổi đột ngột. Tốt nhất là tắt laser trước khi thay đổi kiểu zone.
{% endhint %}

### Hình dạng Quad zone

Bạn có thể di chuyển từng góc của quad bằng chuột. Nhấp `Alt / Option` vào một góc để di chuyển góc đó độc lập với các góc còn lại và làm biến dạng quad. Khi quad đã bị biến dạng, tất cả các góc có thể di chuyển tự do.

Bạn có thể loại bỏ biến dạng và đưa nó về lại hình chữ nhật thẳng theo trục bằng nút _REMOVE DISTORTION_ trong menu nhấp chuột phải.

#### Hiệu chỉnh phối cảnh

Tùy chọn này có thể được đặt bằng nút bật/tắt trong menu nhấp chuột phải và nó quyết định phương pháp biến dạng. Tốt nhất nên tắt tùy chọn này cho beam, nhưng nếu zone này đang chiếu đồ họa lên một mặt phẳng, hãy bật nó để đầu ra được hiệu chỉnh phối cảnh.

{% hint style="info" %}
Nếu _Perspective correction_ bị tắt, nội dung sẽ được biến dạng bằng _nội suy song tuyến_. Nói cách khác, nội dung được phân bố đều trên quad. Đó là lý do phương pháp này phù hợp nhất cho beams.

Khi bật hiệu chỉnh phối cảnh, nội dung được biến dạng bằng phép biến đổi phối cảnh để bù cho hiện tượng rút ngắn do góc nhìn. Vì vậy, nếu bạn đang chiếu đồ họa lên tường ở một góc xiên, bạn có thể dùng tùy chọn này để chỉnh lại đầu ra và sửa méo hình khi chiếu.
{% endhint %}

### Hình dạng Line / Curve zone

Hình dạng Line / Curve zone đã trở thành lựa chọn tôi thường dùng trong các show gần đây, và cũng có thể nói rằng đây nên là mặc định cho beam zones.

Thường thì zones của tôi phải rất mỏng để vừa với những khoảng hẹp khó xử lý tại địa điểm biểu diễn hoặc giữa các cửa sổ trên tòa nhà, và tôi nhận thấy việc chỉnh bốn góc của một quad khi chúng ở quá gần nhau có thể cực kỳ lắt léo. Vì vậy Line / Curve zone ra đời!

Với đường thẳng, bạn chỉ cần hai điểm, sau đó chỉnh _Zone thickness_ trong menu nhấp chuột phải. Đây là cách nhanh nhất để tạo zone đơn giản.

Nhấp `Alt / Option` vào đường để tạo thêm điểm. Các điểm này được tự động làm mượt để tạo hình dạng liền mạch, và bạn có thể chỉnh _Smooth level_ để làm phẳng các đoạn gãy.

Nhấp `Alt / Option` vào một điểm để xóa điểm đó.

Hoặc nếu bạn có kinh nghiệm với các ứng dụng đồ họa vector (Inkscape, Illustrator, v.v.), bạn có thể dùng tùy chọn _Manually adjust bezier curves_ để tinh chỉnh chính xác tất cả các điểm điều khiển.

### Hình dạng Segmented zone

Zone được chia nhỏ này cho phép bạn thực hiện các hiệu chỉnh cực kỳ chi tiết và hữu ích khi bạn mapping lên các hình dạng phức tạp. Bạn có thể thêm hoặc xóa các phần chia nhỏ bằng các nút + và - trong menu nhấp chuột phải.

### Cách chỉnh sửa một zone bị một zone khác che phủ hoàn toàn

Nhấp chuột phải vào zone nằm phía trên, rồi nhấp nút ổ khóa để khóa zone đó. Khi đó bạn sẽ có thể chỉnh sửa và điều chỉnh zone bên dưới.

<br>

{% hint style="info" %}
Sau khi bạn thêm Beam zone vào Output, zone đó sẽ có sẵn để thêm vào một Clip trong Clip Deck.
{% endhint %}
