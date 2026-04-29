---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/appendix-articles/scanner-specifications-and-liberation
---

# 🟩 Thông số kỹ thuật của scanner và Liberation

### Thực tế khá rối của thông số scanner

Tốc độ điểm và thông số scanner có thể hơi khó hiểu. Bạn thường thấy các thông số như 30kpps @ 8º hoặc 50kpps @ 4º, nhưng những con số đó thực sự biểu thị điều gì thì không phải lúc nào cũng rõ ràng.

{% hint style="info" %}
Lưu ý - Tôi không phải là chuyên gia phần cứng scanner, nhưng tôi có nhiều năm kinh nghiệm thực tế trong việc làm cho các scanner thuộc nhiều mức chất lượng khác nhau hiển thị đẹp hơn bằng phần mềm và cách tạo luồng điểm, thay vì tinh chỉnh phần cứng. Nội dung này dựa trên kinh nghiệm đó.
{% endhint %}

#### **Những con số này đến từ đâu**

Các thuật ngữ như “30K” và “50K” là cách viết tắt dựa trên việc đánh giá scanner bằng mẫu kiểm tra ILDA ở các tốc độ điểm đó trong những điều kiện cụ thể.

Khi một scanner được ghi thông số kiểu như: _30Kpps @ 8°_ thì thực chất có nghĩa là:

> “Scanner này có thể tái tạo mẫu kiểm tra ILDA ở 30.000 điểm/giây tại góc quét 8°, khi được căn chỉnh đúng.”

Đây không phải là một phép đo toàn diện hoặc được chuẩn hóa đầy đủ cho hiệu năng thực tế. Thực ra ban đầu nó còn không được thiết kế như một chuẩn benchmark - nó được dùng cho **quy trình căn chỉnh**. Bạn chạy một mẫu đã biết ở tốc độ điểm cố định (ví dụ 30.000 điểm/giây), rồi điều chỉnh damping và gain cho đến khi hình hiển thị đúng.

Dù vậy, đây vẫn là chuẩn tham chiếu được dùng rộng rãi nhất mà chúng ta có, và nó có thể cho bạn hình dung khá tốt về chất lượng scanner, ít nhất là với các nhà sản xuất uy tín. Còn với những nhà sản xuất _kém uy tín hơn_ thì...

#### Nếu bạn muốn kiểm tra scanner theo đúng thông số công bố

{% hint style="danger" %}
**Đây là kỹ thuật nâng cao và bạn có thể làm hỏng scanner nếu không cẩn thận. Không khuyến nghị trừ khi bạn biết rõ mình đang làm gì.**
{% endhint %}

Bạn cần tìm phần mềm có thể xuất [mẫu kiểm tra ILDA](https://ilda.com/technical.htm?r=7950) - tôi nghĩ LaserShowGen có thể làm được - rồi điều chỉnh kích thước Output để khớp với góc quét được chỉ định (ví dụ 8°). Hãy xem tài liệu ILDA để biết cách phân tích Output.

#### Vì sao đây có thể không phải là benchmark tốt

Trước hết, mẫu kiểm tra của bạn có thể hiển thị sai ngay cả khi scanner của bạn tốt, chỉ vì chúng không được căn chỉnh theo cách tối ưu cho mẫu đó.

Nó có thể là hướng dẫn tổng quát hữu ích để phân biệt scanner “tốt” và “kém”, nhưng đôi khi nhà sản xuất có thể diễn giải các thông số này khá linh hoạt.

#### Vậy tôi nên chọn scanner tốt như thế nào?

Tôi nghĩ đơn giản là hãy đảm bảo chúng được sản xuất bởi một nhà sản xuất uy tín. Các hãng scanner cao cấp, đắt tiền như Cambridge Technology (CT), Eye Magic (EMS) và ScannerMAX (công ty con của Pangolin) luôn tốt và bạn gần như không thể chọn sai. Nhưng khi một cặp scanner có giá khoảng 1000 USD, với nhiều người mới bắt đầu thì nó còn đắt hơn cả laser của chúng ta!

Vì vậy phần lớn tôi dùng các nhà sản xuất Trung Quốc. Scanner Dragon Tiger (DT) khá ổn và giá hợp lý, và tôi nghĩ LightSpace dùng chúng. Nhiều nhà sản xuất khác (bao gồm OPT và Able ở một số mẫu) cũng dùng hệ thống dựa trên DT.

Phenix Technology (PT) thường ở phân khúc thấp hơn, nhưng nói thật là chúng có lẽ vẫn ổn cho hầu hết nhu cầu.

**Nếu scanner của bạn không có thương hiệu, đó có lẽ là lúc bạn nên lo về chất lượng!**

#### Liberation giúp như thế nào

Trước hết, với hầu hết công việc, bạn không cần scanner thật sự đắt tiền! DT 30kpps giá hợp lý, hoặc thậm chí PT, vẫn ổn. Các thiết lập scanner mặc định được đặt khá thận trọng, và nhìn chung _bạn không cần điều chỉnh chúng_ (ngoại trừ _Scanner sync_).

Ngay cả khi bạn có scanner tốt hơn, cũng không có lý do gì phải chạy chúng mạnh hơn mức cần thiết. Điều này sẽ kéo dài đáng kể tuổi thọ của chúng.

#### "Luồng điểm" là gì?

Có lẽ bạn đã nghe thuật ngữ này trước đây - đây là cách chúng ta điều khiển đường đi của scanner.

Luồng điểm là danh sách các vị trí X/Y, mỗi vị trí có một màu. Để vẽ thứ gì đó như một đường màu trắng, bạn gửi một chuỗi điểm dọc theo đường đó, tất cả được đặt màu trắng. Sau đó scanner di chuyển từ điểm này sang điểm khác với tốc độ cố định - tốc độ điểm trên giây (PPS) - và chùm tia quét thành hình dạng đó.

#### Cách hoạt động trong phần mềm laser truyền thống

Phần mềm laser truyền thống lưu một luồng điểm cho mỗi cue. Với cue có hoạt hình, điều đó thường có nghĩa là mỗi khung hình có một luồng điểm riêng. Điểm quan trọng là mọi thứ đều được xác định sẵn hoàn toàn. Vì vậy, khi tăng tốc độ điểm, scanner sẽ di chuyển nhanh hơn qua cùng một dữ liệu đã được định nghĩa trước.

{% hint style="info" %}
Với phần mềm cũ, cách này là cần thiết - máy tính đơn giản là chưa đủ nhanh để tạo luồng điểm theo thời gian thực. Đó là lý do thường có một trình biên tập cue riêng, dùng để tạo trước dữ liệu cho từng khung hình hoạt hình.

Điều này cũng giải thích vì sao nội dung có thể chiếm đến hàng gigabyte dung lượng. Về cơ bản, bạn đang lưu các dạng sóng lớn, không nén, ở tốc độ lấy mẫu khá cao.
{% endhint %}

#### Vì sao "tốc độ điểm" ít ý nghĩa hơn trong Liberation

Liberation tạo luồng điểm theo thời gian thực, nhờ đó chúng ta có rất nhiều linh hoạt. Hãy chú ý thiết lập "Scanner speed" trong panel Laser Settings. Thiết lập này cho phép chúng ta tăng hoặc giảm tốc scanner, nhưng điều quan trọng là nó **không** thay đổi tốc độ điểm (PPS) nền tảng.

#### Khoan đã, sao lại thế?

Tôi biết, lúc đầu nghe có vẻ lạ.

Vì Liberation tạo luồng điểm theo thời gian thực, nó có thể điều chỉnh luồng điểm đó. Các điểm càng cách xa nhau, scanner di chuyển càng nhanh. Các điểm càng gần nhau, scanner di chuyển càng chậm.

{% hint style="info" %}
Trong các phiên bản Liberation gần đây, _tốc độ điểm_ thực tế (trong thiết lập nâng cao) hoàn toàn không ảnh hưởng đến tốc độ scanner. Thay vào đó, renderer điều chỉnh phân bố điểm để khớp với tốc độ điểm đã chọn, đồng thời giữ nguyên chuyển động của scanner.

Điều này có ảnh hưởng đến “độ phân giải” của đường điểm, nhưng chủ yếu chỉ tạo khác biệt với đồ họa (và có thể giúp tinh chỉnh thiết lập _Scanner sync_ chính xác hơn).
{% endhint %}

#### Tuyệt! Vậy tất cả những điều này thực sự có nghĩa là gì?

Câu hỏi hay. Đây là các gợi ý của tôi:

* Tránh dùng scanner không có thương hiệu. Nếu có thể chọn scanner nhanh hơn, hãy chọn - tối thiểu 30KPPS.
* Trong hầu hết trường hợp, scanner DT30 là ổn, và scanner PT30 có lẽ cũng chấp nhận được trong các laser giá rẻ.
* Nếu bạn làm đồ họa, trong đa số trường hợp, dùng nhiều laser hơn sẽ tốt hơn là dùng scanner nhanh hơn.
* Khi bạn lên các hệ thống cao cấp hơn, bất kỳ thương hiệu cao cấp đã có tên tuổi nào cũng sẽ ổn.
* Nếu bạn chỉ có thể mua scanner không thương hiệu rẻ nhất, thiết lập mặc định của Liberation khá thận trọng và bạn có thể vẫn đạt kết quả ổn cho các hiệu ứng beam cơ bản. Nếu hệ thống gặp khó, hãy giảm thiết lập **Speed** (nhưng đừng thay đổi tốc độ điểm!).

#### Còn ILDA Test Pattern thì sao?

…vẫn rất hữu ích như một công cụ hiệu chuẩn và tham chiếu, nhưng nó chưa bao giờ được thiết kế như một benchmark toàn diện và có thể bị nhà sản xuất sử dụng sai hoặc diễn giải lỏng lẻo.
