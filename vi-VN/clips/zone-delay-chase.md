---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/zone-delay-chase
---

# 🟩 Zone delay / chase

Ai cũng đồng ý rằng càng nhiều laser thì càng vui, nhưng nếu tất cả đều làm y hệt nhau, bạn sẽ bỏ lỡ nhiều khả năng sáng tạo.

Hệ thống zone delay là một cách đơn giản nhưng hiệu quả để tạo sự đa dạng giữa các zones, và có thể tận dụng rất tốt một cấu hình nhiều laser. Bạn cũng có thể dùng nó để tạo hiệu ứng chase truyền thống hơn.

#### Cách hoạt động

_Zone delay_ thêm độ trễ vào thời gian của Clip trên từng zone, tạo ra một kiểu quét qua các zones.

Zone delay đặc biệt hiệu quả khi được đưa vào một Clip đang chạy. Hãy dùng control tương ứng trên APC40 để điều chỉnh mức và pattern. (Xem [Tham khảo APC40](../reference/apc40-reference.md)). Hoặc bạn có thể dùng panel _Clip Settings_.

Cài đặt zone delay:

* **Zone delay** - điều khiển lượng thời gian trễ áp dụng cho từng zone, được đo theo nốt 1/64.
* **Pattern** - chọn thứ tự zone
  * Left to right
  * Right to left
  * Inside to outside
  * Outside to inside

{% hint style="info" %}
Pattern hoạt động dựa trên số thứ tự zone và giả định rằng các zones của bạn được sắp xếp từ trái sang phải. Khi tính pattern, zone delay xem canvas zones và DMX zones là các nhóm riêng biệt.
{% endhint %}

* **Delay mode**
  1. No delay - dùng tùy chọn này trong chase mode
  2. Delay - chế độ mặc định, làm trễ thời gian của từng zone
  3. Delay with re-trigger - đặt lại Clip về đầu mỗi lần đi qua pattern. Tùy chọn này phù hợp với _Chase mode_.
* **Chase mode** - khi bật chase mode, mỗi zone sẽ được bật và tắt giống như một hiệu ứng chase truyền thống. Điều chỉnh cách chase hiển thị bằng các cài đặt _Fade in, Hold,_ và _Fade out_. Các cài đặt này được đặt theo tỷ lệ của giá trị zone delay, vì vậy giá trị 1 sẽ có cùng thời lượng với giá trị đã chỉ định trong _Zone delay_. Phần này hơi khó giải thích, nên lời khuyên của tôi là bạn hãy tự thử trực tiếp.

{% hint style="info" %}
Zone delay cũng được áp dụng cho mọi hiệu ứng đang hoạt động. Ví dụ, hiệu ứng nhấp nháy cũng sẽ bị trễ giữa các zones, giống như animation bên trong chính Clip.
{% endhint %}

Khi một Clip có bất kỳ kiểu _Zone delay_ nào, bạn sẽ thấy biểu tượng ba chấm ở góc trên bên phải của Clip. Các chấm này được animate để cho biết kiểu _Zone delay_ của Clip đó. Xem [Các biểu tượng nhỏ trên các nút Clip là gì?](what-are-the-small-icons-on-the-clip-buttons.md) để biết thêm chi tiết.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-21 at 10.00.14.png" alt=""><figcaption><p>Biểu tượng ba chấm cho biết một Clip có zone delay và chế độ của nó</p></figcaption></figure>

{% hint style="info" %}
Zone delay là cài đặt thuộc về từng Clip; nó không phải cài đặt global. Đây là một phần trong thiết kế sáng tạo của Clip.
{% endhint %}
