---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/render-profile
---

# 🟩 Render Profile

Mỗi node _Creator_ đều có thiết lập _Render Profile_, dùng để xác định cách các hình được vẽ (hay _render_) bằng laser.

**Trong hầu hết trường hợp, thiết lập&#x20;**_**DEFAULT**_**&#x20;là hoàn toàn phù hợp**. Nhưng nếu bạn làm việc với đồ họa hoặc nội dung phức tạp, bạn có thể muốn kiểm soát chi tiết hơn cách từng hình được render.

{% hint style="info" %}
Khác với hầu hết phần mềm laser, Liberation tạo luồng điểm theo thời gian thực, ngay trước khi chuyển tới các laser controller. Cách này giúp tiết kiệm rất nhiều dung lượng ổ đĩa: các Clip chỉ có dung lượng vài kB, thay vì nhiều MB luồng điểm đã render sẵn.

Điều này cũng có nghĩa là bạn có thể tinh chỉnh cùng một nội dung cho các loại scanner khác nhau trên từng laser, mà không cần thay đổi chính các Clip.

Để biết thêm chi tiết, xem [Cách Liberation tạo nội dung laser](../../advanced/how-liberation-generates-laser-content.md)
{% endhint %}

Có ba _Render Profiles_ cài sẵn: _DEFAULT_, _FAST_ và _DETAIL._

_**DEFAULT**_ - profile tổng quát tốt, phù hợp nhất cho hầu hết nội dung

_**FAST** -_ nếu Clip của bạn có nhiều nội dung và một số phần chỉ là các điểm hoặc đường thẳng rất đơn giản, bạn có thể giảm hiện tượng nhấp nháy bằng cách chọn tùy chọn này.

_**DETAIL**_ - nếu bạn đang vẽ nội dung cần các góc sắc nét, hãy dùng tùy chọn này. Tuy nhiên, lưu ý rằng scanner sẽ di chuyển chậm hơn, khiến Output dễ bị nhấp nháy hơn.

{% hint style="info" %}
Trong Clip Editor, bạn có thể gán Creator vào các Render Profile khác nhau, nhưng mỗi laser sẽ xử lý các profile này tùy theo thiết lập scanner của nó. Xem [Các preset scanner](../../advanced/scanner-presets.md)
{% endhint %}
