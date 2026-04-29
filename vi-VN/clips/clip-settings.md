---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/clip-settings
---

# ✅ Cài đặt Clip

### Bảng cài đặt Clip

<figure><img src="../.gitbook/assets/clip-settings-clip-settings-panel" alt="" width="357"><figcaption><p>Bảng cài đặt Clip</p></figcaption></figure>

Thay đổi kích thước Output của Clip bằng _Scale X_ và _Scale Y_. Hai giá trị này được khóa cùng nhau trừ khi bạn nhấn phím _SHIFT_.

Thay đổi vị trí ngang và dọc của Clip bằng _Shift X_ và _Shift Y_.

_Zone Delay/Chase_ là một tính năng thú vị đến mức cần có hẳn một phần riêng. [Zone Delay/Chase](zone-delay-chase.md)

### Khóa Clip

Nếu một Clip bị khóa, bạn không thể di chuyển hoặc xóa Clip đó. Để khóa một Clip, dùng ô chọn _Locked_ trong menu nhấp chuột phải. Trong bảng cài đặt Clip, bạn có thêm một số tùy chọn.

* _UNLOCK ALL -_ mở khóa mọi Clip trong Clip Deck.
* _AUTO-LOCK_ - khi bật _Auto-Lock_, mọi Clip được phát tự động (bằng timeline hoặc hệ thống ghi/phát lại MIDI) sẽ bị khóa. Tính năng này hữu ích nếu bạn đã lập trình một show trong Logic Pro (hoặc phần mềm tương tự) và không muốn vô tình chỉnh sửa các Clip được dùng trong show.
* _LOCKED CLIPS ZONES_ - nếu bật tùy chọn này, bạn không thể thay đổi zones cho bất kỳ Clip nào đang bị khóa.
* _LOCKED CLIPS PARAMS_ - nếu bật tùy chọn này, bạn không thể thay đổi các tham số (scale, shift, v.v.) cho bất kỳ Clip nào đang bị khóa.

### Menu nhấp chuột phải

Nếu bạn nhấp chuột phải vào một Clip, một menu sẽ xuất hiện với một số tùy chọn cho Clip đó. Xem [Giới thiệu Clip Editor](../clip-editor/clip-editor-intro.md), [Cài đặt Clip](clip-settings.md) và [Nhóm](groups.md) để biết thêm về một vài mục đầu tiên trong menu này.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-14 at 11.22.48.png" alt="" width="322"><figcaption><p>Menu nhấp chuột phải của cài đặt Clip</p></figcaption></figure>

### Retrigger

Theo mặc định, Clips được đặt thành _retrigger_. Điều này nghĩa là bất kể bạn nhấn vào lúc nào, Clip sẽ bắt đầu chạy từ thời điểm đó. Vì vậy nếu bạn khởi chạy muộn, hoạt ảnh của Clip cũng sẽ trễ một chút và lệch nhịp.

{% hint style="info" %}
Nếu bạn dùng _Tap Tempo_ khi một Clip đang chạy với _retrigger_, hệ thống sẽ “quantise” Clip để khớp nhịp, ngay cả khi bạn không khởi chạy Clip đúng vào phách.
{% endhint %}

Nếu _Retrigger_ không được bật, Clip sẽ luôn đúng nhịp - giống như Clip đã được khởi chạy ngay từ đầu đồng hồ. Tùy chọn này phù hợp khi bạn đã đồng bộ hoàn hảo với nhạc bằng tín hiệu đồng hồ bên ngoài.

{% hint style="info" %}
Clips thường được thiết kế để lặp vô hạn, nhưng bạn cũng có thể thiết kế để chúng chỉ chạy một lần hoặc vài vòng. Hãy đảm bảo giữ các Clip đó ở chế độ _retrigger_, nếu không chúng sẽ không khởi động lại!
{% endhint %}

### Thời gian chuyển vào/ra (fade)

Clips có thể được đặt để fade in và fade out với thời lượng tính bằng giây. Theo mặc định, thời gian fade sẽ được kế thừa từ cài đặt của nhóm (và có thể thay đổi bằng cách nhấp chuột phải vào nút nhóm).

Nếu bạn muốn thời lượng fade khác với nhóm của Clip, trước tiên hãy tắt nút _USE GROUP DEFAULT_, sau đó điều chỉnh các thanh trượt _In time_ và _Out time_ của Clip.
