---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timecode
---

# ✅ Timecode

Liberation hỗ trợ đồng bộ với tín hiệu timecode SMPTE/LTC bên ngoài, thường được dùng trong các show nhạc live để giữ ánh sáng, hiệu ứng pháo, video và backing tracks chạy đúng thời điểm với nhau.

{% hint style="info" %}
SMPTE/LTC là gì?

SMPTE là một tiêu chuẩn timecode, còn LTC là timecode này được chuyển thành tín hiệu âm thanh. Nếu nghe tín hiệu âm thanh này, bạn sẽ thấy nó giống tiếng rít cao rất khó chịu, nhưng với máy tính thì đó là thông tin thời gian có độ phân giải cao.

**Thông tin dành cho người thích đào sâu!**

Trước đây, SMPTE thường được dùng để giữ video và audio đồng bộ với nhau. Khi đồng bộ với băng analog, một track trên băng sẽ được ghi âm timecode, đôi khi gọi là "striping" băng. Bạn có thể dùng track timecode này để giữ nhiều máy băng chạy đúng thời điểm với nhau, hoặc để giữ một MIDI sequencer đồng bộ với băng. (Nhờ vậy bạn không cần ghi các nhạc cụ MIDI lên băng; sequencer có thể phát chúng trực tiếp trong lúc bạn mix!)

SMPTE là viết tắt của Society of Motion Picture and Television Engineers, tổ chức đã định nghĩa tiêu chuẩn này. LTC là viết tắt của _Linear TimeCode._
{% endhint %}

Bạn có thể nhận tín hiệu LTC timecode qua bất kỳ audio interface nào trên máy tính, nhưng nên dùng một interface chuyên nghiệp có ít nhất một cổng XLR chỉnh được mức tín hiệu và có khả năng monitoring.

Tôi đã dùng [M-Audio 192/6](https://www.m-audio.com/audio-midi-interfaces/air-192-6.html) và thấy rất ổn, vì nó có headphone monitoring, 2 cổng XLR và không cần driver đặc biệt nào (ít nhất là trên macOS). Nếu bạn chỉ dùng nó cho timecode thì có thể chọn mẫu rẻ hơn một chút là [M-Audio 192/4](https://www.m-audio.com/audio-midi-interfaces/air-192-4.html) (chỉ có một cổng vào và không có MIDI), nhưng thật ra bất kỳ audio interface tương đối tốt nào cũng có thể dùng được.

{% hint style="info" %}
Tín hiệu LTC timecode thường được phân phối qua cáp XLR cân bằng, vì loại cáp này đủ chắc chắn để truyền tín hiệu âm thanh mức thấp trên khoảng cách dài. (XLR là loại đầu nối dạng trụ thường dùng với micro)
{% endhint %}

### Kết nối phần cứng

Cắm cáp XLR mang tín hiệu timecode vào audio interface và đảm bảo bạn đang nhận tín hiệu tốt. Chỉnh mức tín hiệu trên audio interface sao cho đủ mạnh nhưng không bị clipping. Nếu audio interface có cổng tai nghe, bạn có thể nghe timecode để chắc chắn tín hiệu không bị lỗi giật và không có quá nhiều nhiễu.

{% hint style="info" %}
Về lý thuyết, bạn có thể nhận tín hiệu qua jack trên MacBook, nhưng cách này cần cáp tự chế. Các jack này thường là mini jack TRRS 4 cực, và thật lòng tôi không chắc chân nào trong số đó có thể dùng làm ngõ vào audio. Tôi cũng không chắc nó chịu được mức điện áp nào (tôi từng đọc đâu đó là +/-1V, nhưng hãy tự chịu rủi ro nếu dùng cách này!)

Tôi nghĩ tốt hơn là bạn nên kiếm một audio interface USB giá rẻ thay vì thử cách này.
{% endhint %}

Nếu audio interface của bạn không có chức năng input monitoring nào, bạn có thể kiểm tra trong cài đặt hệ thống macOS (trong _Sound_) để chắc chắn rằng bạn đang nhận được tín hiệu. (Trên Windows, dùng _Sound Control Panel_).

<figure><img src=".gitbook/assets/mac-mic-input-volume.png" alt=""><figcaption><p>macOS hiển thị mức đầu vào của mọi audio interface trong panel cài đặt hệ thống Sound</p></figcaption></figure>

### Thiết lập trong Liberation

1. Chọn audio interface và kênh đầu vào đúng trong cửa sổ Timecode settings.

![](.gitbook/assets/timecode-panel.png)

{% hint style="info" %}
Lưu ý rằng menu thả xuống có các tùy chọn riêng cho từng kênh đầu vào trên audio interface của bạn

<img src=".gitbook/assets/m-audio.png" alt="" data-size="original">
{% endhint %}

Hãy để ý ô vuông bên trái: nếu bạn đang nhận tín hiệu timecode hợp lệ, ô này sẽ chuyển sang màu xanh lá. Nếu không, nó sẽ có màu đỏ.

2. Chọn đúng framerate cho timecode đầu vào. Người cung cấp timecode cho bạn sẽ có thể cho biết frame rate là bao nhiêu. (Nếu chọn sai, hệ thống vẫn đồng bộ, nhưng bạn sẽ thấy một đoạn "nhảy" nhỏ mỗi giây)
3. Mở phần cài đặt timecode của Timeline bằng biểu tượng đồng hồ nhỏ trên thanh timeline, rồi chọn tùy chọn SMPTE(LTC).

<figure><img src=".gitbook/assets/timeline-settings.png" alt=""><figcaption></figcaption></figure>

4. Điều chỉnh start offset (theo giờ, phút, giây, frame) để khớp với thời điểm bắt đầu bài hát. Nếu có nhiều timeline, bạn cần thiết lập các tùy chọn này riêng cho từng timeline.

{% hint style="info" %}
Trong giới touring, một quy ước phổ biến là mỗi bài hát bắt đầu ở một giờ khác nhau, ví dụ 01:00:00:00 cho bài đầu tiên, 02:00:00:00 cho bài thứ hai, v.v.

Liberation sẽ tự động chuyển sang timeline tương ứng dựa trên timecode, nên bạn không bao giờ cần đổi timeline thủ công trong lúc show đang chạy.
{% endhint %}

Lưu ý rằng khác với MIDI Clock và Ableton Link, SMPTE là một hệ thống thời gian _tuyệt đối_, được đo bằng giờ, phút, giây và frame. Hệ thống thời gian lõi của Liberation dựa trên phách và ô nhịp, vì vậy khi nhận timecode, nó sẽ dùng tempo đã đặt trong timeline. Bạn cần đảm bảo tempo này đồng bộ với phần nhạc cũng đang được đồng bộ theo timecode.
