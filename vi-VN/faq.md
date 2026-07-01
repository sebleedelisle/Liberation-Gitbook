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

Điều này phụ thuộc vào số lượng laser bạn muốn điều khiển. Nếu bạn chỉ chạy vài laser, một máy cấu hình thấp là đủ. Bất kỳ máy Mac Apple Silicon nào cũng chạy rất tốt và có thể điều khiển tới 100 laser. Nếu bạn chạy các show phức tạp, yêu cầu độ tin cậy cao, chúng tôi khuyên bạn dùng máy tốt nhất trong khả năng của mình.

#### **Tôi có thể điều khiển bao nhiêu laser bằng Liberation?**

Liberation có thể chạy nhiều laser trên một máy tính. Phần mềm đã được thử nghiệm với hơn 100 bộ điều khiển laser, nên câu trả lời phụ thuộc vào:

* CPU của máy tính
* tốc độ mạng
* gói licence của bạn

#### **Tôi có thể dùng những MIDI controller nào?**

Liberation được thiết kế và tối ưu quanh MIDI controller APC40 Mk2 phổ biến. Phần mềm cũng hoạt động với APC40 Mk1. Xem [MIDI controller live](midi-control/live-control-with-the-apc40.md "mention")

Liberation cũng hỗ trợ APC Mini và MIDI Fighter Twister. APC40 Mk2 vẫn là controller tham chiếu đầy đủ nhất.

Ngoài ra còn có hệ thống MIDI Send/Receive, cung cấp thêm khả năng điều khiển bằng MIDI. Xem [MIDI Send/Receive](midi-control/midi-send-receive.md "mention")

Xem [Điều khiển bằng MIDI](midi-control/ "mention") để biết thêm thông tin.

#### **Tôi có thể dùng với bất kỳ MIDI controller nào không?**

Với các controller khác, hãy dùng hệ thống MIDI Send/Receive hoặc một MIDI translator có thể gửi các thông điệp MIDI mặc định của Liberation. Hãy tìm trên [diễn đàn](https://forum.liberationlaser.com) để xem lời khuyên về cách thiết lập này, nhưng trên thực tế APC40 Mk2 vẫn là lựa chọn tốt nhất cho hầu hết các show live.

## Bộ điều khiển laser

#### **Những bộ điều khiển laser nào tương thích với Liberation?**

* [Ether Dream (khuyến nghị)](https://ether-dream.com)
* [Helios DAC](https://bitlasers.com/helios-laser-dac/)
* [Mercury by X-Laser](https://x-laser.com/pages/mercury-laser-control-system) (có thể bạn cần cập nhật firmware)
* LaserCube USB (và LaserDock)
* Giao thức mạng LaserCube (với kết nối có dây)
* AVB như được dùng bởi [laser LASollinger](https://laseranimation.com/en/) (hiện chỉ đang thử nghiệm trên macOS)

Xem [Laser và bộ điều khiển tương thích (DAC)](hardware/compatible-lasers-and-controllers-dacs.md "mention") để biết thêm thông tin

#### **Vì sao Liberation không hỗ trợ bộ điều khiển laser của \[hãng khác]?**

Để khuyến khích khả năng tương tác tốt hơn giữa phần mềm và phần cứng, Liberation chỉ hỗ trợ các DAC có giao thức truyền thông được công bố. Tôi tin rằng đây là hướng đi tốt nhất cho ngành laser.

#### **Làm sao biết laser của tôi có dùng được với Liberation không?**

Nếu laser của bạn có một trong các mục sau, bạn có thể dùng với Liberation:

* **Đầu vào ILDA** bên ngoài – đầu nối D 25-pin, dùng với bộ điều khiển ngoài tương thích.
* **Ether Dream** được lắp bên trong.
* Bất kỳ **LaserCube** nào (hoạt động với cả LaserCube USB và Wi-Fi).
* **Thiết bị X-Laser có hệ thống Mercury tích hợp** (ở chế độ Ether Dream).
* **Máy chiếu LaserAnimation Sollinger có AVB tích hợp** (chỉ macOS, yêu cầu thiết bị mạng tương thích AVB, hiện đang thử nghiệm).

Xem [Laser và bộ điều khiển tương thích (DAC)](hardware/compatible-lasers-and-controllers-dacs.md "mention") để biết thêm thông tin

#### **Tôi có thể dùng Liberation với LaserCube của mình không?**

Có, Liberation hoạt động trực tiếp với bất kỳ LaserCube nào. Xem [LaserCube](hardware/lasercube.md "mention")

## Licence

#### **Giá licence là bao nhiêu?**

Xem trang [cửa hàng](https://liberationlaser.com/shop) để biết giá hiện tại.

#### **Các giới hạn giữa các gói licence là gì?**

Xem trang [cửa hàng](https://liberationlaser.com/shop) để biết các lựa chọn licence hiện tại.

Lưu ý rằng bạn có thể thiết lập, preview và thiết kế show với bao nhiêu laser tùy ý ở **mọi** gói, kể cả gói miễn phí. Hoàn toàn không có giới hạn nào khác ngoài số lượng laser mà bạn có thể _arm_. Mọi tính năng khác của Liberation đều có sẵn cho tất cả người dùng.

#### **Tôi có thể nâng cấp lên gói mới không?**

Bạn có thể nâng cấp lên gói cao hơn bất kỳ lúc nào. Bạn sẽ được hoàn lại một phần cho thời gian còn lại trong kỳ đã thanh toán hiện tại, và gói licence mới sẽ bắt đầu ngay lập tức. Xem [Nâng cấp / hạ cấp licence](installation/upgrade-downgrade-your-license.md "mention")

#### **Tôi có thể hạ cấp licence không?**

Bạn có thể hạ cấp bất kỳ lúc nào, nhưng thay đổi sẽ có hiệu lực khi kết thúc kỳ đã thanh toán hiện tại. Xem [Nâng cấp / hạ cấp licence](installation/upgrade-downgrade-your-license.md "mention")

#### **Tôi có thể tạm dừng thanh toán licence không?**

Có. Licence có thể được tạm dừng vào ngày đăng ký tiếp theo và khởi động lại bất kỳ lúc nào. Việc này hữu ích nếu bạn sử dụng theo từng giai đoạn, và bạn không cần nhập lại thông tin thẻ. Xem [Tạm dừng hoặc hủy thanh toán](installation/cancel-your-subscription.md "mention")

#### **Làm sao để hủy licence vĩnh viễn?**

Bạn có thể hủy licence định kỳ bất kỳ lúc nào, và licence sẽ tự động ngừng kích hoạt khi kết thúc kỳ đã thanh toán hiện tại. Xem [Tạm dừng hoặc hủy thanh toán](installation/cancel-your-subscription.md "mention")

#### **Làm sao để authorise máy tính bằng licence của tôi?**

Sau khi mua licence, bạn có thể authorise máy tính ngay trong phần mềm Liberation. Bạn sẽ thấy nút _Authorise_ trên màn hình _About_; nút này sẽ yêu cầu bạn đăng nhập vào website. Làm theo hướng dẫn trên màn hình để hoàn tất quá trình authorisation. Xem [Authorise và de-authorise](installation/authorising-and-de-authorising.md "mention")

#### **Tôi cần kết nối máy tính với internet bao lâu một lần?**

Mỗi khi licence trả phí định kỳ được gia hạn thành công, bạn cần kết nối Liberation với internet để cập nhật licence nội bộ của phần mềm. Vì vậy, với licence tự động gia hạn hằng tháng, bạn cần kết nối mỗi tháng.

#### **Điều gì xảy ra nếu tôi không thể kết nối máy tính với internet sau lần thanh toán tiếp theo?**

Với licence trả phí định kỳ hằng tháng, Liberation thường cho bạn thời gian gia hạn 7 ngày sau khi licence trả phí được gia hạn để kết nối internet và cập nhật licence nội bộ. Sau thời gian đó, Liberation sẽ quay lại chế độ _Free_.

#### **Điều gì xảy ra nếu thẻ tín dụng của tôi hết hạn?**

Bạn sẽ nhận được email thông báo từ nhà cung cấp thanh toán của chúng tôi, và bạn cần cập nhật thông tin thẻ. Đăng nhập vào website và dùng _UPDATE CARD DETAILS_ trên trang licence, hoặc _Update_ trong _Billing and payments_. Bạn phải thực hiện trong thời gian gia hạn để tránh mất quyền truy cập các tính năng trả phí.

#### **Tôi có thể cài Liberation trên bao nhiêu máy tính?**

Bạn có thể cài Liberation trên bao nhiêu máy tính tùy ý. Authorisation licence chỉ cần thiết để bật đầu ra laser / DMX, và gói licence của bạn quyết định số máy tính có thể được authorise cho đầu ra cùng lúc. Xem [Cách licence hoạt động](installation/how-licensing-works.md "mention")

#### **Làm sao để chuyển licence từ máy tính này sang máy tính khác?**

* Mở Liberation trên máy tính bạn không muốn dùng nữa
* Đảm bảo bạn đang kết nối internet và nhấp nút _De-authorise this computer_ trên màn hình _About_
* Bây giờ mở Liberation trên máy tính mới
* Nhấp nút _Authorise this computer_ trên màn hình _About_.
* Website sẽ mở ra; hãy đăng nhập và làm theo hướng dẫn trên màn hình để hoàn tất authorisation

Bạn cũng có thể de-authorise từ xa một máy tính mà bạn không còn truy cập được nữa (có một số giới hạn). Xem [Authorise và de-authorise](installation/authorising-and-de-authorising.md "mention")

#### **Tôi có thể deauthorise Liberation trên máy tính bị mất hoặc bị đánh cắp không?**

Bạn có thể deauthorise máy tính qua website. Nếu bản cài đặt Liberation chưa online kể từ lần làm mới licence gần nhất, việc này có thể thực hiện ngay lập tức.

Nếu không, việc deauthorise sẽ có hiệu lực khi licence được làm mới lần tiếp theo hoặc khi máy tính kết nối internet, tùy điều kiện nào đến trước. Nếu bạn cần gấp để re-authorise một máy tính mới, hãy liên hệ bộ phận hỗ trợ.

### Sử dụng Liberation

#### Thiết lập mặc định có 8 laser - làm sao để thay đổi?

Xem [Thiết lập project của bạn](setting-up/setting-up-your-project.md "mention") và [Thêm / xóa laser](setting-up/adding-removing-lasers.md "mention")

#### Tôi có thể sao chép thiết lập zone từ một laser sang các laser khác không?

Có! Xem [Sao chép zone giữa các laser](output-view/copy-zones-between-lasers.md "mention")

#### Tôi có thể nhập số thay vì dùng thanh trượt không?

Có. `Cmd / Ctrl`-click vào thanh trượt và bạn có thể nhập giá trị bằng bàn phím.

#### **Làm sao để đồng bộ Liberation với nhạc?**

Phần mềm có hệ thống "tap tempo" thông minh hoạt động đúng như bạn mong đợi, nhưng bạn cũng có thể dùng MIDI clock ngoài hoặc Ableton Link. Xem [Tempo / đồng bộ hóa](tempo-synchronisation.md "mention"). Timeline có thể được đồng bộ với timecode LTC/SMPTE đầu vào qua bất kỳ audio interface nào. Xem [Timecode](timecode.md "mention").

#### Tôi cần điều chỉnh thiết lập nào để có đầu ra tốt nhất từ laser?

Thiết lập chính là _Scanner Sync,_ dùng để bù độ trễ nhỏ giữa việc gương di chuyển và laser thay đổi độ sáng. Nếu các điểm/tia laser của bạn có những “đuôi” nhỏ, bạn sẽ cần điều chỉnh mục này. (Xem ảnh trên trang [Bảng thiết lập đầu ra laser](setting-up/laser-settings.md "mention") để xem ví dụ về “đuôi”)

Bạn cũng có thể thử thay đổi tốc độ scanner: chậm hơn nếu scanner của bạn cơ bản, hoặc nhanh hơn nếu scanner tốt. Nhưng **hãy dùng cẩn thận vì bạn có thể làm hỏng scanner nếu điều khiển chúng quá mạnh.**

Ngoài ra còn có một số preset thiết lập scanner. Tùy chọn mặc định khá thận trọng và phù hợp với hầu hết yêu cầu laser beam. Nhưng cũng có các preset khác nếu bạn có scanner tốt hơn, và có các preset được tinh chỉnh cho đồ họa.

Để biết thêm thông tin, xem [Bảng thiết lập đầu ra laser](setting-up/laser-settings.md "mention"); và để biết cách tạo preset riêng, xem [◼️ Preset scanner & render profile](advanced/scanner-presets.md "mention") (nâng cao, đang thực hiện)

Bạn cũng có thể hiệu chỉnh cân bằng màu bằng các thiết lập _Colour calibration_. Xem [Hiệu chuẩn màu](advanced/colour-calibration.md "mention") (kỹ thuật nâng cao)

#### Thiết lập _Latency(ms)_ có tác dụng gì?

Đây là độ trễ khung hình, tức khoảng thời gian tối đa giữa lúc một frame được tạo và sau đó được gửi tới laser. Thông thường bạn không cần điều chỉnh, nhưng nếu gặp vấn đề mạng, bạn có thể thử tăng giá trị này. Xem [Thiết lập độ trễ](setting-up/latency-setting.md "mention") để biết thêm chi tiết.

### Clips

#### Làm sao để chỉnh zone và thiết lập cho một Clip mà không chạy Clip đó?

`Alt / Option`-click để đặt Clip đó làm _currently selected clip_ nhưng không kích hoạt. Xem thêm [Bắt đầu / dừng Clips](clips/starting-stopping-clips.md "mention")

#### Làm sao để sao chép Clips?

Nhấp và kéo trong khi giữ phím `Alt / Option`. Xem thêm [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Làm sao để xóa Clips?

Nhấp và kéo chúng ra khỏi Clip Deck. Xem thêm [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Làm sao để chọn nhiều mục, xóa, kết hợp Clip Deck, v.v.?

Xem [Sắp xếp Clip Deck](clips/organising-your-clip-deck.md "mention")

#### Biểu tượng micro nhỏ và các biểu tượng khác trên Clip có nghĩa là gì?

Các biểu tượng này cho biết Clip nhận đầu vào âm thanh hoặc MIDI, và 3 dấu chấm cho biết có độ trễ zone. Xem [Các biểu tượng nhỏ trên nút Clip là gì?](clips/what-are-the-small-icons-on-the-clip-buttons.md "mention")
