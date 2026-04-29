---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/colour-settings-and-hsb
---

# 🟩 Cài đặt màu và HSB

Trong Liberation, màu sắc được định nghĩa bằng HSB thay vì RGB. Có thể bạn chưa quen với cách này, nhưng khi đã dùng quen, tôi thấy đây là một hệ thống trực quan hơn nhiều.

{% hint style="info" %}
Nếu bạn thích dùng RGB, bạn có thể nhấp vào ô màu trong bất kỳ cài đặt màu nào. Thao tác này sẽ mở panel chỉnh sửa màu, nơi có các tùy chọn cho RGB và HSB.
{% endhint %}

### HSB - Hue, Saturation và Brightness

#### Hue

Hue của màu có giá trị từ 0 đến 255. 0 là màu đỏ, và khi tăng giá trị, bạn sẽ đi qua mọi sắc độ trong cầu vồng: cam, vàng, lục, cyan, lam, tím, magenta, rồi quay lại đỏ tại 255.

Vì đây là một vòng lặp, bạn có thể dùng sóng tam giác để chạy qua toàn bộ các màu.

#### Saturation

Cài đặt này điều chỉnh độ bão hòa, tức độ rực của màu. Nói cách khác, màu đó _nhiều màu_ đến mức nào, với giá trị từ 0 đến 255. Đặt Saturation là 0 để có các sắc xám, và 255 để có màu cầu vồng đầy đủ. Các giá trị ở giữa sẽ cho màu pastel nhạt hơn.

{% hint style="info" %}
Xin lỗi các bạn ở Mỹ vì chữ “colour” có thêm một nguyên âm. Liberation được phát triển ở Anh nên tiếng Anh Anh là mặc định. Trong tương lai, tôi hy vọng sẽ cung cấp bản dịch sang tiếng Pháp, Tây Ban Nha, Đức, Ý, Trung giản thể, và vâng, cả tiếng Anh Mỹ nữa. :innocent:
{% endhint %}

#### Brightness

Có lẽ đây là phần dễ hiểu nhất: 0 là đen hoàn toàn, 255 là độ sáng tối đa.

### Ví dụ sử dụng

#### Vòng lặp cầu vồng :

Đặt _Brightness_ và _Saturation_ thành 255. Kết nối bộ dao động _Sawtooth_ vào cổng _Hue_, rồi điều chỉnh phạm vi của nó từ 0 đến 255.

#### Độ sáng nhấp nháy theo nhịp :

Kết nối bộ dao động _Sawtooth_ vào cổng _Brightness_, rồi điều chỉnh phạm vi của nó từ 255 đến 0. Bạn có thể tiếp tục điều chỉnh clamp min và clamp max để kiểm tra thời lượng thay đổi. Sau đó dùng các hàm easing để tinh chỉnh animation hơn nữa.

#### Nháy mạnh / strobe :

Chọn một màu bằng _Hue_ và _Saturation_ hoặc bằng cách nhấp vào bộ chọn màu. Kết nối bộ dao động _Square Wave_ vào cổng _Brightness_, rồi điều chỉnh phạm vi của nó từ 255 đến 0.

#### Chạy qua một dải Hue tùy chỉnh :

Đặt _Brightness_ và _Saturation_ thành 255. Kết nối bộ dao động _Triangle Wave_ vào cổng _Hue_, rồi điều chỉnh phạm vi của nó:

* để chuyển từ lam sang cyan, dùng phạm vi 70 đến 128
* để chuyển từ đỏ sang vàng, dùng phạm vi 0 đến 40
* để chuyển từ đỏ sang magenta, dùng phạm vi 255 đến 220
