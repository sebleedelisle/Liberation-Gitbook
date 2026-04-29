---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/timeline/synchronising-tempo-to-an-audio-track
---

# 🟩 Đồng bộ tempo với một track âm thanh

<iframe src="https://www.youtube.com/embed/sL0SsuTf7Pc" title="Đồng bộ tempo với một track âm thanh" style="width: 100%; aspect-ratio: 16 / 9; border: 0;" allowfullscreen></iframe>

Timeline của Liberation được thiết kế để làm việc với tempo cố định hoặc thay đổi, nhưng để đồng bộ ổn định, bạn luôn cần bắt đầu bằng cách xác định tempo và căn chỉnh âm thanh cho đúng. Phần này mô tả quy trình được khuyến nghị.

#### 1. Căn chỉnh phách mạnh đầu tiên

Thêm track âm thanh vào timeline và đảm bảo nó được snap vào một phách, sao cho **phách mạnh đầu tiên của bản nhạc** khớp chính xác với điểm bắt đầu của một ô nhịp.

Bước này rất quan trọng.

Nếu âm thanh không bắt đầu tự nhiên ở phách mạnh, bạn có hai lựa chọn:

* **Điều chỉnh độ trễ của clip**\
  Nhấp chuột phải vào audio clip và điều chỉnh giá trị Delay cho đến khi phách mạnh đầu tiên khớp với một phách hoặc mốc ô nhịp.
* **Cắt âm thanh bằng công cụ bên ngoài**\
  Chỉnh sửa file âm thanh trong một trình biên tập bên ngoài, chẳng hạn như Audacity, để file bắt đầu chính xác tại phách mạnh đầu tiên, rồi import lại.

{% hint style="info" %}
**Quan trọng:**\
Nếu điểm bắt đầu của âm thanh không được căn vào một phách hoặc ô nhịp, vị trí bắt đầu mà bạn cảm nhận được của bản nhạc sẽ dịch lùi hoặc tiến khi bạn thay đổi tempo. Điều này khiến việc khớp tempo chính xác trở nên rất khó.
{% endhint %}

#### 2. Đặt tempo ban đầu

Nếu bạn có ước lượng sơ bộ về BPM, hãy nhập giá trị đó vào phần điều khiển tempo của timeline và bắt đầu phát từ đầu.

Quan sát kỹ các mốc phách và ô nhịp khi track đang phát.

* Nếu các mốc trôi lên trước nhạc, hãy giảm tempo một chút.
* Nếu các mốc bị tụt lại sau nhạc, hãy tăng tempo một chút.
* Dừng phát, điều chỉnh tempo, rồi thử lại.

Với hầu hết nhạc hiện đại, tempo là một giá trị BPM nguyên và cố định. Khi bạn tìm được giá trị đúng, nó sẽ giữ khớp trong suốt toàn bộ track.

#### 3. Dùng dạng sóng làm hướng dẫn trực quan

Dạng sóng âm thanh là tham chiếu hữu ích khi khớp tempo.

* Các transient và đỉnh tín hiệu nên thẳng hàng với các mốc ô nhịp dọc.
* Phóng to để kiểm tra căn chỉnh qua nhiều ô nhịp.

**Mẹo:**\
Dùng bánh xe chuột hoặc thao tác trên trackpad để zoom timeline. Dùng bánh xe cuộn ngang hoặc thao tác tương ứng để di chuyển sang trái và phải. Làm việc ở mức zoom lớn giúp điều chỉnh các sai lệch nhỏ dễ hơn nhiều.

#### 4. Track có BPM không nguyên

Nếu track không dùng BPM nguyên, độ lệch sẽ diễn ra từ từ hơn.

* Phóng to thêm.
* Điều chỉnh tempo với bước nhỏ hơn.
* Kiểm tra căn chỉnh trên các đoạn dài hơn của track, thay vì chỉ vài ô nhịp đầu tiên.

#### 5. Nhạc có thay đổi tempo

Nếu nhạc nhanh dần hoặc chậm dần, hãy dùng Tempo Map:

* Phát track và quan sát các mốc phách.
* Khi độ lệch trở nên rõ ràng, thêm một thay đổi tempo tại điểm đó.
* Điều chỉnh tempo cho đoạn mới cho đến khi nó khớp lại.

Lặp lại quy trình này cho từng lần thay đổi tempo trong bản nhạc.

#### 6. Phân tích tempo bằng công cụ bên ngoài (tùy chọn)

Trong trường hợp cuối cùng, bạn có thể phân tích track trong một DAW như Logic Pro và tự động tạo tempo map. Lưu ý rằng cách này thường tạo ra rất nhiều thay đổi tempo, đôi khi mỗi ô nhịp một lần, mức chi tiết này có thể không cần thiết cho hầu hết show.
