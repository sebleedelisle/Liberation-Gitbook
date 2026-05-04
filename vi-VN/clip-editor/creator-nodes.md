---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/creator-nodes
---

# 🟩 Creator nodes

### <img src="../.gitbook/assets/Creator Point.png" alt="" data-size="line"> Point Creator

Tạo một chấm / tia đơn.

* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **Colour** - màu của chấm. Xem [Cài đặt màu và HSB](fundamentals/colour-settings-and-hsb.md "mention")
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorLine.png" alt="" data-size="line"> Line Creator

Tạo một đường / màn tia.

* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **Size** - chiều dài của đường
* **Colour** - màu của đường. Xem [Cài đặt màu và HSB](fundamentals/colour-settings-and-hsb.md "mention")
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* **rotation** - góc của đường, tính bằng độ
* **resolution** - xem [Resolution](fundamentals/resolution.md "mention")
* **alignment** - _LEFT / CENTRE / RIGHT -_ xác định điểm bắt đầu và tâm xoay của đường
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorCircle.png" alt="" data-size="line"> Circle Creator

Tạo một hình tròn / hình nón.

* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **radius** - bán kính của hình tròn
* **Colour** - màu của hình tròn. Xem [Cài đặt màu và HSB](fundamentals/colour-settings-and-hsb.md "mention")
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* **resolution** - xem [Resolution](fundamentals/resolution.md "mention")
* **Fill state** - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorPoly.png" alt="" data-size="line"> Polygon Creator

Tạo một đa giác đều, chẳng hạn tam giác, hình vuông, ngũ giác, v.v.

* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **size** - khoảng cách từ tâm đến từng góc
* **Colour** - màu của đa giác. Xem [Cài đặt màu và HSB](fundamentals/colour-settings-and-hsb.md "mention")
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* **rotation** - góc xoay của hình, tính bằng độ
* **resolution** - xem [Resolution](fundamentals/resolution.md "mention")
* **Fill state** - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorShape.png" alt="" data-size="line"> Shape Creator

Tải một tệp SVG để dùng hình tùy chỉnh.

{% hint style="warning" %}
Liberation tương thích với định dạng _SVGTiny_. Khuyến nghị dùng InkScape, nhưng hầu hết ứng dụng đồ họa vector đều có thể xuất sang định dạng này. Hãy đảm bảo chuyển mọi chữ thành hình trước khi xuất. Liberation sẽ render các nét vẽ, và có thể tùy chọn dùng phần fill làm mask. Hãy đảm bảo các đường của bạn không phải màu đen, nếu không chúng sẽ không hiển thị nếu không có bộ chỉnh màu!
{% endhint %}

* **Import SVG** - tải một tệp SVG từ ổ đĩa.

{% hint style="info" %}
Sau khi SVG được tải, nội dung sẽ được chuyển đổi và lưu bên trong clip, nên bạn không cần duy trì tham chiếu đến tệp, trừ khi sau này bạn muốn thay đổi cài đặt mask.
{% endhint %}

* **Use fills as masks** - xử lý mọi hình có fill như một mask, tức là được tô bằng màu đen. Tùy chọn này sẽ được bật tự động nếu SVG của bạn có bất kỳ hình nào có fill. Nếu không có hình nào có fill, tùy chọn này sẽ bị tắt. Xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - nếu các hình trong SVG của bạn không có viền, chúng ta không thể vẽ chúng! Tùy chọn này thêm viền (hay _stroke_) vào mọi hình có fill. Nếu SVG của bạn không có hình nào có stroke, tùy chọn này sẽ được bật tự động. Nếu không có hình nào có fill, tùy chọn này sẽ bị tắt.
* **Invert black lines** - nếu tất cả các đường trong SVG của bạn đều màu đen thì bạn sẽ không nhìn thấy chúng! Tùy chọn này chuyển chúng thành màu trắng. Nó được bật tự động nếu SVG của bạn chỉ có các hình màu đen, nhưng sẽ bị tắt nếu không có hình màu đen nào.
* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **scale** - điều chỉnh kích thước của SVG. Giá trị này được tính tự động khi SVG được tải (để đảm bảo hình ảnh hiển thị được), nhưng sau đó bạn có thể chỉnh thủ công.
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* **rotation** - góc xoay của hình ảnh, tính bằng độ
* **resolution** - xem [Resolution](fundamentals/resolution.md "mention")
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorAnim.png" alt="" data-size="line"> Anim Creator

Tạo hoạt ảnh từ một chuỗi tệp SVG.

* **Import SVG Sequence** - chọn thư mục chứa tất cả các tệp SVG. Lưu ý rằng chúng được tải theo thứ tự chữ và số.

{% hint style="info" %}
Sau khi chuỗi SVG được tải, nội dung sẽ được chuyển đổi và lưu bên trong clip, nên bạn không cần duy trì tham chiếu đến các tệp, trừ khi sau này bạn muốn thay đổi cài đặt mask.
{% endhint %}

* **Use fills as masks** - xử lý mọi hình có fill như một mask, tức là được tô bằng màu đen. Tùy chọn này sẽ được bật tự động nếu bất kỳ SVG nào của bạn có hình có fill. Nếu không SVG nào có hình có fill, tùy chọn này sẽ bị tắt. Xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **Add outlines to filled shapes** - nếu các hình trong SVG của bạn không có viền, chúng ta không thể vẽ chúng! Tùy chọn này thêm viền (hay _stroke_) vào mọi hình có fill. Nếu các SVG của bạn không có hình nào có stroke, tùy chọn này sẽ được bật tự động. Nếu không có hình nào có fill, tùy chọn này sẽ bị tắt.
* **Invert black lines** - nếu tất cả các đường trong SVG của bạn đều màu đen thì bạn sẽ không nhìn thấy chúng! Tùy chọn này chuyển chúng thành màu trắng. Nó được bật tự động nếu các SVG của bạn chỉ có các hình màu đen, nhưng sẽ bị tắt nếu không có hình màu đen nào.
* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **scale** - điều chỉnh kích thước của hình ảnh.
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* **rotation** - góc xoay của hình ảnh, tính bằng độ
* **resolution** - xem [Resolution](fundamentals/resolution.md "mention")
* **speed** - thời lượng của toàn bộ hoạt ảnh, tính theo ô nhịp.
* **time per frame** - nếu bật tùy chọn này, thời lượng sẽ được tính cho mỗi frame thay vì cho toàn bộ hoạt ảnh. Vì vậy, nếu _speed_ được đặt thành ¼ thì mỗi frame sẽ dài 1 beat.
* **animation direction** -
  * _FORWARDS_ - hoạt ảnh chạy tiến rồi lặp lại từ đầu
  * _BACKWARDS_ - hoạt ảnh chạy lùi rồi lặp lại từ cuối
  * _PINGPONG_ - hoạt ảnh chạy tiến rồi chạy lùi trong một vòng lặp
  * _MANUAL_ - frame hiện tại được đặt bằng thiết lập _position manual_
* **position manual** - đặt frame hiện tại; 0% là frame đầu tiên, 100% là frame cuối cùng. Có thể đặt thủ công hoặc bằng oscillator bên ngoài.
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

### <img src="../.gitbook/assets/CreatorText.png" alt="" data-size="line"> Text Creator

Tạo chữ bằng phông TrueType hoặc OpenType.

* **Text** - nhập chữ bạn muốn tại đây
* **Font** - chọn phông bạn muốn

{% hint style="info" %}
Để thêm phông vào Liberation, hãy sao chép các tệp .ttf hoặc .otf vào thư mục `data/fonts` bên trong thư mục làm việc của Liberation, rồi khởi động lại Liberation.
{% endhint %}

* **Render profile** - xem [Render profile](fundamentals/render-profile.md "mention")
* **horizontal alignment** - chọn _LEFT_, _CENTRE_, hoặc _RIGHT_ để chọn căn chỉnh chữ.
* **Fill state** - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")
* **size** - kích thước chữ
* **monospace** - vẽ mọi ký tự với cùng một độ rộng. Tùy chọn này hữu ích cho bộ đếm thời gian và bộ đếm số, vì văn bản sẽ không bị xê dịch ngang khi các số thay đổi.
* **character spacing** - điều chỉnh khoảng cách giữa các ký tự. Tăng giá trị để giãn chữ rộng hơn, hoặc giảm để siết văn bản chặt hơn.
* **colour -** xem [Cài đặt màu và HSB](fundamentals/colour-settings-and-hsb.md "mention")
* Vị trí **x** và **y** - xem [Hệ tọa độ](fundamentals/co-ordinate-system.md "mention")
* **rotation** - góc xoay của hình ảnh, tính bằng độ
* **resolution** - xem [Resolution](fundamentals/resolution.md "mention")
* **reveal** - dùng tùy chọn này để hiện dần chữ, từng ký tự một. Khi giá trị nằm trong khoảng 0 đến 50%, chữ sẽ dần xuất hiện từ trái sang phải. Khi nằm trong khoảng 50% đến 100%, chữ sẽ biến mất từ trái sang phải. Bạn có thể kết nối một oscillator vào socket này để tạo hoạt ảnh.
* **reveal by word** - khi bật, _reveal_ sẽ hoạt động theo từng từ thay vì từng ký tự.
* **countdown** - thay thế văn bản đã nhập bằng bộ đếm ngược. Khi bộ đếm ngược về 0, giá trị **Text** bình thường sẽ được hiển thị.
* **use seconds** - đếm theo giây thực. Khi tùy chọn này tắt, bộ đếm ngược sẽ dựa trên beat: hai beat được tính là một giây, vì vậy 120bpm sẽ khớp với giây thực.
* **show minutes/seconds** - hiển thị thời gian còn lại theo phút và giây. Nếu thời gian còn lại hơn một giờ, tùy chọn này cũng hiển thị cả giờ.
* **countdown to date/time** - đếm ngược đến một ngày và giờ UTC cụ thể thay vì đếm ngược từ một con số.
* **countdown datetime** - đặt ngày/giờ UTC mục tiêu khi **countdown to date/time** đang bật.
* **start number** - số bắt đầu khi **countdown to date/time** đang tắt.
* _MOVE TO FRONT / MOVE TO BACK_ - xem [Fill, mask và sắp xếp độ sâu](fundamentals/fills-masks-and-depth-sorting.md "mention")

{% hint style="info" %}
Nếu menu thả xuống chọn phông đang mở, các phím mũi tên lên và xuống sẽ chuyển qua các phông hiện có.
{% endhint %}
