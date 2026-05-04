---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/clip-editor-intro
---

# 🟩 Giới thiệu về Clip Editor

Clip Editor là một cách linh hoạt để tạo nội dung laser và là phần cốt lõi của Liberation. Bạn có thể dễ dàng tạo những nội dung đơn giản, nhưng công cụ này cũng đủ linh hoạt để tạo ra các hiệu ứng cực kỳ tinh vi và phức tạp.

{% hint style="info" %}
Trình chỉnh sửa dựa trên node là phần đầu tiên của Liberation được xây dựng! Ý tưởng này bắt nguồn từ một cuộc trò chuyện với Rob Stanley tại một buổi gặp mặt về laser ở Vương quốc Anh năm 2018, xoay quanh việc một công cụ thiết kế nội dung laser “hướng đối tượng” sẽ trông như thế nào.

Dù nhìn có vẻ đơn giản, đây thực ra là một hệ thống khá phức tạp để xây dựng. Nhưng đến đầu năm 2019, tôi đã có một bản demo hoạt động được để chứng minh ý tưởng — và từ đó toàn bộ hành trình này bắt đầu!
{% endhint %}

Đây là một trình chỉnh sửa trực quan dựa trên node (hay [kiến trúc đồ thị node](https://en.wikipedia.org/wiki/Node_graph_architecture#Node_graph)), sẽ khá quen thuộc nếu bạn từng dùng các sản phẩm như TouchDesigner, MaxMSP hoặc VVVV. Tuy vậy, Clip Editor hơi khác và đơn giản hơn đôi chút vì được thiết kế riêng cho đồ họa vector.

Bạn có thể mở Clip Editor bằng cách nhấp chuột phải vào nút Clip rồi chọn _EDIT CLIP_. Hoặc nhấp chuột phải vào một nút Clip trống rồi chọn _CREATE AND EDIT CLIP_.

### Tổng quan

Những gì bạn sẽ thấy trong Clip Editor:

* Các nút **Creator** và **Operator node** ở phía trên
* Các nút **Oscillator node** ở bên trái
* Bản xem trước của nội dung trong một panel ở bên phải; nếu bạn nhấp vào một node, bạn sẽ thấy thêm bản xem trước thứ hai hiển thị nội dung ngay tại node đó.
* Tất cả node và kết nối của clip bạn đang chỉnh sửa (nếu là clip mới thì phần này sẽ trống)
* Panel Clip Editor với nhiều tùy chọn khác nhau

Trong khi chỉnh sửa, bạn cũng sẽ thấy clip trông như thế nào trong trình trực quan hóa 3D ở nền phía sau.

{% hint style="info" %}
Nếu bạn không thấy output nào trong trình trực quan hóa 3D, có thể bạn cần dùng các nút zone để bật những zone mong muốn. Bạn cũng cần đảm bảo đã bật _Preview to lasers_; xem [Giới thiệu về Clip Editor](clip-editor-intro.md#clip-editor-panel "mention") bên dưới.
{% endhint %}

### Xây dựng một clip

Thông thường, bạn bắt đầu với một hoặc nhiều [node Creator](creator-nodes.md), rồi kết nối các [Operator nodes](operator-nodes/) từ trái sang phải để xử lý nội dung. Khi bạn di chuyển các Creator và/hoặc Operator lại gần nhau, chúng sẽ tự động kết nối với nhau. Bạn cũng có thể kéo chúng ra xa để ngắt kết nối.

### Thêm node vào clip

Nhấp và kéo từ một trong các nút node ở phía trên hoặc bên trái vào một vùng trống trong Clip Editor.

### Điều chỉnh thiết lập cho một node

Nhấp vào nút biểu tượng bánh răng (ở góc trên bên phải của node) để mở panel thuộc tính cho node đó.

### Bật và tắt một node

Nhấp vào nút biểu tượng nguồn (ở góc trên bên trái của node) để bật hoặc tắt node. Node sẽ mờ đi để cho biết hiện tại nó không hoạt động. Lưu ý rằng nội dung vẫn đi qua một Operator ngay cả khi Operator đó bị tắt, nhưng node sẽ không tác động đến nội dung.

### Kết nối các node với nhau

Nội dung được tạo bằng một node Creator và được truyền qua các node từ trái sang phải; mỗi Operator tác động đến nội dung theo một cách nào đó rồi truyền tiếp sang Operator kế tiếp. Phần còn lại ở cuối đường đi chính là nội dung của clip. Creator và Operator sẽ tự động kết nối với nhau khi bạn di chuyển chúng lại gần. Để tách chúng ra, hãy kéo chúng ra xa nhau.

{% hint style="info" %}
Bạn có thể kết nối nhiều hơn một node vào input của node kế tiếp. Điều này hữu ích khi cần kết hợp nhiều phần nội dung.
{% endhint %}

### Thuộc tính và socket của node

Mỗi node có một dãy socket ở phía dưới, và mỗi socket đại diện cho một thuộc tính trong node, chẳng hạn như độ sáng, vị trí, tỷ lệ, góc xoay, v.v.

Các [node Oscillator](oscillators/) có thể được kết nối vào các socket này từ phía dưới và dùng để tạo hoạt ảnh cho các thiết lập đó. Node Oscillator có một output ở phía trên; nhấp và kéo để rút kết nối ra, rồi thả vào một trong các socket thuộc tính của node khác.

### Node Oscillator

Node Oscillator được dùng để thay đổi thuộc tính theo thời gian. Chúng thường đại diện cho các dạng sóng như sóng răng cưa hoặc sóng sin, nhưng một số node Oscillator dùng input bên ngoài (chẳng hạn như mức input của micro) làm nguồn.

{% hint style="info" %}
Nếu bạn từng dùng synthesizer analog, bạn sẽ quen với khái niệm oscillator, thường được dùng để tạo dạng sóng hoặc điều chỉnh âm thanh theo thời gian. Oscillator trong Liberation cũng làm công việc tương tự.

**Thông tin thú vị:** tên _Liberation_ được lấy cảm hứng từ Moog Liberation, một synthesizer “keytar” ra mắt năm 1980 và trở nên nổi tiếng nhờ Herbie Hancock, Jean-Michel Jarre, thậm chí cả James Brown!
{% endhint %}

Oscillator luôn có các thiết lập _range_ để điều khiển giá trị tối thiểu và tối đa của thuộc tính cần điều chỉnh. Và _Wave Oscillators_ luôn có thiết lập _duration_ để xác định tốc độ Oscillator thay đổi giá trị. Xem [Bộ dao động dạng sóng](oscillators/wave-oscillators.md "mention") để biết thêm thông tin.

### Panel Clip Editor

* Timer - ở phía trên panel, bạn sẽ thấy thời gian hiện tại của clip khi clip đang chạy
* _RETRIGGER_ - khởi động lại clip từ đầu; đặc biệt hữu ích nếu clip của bạn không lặp
* _Preview to lasers_ - khi tùy chọn này được chọn, bạn sẽ thấy trình trực quan hóa 3D cập nhật trong lúc chỉnh sửa clip này. Nếu tắt, bạn sẽ thấy bất kỳ clip nào đang chạy bên ngoài editor. Đây là thiết lập toàn cục, không phải thiết lập riêng cho từng clip.
* _UNDO/REDO_ - dành cho chính Clip Editor. Cũng được gán với `Cmd / Ctrl + Z` và `Cmd / Ctrl + Shift + Z`.
* _SAVE CLIP_ - lưu các chỉnh sửa của bạn nhưng sẽ cảnh báo về việc ghi đè
* _SAVE AS A COPY_ - lưu clip của bạn vào ô trống kế tiếp trong Clip Deck. Vị trí này trở thành vị trí mới của clip, và mọi lần lưu sau đó sẽ được lưu tại vị trí mới này.
* _EXIT EDITOR_ - đóng Clip Editor. Nếu bạn có thay đổi chưa lưu, một panel xác nhận sẽ xuất hiện.
