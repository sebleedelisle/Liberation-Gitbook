---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/loading-and-saving
---

# 🟩 Tải và lưu

Liberation liên tục lưu trạng thái xuống ổ đĩa, vì vậy nếu bị mất điện hoặc gặp sự cố hệ thống, phần mềm sẽ khởi động lại đúng tại trạng thái trước đó. Bạn sẽ không bị mất zones, timeline hoặc nội dung khác.

Tuy nhiên, bạn vẫn có thể xuất thiết lập của mình để sao lưu và chuyển sang máy tính khác.

### Nhập / xuất dự án

File dự án lưu gần như mọi thứ trong thiết lập hiện tại của bạn, bao gồm:

* Mọi nội dung được mô tả trong phần [Nhập / xuất Laser Settings](loading-and-saving.md#laser-settings-import-export) bên dưới
* Clips, hiệu ứng và cài đặt nhóm
* Tất cả timeline của bạn (không bao gồm media âm thanh và video)
* Thiết lập Art-Net
* Cài đặt gửi/nhận MIDI
* Cài đặt tempo / đồng bộ hóa

Hiện tại, file này chưa lưu và tải:

* Cài đặt đầu vào âm thanh và Midi được dùng trong node MIDI notes và Sound Input Oscillator (phần mềm _có_ lưu cài đặt gửi/nhận MIDI cũng như đầu vào âm thanh timecode)
* Tỷ lệ giao diện
* Media cho ảnh hướng dẫn Canvas
* Media âm thanh và video cho timeline
* Phông chữ dùng trong Text node

{% hint style="danger" %}
File âm thanh và video trong timeline không được lưu cùng file dự án, vì vậy hãy nhớ lưu chúng riêng nếu bạn muốn chuyển sang máy tính khác. Xem [Lưu ý quan trọng về file media của timeline](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Nhập / xuất Laser Settings

* Laser Settings cho từng laser
* Beam zones
* Vùng đích Canvas
* DMX zones
* Gán laser controller (và alias cho bất kỳ controller nào bạn đã đổi tên)
* Cài đặt và preset hiệu chuẩn scanner laser và màu sắc
* Cài đặt và preset trình hiển thị 3D

### Nhập / xuất Clip Deck

* Tất cả Clip cùng zone assignments, cài đặt và tham số của chúng
* Tất cả cài đặt nhóm, flash mode, thời gian fade in/out, v.v.

Hiện tại, file này chưa lưu và tải:

* Tất cả hiệu ứng cùng tham số và cài đặt của chúng

{% hint style="info" %}
**Tải Clip từ file dự án mà không tải toàn bộ dự án**

Để chỉ nhập Clip từ một dự án, chọn _**Clips->Import Clip Deck**_; thay vì chọn file Clip Deck (.cpdk), hãy chọn file dự án.
{% endhint %}

### Nối thêm Clip Deck

Bạn có thể thêm Clip từ một file Clip Deck đã xuất vào dự án hiện tại bằng _Append Clip Deck_. Clip sẽ được thêm vào cuối Clip Deck hiện tại, nhưng các hiệu ứng và cài đặt nhóm trong file sẽ không được nhập.

### Xuất các Clip đã chọn

Mọi Clip đang được chọn sẽ được xuất vào một file. Cài đặt nhóm và hiệu ứng sẽ không được lưu, chỉ lưu Clip. Lưu ý rằng các Clip đang chạy sẽ không được xuất, trừ khi chúng cũng đang được chọn.

{% hint style="info" %}
Option/Alt - shift - click vào Clip để chọn chúng (hoặc dùng lasso). Bạn có thể nhận biết Clip nào đang được chọn bằng viền trắng dày xung quanh Clip đó. Xem [Bắt đầu và dừng Clips](clips/starting-stopping-clips.md)
{% endhint %}

### Nhập / xuất hiệu ứng

Tải và lưu tất cả hiệu ứng cùng cài đặt nhóm và tham số của chúng.

{% hint style="info" %}
**Tải hiệu ứng từ file dự án mà không tải toàn bộ dự án**

Để chỉ nhập hiệu ứng từ một dự án, chọn _**Effects->Import Effects**_; thay vì chọn file hiệu ứng (.efts), hãy chọn file dự án.
{% endhint %}

### Xuất timeline

Xuất file timeline có một hoặc nhiều timeline. Lưu ý rằng Clip Deck luôn được bao gồm trong các file timeline đã xuất (mặc dù bạn có thể chọn Clip nào sẽ nhập lại; xem [Nhập timeline](loading-and-saving.md#timeline-import) bên dưới).

Nếu file dự án của bạn có nhiều hơn một timeline, một panel sẽ mở ra để bạn chọn các timeline muốn xuất.

{% hint style="danger" %}
File âm thanh và video trong timeline không được lưu cùng file timeline, vì vậy hãy nhớ lưu chúng riêng nếu bạn muốn chuyển nội dung sang máy tính khác. Xem [Lưu ý quan trọng về file media của timeline](loading-and-saving.md#important-note-about-timeline-media-files)
{% endhint %}

### Nhập timeline

Nhập một hoặc nhiều timeline từ một file timeline duy nhất. Sau khi bạn chọn file timeline, một panel sẽ mở ra với nhiều tùy chọn nhập.

Nếu file timeline có nhiều hơn một timeline, tất cả sẽ được liệt kê. Hãy chọn các timeline bạn muốn đưa vào.

* Replace existing timelines\
  Xóa tất cả timeline hiện tại của bạn và thay bằng các timeline được nhập
* Import used clips only\
  Chỉ nhập các Clip được sử dụng, đồng thời sắp xếp Clip theo nhóm, mỗi timeline một nhóm. Nếu tùy chọn này không được chọn, toàn bộ Clip Deck của file timeline sẽ được nối thêm vào các Clip hiện có của bạn.
* Replace existing clip deck\
  Thay Clip Deck hiện tại của bạn bằng các Clip trong file timeline. Chỉ khả dụng nếu _Replace existing timelines_ được chọn.

{% hint style="info" %}
**Tải timeline từ file dự án mà không tải toàn bộ dự án**

Để chỉ nhập timeline từ một dự án, chọn _**Timeline->Import Timeline(s)**_; thay vì chọn file timeline (.ltml), hãy chọn file dự án.
{% endhint %}

### Nhập / xuất DMX / Art-Net

Lưu và tải Art-Net nodes cùng địa chỉ IP của chúng. Phần này cũng bao gồm DMX zones và tất cả preset DMX của bạn.

### Lưu ý quan trọng về file media của timeline

File âm thanh và video hiện **không** được xuất cùng file timeline, vì vậy nếu bạn cần chuyển nội dung sang máy tính khác, hãy nhớ bao gồm cả các file này.

{% hint style="info" %}
**Cách timeline tìm file media**

Khi timeline được tải, nó sẽ tìm trong cùng thư mục với file timeline (hoặc file dự án), đồng thời tìm trong thư mục đó và mọi thư mục con. Vì vậy, miễn là các file nằm trong cùng thư mục hoặc trong một thư mục con (chẳng hạn như _/videos_ hoặc _/sound_), timeline sẽ tìm thấy chúng khi tải.
{% endhint %}
