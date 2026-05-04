---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/getting-started
---

# ✅ Hướng dẫn bắt đầu nhanh

## Giới thiệu

Chào mừng bạn đến với **Liberation** - thế hệ phần mềm laser show tiếp theo.

Liberation là một phần mềm hiện đại mạnh mẽ và phức tạp; được xây dựng trên các nền tảng về tính dễ dùng và độ tin cậy để bạn tự do thể hiện sáng tạo. Phần mềm nhanh, hiệu quả và liền mạch; hãy làm theo _Hướng dẫn bắt đầu nhanh_ này để sẵn sàng sử dụng chỉ trong thời gian ngắn!

### Quản lý laser

Liberation đủ linh hoạt để bạn có thể thiết lập và mô phỏng laser mà không cần kết nối laser thật. Sau đó, khi đã sẵn sàng, bạn có thể gán liền mạch từng Output cho một bộ điều khiển laser.

{% hint style="info" %}
Bạn có thể thiết lập và mô phỏng bao nhiêu laser tùy ý trong Liberation; các cấp giấy phép (Hobbyist, Pro, v.v.) chỉ giới hạn số laser bạn có thể _kích hoạt._ Điều này có nghĩa là bạn có thể thiết kế laser show với 100 laser ngay cả khi dùng giấy phép miễn phí. Bạn chỉ cần nâng cấp khi thực sự chạy show trên laser thật.
{% endhint %}

Mặc định có 8 laser được trải theo chiều ngang, nhưng bạn có thể tùy chỉnh theo ý muốn. Có lẽ tốt nhất là giữ mặc định này trong khi bạn làm quen với phần mềm, sau đó điều chỉnh để khớp với hệ thống phần cứng của mình. (Xem [Thiết lập dự án của bạn](setting-up/setting-up-your-project.md "mention"))

{% hint style="warning" %}
Quan trọng: Trước khi kích hoạt bất kỳ laser nào, hãy chắc chắn rằng bạn hiểu các rủi ro liên quan và đọc kỹ chương [Thiết lập laser](setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Tổng quan về phần mềm

### Ngắt an toàn

Bất cứ khi nào chạy laser, bạn phải có sẵn **nút dừng khẩn cấp phần cứng** trong tầm tay (xem [Dừng khẩn cấp và khóa liên động](hardware/emergency-stop-interlocks.md "mention")), nhưng nếu bạn muốn tắt kích hoạt toàn bộ hệ thống trong tình huống ít khẩn cấp hơn, bạn có thể dùng nút _**DISARM ALL**_, hoặc phím `Escape` (hoặc phím _**SESSION**_ trên APC40). Bạn cũng có thể giảm Global Brightness bằng thanh trượt trên màn hình hoặc fader chính trên APC40.

### Thành phần thanh trượt

Trong Liberation có nhiều thanh trượt và bộ điều khiển khác nhau.

{% hint style="info" %}
`Cmd / Ctrl`-click vào thanh trượt để nhập giá trị mới nếu bạn cần điều khiển chính xác hơn mức thanh trượt cho phép.
{% endhint %}

### Phím tắt

Danh sách đầy đủ các phím tắt có tại đây: [Phím tắt](reference/keyboard-shortcuts.md "mention")

### Bố cục màn hình

<figure><img src=".gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Không chắc một nút nào đó dùng để làm gì? Di chuột lên nút đó để xem mô tả!
{% endhint %}

#### Menu

<figure><img src=".gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menu là nơi bạn tìm thấy tất cả tùy chọn nhập / xuất file và mở các panel. Bạn cũng sẽ tìm thấy tùy chọn ủy quyền máy tính với gói đăng ký của mình tại đây (trong _Liberation -> Authorise/Deauthorise this computer_).

#### Thanh biểu tượng

<figure><img src=".gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Các tác vụ thường dùng nằm ở đây, chẳng hạn như kích hoạt/tắt kích hoạt tất cả laser, Global Brightness, Test Pattern, và chuyển đổi giữa các view 3D, Canvas và Output.

### View

Khu vực lớn ở góc trên bên trái màn hình có thể là một trong 3 view chính: **3D**, **CANVAS** và **OUTPUT.** Chuyển đổi giữa chúng bằng các nút trên thanh biểu tượng (hoặc dùng phím `Tab` để chuyển giữa 3D view và OUTPUT view, rồi tiếp tục nhấn tab để lần lượt duyệt qua từng Output của laser).

<figure><img src=".gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src=".gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view cho bạn thấy laser sẽ trông như thế nào và có thể được cấu hình để khớp với thiết lập laser của riêng bạn. Click và kéo để xoay camera, dùng con lăn chuột để di chuyển tiến/lùi. Bạn có thể tìm thấy nhiều tùy chọn khác trong panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Xem [Trình hiển thị 3D](setting-up/3d-visualiser.md "mention").

#### Output view

<figure><img src=".gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view được dùng để cấu hình zone và mask cho từng laser. (Hãy chú ý con số rất lớn ở góc trên bên trái để bạn dễ biết mình đang thao tác trên laser nào!)

View này biểu diễn toàn bộ Output của laser này, cũng như vị trí của từng zone bên trong đó. Theo mặc định chỉ có một zone cho mỗi laser, nhưng bạn có thể thêm bao nhiêu zone tùy mức hợp lý trong thực tế, và bạn sẽ thấy tất cả chúng trong view này.

{% hint style="info" %}
**Zone là gì?**

Zone là một không gian trong Output của laser mà bạn có thể đưa nội dung laser vào. Mỗi laser có thể có nhiều hơn một zone. Loại zone đơn giản nhất là _beam zone_, nhưng cũng có _canvas zone_ và _DMX zone_. Trong hướng dẫn này, chúng ta chủ yếu tập trung vào beam zone, thường được dùng để tạo hiệu ứng chùm tia trong không khí.
{% endhint %}

Bạn có thể chọn laser muốn chỉnh sửa bằng một trong các cách sau:

* các nút đánh số trên thanh ở phía trên
* nhấn phím số tương ứng với laser bạn muốn (_các phím 1-9_)
* phím `Tab` để lần lượt chuyển từ laser này sang laser tiếp theo

Thêm laser mới vào thiết lập bằng cách nhấn nút _+_. (Cũng có một nút _ADD LASER_ trong panel _Laser Overview_)

Xóa một laser khỏi thiết lập bằng cách nhấn nút ⊖ màu đỏ trong panel _Laser Overview_.

Bạn có thể phóng to/thu nhỏ bằng con lăn chuột, và click-kéo ở bất kỳ khu vực nào không có zone để di chuyển view.

Click vào một zone để chọn, sau đó dùng chuột điều chỉnh các điểm góc của nó. Giữ phím `Alt / Option` trong khi kéo một góc để điều chỉnh không đồng đều. Right-click vào zone để xem thêm tùy chọn, bao gồm cả đổi loại zone.

Dọc bên trái là một thanh với nhiều nút biểu tượng; di chuột lên bất kỳ nút nào để xem mô tả chức năng. Các nút ở đây cho phép bạn thêm beam zone, canvas zone và mask. Cũng có các tùy chọn để đặt Test Pattern chỉ cho laser này, cùng với thiết lập lưới và snapping.

Để biết thêm chi tiết, xem [Output view](output-view/ "mention").

#### Canvas

Hệ thống Canvas chủ yếu được dùng cho đồ họa và mapping kiến trúc. Bạn có thể phân phối hình ảnh phức tạp qua nhiều laser và hiệu chỉnh phối cảnh cho từng phần. Xem [Đồ họa và hệ thống Canvas](graphics-and-the-canvas-system/ "mention").

### Bộ điều khiển MIDI APC40

<figure><img src=".gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Mặc dù có thể điều khiển Liberation bằng chuột và bàn phím, tốt hơn nhiều là dùng giao diện điều khiển MIDI APC40 (Mark 2 là tốt nhất, nhưng Mark 1 cũng hoạt động).

Xem thêm: [Tham khảo APC40](reference/apc40-reference.md "mention")

Liberation cũng hỗ trợ APC Mini và MIDI Fighter Twister. APC40 Mark 2 vẫn là lựa chọn tốt nhất trong hầu hết trường hợp.

### Clip và hiệu ứng

{% hint style="info" %}
**Clip là gì?**

Clip là một vùng chứa cho mọi nội dung laser trong Liberation. Clip có thể chứa beam hoặc hoạt ảnh đồ họa và thường là một vòng lặp. Clip có thể được đưa vào bất kỳ zone nào (hoặc _Canvas target area_) và được kích hoạt bằng các nút Clip trong Clip Deck.
{% endhint %}

#### Tổng quan Clip Deck

<figure><img src=".gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Lưới này được gọi là _Clip Deck_ và là nơi lưu tất cả Clip laser. Nó được thiết kế để ánh xạ trực tiếp với lưới nút 8 x 5 trên APC40 của bạn.

**Điều hướng Clip Deck.**

Bạn có thể cuộn Clip Deck sang trái và phải bằng:

* Phím mũi tên trái và phải. Thêm `Cmd / Ctrl` để cuộn mỗi lần một trang đầy đủ.
* Trackpad: Vuốt
* Chuột: nếu chuột của bạn có cuộn ngang, bạn có thể dùng khi con trỏ đang nằm trên Clip Deck
* Núm cuộn APC40
* Các nút APC40 _<- DEVICE ->_

Để giúp bạn định hướng, có một trình hiển thị mini của Clip Deck dọc phía trên. Xem thêm [Clips và Clip Deck](clips/ "mention")

#### Bắt đầu và dừng Clip

Nhấn một nút Clip (bằng chuột hoặc bằng APC40) để bắt đầu Clip. Nhấn lại để dừng. Khi bạn bắt đầu một Clip, tất cả Clip khác cùng màu sẽ tự động dừng, trừ khi bạn giữ _shift_.

Một số Clip sẽ ở _Flash mode_ (mặc định là các Clip màu đỏ); trong trường hợp này, chúng sẽ dừng ngay khi bạn nhả nút Clip.

Nút _STOP_ dừng tất cả Clip đang chạy.

#### Đặt zone đầu ra cho Clip

Bên dưới các nút Clip, bạn sẽ thấy các nút zone, mặc định là beam zone 1 đến 8 (_BEAM 1_, _BEAM 2_, v.v.). Các nút zone sáng lên để cho biết zone nào đang được gán cho Clip hiện được chọn.

<figure><img src=".gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Hai hàng bên dưới các nút zone, bạn sẽ thấy các nút lật X/Y; bật/tắt các nút này để lật Clip theo chiều ngang và chiều dọc.

{% hint style="info" %}
Lưu ý rằng các phân bổ zone và thiết lập lật X/Y này được gắn với chính Clip; chúng sẽ được giữ lại lần sau bạn chạy Clip đó. Đây không phải là thiết lập toàn cục.
{% endhint %}

Right-click vào một Clip để chỉnh thêm các thiết lập của Clip. Xem thêm [Cài đặt Clip](clips/clip-settings.md "mention")

### Nhóm

Bạn sẽ thấy mỗi Clip có một viền màu, và màu này biểu thị Clip thuộc _nhóm_ nào. Các nút Clip trên APC40 cũng sáng theo màu này.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Nhóm 1</td><td>Xanh cyan</td></tr><tr><td>Nhóm 2</td><td>Cam</td></tr><tr><td>Nhóm 3</td><td>Đỏ</td></tr><tr><td>Nhóm 4</td><td>Chàm</td></tr><tr><td>Nhóm 5</td><td>Xanh lá</td></tr></tbody></table>

Hệ thống nhóm rất linh hoạt và cho phép bạn:

* Giữ các Clip trong một nhóm tiếp tục chạy, trong khi bạn bật/tắt các nhóm ở nhóm khác
* Gán nhanh zone và lật X/Y cho tất cả Clip trong một nhóm
* Đặt _Flash mode_ cho một Clip (Nhóm 3 được đặt _Flash mode_ theo mặc định)

Các nhóm cũng có thiết lập chuyển tiếp vào/ra mà các Clip trong nhóm có thể kế thừa, hoặc ghi đè.

Bạn có thể gán nhóm cho Clip bằng các nút trong menu right-click, hoặc dùng APC40: nhấn nút nhóm và _trong khi vẫn giữ nút đó,_ nhấn các nút Clip.

Thay đổi thiết lập zone cho tất cả Clip trong một nhóm

Khi dùng APC40, nhấn nút nhóm, rồi _trong khi vẫn giữ nút đó,_ dùng các nút zone và X/Y để bật/tắt thiết lập zone cho tất cả Clip trong nhóm đó.

Xem thêm [Nhóm](clips/groups.md "mention")

### Hiệu ứng

Hệ thống hiệu ứng trong Liberation là một cách mạnh mẽ và linh hoạt để thay đổi Output của Clip theo thời gian thực. Các nút hiệu ứng mặc định 1-8 nằm bên dưới các nút zone.

#### Áp dụng hiệu ứng

Nhấn một nút hiệu ứng để bật/tắt hiệu ứng, hoặc tốt hơn nữa là dùng các slider 1-8 trên APC40 để fade hiệu ứng vào/ra.

#### Tham số hiệu ứng

Dùng các rotary controller 1-8\* để điều chỉnh _tham số_ cho từng hiệu ứng. (Hoặc bạn có thể right-click bằng chuột để điều chỉnh mức và tham số). Việc thay đổi tham số sẽ tạo ra các tác động khác nhau tùy cách hiệu ứng được thiết lập. Xem danh sách bên dưới để biết các hiệu ứng mặc định.

{% hint style="info" %}
Các con số nhỏ bạn thấy trên nút hiệu ứng thể hiện _level_ và _parameter_ của hiệu ứng. _Level_ được điều khiển bằng fader trên APC40, hoặc bạn có thể click và kéo trên nút. Tham số được điều chỉnh bằng các núm xoay trên APC40, hoặc bạn có thể right-click để điều chỉnh bằng chuột.
{% endhint %}

_\*Rotary controller 1-8 nằm dọc phía trên APC40 Mk2 và ở góc trên bên phải trên Mk1. Xem thêm:_ [Tham khảo APC40](reference/apc40-reference.md "mention")

#### Các hiệu ứng mặc định

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Áp dụng chuyển động hỗn loạn cho Output của Clip. Tham số điều chỉnh lượng/tốc độ hỗn loạn.
2. **Sine wave** :\
   Uốn cong toàn bộ nội dung theo một sóng sin đang di chuyển. Tham số điều chỉnh bước sóng.
3. **Rotation** :\
   Xoay mọi thứ quanh tâm. Tham số điều chỉnh tốc độ xoay.
4. **Horizontal flip** :\
   Nén và kéo giãn mọi thứ theo chiều ngang. Tham số điều chỉnh tốc độ.
5. **Scale** :\
   Liên tục thu phóng mọi thứ từ đầy đủ về 0. Tham số điều chỉnh tốc độ.
6. **Hue** :\
Thay đổi sắc độ của mọi thứ, nhưng không thay đổi độ bão hòa (tức là phần nào màu trắng vẫn giữ màu trắng). Tham số điều chỉnh sắc độ.
7. **Saturation and hue** :\
Thay đổi sắc độ của mọi thứ và đồng thời bão hòa màu hoàn toàn (tức là phần nào màu trắng sẽ đổi sang màu đó). Tham số điều chỉnh sắc độ.
8. **Flash** :\
   Liên tục nhấp nháy độ sáng của mọi thứ từ đầy đủ về 0. Tham số điều chỉnh tốc độ nhấp nháy.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Có thêm 16 hiệu ứng màu ở hàng dưới để áp dụng các giá trị sắc độ và độ bão hòa đặt sẵn.

Lưu ý rằng đây là các hiệu ứng mặc định, nhưng bạn có thể chỉnh sửa để chúng làm gần như bất kỳ điều gì bạn muốn!

#### _"Clip hiện được chọn"_ là gì?

Khi bạn bắt đầu một Clip, Clip đó sáng lên để cho biết nó đang hoạt động. Nó cũng có viền trắng xung quanh, cho biết đây là Clip hiện đang _được chọn_. Bất cứ khi nào bạn bật/tắt các nút zone hoặc điều chỉnh thiết lập Clip, các thay đổi này sẽ được áp dụng cho _Clip hiện được chọn._

{% hint style="info" %}
Để chọn một Clip mà không kích hoạt nó, hãy nhấn phím `Alt / Option` trước khi nhấn nút Clip. Đây là cách tốt để điều chỉnh zone và các thiết lập khác mà không cần chạy Clip.
{% endhint %}

### Panel Clip Settings

Dùng panel _Clip Settings_ để chỉnh tỷ lệ, vị trí X/Y và truy cập hệ thống trễ zone mạnh mẽ.

<figure><img src=".gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

Tìm panel _Global Settings_ để điều chỉnh các thiết lập Output toàn cục ảnh hưởng đến toàn bộ Output trên tất cả zone.

<figure><img src=".gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Bật AUTO RESET để tự động đặt lại toàn bộ _Global settings_ mỗi khi không có Clip nào đang phát.

### Timing

Hầu hết mọi màn trình diễn laser đều có một dạng nhạc nền, vì vậy hệ thống timing trong Liberation được xây dựng quanh tempo tính bằng nhịp mỗi phút. Trong _Tempo Panel_, bạn có thể thấy biểu diễn thời gian; mỗi ô vuông biểu thị một phách và bạn có thể thấy chúng nhấp nháy theo nhịp.

<figure><img src=".gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Có nhiều tùy chọn đồng bộ, bao gồm MIDI clock và Ableton Link. Nếu bạn biết tempo của bản nhạc, bạn có thể điều chỉnh thủ công bằng thanh trượt trên màn hình hoặc núm Tempo trên APC40, nhưng bạn cũng có thể giữ đúng nhịp với nhạc bằng hệ thống _Tap Tempo_.

#### Tap Tempo

_Tap Tempo_ là thuật ngữ thường dùng trong các ứng dụng âm nhạc, cho phép bạn gõ theo nhịp để đặt tempo trong khi nhạc đang phát. Bạn có thể dùng nút trên màn hình, dù khuyến nghị là dùng phím _T_ hoặc nút _Tap Tempo_ trên APC40 (hoặc thậm chí công tắc chân nếu bạn thích).

Nhấn phím _R_ hoặc nút _Metronome_ (APC40) để đặt lại tempo về đầu ô nhịp.

Nhấn phím _Y_ hoặc xoay núm _Tempo_ (APC40) để làm tròn tempo thành số nguyên. Điều này có thể hữu ích với nhạc điện tử, vốn thường có số nhịp mỗi phút là số tròn.

### Sắp xếp Clip Deck

Để di chuyển một Clip trên Clip Deck, click và kéo Clip đó đến vị trí mới. Trong khi kéo, bạn có thể dùng các phím con trỏ (hoặc con lăn/nút cuộn trên APC40) để cuộn sang trái và phải.

Nhấn phím `Alt / Option` trong khi kéo để tạo bản sao.

`Alt / Option`-click một Clip để chọn mà không bắt đầu chạy Clip đó.

`Alt / Option + Shift`-click một Clip để chọn nhiều Clip, hoặc click và kéo bên ngoài Clip để chọn kiểu "lasso".

Click và kéo sẽ kéo TẤT CẢ Clip đang được chọn.

Để xóa một hoặc nhiều Clip, hãy kéo chúng ra khỏi Clip Deck (biểu tượng thùng rác sẽ xuất hiện) hoặc dùng nút DELETE trong menu right-click của Clip.

### Panel Laser Overview

<figure><img src=".gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ cho bạn cái nhìn nhanh về trạng thái của các laser đang chạy. Ô vuông màu xanh lá ở bên phải cho biết bộ điều khiển laser đang hoạt động ổn. Nếu nó chuyển sang màu cam, có một số lần mất kết nối ngắn; nếu màu đỏ, nó đã bị ngắt kết nối. Nếu màu xám, laser đó chưa được kết nối với bộ điều khiển nào.

Biểu đồ ở giữa là lịch sử độ dài frame, và con số bên phải là tốc độ khung hình hiện tại. Nội dung càng phức tạp thì tốc độ khung hình càng chậm (tức là dễ nhấp nháy hơn). Bất kỳ giá trị nào dưới khoảng 25fps sẽ bắt đầu trông hơi nhấp nháy.

### Kết nối với laser - Panel Controller Assignment

Click nút _Assign Laser Controllers_ để mở panel _Controller Assignment_. (Bạn cũng có thể truy cập panel này qua _View -> Controller Assignment_ trên thanh menu).

Tại đây, bạn có thể chọn Output laser nào đi tới bộ điều khiển laser nào. Kéo và thả các bộ điều khiển từ danh sách bên phải vào các ô bên trái. Bạn có thể đổi tên bộ điều khiển để khớp với laser đang ghép cặp với nó (dùng nút biểu tượng cây bút).

Đọc chương [Controller Assignment](setting-up/controller-assignment.md "mention") để biết thêm chi tiết.

{% hint style="danger" %}
Trước khi kích hoạt bất kỳ laser nào, hãy chắc chắn đọc chương [Thiết lập laser](setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panel Laser Settings

<figure><img src=".gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Panel này hiển thị các thiết lập cho _laser hiện được chọn_ (được biểu thị bằng con số ở phía trên). Thay đổi laser hiện được chọn bằng phím _tab_, nhấn phím số, click một số laser trong panel _Laser Overview_ hoặc trong _Output view._

* **Number button** kích hoạt và tắt kích hoạt laser; nếu nút màu đỏ thì laser đang được kích hoạt.
* **Brightness** điều chỉnh độ sáng laser độc lập với các laser khác (và được kết hợp với thiết lập _global brightness_ - tức là nếu cả hai đều ở 50%, laser của bạn sẽ ở mức 25%).
* **Test Pattern** bật một mẫu kiểm tra chỉ cho laser này (ghi đè thiết lập Test Pattern toàn cục)
* **Orientation** hiệu chỉnh cho các laser được lắp nghiêng hoặc lộn ngược.
* **Flip Horizontal and Flip Vertical** đảo ngược Output của laser. Hữu ích để hiệu chỉnh Output trên các laser được đấu dây không đồng nhất.
* **Copy Laser Settings** mở một panel cho phép bạn sao chép nhiều thiết lập khác nhau từ laser này sang các laser khác.

### Thiết lập scanner

Laser trình diễn hoạt động bằng cách di chuyển một chùm tia laser đơn cực nhanh và bật/tắt nó để vẽ hình trong không khí. Những gì bạn thấy là đường, hình dạng và hình ảnh thực ra là chùm tia đang quét theo các đường đi nhanh hơn khả năng mắt bạn theo kịp.

Luồng điểm là dữ liệu cho laser biết cần di chuyển tới đâu tiếp theo và khi nào chùm tia nên bật hoặc tắt. Trong Liberation, Clip được chuyển đổi thành luồng điểm này theo thời gian thực khi được gửi tới laser.

Liberation cho bạn quyền kiểm soát chi tiết cách luồng điểm này được tạo, cho phép cân bằng giữa độ mượt, độ sáng và hiệu năng cho từng laser.

{% hint style="info" %}
Nếu bạn đã quen với phần mềm laser cũ dựa trên các luồng điểm được tính toán trước, cách tiếp cận này ban đầu có thể hơi khác. Tuy nhiên, việc tạo điểm theo thời gian thực cho phép cùng một nội dung được tối ưu khác nhau cho từng laser. Điều này giúp làm việc dễ hơn với nhiều laser có tốc độ hoặc chất lượng scanner khác nhau, mà không cần nhân bản hoặc dựng lại nội dung. Nó cũng giữ cho file Clip rất nhỏ, đó là lý do toàn bộ Clip Deck mặc định của Liberation chỉ có dung lượng vài megabyte thay vì gigabyte.
{% endhint %}

Các thiết lập scanner cơ bản gồm:

* **Speed** là tốc độ scanner, tức là laser di chuyển nhanh đến mức nào để vẽ hình. Thiết lập này tương đương việc điều chỉnh point rate trong phần mềm laser truyền thống, nhưng trong Liberation bạn có thể thay đổi tốc độ di chuyển của laser _độc lập với point rate._ Thông thường bạn không cần điều chỉnh mục này.
* **Scanner sync** (đôi khi được gọi là _blank shift, trước đây là Colour Shift_) Scanner di chuyển laser rất nhanh, nhưng thường thì thay đổi độ sáng và màu sắc không đồng bộ với chuyển động. Điều này xuất hiện dưới dạng các "đuôi" sáng nhỏ nhấp nháy ở rìa của beam và đường. Dùng điều chỉnh này để đồng bộ chuyển động và màu sắc với nhau. Xem [Laser Settings](setting-up/laser-settings.md "mention")

Các thiết lập scanner nâng cao khác được trình bày trong chương [Nâng cao](advanced/ "mention").

### Zoning

Để xem hướng dẫn đầy đủ về thiết lập và zoning laser, xem: [Thiết lập laser](setting-up/setting-up-lasers.md "mention")
