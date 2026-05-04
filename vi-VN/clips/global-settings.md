---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clips/global-settings
---

# 🟩 Biến đổi toàn cục

Ngoài các biến đổi của Clip (shift x/y, scale x/y), còn có Global Transformations áp dụng cho mọi Clip bạn chạy. Mở panel _Global Transformations_ để xem các thiết lập này. (Panel này thường nằm trong một tab cạnh _Clip Settings_).

Theo mặc định, tất cả các thiết lập này sẽ được đặt lại ngay khi không còn Clip nào đang phát. Bạn có thể tắt hành vi tự đặt lại này bằng nút _AUTO RESET_ ở cuối panel _Global Transformations_.

{% hint style="info" %}
Lưu ý rằng Global Transformations không ảnh hưởng đến bất kỳ nội dung nào trong canvas, mà chỉ ảnh hưởng đến beam zone và DMX zone.
{% endhint %}

### Scale X/Y

Tỷ lệ theo chiều ngang và chiều dọc; hai giá trị này được khóa cùng nhau trừ khi bạn nhấn `Shift`. Theo mặc định, các giá trị này cũng được gán vào núm APC40 Device Control 4 và 8, đồng thời xuất hiện trong panel Parameters theo ngữ cảnh ở bên phải Clip Deck.

### Shift X/Y

Dịch chuyển theo chiều ngang và chiều dọc. Di chuyển toàn bộ nội dung theo phương ngang / dọc.

### Spin

Xoay toàn bộ nội dung quanh tâm. Giá trị dương xoay theo chiều kim đồng hồ, giá trị âm xoay ngược chiều kim đồng hồ. Bạn sẽ thấy thiết lập này ảnh hưởng đến biến đổi _Rotation_. Theo mặc định, thiết lập này được gán vào núm APC40 Device Control 3 và xuất hiện trong panel Parameters theo ngữ cảnh ở bên phải Clip Deck.

### Spin 3D

Xoay toàn bộ nội dung quanh trục Y (là một đường thẳng đứng ở giữa). Bạn sẽ thấy thiết lập này ảnh hưởng đến biến đổi _Rotation3D_. Theo mặc định, thiết lập này được gán vào núm APC40 Device Control 7 và xuất hiện trong panel Parameters theo ngữ cảnh ở bên phải Clip Deck.

### Rotation

Xoay quanh tâm, giá trị tính bằng độ.

### Rotation 3D

Xoay quanh trục Y (là một đường thẳng đứng ở giữa), giá trị tính bằng độ.

### Auto reset

Khi bật, thiết lập này sẽ đặt lại tất cả Global Transformations ngay khi mọi Clip đang chạy được tắt. Nhờ vậy, bạn có thể chắc chắn rằng lần sau khi chạy Clip sẽ không gặp bất ngờ nào!
