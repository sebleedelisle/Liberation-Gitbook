---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/faq
---

# ✅ Câu hỏi thường gặp

## Phần cứng

#### **Liberation có chạy trên Windows không?**

Có - Liberation hỗ trợ đầy đủ **Windows 10 và 11 (64-bit)**, với đúng các tính năng như phiên bản Mac. Mọi bản phát hành đều được cung cấp đồng thời cho cả hai nền tảng.

#### **Liberation có chạy trên Mac không?**

Có - Liberation hỗ trợ đầy đủ **Mac (macOS 12 Monterey trở lên)**, với đầy đủ tính năng tương đương phiên bản Windows. Tất cả bản cập nhật đều được phát hành cùng lúc.

#### **Cấu hình máy tối thiểu cần có là gì?**

Điều này phụ thuộc vào số lượng laser bạn muốn điều khiển. Nếu bạn chỉ chạy vài laser, một máy cấu hình thấp là đủ. Bất kỳ máy Mac Apple Silicon nào cũng chạy rất tốt và có thể điều khiển tới 100 laser. Nếu bạn chạy các show phức tạp, yêu cầu độ ổn định cao, chúng tôi khuyên bạn dùng máy tốt nhất trong khả năng của mình.

#### **Tôi có thể điều khiển bao nhiêu laser bằng Liberation?**

Liberation có thể chạy rất nhiều laser trên một máy tính; phần mềm đã được thử nghiệm với hơn 100 laser, vì vậy câu trả lời phụ thuộc vào:

* CPU của máy tính
* tốc độ mạng
* gói giấy phép của bạn

#### **Tôi có thể dùng những MIDI controller nào?**

Liberation được thiết kế và tối ưu quanh MIDI controller phổ biến APC40 Mk2. Phần mềm cũng hoạt động với APC40 Mk1. Xem [MIDI controller dùng khi diễn live](midi-control/live-control-with-the-apc40.md)

Liberation cũng hỗ trợ APC Mini và MIDI Fighter Twister. APC40 Mk2 vẫn là controller tham chiếu đầy đủ nhất.

Ngoài ra còn có hệ thống MIDI Send/Receive để bổ sung khả năng điều khiển qua MIDI. Xem [MIDI Send/Receive](midi-control/midi-send-receive.md)

Xem [Điều khiển bằng MIDI](midi-control/) để biết thêm thông tin.

#### **Tôi có thể dùng với bất kỳ MIDI controller nào không?**

Với các controller khác, hãy dùng hệ thống MIDI Send/Receive hoặc một MIDI translator có thể gửi các thông điệp MIDI mặc định của Liberation. Tìm trên [diễn đàn](https://forum.liberationlaser.com) để xem lời khuyên về cách thiết lập này, nhưng thực tế APC40 Mk2 vẫn là lựa chọn tốt nhất cho hầu hết các show live.

## Bộ điều khiển laser

#### **Những bộ điều khiển laser nào tương thích với Liberation?**

* [Ether Dream (khuyến nghị)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (có thể bạn cần cập nhật firmware)
* LaserCube USB (và LaserDock)
* Giao thức mạng LaserCube (với kết nối có dây)
* AVB như được dùng bởi [laser LASollinger](https://laseranimation.com/en/) (hiện chỉ đang thử nghiệm trên macOS)

Xem [Laser và bộ điều khiển tương thích (DAC)](hardware/compatible-lasers-and-controllers-dacs.md) để biết thêm thông tin

#### **Vì sao bạn không hỗ trợ bộ điều khiển laser của \[hãng khác]?**

Để khuyến khích khả năng tương tác tốt hơn giữa phần mềm và phần cứng, Liberation sẽ chỉ hỗ trợ các DAC có giao thức giao tiếp được công bố. Tôi tin rằng đây là hướng đi tốt nhất cho ngành laser.

#### **Làm sao để biết laser của tôi có dùng được với Liberation không?**

Nếu laser của bạn có một trong các mục sau, bạn có thể dùng với Liberation:

* **Đầu vào ILDA** bên ngoài – đầu nối D 25-pin, dùng với một controller bên ngoài tương thích.
* **Ether Dream** được lắp bên trong.
* Bất kỳ **LaserCube** nào (hoạt động với cả LaserCube USB và Wi-Fi).
* **Thiết bị X-Laser có hệ thống Mercury tích hợp** (ở chế độ Ether Dream).
* **Máy chiếu LaserAnimation Sollinger có AVB tích hợp** (chỉ macOS, yêu cầu thiết bị mạng tương thích AVB, hiện đang thử nghiệm).

Xem [Laser và bộ điều khiển tương thích (DAC)](hardware/compatible-lasers-and-controllers-dacs.md) để biết thêm thông tin

#### **Tôi có thể dùng Liberation với LaserCube của mình không?**

Có, Liberation hoạt động trực tiếp với mọi LaserCube. Xem [LaserCube](hardware/lasercube.md)

## Giấy phép

#### **Giá giấy phép là bao nhiêu?**

Xem trang [cửa hàng](https://liberationlaser.com/shop) để biết giá hiện tại.

#### **Các gói giấy phép khác nhau ở những giới hạn nào?**

Xem trang [cửa hàng](https://liberationlaser.com/shop) để biết các tùy chọn giấy phép hiện tại.

Lưu ý rằng bạn có thể thiết lập, xem trước và thiết kế show với bao nhiêu laser tùy ý trên **mọi** gói, kể cả gói miễn phí. Hoàn toàn không có giới hạn nào khác ngoài số lượng laser mà bạn có thể _kích hoạt để xuất_. Tất cả tính năng khác của Liberation đều có sẵn cho mọi người.

#### **Tôi có thể nâng cấp lên gói mới không?**

Bạn có thể nâng cấp lên gói cao hơn bất kỳ lúc nào. Bạn sẽ được hoàn tiền một phần cho thời gian còn lại trong kỳ đã thanh toán hiện tại, và gói giấy phép mới sẽ bắt đầu ngay lập tức. Xem [Nâng cấp / hạ cấp giấy phép](installation/upgrade-downgrade-your-license.md)

#### **Tôi có thể hạ cấp giấy phép không?**

Bạn có thể hạ cấp bất kỳ lúc nào, nhưng thay đổi sẽ có hiệu lực vào cuối kỳ đã thanh toán hiện tại. Xem [Nâng cấp / hạ cấp giấy phép](installation/upgrade-downgrade-your-license.md)

#### **Tôi có thể tạm dừng thanh toán cho giấy phép không?**

Có. Giấy phép có thể được tạm dừng vào ngày đăng ký tiếp theo và khởi động lại bất kỳ lúc nào. Điều này hữu ích nếu bạn dùng phần mềm theo từng đợt, và bạn không cần nhập lại thông tin thẻ. Xem [Tạm dừng hoặc hủy thanh toán](installation/cancel-your-subscription.md)

#### **Làm sao để hủy vĩnh viễn giấy phép của tôi?**

Bạn có thể hủy giấy phép định kỳ bất kỳ lúc nào, và giấy phép sẽ tự động ngừng hoạt động vào cuối kỳ đã thanh toán hiện tại. Xem [Tạm dừng hoặc hủy thanh toán](installation/cancel-your-subscription.md)

#### **Vì sao Liberation dùng hình thức đăng ký thuê bao?**

Nói ngắn gọn, cách này giúp Liberation bền vững, được phát triển liên tục và công bằng, đồng thời vẫn cho phép mọi người mở, chỉnh sửa, lưu, luyện tập và xem trước show mà không phải trả phí.

Tôi đã viết thêm về lý do đằng sau việc này tại đây: [Vì sao Liberation dùng hình thức đăng ký thuê bao](https://liberationlaser.com/articles/why-a-subscription).

#### **Tôi có thể lấy giấy phép vĩnh viễn hoặc dài hạn cho công trình lắp đặt / tour diễn của mình không?**

Có các giấy phép trả trước theo năm (hoặc thậm chí nhiều năm) cho các công trình lắp đặt cố định và sản xuất tour diễn. Gửi email tới [billing@liberationlaser.com](mailto:billing@liberationlaser.com) nếu bạn muốn thiết lập loại giấy phép này.

Hiện chưa có giấy phép vĩnh viễn. Để biết thêm bối cảnh, xem [Vì sao Liberation dùng hình thức đăng ký thuê bao](https://liberationlaser.com/articles/why-a-subscription).

#### **Làm sao để ủy quyền máy tính bằng giấy phép của tôi?**

Sau khi mua giấy phép, bạn có thể ủy quyền máy tính ngay trong phần mềm Liberation. Bạn sẽ thấy nút _Authorise_ trên màn hình _About_; nút này sẽ nhắc bạn đăng nhập vào website. Làm theo hướng dẫn trên màn hình để hoàn tất quy trình ủy quyền. Xem [Ủy quyền và hủy ủy quyền](installation/authorising-and-de-authorising.md)

#### **Bao lâu tôi cần kết nối máy tính với internet một lần?**

Mỗi khi giấy phép trả phí định kỳ được gia hạn thành công, bạn cần kết nối Liberation với internet để cập nhật giấy phép nội bộ của phần mềm. Vì vậy, với giấy phép tự động gia hạn hằng tháng, bạn cần kết nối mỗi tháng.

#### **Điều gì xảy ra nếu tôi không thể kết nối máy tính với internet sau kỳ thanh toán tiếp theo?**

Với giấy phép trả phí định kỳ hằng tháng, Liberation thường cho bạn thời gian gia hạn 7 ngày sau khi giấy phép trả phí được gia hạn để kết nối internet và cập nhật giấy phép nội bộ. Sau thời gian đó, Liberation sẽ quay lại chế độ _Free_.

#### **Điều gì xảy ra nếu thẻ tín dụng của tôi hết hạn?**

Bạn sẽ nhận được email thông báo từ nhà cung cấp thanh toán của chúng tôi, và bạn cần cập nhật thông tin thẻ. Đăng nhập vào website và dùng _UPDATE CARD DETAILS_ trên trang giấy phép, hoặc _Update_ trong _Billing and payments_. Bạn phải thực hiện việc này trong thời gian gia hạn để tránh mất quyền truy cập các tính năng trả phí.

#### **Tôi có thể cài Liberation trên bao nhiêu máy tính?**

Bạn có thể cài Liberation trên bao nhiêu máy tính tùy ý. Chỉ cần ủy quyền giấy phép để bật đầu ra laser / DMX, và gói giấy phép của bạn quyết định có bao nhiêu máy tính có thể được ủy quyền để xuất tín hiệu cùng lúc. Xem [Cơ chế hoạt động của giấy phép](installation/how-licensing-works.md)

#### **Làm sao để chuyển giấy phép từ máy tính này sang máy tính khác?**

* Mở Liberation trên máy tính bạn không muốn dùng nữa
* Đảm bảo bạn đã kết nối internet và nhấp nút _De-authorise this computer_ trên màn hình _About_
* Bây giờ mở Liberation trên máy tính mới
* Nhấp nút _Authorise this computer_ trên màn hình _About_.
* Website sẽ mở ra; hãy đăng nhập và làm theo hướng dẫn trên màn hình để hoàn tất ủy quyền

Bạn cũng có thể hủy ủy quyền từ xa một máy tính mà bạn không còn truy cập được nữa (với một số giới hạn). Xem [Ủy quyền và hủy ủy quyền](installation/authorising-and-de-authorising.md)

#### **Tôi có thể hủy ủy quyền Liberation trên một máy tính đã bị mất hoặc bị đánh cắp không?**

Bạn có thể hủy ủy quyền máy tính qua website. Nếu bản cài đặt Liberation chưa lên mạng kể từ lần làm mới giấy phép gần nhất, việc này có thể được thực hiện ngay lập tức.

Nếu không, việc hủy ủy quyền sẽ có hiệu lực khi giấy phép được làm mới lần tiếp theo hoặc khi máy tính kết nối internet, tùy sự kiện nào xảy ra trước. Nếu bạn cần gấp việc ủy quyền lại cho một máy tính mới, hãy liên hệ bộ phận hỗ trợ.

### Sử dụng Liberation

#### Thiết lập mặc định có 8 laser - làm sao để thay đổi?

Xem [Thiết lập project của bạn](setting-up/setting-up-your-project.md) và [Thêm / gỡ laser](setting-up/adding-removing-lasers.md)

#### Tôi có thể sao chép cài đặt zone từ một laser sang các laser khác không?

Có! Xem [Sao chép zone giữa các laser](output-view/copy-zones-between-lasers.md)

#### Tôi có thể nhập số thay vì dùng thanh trượt không?

Có. `Cmd / Ctrl`-nhấp vào thanh trượt và bạn có thể nhập giá trị bằng bàn phím.

#### **Làm sao để đồng bộ Liberation với nhạc?**

Liberation có hệ thống “tap tempo” thông minh hoạt động đúng như bạn mong đợi, nhưng bạn cũng có thể dùng MIDI clock bên ngoài hoặc Ableton Link. Xem [Tempo / đồng bộ hóa](tempo-synchronisation.md). Timeline có thể được đồng bộ với timecode LTC/SMPTE đầu vào qua bất kỳ giao diện âm thanh nào. Xem [Timecode](timecode.md).

#### Tôi cần điều chỉnh cài đặt nào để có đầu ra tốt nhất từ laser?

Cài đặt chính là _Scanner Sync,_ dùng để bù độ trễ nhỏ giữa lúc gương di chuyển và lúc laser thay đổi độ sáng. Nếu các chấm/tia laser của bạn có “đuôi” nhỏ, bạn cần điều chỉnh mục này. (Xem ảnh trên trang [Bảng cài đặt đầu ra laser](setting-up/laser-settings.md) để xem ví dụ về “đuôi”)

Bạn cũng có thể thử thay đổi tốc độ scanner: chậm hơn nếu scanner của bạn cơ bản, hoặc nhanh hơn nếu scanner tốt. Nhưng **hãy thận trọng vì bạn có thể làm hỏng scanner nếu điều khiển chúng quá mạnh.**

Ngoài ra còn có một số cài đặt scanner đặt sẵn. Tùy chọn mặc định khá an toàn và phù hợp với hầu hết yêu cầu laser beam. Nhưng cũng có các preset khác nếu bạn có scanner tốt hơn, và có các preset được tinh chỉnh cho đồ họa.

Để biết thêm thông tin, xem [Bảng cài đặt đầu ra laser](setting-up/laser-settings.md), và để biết cách tạo preset riêng, xem [◼️ Preset scanner & render profile](advanced/scanner-presets.md) (nâng cao, đang hoàn thiện)

Bạn cũng có thể hiệu chỉnh cân bằng màu bằng cài đặt _Colour calibration_. Xem [Hiệu chỉnh màu](advanced/colour-calibration.md) (kỹ thuật nâng cao)

#### Cài đặt _Latency(ms)_ có tác dụng gì?

Đây là độ trễ frame, tức khoảng thời gian tối đa từ khi một frame được tạo đến khi frame đó được gửi đến laser. Bạn thường không cần điều chỉnh mục này, nhưng nếu gặp vấn đề mạng, bạn có thể thử tăng giá trị. Xem [Cài đặt độ trễ](setting-up/latency-setting.md) để biết thêm chi tiết.

### Clips

#### Làm sao để điều chỉnh zone và cài đặt cho một Clip mà không chạy Clip đó?

`Alt / Option`-nhấp để đặt Clip đó làm _Clip đang được chọn_ nhưng không kích hoạt nó. Xem thêm [Bắt đầu / dừng Clip](clips/starting-stopping-clips.md)

#### Làm sao để sao chép Clip?

Nhấp và kéo trong khi giữ phím `Alt / Option`. Xem thêm [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md)

#### Làm sao để xóa Clip?

Nhấp và kéo chúng ra khỏi Clip Deck. Xem thêm [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md)

#### Làm sao để chọn nhiều mục, xóa, kết hợp Clip Deck, v.v.?

Xem [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md)

#### Biểu tượng micro nhỏ và các biểu tượng khác trên Clip có ý nghĩa gì?

Chúng cho biết Clip đó nhận đầu vào âm thanh hoặc MIDI, và 3 chấm cho biết có độ trễ zone. Xem [Các biểu tượng nhỏ trên nút Clip là gì?](clips/what-are-the-small-icons-on-the-clip-buttons.md)
