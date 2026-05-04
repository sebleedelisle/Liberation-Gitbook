---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/tempo-synchronisation
---

# 🟧 Tempo / đồng bộ hóa

Đồng bộ hóa với nhạc là một phần nền tảng của Liberation; khi bạn đã khớp tempo và nhịp với bản nhạc, bạn có thể yên tâm rằng mọi thứ sẽ chạy đồng bộ. Nếu bạn có MIDI clock (hoặc Ableton Link) thì bạn không cần lo về việc đồng bộ thủ công. Nếu không có cũng không sao - bạn có thể khớp thủ công bằng tính năng tempo _Live_.

Nếu bạn đã có kinh nghiệm với phần mềm âm nhạc hoặc ánh sáng, quy trình này sẽ khá quen thuộc. Nếu chưa, bạn nên dành thời gian làm quen với hệ thống và luyện tập ở nhà trước khi chạy một buổi diễn trực tiếp.

## Panel Tempo

Panel _Tempo_ luôn hiển thị trên màn hình và chứa tất cả cài đặt đồng bộ hóa. Ở phía trên, bạn sẽ thấy bộ đếm ô nhịp/phách hiện tại và phần điều khiển transport với các nút phát/tạm dừng và tua lùi/tua tới.

Bên dưới là beat marker; bốn ô vuông “nhấp” theo nhịp. _Beat marker_ này là một hình dung trực quan cực kỳ hữu ích và bạn sẽ thường xuyên nhìn vào nó khi dùng hệ thống tempo _Live_.

### Cài đặt tempo

Bạn có các cách sau để đặt tempo:

* Nhấp và kéo thanh trượt _Tempo_
* Shift-click và kéo thanh trượt _Tempo_ để thay đổi tempo theo bước 0,1
* Nhấp đúp vào thanh trượt _Tempo_ và nhập số thủ công
* Dùng núm _Tempo_ trên APC40 (nhấn shift để chỉnh theo bước 0,1)
* Tap Tempo

{% hint style="info" %}
Tempo được định nghĩa bằng “beats per minute” (nhịp mỗi phút), và giá trị mặc định truyền thống thường là 120.
{% endhint %}

## Tap Tempo

Tự động đặt tempo bằng cách nhấp nút _TAP_ đúng theo nhịp. Đặt điểm bắt đầu của ô nhịp bằng nút _RESET_.

{% hint style="info" %}
Hệ thống Tap Tempo đủ thông minh để nhận biết nếu bạn tạm dừng gõ một lúc, hoặc nếu bạn lỡ vài nhịp. Nếu bạn bắt đầu gõ ở double time, hệ thống sẽ hiểu rằng bạn muốn nhân đôi tempo; tương tự nếu bạn gõ ở half time.

Hệ thống cũng đủ thông minh để nhận ra khi có hai người cùng gõ tempo cùng lúc (ví dụ một người trên bàn phím và một người trên APC40). Liberation sẽ lấy trung bình các lần gõ kép.
{% endhint %}

#### Lệnh bàn phím:

T - tap tempo\
R - đặt lại ô nhịp\
Y - làm tròn tempo đến số nhịp mỗi phút gần nhất.

{% hint style="info" %}
Vì phần lớn nhạc hiện nay được tạo bằng kỹ thuật số, tempo thường là một số nguyên đã làm tròn. Vì vậy, nếu tempo bạn gõ có vẻ đã gần đúng, hãy dùng phím Y (hoặc xoay núm tempo của APC40 một “nấc”) để làm tròn về số nguyên.
{% endhint %}

#### Điều khiển trên APC40:

APC40 có nút _TAP TEMPO_ riêng, hoặc bạn cũng có thể dùng footswitch đã kết nối để gõ bằng chân!

Dùng núm _TEMPO_ để điều chỉnh. Nhấn _SHIFT_ trong khi dùng núm _TEMPO_ để tinh chỉnh.

Dùng nút _METRONOME_ để **đặt lại ô nhịp**. (Lưu ý rằng nút _METRONOME_ cũng sáng theo nhịp)

Xoay núm _TEMPO_ một “nấc” sang phải hoặc trái để **làm tròn tempo** lên hoặc xuống về một số BPM nguyên.

Xem thêm [Tham chiếu APC40](reference/apc40-reference.md "mention")

### Nudge tempo

Nếu bạn tự tin rằng tempo đã đủ gần với tempo thực tế nhưng thấy nó đang bị lệch dần khỏi nhịp, hãy dùng các nút _NUDGE_ để hiệu chỉnh.

Nếu tempo của Liberation đang chạy nhanh hơn nhạc, nhấn và giữ _NUDGE -_ để tạm thời làm chậm cho đến khi khớp lại.

Nếu tempo của Liberation đang chạy chậm hơn nhạc, nhấn và giữ _NUDGE +_ để tạm thời tăng tốc cho đến khi khớp lại.

{% hint style="info" %}
Bạn có thể dùng các nút NUDGE trên màn hình hoặc các nút chuyên dụng trên APC40.
{% endhint %}

### Half time / double time

Dùng các nút _÷2_ và _x2_ để giảm một nửa hoặc nhân đôi tempo vĩnh viễn. Khác với tempo multiplier, đây là thay đổi vĩnh viễn đối với tempo hiện tại.

## Tempo Multiplier

Hệ thống _Tempo Multiplier_ cho phép bạn tạm thời điều chỉnh tempo rồi quay lại giá trị trước đó.

Bật/tắt _Tempo Multiplier_ bằng cách nhấn nút _TEMPO MULTIPLIER_ hoặc nút _BANK_ trên APC40. Điều chỉnh bằng thanh trượt trên màn hình hoặc bằng thanh trượt A-B của APC40. Hoặc dùng các nút preset _25%, 50%, 100% 200%_.

## Nguồn tempo bên ngoài

### MIDI Clock

Để đồng bộ với tín hiệu MIDI clock bên ngoài, chọn nút radio _MIDI CLOCK_ và chọn thiết bị MIDI từ menu thả xuống. Lưu ý đèn trạng thái có màu bên cạnh các menu thả xuống:

* Xanh lá - đang nhận tín hiệu MIDI clock
* Cam - có thể kết nối tới thiết bị MIDI nhưng hiện không có tín hiệu clock
* Đỏ - không thể kết nối tới thiết bị MIDI

{% hint style="info" %}
MIDI Clock phát một chuỗi frame (24 frame cho mỗi nốt đen), nhưng trong các thông điệp không có dữ liệu vị trí. Điều này có nghĩa là nó hữu ích để giữ đúng nhịp, nhưng bạn vẫn có thể cần đặt lại ô nhịp.

Nguồn tempo MIDI Clock của Liberation cũng phản hồi các thông điệp **MIDI Machine Control (MMC)**, vì vậy nếu nguồn clock của bạn truyền các thông điệp này, bạn sẽ không cần đặt lại ô nhịp thủ công.
{% endhint %}



### Ableton Link

Để đồng bộ với Ableton Link, chọn _ABLETON LINK_ làm nguồn tempo. Liberation sẽ tham gia phiên Link trên mạng cục bộ của bạn và chạy theo tempo cũng như pha phách được chia sẻ từ các ứng dụng hỗ trợ Link khác.

Ableton Link không sử dụng cổng MIDI và không truyền vị trí bài hát tuyệt đối. Hãy dùng các điều khiển đặt lại ô nhịp nếu bạn cần thời điểm bắt đầu ô nhịp của Liberation khớp với một khoảnh khắc cụ thể trong chương trình.

### Timeline

Mỗi timeline có tempo riêng, có thể là một giá trị cố định hoặc một _Tempo Map_. _Tempo Map_ cho phép bạn điều chỉnh tempo tại các thời điểm cụ thể trong timeline.

Tempo của timeline sẽ được dùng khi _TIMELINE_ được chọn làm nguồn tempo.

{% hint style="info" %}
Bạn có thể chạy timeline cùng với _bất kỳ_ nguồn tempo nào! Vì vậy, nếu bạn có một ban nhạc live không chơi theo click, bạn có thể khởi động timeline thủ công và giữ nó đồng bộ bằng nguồn tempo _LIVE_. Hoặc nếu bạn có tín hiệu MIDI clock, bạn có thể dùng tín hiệu đó!
{% endhint %}
