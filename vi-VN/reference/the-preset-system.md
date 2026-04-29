---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/the-preset-system
---

# ✅ Hệ thống Preset

Hệ thống Preset được dùng ở nhiều nơi trong Liberation, mỗi khi cần lưu nhiều thiết lập có thể chọn từ một danh sách _preset_.

Hiện hệ thống này được dùng cho:

* Thiết lập scanner
* Thiết lập hiệu chỉnh màu
* Thiết lập camera của trình hiển thị 3D
* Thiết lập laser của trình hiển thị 3D
* Hồ sơ DMX

Vì vậy, nếu bạn tinh chỉnh thiết lập scanner cho bộ scanner CT6210 mới của mình, bạn có thể lưu thiết lập đó thành một preset, đặt tên là "CT6210", và sau này preset này sẽ có trong danh sách preset cũng như menu thả xuống mỗi khi bạn cần dùng.

Tất cả preset đều được lưu cùng với project của bạn (hoặc Laser Settings), dù bạn có đang sử dụng chúng hay không. Vì vậy, mỗi khi bạn mở một trong các file này, tất cả preset bên trong sẽ được thêm vào các preset hiện có của bạn. Nếu một preset được tải vào có cùng tên với một preset hiện có, preset hiện có sẽ bị ghi đè.

Bạn cũng có thể nhập và xuất file preset bằng nút tải/lưu (biểu tượng đĩa mềm) nằm cạnh danh sách preset thả xuống. Nút này mở một cửa sổ pop-up có các nút import/export, đồng thời có tùy chọn xóa một hoặc nhiều preset của bạn.

<figure><img src="../.gitbook/assets/scanner-settings-presets.png" alt=""><figcaption><p>Menu pop-up mở ra khi bạn nhấp vào biểu tượng tải/lưu</p></figcaption></figure>

Nếu bạn chỉnh sửa một preset, ví dụ thiết lập scanner có tên _Default_, hãy lưu ý rằng các laser khác sẽ không được tự động cập nhật. Thay vào đó, thiết lập scanner của từng laser đó sẽ được gắn nhãn _Default(edited)_. Để cập nhật sang preset _Default_ mới, hãy chọn lại preset đó trong danh sách thả xuống.

{% hint style="info" %}
Nếu bạn có nhiều laser và muốn cập nhật thiết lập scanner cho tất cả, hãy dùng hệ thống _COPY LASER SETTINGS_. Xem [Sao chép cài đặt laser](../setting-up/copy-laser-settings.md)
{% endhint %}

Nếu bạn xóa một preset đang được dùng ở nơi khác, bạn sẽ không mất thiết lập đó; thay vào đó, thiết lập sẽ được gắn nhãn là _(deleted)._
