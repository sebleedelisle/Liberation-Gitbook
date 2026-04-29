---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/sound-input-oscillator
---

# ✅ Bộ dao động đầu vào âm thanh

## <img src="../../.gitbook/assets/sound-input-icon.png" alt="" data-size="line"> Sound input

Chuyển đổi mức đầu vào âm thanh thành giá trị thuộc tính.

{% hint style="info" %}
Bộ dao động Sound input sử dụng giao diện âm thanh mặc định, nhưng bạn có thể thay đổi trong _Preferences_. Mở menu _Liberation -> Preferences._

Trong các cài đặt _Sound Input_, bạn có thể chọn giao diện âm thanh muốn sử dụng, cùng với một số cài đặt khác để điều chỉnh mức âm lượng.
{% endhint %}

* **range min / range max** - giá trị tối thiểu và tối đa mà dạng sóng được ánh xạ vào
* **channel** - Nếu giao diện âm thanh của bạn có nhiều hơn một kênh đầu vào, bạn có thể chọn kênh muốn lấy tín hiệu tại đây.

{% hint style="info" %}
Một kỹ thuật khá thú vị là lấy nhiều nguồn âm thanh từ bàn mixer; nhờ đó, các Clips khác nhau có thể phản hồi theo các nhạc cụ khác nhau.
{% endhint %}

{% hint style="info" %}
Bạn chỉ có thể sử dụng một giao diện âm thanh tại một thời điểm cho tất cả _Sound Inputs_ (được chọn trong panel _App Settings_). Nếu muốn dùng nhiều hơn một giao diện cho việc này, trên macOS bạn có thể [tạo một Aggregate Device](https://support.apple.com/en-gb/HT202000) để gộp các đầu vào thành một nguồn âm thanh ảo duy nhất. (Trên Windows cũng có nhiều ứng dụng làm được việc này, nhưng tôi chưa thử).
{% endhint %}

* **clamp min / clamp max** - dùng tùy chọn này để chọn dải mức âm thanh mà bạn muốn phản hồi. Bạn thường không cần điều chỉnh mục này nếu các cài đặt gate và limit (trong panel _App Settings_) đã được chỉnh đúng, nhưng chúng có thể hữu ích cho một số hiệu ứng sáng tạo.

{% hint style="info" %}
Bạn sẽ thấy một biểu tượng micro nhỏ trên nút Clip mỗi khi Clip đó có bộ dao động _Sound Input_.

<img src="../../.gitbook/assets/image (8).png" alt="" data-size="original">
{% endhint %}
