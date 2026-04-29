---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Câu hỏi thường gặp

## Phần cứng

#### **Liberation có chạy trên Windows không?**

Có - Liberation hỗ trợ đầy đủ **Windows 10 và 11 (64-bit)**, với đúng cùng bộ tính năng như phiên bản Mac. Mọi bản phát hành đều được cung cấp đồng thời cho cả hai nền tảng.

#### **Liberation có chạy trên Mac không?**

Có - Liberation hỗ trợ đầy đủ **Mac (macOS 12 Monterey trở lên)**, với đầy đủ tính năng tương đương phiên bản Windows. Tất cả bản cập nhật đều được phát hành cùng lúc.

#### **Cần máy có cấu hình tối thiểu như thế nào?**

Điều này phụ thuộc vào số lượng laser bạn muốn điều khiển. Nếu bạn chỉ chạy vài laser, một máy cấu hình thấp vẫn đủ dùng. Mọi máy Mac dùng Apple Silicon đều chạy rất tốt và có thể điều khiển tới 100 laser. Nếu bạn chạy các show phức tạp, yêu cầu độ tin cậy cao, chúng tôi khuyên dùng máy tốt nhất trong khả năng của bạn.

#### **Tôi có thể điều khiển bao nhiêu laser bằng Liberation?**

Liberation có thể chạy nhiều laser trên một máy tính; phần mềm đã được thử nghiệm với hơn 100 laser controllers, nên câu trả lời phụ thuộc vào:

* CPU của máy tính
* tốc độ mạng
* loại gói đăng ký của bạn

#### **Tôi có thể dùng những MIDI controller nào?**

Liberation được thiết kế và tối ưu quanh MIDI controller phổ biến APC40 Mk2. Phần mềm cũng hoạt động với APC40 Mk1. Xem [Điều khiển trực tiếp bằng APC40](midi-control/live-control-with-the-apc40.md)

Chúng tôi đang bổ sung dần thêm các MIDI controller và hiện cũng hỗ trợ APC Mini Mk2 cùng MIDI Fighter Twister.

Ngoài ra còn có hệ thống MIDI Send/Receive, cung cấp thêm khả năng điều khiển qua MIDI. Xem [MIDI Send/Receive](midi-control/midi-send-receive.md)

Xem [Điều khiển bằng MIDI](midi-control/) để biết thêm thông tin.

#### **Tôi có thể dùng phần mềm với bất kỳ MIDI controller nào không?**

Hiện chúng tôi đang phát triển một hệ thống MIDI có thể cấu hình để hỗ trợ việc này trong tương lai. Trong lúc đó, một số người dùng đã thành công khi dùng bộ diễn dịch MIDI để chuyển đổi bất kỳ thông điệp MIDI nào cho hệ thống MIDI Send/Receive, nhưng đây là quy trình khá rườm rà và nâng cao. Hãy tìm trên [diễn đàn](https://forum.liberationlaser.com) để xem lời khuyên về cách thiết lập này, nhưng thực tế APC40 vẫn là lựa chọn tốt nhất.

## Laser controllers

#### **Những laser controller nào tương thích với Liberation?**

* [Ether Dream (khuyến nghị)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (có thể bạn cần cập nhật firmware)
* LaserCube USB (và LaserDock)
* Giao thức mạng LaserCube (với kết nối có dây)
* AVB như được dùng bởi [laser LASollinger](https://laseranimation.com/en/) (hiện chỉ đang thử nghiệm trên macOS)

Xem [Laser và controller/DAC tương thích](hardware/compatible-lasers-and-controllers-dacs.md) để biết thêm thông tin

#### **Vì sao các bạn không hỗ trợ laser controller của \[hãng khác]?**

Để khuyến khích khả năng tương tác tốt hơn giữa phần mềm và phần cứng, Liberation sẽ chỉ hỗ trợ các DAC có giao thức giao tiếp được công bố. Tôi tin rằng đây là hướng đi tốt nhất cho ngành laser.

#### **Làm sao biết laser của tôi có dùng được với Liberation không?**

Nếu laser của bạn có một trong các mục sau, bạn có thể dùng nó với Liberation:

* **Ngõ vào ILDA** bên ngoài – đầu nối D 25 chân, dùng với controller ngoài tương thích.
* **Ether Dream** được lắp sẵn bên trong.
* Bất kỳ **LaserCube** nào (hoạt động với cả LaserCube USB và Wi-Fi).
* **Thiết bị X-Laser có hệ thống Mercury tích hợp** (ở chế độ Ether Dream).
* **Máy chiếu LaserAnimation Sollinger có AVB tích hợp** (chỉ macOS, yêu cầu thiết bị mạng tương thích AVB, hiện đang thử nghiệm).

Xem [Laser và controller/DAC tương thích](hardware/compatible-lasers-and-controllers-dacs.md) để biết thêm thông tin

#### **Tôi có thể dùng Liberation với LaserCube của mình không?**

Có, Liberation hoạt động trực tiếp với mọi LaserCube. Xem [LaserCube](hardware/lasercube.md)

## Giấy phép

#### **Giá giấy phép là bao nhiêu?**

Xem trang [cửa hàng](https://liberationlaser.com/shop) để biết giá hiện tại.

#### **Các giới hạn giữa các gói giấy phép là gì?**

Xem trang [cửa hàng](https://liberationlaser.com/shop) để biết các tùy chọn giấy phép hiện tại.

Lưu ý rằng bạn có thể thiết lập, xem trước và thiết kế show với bao nhiêu laser tùy ý ở **mọi** gói, kể cả gói miễn phí. Ngoài số lượng laser bạn có thể _arm_, không có giới hạn nào khác. Mọi tính năng khác của Liberation đều khả dụng cho tất cả người dùng.

#### **Tôi có thể nâng cấp lên gói mới không?**

Bạn có thể nâng cấp lên gói cao hơn bất cứ lúc nào. Bạn sẽ nhận được khoản hoàn tiền một phần cho thời gian còn lại của giấy phép hiện tại, và gói mới sẽ bắt đầu ngay lập tức. Xem [Nâng cấp hoặc hạ cấp giấy phép](installation/upgrade-downgrade-your-license.md)

#### **Tôi có thể hạ cấp giấy phép không?**

Bạn có thể hạ cấp bất cứ lúc nào, nhưng thay đổi sẽ có hiệu lực vào cuối kỳ giấy phép hiện tại. Xem [Nâng cấp hoặc hạ cấp giấy phép](installation/upgrade-downgrade-your-license.md)

#### **Làm sao để ủy quyền máy tính bằng giấy phép của tôi?**

Sau khi mua giấy phép, bạn có thể ủy quyền máy tính ngay trong phần mềm Liberation. Bạn sẽ thấy nút _Authorise_ trên màn hình _About_; nút này sẽ yêu cầu bạn đăng nhập vào website. Làm theo hướng dẫn trên màn hình để hoàn tất quy trình ủy quyền. Xem [Ủy quyền và hủy ủy quyền](installation/authorising-and-de-authorising.md)

#### **Bao lâu tôi cần kết nối máy tính với internet một lần?**

Mỗi khi giấy phép gia hạn, bạn cần kết nối Liberation với internet để cập nhật giấy phép nội bộ. Với thanh toán định kỳ hằng tháng, bạn sẽ cần kết nối mỗi tháng.

#### **Điều gì xảy ra nếu tôi không thể kết nối máy tính với internet sau khi gia hạn?**

Liberation sẽ cho bạn thời gian gia hạn 7 ngày sau khi giấy phép được gia hạn để kết nối internet và cập nhật giấy phép nội bộ. Sau thời gian đó, Liberation sẽ quay lại chế độ _Free_.

#### **Điều gì xảy ra nếu thẻ tín dụng của tôi hết hạn?**

Bạn sẽ nhận được email thông báo từ nhà cung cấp thanh toán của chúng tôi và cần cập nhật phương thức thanh toán. Đăng nhập vào website và dùng liên kết _Update payment details_ trên trang đăng ký.

#### **Làm sao để hủy giấy phép định kỳ?**

Đăng nhập vào website, mở trang _Your subscriptions_, chọn đăng ký bạn muốn hủy, rồi nhấp liên kết _Cancel Subscription_. Bạn vẫn có thể tiếp tục dùng Liberation cho đến hết thời hạn giấy phép còn lại.

#### **Tôi có thể cài Liberation trên bao nhiêu máy tính?**

Bạn có thể cài Liberation trên bao nhiêu máy tính tùy ý. Việc ủy quyền giấy phép chỉ cần thiết để bật đầu ra laser / DMX, và gói giấy phép của bạn quyết định có bao nhiêu máy tính có thể được ủy quyền cho đầu ra cùng lúc. Xem [Cách hoạt động của giấy phép](installation/how-licensing-works.md)

#### **Làm sao để chuyển giấy phép từ máy tính này sang máy tính khác?**

* Mở Liberation trên máy tính bạn không còn muốn dùng nữa
* Đảm bảo bạn đang kết nối internet và nhấp nút _De-authorise this computer_ trên màn hình _About_
* Bây giờ mở Liberation trên máy tính mới
* Nhấp nút _Authorise this computer_ trên màn hình _About_.
* Website sẽ mở ra; đăng nhập và làm theo hướng dẫn trên màn hình để hoàn tất ủy quyền

Bạn cũng có thể hủy ủy quyền từ xa một máy tính mà bạn không còn truy cập được nữa (với một số giới hạn). Xem [Ủy quyền và hủy ủy quyền](installation/authorising-and-de-authorising.md)

#### **Tôi có thể hủy ủy quyền Liberation trên máy tính bị mất hoặc bị đánh cắp không?**

Bạn có thể hủy ủy quyền máy tính qua website. Nếu bản cài đặt Liberation chưa từng online kể từ lần gia hạn gần nhất, việc này có thể được thực hiện ngay lập tức.

Nếu không, việc hủy ủy quyền sẽ có hiệu lực khi đăng ký gia hạn hoặc khi máy tính kết nối internet, tùy điều kiện nào xảy ra trước. Nếu bạn cần gấp để ủy quyền lại cho máy tính mới, hãy liên hệ bộ phận hỗ trợ.

### Sử dụng Liberation

#### Thiết lập mặc định có 8 laser - làm sao để thay đổi?

Xem [Thiết lập dự án của bạn](setting-up/setting-up-your-project.md) và [Thêm và xóa laser](setting-up/adding-removing-lasers.md)

#### Tôi có thể sao chép thiết lập zone từ một laser sang các laser khác không?

Có! Xem [Sao chép zones giữa các laser](output-view/copy-zones-between-lasers.md)

#### Tôi có thể nhập số thay vì dùng thanh trượt không?

Có. `Cmd / Ctrl`-click vào thanh trượt và bạn có thể nhập giá trị bằng bàn phím.

#### **Làm sao để đồng bộ Liberation với nhạc?**

Liberation có hệ thống "tap tempo" thông minh, hoạt động đúng như bạn mong đợi, nhưng bạn cũng có thể dùng MIDI clock ngoài hoặc Ableton Link. Xem [Đồng bộ tempo](tempo-synchronisation.md). Timeline có thể đồng bộ với LTC/SMPTE timecode đầu vào qua bất kỳ audio interface nào. Xem [Timecode](timecode.md).

#### Tôi cần điều chỉnh thiết lập nào để có đầu ra tốt nhất từ laser?

Thiết lập chính là _Colour Shift_, dùng để bù độ trễ nhỏ giữa thời điểm gương di chuyển và thời điểm laser thay đổi độ sáng. Nếu các chấm/tia laser của bạn có những “đuôi” nhỏ thì bạn cần điều chỉnh thiết lập này. (Xem ảnh trên trang [Laser Settings](setting-up/laser-settings.md) để xem ví dụ về “đuôi”)

Bạn cũng có thể thử thay đổi tốc độ scanner: chậm hơn nếu scanner của bạn là loại cơ bản, hoặc nhanh hơn nếu scanner tốt. Nhưng **hãy dùng cẩn thận vì bạn có thể làm hỏng scanner nếu đẩy chúng chạy quá tải.**

Ngoài ra còn có một số preset scanner. Tùy chọn mặc định khá an toàn và phù hợp với hầu hết nhu cầu tia laser. Nhưng cũng có các preset khác nếu bạn có scanner tốt hơn, và có các preset được tinh chỉnh cho đồ họa.

Để biết thêm thông tin, xem [Laser Settings](setting-up/laser-settings.md); và để biết cách tạo preset riêng, xem [Preset scanner](advanced/scanner-presets.md) (nâng cao, đang hoàn thiện)

Bạn cũng có thể hiệu chỉnh cân bằng màu bằng các thiết lập _Colour calibration_. Xem [Hiệu chuẩn màu](advanced/colour-calibration.md)(kỹ thuật nâng cao)

#### Thiết lập _Latency(ms)_ có tác dụng gì?

Đây là độ trễ khung hình, tức khoảng thời gian tối đa từ khi một frame được tạo cho đến khi frame đó được gửi tới laser. Thông thường bạn không cần điều chỉnh, nhưng nếu gặp vấn đề mạng, bạn có thể thử tăng giá trị này. Xem [Thiết lập Latency](setting-up/latency-setting.md) để biết thêm chi tiết.

### Clips

#### Làm sao để điều chỉnh zones và thiết lập cho một Clip mà không chạy Clip đó?

`Alt / Option`-click để đặt Clip đó làm _currently selected clip_ nhưng không kích hoạt nó. Xem thêm [Bắt đầu và dừng Clips](clips/starting-stopping-clips.md)

#### Làm sao để sao chép Clips?

Nhấp và kéo trong khi giữ phím `Alt / Option`. Xem thêm [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md)

#### Làm sao để xóa Clips?

Nhấp và kéo chúng ra khỏi Clip Deck. Xem thêm [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md)

#### Làm sao để chọn nhiều mục, xóa, kết hợp Clip Deck, v.v.?

Xem [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md)

#### Biểu tượng micro nhỏ và các biểu tượng khác trên Clip cho biết điều gì?

Chúng cho bạn biết rằng Clip nhận âm thanh hoặc MIDI input, còn 3 dấu chấm cho biết có zone delay. Xem [Các biểu tượng nhỏ trên nút Clip có ý nghĩa gì?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
