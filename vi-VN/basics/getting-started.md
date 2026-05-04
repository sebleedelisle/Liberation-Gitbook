# ✅ Hướng dẫn khởi động nhanh

## Giới thiệu

Chào mừng bạn đến với **Liberation** - thế hệ tiếp theo của phần mềm trình diễn laser.

Liberation là một phần mềm hiện đại mạnh mẽ và phức tạp; phần mềm được xây dựng trên các nền tảng về tính dễ sử dụng và độ tin cậy, giúp bạn tự do thể hiện ý tưởng sáng tạo. Liberation nhanh, hiệu quả và liền mạch; hãy làm theo _Hướng dẫn khởi động nhanh_ này để bắt đầu sử dụng trong thời gian ngắn!

### Quản lý laser

Liberation đủ linh hoạt để bạn có thể thiết lập và hình dung laser mà không cần kết nối bất kỳ laser thực tế nào. Sau đó, khi đã sẵn sàng, bạn có thể gán liền mạch từng đầu ra cho một bộ điều khiển laser.

{% hint style="info" %}
Bạn có thể thiết lập và hình dung bao nhiêu laser tùy ý trong Liberation; các gói giấy phép (Hobbyist, Pro, v.v.) chỉ giới hạn số lượng laser bạn có thể _kích hoạt đầu ra._ Điều này có nghĩa là bạn có thể thiết kế chương trình laser với 100 laser ngay cả khi dùng giấy phép miễn phí. Bạn chỉ cần nâng cấp khi thực sự chạy chương trình trên laser thật.
{% endhint %}

Mặc định có 8 laser được bố trí ngang, nhưng bạn có thể tùy chỉnh theo ý muốn. Có lẽ tốt nhất là giữ cấu hình mặc định này trong khi bạn làm quen với phần mềm, rồi sau đó điều chỉnh cho khớp với thiết lập phần cứng của bạn. (Xem [Thiết lập dự án của bạn](../setting-up/setting-up-your-project.md "mention"))&#x20;

{% hint style="warning" %}
Quan trọng: Trước khi kích hoạt đầu ra bất kỳ laser nào, hãy bảo đảm bạn hiểu các rủi ro liên quan và đọc kỹ chương [Thiết lập laser](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

## Tổng quan về phần mềm

### Ngắt an toàn

Bất cứ khi nào chạy laser, bạn phải có sẵn **nút dừng khẩn cấp phần cứng** (xem [Dừng khẩn cấp và khóa liên động](../hardware/emergency-stop-interlocks.md "mention")), nhưng nếu bạn muốn tắt toàn bộ đầu ra trong tình huống ít khẩn cấp hơn, bạn có thể dùng nút _**DISARM ALL**_, hoặc phím `Escape` (hoặc phím _**SESSION**_ trên APC40). Bạn cũng có thể giảm Global Brightness bằng thanh trượt trên màn hình hoặc fader chính trên APC40.

### Các thành phần thanh trượt

Trong Liberation có nhiều thanh trượt và điều khiển khác nhau.

{% hint style="info" %}
`Cmd / Ctrl`-click vào một thanh trượt để nhập giá trị mới nếu bạn cần điều khiển chính xác hơn mức thanh trượt có thể cung cấp.
{% endhint %}

### Phím tắt

Bạn có thể xem danh sách đầy đủ các phím tắt tại đây: [Phím tắt](../reference/keyboard-shortcuts.md "mention")

### Bố cục màn hình

<figure><img src="../.gitbook/assets/screen-layout.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Không chắc một nút nào đó dùng để làm gì? Hãy đưa chuột lên nút đó để xem mô tả!
{% endhint %}

#### Menu

<figure><img src="../.gitbook/assets/qs-menu-bar.png" alt="" width="359"><figcaption></figcaption></figure>

Menu là nơi bạn tìm thấy mọi tùy chọn nhập/xuất file và mở các panel. Bạn cũng sẽ tìm thấy tùy chọn ủy quyền máy tính với gói đăng ký của mình tại đây (trong _Liberation -> Authorise/Deauthorise this computer_).

#### Thanh biểu tượng

<figure><img src="../.gitbook/assets/icon-bar.png" alt=""><figcaption></figcaption></figure>

Các tác vụ thường dùng nằm ở đây, chẳng hạn như kích hoạt/tắt đầu ra của tất cả laser, Global Brightness, Test Pattern, và chuyển đổi giữa các chế độ xem 3D, Canvas và Output

### Chế độ xem

Khu vực lớn ở phía trên bên trái màn hình có thể là một trong 3 chế độ xem chính: **3D**, **CANVAS** và **OUTPUT.** Chuyển đổi giữa chúng bằng các nút trên thanh biểu tượng (hoặc dùng phím `Tab` để chuyển giữa 3D view và Output view, rồi tiếp tục nhấn tab để lần lượt đi qua từng đầu ra laser).

<figure><img src="../.gitbook/assets/qs-icon-bar-views.png" alt="" width="154"><figcaption></figcaption></figure>

#### 3D view

<figure><img src="../.gitbook/assets/qs-3d-view.png" alt=""><figcaption></figcaption></figure>

3D view cho bạn xem laser sẽ trông như thế nào và có thể được cấu hình để khớp với thiết lập laser của riêng bạn. Click và kéo để xoay camera, dùng bánh xe chuột để tiến/lùi. Bạn có thể tìm thấy nhiều tùy chọn khác trong panel _3D Visualiser settings_ (_View -> 3D Visualiser Settings_). Xem [Trình hiển thị 3D](../setting-up/3d-visualiser.md "mention").

#### Output view

<figure><img src="../.gitbook/assets/qs-view-output.png" alt=""><figcaption></figcaption></figure>

Output view được dùng để cấu hình zone và mask cho từng laser. (Hãy để ý con số rất lớn ở góc trên bên trái để bạn dễ dàng biết mình đang ở laser nào!)

Chế độ xem này biểu diễn toàn bộ đầu ra của laser này, và vị trí của từng zone bên trong đầu ra đó. Theo mặc định chỉ có một zone cho mỗi laser, nhưng bạn có thể thêm số lượng zone hợp lý theo nhu cầu, và bạn sẽ thấy tất cả chúng trong chế độ xem này.

{% hint style="info" %}
**Zone là gì?**

Zone là một vùng không gian trong đầu ra của laser mà bạn có thể đưa nội dung laser vào. Và bạn có thể có nhiều hơn một zone cho mỗi laser. Loại zone đơn giản nhất là _beam_ zone, nhưng cũng có _canvas_ zone và _DMX_ zone. Trong hướng dẫn này, chúng ta chủ yếu tập trung vào beam zone, thường được dùng để tạo hiệu ứng chùm tia trong không khí.
{% endhint %}

Bạn có thể chọn laser muốn chỉnh sửa bằng một trong các cách sau:

* các nút đánh số trên thanh ở phía trên
* nhấn phím số tương ứng với laser bạn muốn (_các phím 1-9_)
* dùng phím `Tab` để chuyển lần lượt từ laser này sang laser tiếp theo

Thêm laser mới vào thiết lập bằng cách nhấn nút _+_. (Cũng có nút _ADD LASER_ trong panel _Laser Overview_)

Xóa một laser khỏi thiết lập bằng cách nhấn nút ⊖ màu đỏ trong panel _Laser Overview_.

Bạn có thể phóng to/thu nhỏ bằng bánh xe cuộn chuột, và click rồi kéo ở bất kỳ chỗ nào không có zone để di chuyển chế độ xem.

Click vào một zone để chọn, sau đó điều chỉnh các điểm góc của nó bằng chuột. Giữ phím `Alt / Option` trong khi kéo một góc để chỉnh không đồng đều. Right-click vào zone để xem thêm tùy chọn, bao gồm thay đổi loại zone.

Dọc bên trái là một thanh với loạt nút biểu tượng; đưa chuột lên bất kỳ nút nào để xem mô tả chức năng. Các nút ở đây cho phép bạn thêm beam zone, canvas zone và mask. Cũng có các tùy chọn để đặt mẫu kiểm tra chỉ cho laser này, cùng với thiết lập lưới và snapping.

Để biết thêm chi tiết, xem [Output view](../output-view/ "mention").

#### Canvas

Hệ thống Canvas chủ yếu được dùng cho đồ họa và mapping kiến trúc. Bạn có thể phân phối hình ảnh phức tạp qua nhiều laser, và hiệu chỉnh phối cảnh cho từng phần. Xem [Đồ họa và hệ thống Canvas](../graphics-and-the-canvas-system/ "mention").

### Bộ điều khiển MIDI APC40

<figure><img src="../.gitbook/assets/qs-apc40.jpeg" alt=""><figcaption></figcaption></figure>

Mặc dù có thể điều khiển Liberation bằng chuột và bàn phím, sử dụng giao diện điều khiển MIDI APC40 sẽ tốt hơn nhiều (Mark 2 là lựa chọn tốt nhất, nhưng Mark 1 cũng hoạt động).

Xem thêm: [Tham khảo APC40](../reference/apc40-reference.md "mention")

Liberation cũng hỗ trợ APC Mini và MIDI Fighter Twister. APC40 Mark 2 vẫn là lựa chọn tốt nhất trong hầu hết trường hợp.&#x20;

### Clip và hiệu ứng

{% hint style="info" %}
**Clip là gì?**

Clip là vùng chứa cho mọi nội dung laser trong Liberation. Clip có thể chứa beam hoặc hoạt ảnh đồ họa, và thường là một chu kỳ lặp. Clip có thể được đưa vào bất kỳ zone nào (hoặc _vùng đích Canvas_) và được kích hoạt bằng các nút clip trong Clip Deck.
{% endhint %}

#### Tổng quan Clip Deck

<figure><img src="../.gitbook/assets/qs-clipdeck.png" alt=""><figcaption></figcaption></figure>

Lưới này được gọi là _Clip Deck_ và là nơi lưu trữ tất cả Clip laser. Nó được thiết kế để ánh xạ trực tiếp với lưới nút 8 x 5 trên APC40 của bạn.

**Di chuyển trong Clip Deck.**

Bạn có thể cuộn Clip Deck sang trái và phải bằng:

* Phím mũi tên trái và phải. Thêm `Cmd / Ctrl` để cuộn một trang đầy đủ mỗi lần.
* Trackpad: Vuốt
* Chuột: nếu chuột của bạn có cuộn ngang, bạn có thể dùng chức năng đó khi con trỏ đang ở trên Clip Deck
* Núm cuộn APC40
* Các nút APC40 _<- DEVICE ->_

Để giúp bạn định hướng, có một trình hiển thị thu nhỏ của Clip Deck dọc phía trên. Xem thêm [Clips và Clip Deck](../clips/ "mention")

#### Bắt đầu và dừng Clip

Nhấn một nút Clip (bằng chuột hoặc bằng APC40) để bắt đầu Clip. Nhấn lại để dừng Clip đó. Khi bạn bắt đầu một Clip, tất cả Clip khác cùng màu sẽ tự động dừng trừ khi bạn giữ _shift_.

Một số Clip sẽ ở _Flash mode_ (theo mặc định là các Clip màu đỏ), khi đó chúng sẽ dừng ngay khi bạn thả nút Clip.

Nút _STOP_ dừng tất cả Clip đang chạy.

#### Thiết lập output zone cho Clip

Bên dưới các nút Clip, bạn sẽ thấy các nút zone, mặc định là beam zone 1 đến 8 (_BEAM 1_, _BEAM 2_, v.v.). Các nút zone sáng lên để cho biết zone nào đang được gán cho Clip hiện đang được chọn.

<figure><img src="../.gitbook/assets/qs-zone-buttons.png" alt=""><figcaption></figcaption></figure>

Hai hàng bên dưới các nút zone, bạn sẽ thấy các nút lật X/Y; bật/tắt các nút này để lật Clip theo chiều ngang và chiều dọc.

{% hint style="info" %}
Lưu ý rằng các phân bổ zone và thiết lập lật X/Y này gắn với chính Clip; chúng được giữ lại vào lần tiếp theo bạn chạy Clip đó. Chúng không phải là thiết lập toàn cục.
{% endhint %}

Right-click vào một Clip để chỉnh sửa thêm thiết lập cho Clip đó. Xem thêm [Cài đặt Clip](../clips/clip-settings.md "mention")

### Nhóm

Bạn sẽ thấy mỗi Clip có một viền màu, và màu này cho biết Clip đó thuộc _group_ nào. Các nút Clip trên APC40 cũng sáng theo màu này.

<table data-header-hidden><thead><tr><th width="108"></th><th></th></tr></thead><tbody><tr><td>Group 1</td><td>Xanh cyan</td></tr><tr><td>Group 2</td><td>Cam</td></tr><tr><td>Group 3</td><td>Đỏ</td></tr><tr><td>Group 4</td><td>Chàm</td></tr><tr><td>Group 5</td><td>Xanh lá</td></tr></tbody></table>

Hệ thống group rất linh hoạt và cho phép bạn:

* Giữ các Clip trong một group tiếp tục chạy, trong khi bạn bật/tắt các group ở group khác
* Nhanh chóng gán zone và lật X/Y cho tất cả Clip trong một group
* Đặt _Flash mode_ cho một Clip (Group 3 được đặt ở _Flash mode_ theo mặc định)

Group cũng có các thiết lập chuyển vào/ra mà Clip của group đó có thể kế thừa, hoặc có thể được ghi đè.

Bạn có thể gán group của Clip bằng các nút trong menu right-click, hoặc dùng APC40: nhấn nút group và _trong khi vẫn giữ nút đó,_ nhấn các nút Clip.

Thay đổi thiết lập zone cho tất cả Clip trong một group

Khi dùng APC40, nhấn nút group, sau đó _trong khi vẫn giữ nút đó,_ dùng các nút zone và X/Y để bật/tắt thiết lập zone cho tất cả Clip trong group đó.

Xem thêm [Nhóm Clip](../clips/groups.md "mention")

### Hiệu ứng

Hệ thống hiệu ứng trong Liberation là một cách mạnh mẽ và linh hoạt để thay đổi đầu ra Clip theo thời gian thực. Các nút hiệu ứng mặc định 1-8 nằm bên dưới các nút zone.

#### Áp dụng hiệu ứng

Nhấn một nút hiệu ứng để bật/tắt hiệu ứng, hoặc tốt hơn nữa là dùng các thanh trượt APC40 1-8 để fade hiệu ứng vào và ra.

#### Tham số hiệu ứng

Dùng các bộ điều khiển xoay 1-8\* để điều chỉnh _parameter_ cho từng hiệu ứng. (Hoặc bạn có thể right-click bằng chuột để điều chỉnh level và parameter). Thay đổi parameter sẽ có tác dụng khác nhau tùy theo cách hiệu ứng được thiết lập. Xem danh sách bên dưới để biết các hiệu ứng mặc định.

{% hint style="info" %}
Các con số nhỏ bạn thấy trên nút hiệu ứng biểu thị _level_ và _parameter_ của hiệu ứng. _Level_ được điều khiển bằng fader trên APC40, hoặc bạn có thể click và kéo trên nút. Parameter được điều chỉnh bằng các núm xoay trên APC40, hoặc bạn có thể right-click để điều chỉnh bằng chuột.
{% endhint %}

_\*Các bộ điều khiển xoay 1-8 nằm dọc phía trên APC40 Mk2 và ở phía trên bên phải trên Mk1. Xem thêm:_ [Tham khảo APC40](../reference/apc40-reference.md "mention")

#### Các hiệu ứng mặc định

<figure><img src="../.gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Áp dụng chuyển động hỗn loạn cho đầu ra Clip. Parameter điều chỉnh mức độ/tốc độ hỗn loạn.
2. **Sine wave** :\
   Uốn cong toàn bộ nội dung theo một sóng sin chuyển động. Parameter điều chỉnh bước sóng.
3. **Rotation** :\
   Xoay mọi thứ. Parameter điều chỉnh tốc độ xoay.
4. **Horizontal flip** :\
   Nén và kéo giãn mọi thứ theo chiều ngang. Parameter điều chỉnh tốc độ.
5. **Scale** :\
   Liên tục scale mọi thứ từ tối đa về không. Parameter điều chỉnh tốc độ.
6. **Hue** :\
Thay đổi sắc độ của mọi thứ, nhưng không thay đổi độ bão hòa (tức là bất kỳ thứ gì màu trắng vẫn giữ màu trắng). Parameter điều chỉnh hue.
7. **Saturation and hue** :\
Thay đổi hue của mọi thứ và cũng bão hòa màu hoàn toàn (tức là bất kỳ thứ gì màu trắng sẽ đổi sang màu đó). Parameter điều chỉnh hue.
8. **Flash** :\
   Liên tục nhấp nháy độ sáng của mọi thứ từ tối đa về không. Parameter điều chỉnh tốc độ nhấp nháy.

<figure><img src="../.gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Ngoài ra còn có 16 hiệu ứng màu ở hàng dưới cùng để áp dụng các giá trị hue và saturation đặt sẵn.

Lưu ý rằng đây là các hiệu ứng mặc định, nhưng bạn có thể chỉnh sửa chúng để làm gần như bất cứ điều gì bạn muốn!

#### _"Clip hiện đang được chọn"_ là gì?

Khi bạn bắt đầu một Clip, Clip đó sẽ sáng lên để cho biết đang hoạt động. Nó cũng có viền trắng xung quanh, cho biết đây là Clip hiện đang được _chọn_. Mỗi khi bạn bật/tắt các nút zone hoặc điều chỉnh thiết lập Clip, các thay đổi này sẽ được áp dụng cho _Clip hiện đang được chọn._

{% hint style="info" %}
Để chọn một Clip mà không kích hoạt nó, hãy nhấn phím `Alt / Option` trước khi nhấn nút Clip. Đây là cách tốt để điều chỉnh zone và các thiết lập khác của Clip mà không chạy Clip đó.
{% endhint %}

### Panel Clip Settings

Dùng panel _Clip Settings_ để chỉnh sửa scale, vị trí X/Y và truy cập hệ thống trễ zone mạnh mẽ.

<figure><img src="../.gitbook/assets/qs-clip-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

### Panel Global Settings

Tìm panel _Global Settings_ để điều chỉnh các thiết lập đầu ra toàn cục ảnh hưởng đến toàn bộ đầu ra trên tất cả zone.

<figure><img src="../.gitbook/assets/qs-global-settings-panel.png" alt="" width="362"><figcaption></figcaption></figure>

Bật AUTO RESET để tự động đặt lại toàn bộ _Global settings_ mỗi khi không có Clip nào đang phát.&#x20;

### Timing

Hầu như mọi màn trình diễn laser đều có một dạng nhạc nền, vì vậy hệ thống timing trong Liberation được xây dựng quanh tempo tính bằng nhịp mỗi phút. Trong _Tempo Panel_, bạn có thể thấy phần biểu diễn thời gian; mỗi ô vuông đại diện cho một beat và bạn có thể thấy chúng nhấp nháy theo nhịp.

<figure><img src="../.gitbook/assets/qs-tempo-window.png" alt="" width="364"><figcaption></figcaption></figure>

Có nhiều tùy chọn đồng bộ hóa, bao gồm MIDI clock và Ableton Link. Nếu biết tempo của nhạc, bạn có thể điều chỉnh thủ công bằng thanh trượt trên màn hình hoặc núm Tempo trên APC40, nhưng bạn cũng có thể giữ nhịp với nhạc bằng hệ thống _Tap Tempo_.

#### Tap Tempo

_Tap Tempo_ là thuật ngữ thường dùng trong các ứng dụng âm nhạc, cho phép bạn gõ theo nhịp để đặt tempo trong khi nhạc đang phát. Bạn có thể dùng nút trên màn hình, nhưng nên dùng phím _T_ hoặc nút _Tap Tempo_ trên APC40 (hoặc thậm chí công tắc chân nếu bạn thích).

Nhấn phím _R_ hoặc nút _Metronome_ (APC40) để đặt lại tempo về đầu ô nhịp.

Nhấn phím _Y_ hoặc xoay núm _Tempo_ (APC40) để làm tròn tempo thành số nguyên. Điều này có thể hữu ích với nhạc điện tử, vốn thường có số beat mỗi phút là số tròn.

### Sắp xếp Clip Deck

Để di chuyển một Clip trên Clip Deck, click và kéo Clip đó đến vị trí mới. Trong khi kéo, bạn có thể dùng các phím mũi tên (hoặc bánh xe/nút cuộn trên APC40) để cuộn trái và phải.

Giữ phím `Alt / Option` trong khi kéo để tạo bản sao.

`Alt / Option`-click một Clip để chọn Clip đó mà không bắt đầu phát.

`Alt / Option + Shift`-click một Clip để chọn nhiều Clip, hoặc click và kéo bên ngoài Clip để chọn theo kiểu "lasso".&#x20;

Click và kéo sẽ kéo TẤT CẢ Clip đang được chọn.

Để xóa một hoặc nhiều Clip, hãy kéo chúng ra khỏi Clip Deck (biểu tượng thùng rác sẽ xuất hiện) hoặc dùng nút DELETE trong menu right-click của Clip.

### Panel Laser Overview

<figure><img src="../.gitbook/assets/qs-laser-overview.png" alt="" width="375"><figcaption></figcaption></figure>

Panel _Laser Overview_ cho bạn xem nhanh trạng thái của các laser hiện đang chạy. Hình vuông màu xanh lá ở bên phải cho biết bộ điều khiển laser đang hoạt động ổn. Nếu nó chuyển sang màu cam, có nghĩa là thỉnh thoảng có mất gói/gián đoạn; nếu màu đỏ, kết nối đã bị ngắt. Nếu màu xám, laser đó chưa được kết nối với bộ điều khiển nào.&#x20;

Biểu đồ ở giữa là lịch sử độ dài frame, và con số bên phải là tốc độ frame hiện tại. Nội dung càng phức tạp, tốc độ frame càng chậm (tức là dễ nhấp nháy hơn). Bất kỳ mức nào dưới khoảng 25fps sẽ bắt đầu trông hơi nhấp nháy.&#x20;

### Kết nối tới laser - panel Controller Assignment

Click nút _Assign Laser Controllers_ để mở panel _Controller Assignment_. (Bạn cũng có thể truy cập panel này qua _View -> Controller Assignment_ trên thanh menu).

Tại đây, bạn có thể chọn đầu ra laser nào đi tới bộ điều khiển laser nào. Kéo và thả bộ điều khiển từ danh sách bên phải vào các vị trí ở bên trái. Bạn có thể đổi tên bộ điều khiển để khớp với laser được ghép nối với nó (dùng nút biểu tượng cây bút).

Đọc chương [Controller Assignment](../setting-up/controller-assignment.md "mention") để biết thêm chi tiết.

{% hint style="danger" %}
Trước khi kích hoạt đầu ra bất kỳ laser nào, hãy bảo đảm bạn đã đọc chương [Thiết lập laser](../setting-up/setting-up-lasers.md "mention").
{% endhint %}

### Panel Laser Settings

<figure><img src="../.gitbook/assets/qs-laser-settings.png" alt="" width="375"><figcaption></figcaption></figure>

Panel này hiển thị các thiết lập cho _laser hiện đang được chọn_ (được biểu thị bằng con số ở phía trên). Thay đổi laser hiện đang được chọn bằng phím _tab_, nhấn một phím số, click vào số laser trong panel _Laser Overview_ hoặc trong _Output view._

* **Number button** kích hoạt và tắt đầu ra laser; nếu nút màu đỏ thì laser đang được kích hoạt đầu ra.
* **Brightness** điều chỉnh độ sáng laser độc lập với các laser khác (và được kết hợp với thiết lập _Global Brightness_ - tức là nếu cả hai đều ở 50%, laser của bạn sẽ ở mức 25%).
* **Test Pattern** bật mẫu kiểm tra chỉ cho laser này (ghi đè thiết lập mẫu kiểm tra toàn cục)
* **Orientation** hiệu chỉnh cho laser được treo ngang hoặc lộn ngược.
* **Flip Horizontal and Flip Vertical** đảo ngược đầu ra của laser. Hữu ích để hiệu chỉnh đầu ra trên các laser có dây nối không nhất quán.
* **Copy Laser Settings** mở một panel cho phép bạn sao chép nhiều thiết lập khác nhau từ laser này sang các laser khác.

### Thiết lập scanner

Laser trình diễn hoạt động bằng cách di chuyển một chùm tia laser đơn lẻ với tốc độ cực nhanh và bật/tắt nó để vẽ hình trong không khí. Những gì bạn thấy dưới dạng đường, hình khối và hình ảnh thực ra là chùm tia đang vẽ các đường đi nhanh hơn mắt bạn có thể theo kịp.

Luồng điểm là dữ liệu cho laser biết cần di chuyển đến đâu tiếp theo và khi nào chùm tia nên bật hoặc tắt. Trong Liberation, Clip được chuyển đổi thành luồng điểm này theo thời gian thực khi chúng được gửi tới laser.

Liberation cho bạn khả năng kiểm soát chi tiết cách tạo luồng điểm này, cho phép bạn cân bằng độ mượt, độ sáng và hiệu năng cho từng laser.

{% hint style="info" %}
Nếu bạn đã quen với phần mềm laser cũ dựa vào các luồng điểm được tính trước, cách tiếp cận này ban đầu có thể hơi khác. Tuy nhiên, việc tạo điểm theo thời gian thực cho phép cùng một nội dung được tối ưu khác nhau cho từng laser. Điều này giúp làm việc với nhiều laser có tốc độ hoặc chất lượng scanner khác nhau dễ hơn, mà không cần nhân bản hoặc dựng lại nội dung. Nó cũng giúp file Clip rất nhỏ, đó là lý do toàn bộ Clip Deck mặc định của Liberation chỉ có dung lượng vài megabyte thay vì gigabyte.
{% endhint %}

Các thiết lập scanner cơ bản là:

* **Speed** là tốc độ scanner, tức là laser di chuyển nhanh đến mức nào để vẽ hình. Thiết lập này tương đương với việc điều chỉnh point rate trong phần mềm laser truyền thống, nhưng trong Liberation bạn có thể thay đổi tốc độ di chuyển của laser _độc lập với point rate._ Bạn thường không cần điều chỉnh mục này.
* **Scanner sync** (đôi khi được gọi là _blank shift, trước đây là Colour Shift_) Scanner di chuyển laser rất nhanh, nhưng thường thì thay đổi độ sáng và màu sắc không đồng bộ với chuyển động. Điều này xuất hiện dưới dạng các "đuôi" sáng nhỏ nhấp nháy ở rìa beam và đường. Dùng điều chỉnh này để làm cho chuyển động và màu sắc đồng bộ với nhau. Xem [Laser Settings](../setting-up/laser-settings/ "mention")

Các thiết lập scanner nâng cao khác được trình bày trong chương [Nâng cao](../advanced/ "mention").

### Zoning

Để xem hướng dẫn đầy đủ về thiết lập và zoning laser, xem: [Thiết lập laser](../setting-up/setting-up-lasers.md "mention")
