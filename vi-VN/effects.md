---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/effects
---

# 🟩 Hiệu ứng

Hệ thống hiệu ứng trong Liberation là một cách thú vị và linh hoạt để thay đổi Output của Clip theo thời gian thực. Hiệu ứng hoàn toàn linh hoạt và có thể dùng để làm mọi thứ nhấp nháy bật/tắt, xoay vòng, đổi màu, hoặc thậm chí bay ngẫu nhiên!

Bất kỳ thứ gì bạn có thể làm trong Clip Editor đều có thể dùng làm hiệu ứng. Thực tế, hiệu ứng được chỉnh sửa bằng đúng cùng node editor như Clip! Xem [Chỉnh sửa hiệu ứng](effects.md#editing-effects). Khả năng sáng tạo gần như là vô hạn.

Các nút hiệu ứng mặc định 1-8 nằm bên dưới các nút zone, còn hiệu ứng 9-24 là các nút nhỏ ở phía dưới.

#### Áp dụng hiệu ứng

Nhấn một nút hiệu ứng để bật/tắt hiệu ứng, hoặc tốt hơn nữa là dùng các cần gạt APC40 1-8 để fade hiệu ứng vào/ra. Để fade in một hiệu ứng khi không có APC40, hãy nhấp và kéo lên/xuống trên nút. Hoặc nhấp chuột phải vào nút hiệu ứng và chỉnh thanh trượt _level_.

{% hint style="warning" %}
Nhấn nút hiệu ứng sẽ kích hoạt hiệu ứng đó ngay lập tức. Tuy nhiên, lưu ý rằng nếu level được đặt về 0 thì sẽ không có gì xảy ra! Nhấp/kéo trên nút để thay đổi level, hoặc nhấp chuột phải và dùng thanh trượt _level_, hoặc dùng các fader trên APC40.
{% endhint %}

#### Hiệu ứng và độ trễ zone của Clip

Hiệu ứng sẽ kế thừa cài đặt độ trễ zone của từng Clip đang chạy. Vì vậy, nếu Clip của bạn có độ trễ di chuyển từ trái sang phải và bạn thêm hiệu ứng nhấp nháy, phần nhấp nháy cũng sẽ bị trễ từ trái sang phải.

{% hint style="info" %}
Cách hiệu ứng kế thừa độ trễ zone của Clip là một trong những thứ cực kỳ khó mô tả, nhưng sẽ rất rõ ràng khi bạn thử!

Tôi cho rằng đây là một trong những công cụ thú vị và sáng tạo nhất được tích hợp trong Liberation. Hãy thử và bạn sẽ thấy ý tôi là gì!
{% endhint %}

#### Tham số hiệu ứng

Thêm một tham số vào hiệu ứng của bạn bằng _Parameter node._ Hệ thống Parameter là một cách để điều chỉnh nhiều cài đặt bên trong hiệu ứng từ bên ngoài. Xem [Điều khiển tham số](clip-editor/oscillators/parameter-control.md) để biết thêm thông tin.

Dùng các núm xoay 1-8 để điều chỉnh _parameter_ cho từng hiệu ứng. Hoặc nhấp chuột phải vào nút hiệu ứng và chỉnh các thanh trượt parameter. Việc thay đổi parameter sẽ tạo ra các kết quả khác nhau tùy theo cách hiệu ứng được thiết lập. Xem danh sách bên dưới để biết các hiệu ứng mặc định và chức năng parameter của chúng.

{% hint style="info" %}
Các núm xoay 1-8 nằm dọc phía trên của APC40 Mk2 và ở góc trên bên phải trên Mk1. Xem thêm: [Tham chiếu APC40](reference/apc40-reference.md)
{% endhint %}

{% hint style="info" %}
Các con số nhỏ bạn thấy trên nút hiệu ứng biểu thị _level_ và _parameter_ của hiệu ứng. _level_ được điều khiển bằng fader trên APC40, hoặc bạn có thể nhấp-kéo trên nút. Parameter được điều chỉnh bằng các núm xoay trên APC40, hoặc bạn có thể nhấp chuột phải để chỉnh bằng chuột.
{% endhint %}

#### Các hiệu ứng mặc định

<figure><img src=".gitbook/assets/qs-default-effects.png" alt=""><figcaption></figcaption></figure>

1. **Randomiser** :\
   Áp dụng chuyển động hỗn loạn cho Output của Clip. Parameter điều chỉnh mức độ/tốc độ hỗn loạn.
2. **Sine wave** :\
   Làm biến dạng toàn bộ nội dung theo một sóng sin đang di chuyển. Parameter điều chỉnh bước sóng.
3. **Rotation** :\
   Xoay mọi thứ. Parameter điều chỉnh tốc độ xoay.
4. **Horizontal flip** :\
   Nén và kéo giãn mọi thứ theo chiều ngang. Parameter điều chỉnh tốc độ.
5. **Scale** :\
   Lặp lại việc scale mọi thứ từ đầy đủ về 0. Parameter điều chỉnh tốc độ.
6. **Hue** :\
   Thay đổi hue của mọi thứ, nhưng không thay đổi saturation (tức là phần nào màu trắng thì vẫn giữ màu trắng). Parameter điều chỉnh hue.
7. **Saturation and hue** :\
   Thay đổi hue của mọi thứ và cũng bão hòa màu hoàn toàn (tức là phần nào màu trắng sẽ chuyển sang màu đó). Parameter điều chỉnh hue.
8. **Flash** :\
   Lặp lại việc nhấp nháy độ sáng của mọi thứ từ đầy đủ về 0. Parameter điều chỉnh tốc độ nhấp nháy.

<figure><img src=".gitbook/assets/qs-colour-effects.png" alt=""><figcaption></figcaption></figure>

Có thêm 16 hiệu ứng màu ở hàng dưới cùng để áp dụng các giá trị hue và saturation đặt sẵn.

Lưu ý rằng đây là các hiệu ứng mặc định, nhưng bạn có thể chỉnh sửa chúng để làm gần như bất cứ điều gì bạn muốn!

### Áp dụng cho nhóm

Bạn có thể chọn những nhóm nào bị ảnh hưởng bởi hiệu ứng. Nhấp chuột phải và bật/tắt các ô chọn nhóm có nhãn _Apply to groups._

Tôi chủ yếu dùng cách thiết lập này khi làm việc riêng giữa đồ họa canvas và tia laser. Tôi gán tất cả Clip canvas vào nhóm 5, rồi loại trừ nhóm này khỏi các hiệu ứng mà tôi không muốn ảnh hưởng đến các Clip đồ họa đó.

Bạn cũng có thể dùng cách này để áp dụng trực tiếp 2 thay đổi màu khác nhau cho 2 nhóm laser cùng lúc. Tạo hai hiệu ứng thay đổi màu và chọn các nhóm Clip mà mỗi hiệu ứng sẽ áp dụng.

### MX group

Viết tắt của _Mutually Exclusive_, đây là cách nhóm các hiệu ứng lại với nhau sao cho chỉ một hiệu ứng trong nhóm có thể hoạt động tại cùng một thời điểm. Hãy để ý rằng chỉ một trong các hiệu ứng đổi màu mặc định có thể hoạt động cùng lúc. Đó là vì tất cả chúng đều nằm trong MX Group 1.

Chức năng này bị tắt nếu cài đặt _MX Group_ là 0.

### Chỉnh sửa hiệu ứng

Nhấp chuột phải vào bất kỳ hiệu ứng nào, rồi nhấp nút _EDIT EFFECT_ để mở effect editor. Lưu ý rằng editor này giống hệt Clip Editor!

Chỉnh sửa hiệu ứng theo cùng cách bạn chỉnh sửa bất kỳ Clip nào. Xem [Clip Editor](clip-editor/).

Bạn cần có ít nhất một Creator node; node này có thể là bất kỳ thứ gì (line, circle, shape, thậm chí text!), nhưng có lẽ bạn nên chọn thứ có ý nghĩa nhất trong phần xem trước của nút hiệu ứng.

Khi hiệu ứng được áp dụng, tất cả Creator node trong hiệu ứng sẽ được thay thế bằng Output của các Clip đang chạy.

{% hint style="warning" %}
Vì một số lý do kỹ thuật cực kỳ nhàm chán, các node "trails" không được bật khi ở bên trong một hiệu ứng. Điều tương tự cũng áp dụng cho cài đặt "delay" bên trong các pattern node (chúng dùng cùng một hệ thống). Việc này sẽ được khắc phục trong các bản cập nhật sau.
{% endhint %}
