---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/oscillators/wave-oscillators
---

# ✅ Bộ dao động dạng sóng

## Trên trang này:

* <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> [Sóng răng cưa](wave-oscillators.md#sawtooth-wave-1)
* <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> [Sóng tam giác](wave-oscillators.md#triangle-wave-1)
* <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> [Sóng sin](wave-oscillators.md#sine-wave)
* <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> [Sóng vuông](wave-oscillators.md#square-wave-1)
* <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> [Nhiễu](wave-oscillators.md#noise)
* <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> [Bộ dao động tùy chỉnh](wave-oscillators.md#custom-oscillator-1)

## Cài đặt của bộ dao động dạng sóng

Tất cả Wave oscillator đều có các cài đặt sau:

* **range min / range max** - xác định phạm vi giá trị cho thuộc tính mà oscillator đang điều khiển. Thuộc tính được đặt thành _range min_ khi dạng sóng ở đáy, và được đặt thành _range max_ khi dạng sóng ở đỉnh.

{% hint style="info" %}
Ví dụ, nếu bạn muốn một điểm di chuyển sang trái và phải trong khoảng từ -100 đến 100, hãy kết nối oscillator với _x property socket_, đặt _min range_ thành -100 và _max range_ thành 100.
{% endhint %}

* **duration** - khoảng thời gian cần để hoàn tất một chu kỳ đầy đủ (hay _loop_). Giá trị này tính tương đối theo tempo bằng ô nhịp. Vì vậy ¼ là một phách. 1 là một ô nhịp đầy đủ, v.v.
* **duration multiplier** - nhân duration cơ sở với một hệ số đã chọn. Ví dụ, nếu duration được đặt là nốt đen và multiplier là 3, oscillator sẽ kéo dài trong ba nốt đen (một nốt trắng chấm dôi). Cũng hỗ trợ multiplier dạng phân số — giữ _SHIFT_ khi kéo thanh trượt để đặt số không nguyên, hữu ích cho hiệu ứng phasing hoặc tạo các dịch chuyển thời gian tinh tế.
* **offset** - độ lệch bắt đầu của sóng, tính theo phần trăm của duration. Nếu bạn muốn sóng bắt đầu ở vị trí một phần tư chu kỳ, hãy đặt giá trị này thành 25%.
* **repeat count** - số lần loop chạy trước khi dừng. Mặc định là _FOREVER_, nhưng bạn có thể thay đổi nếu không muốn oscillator chạy vô hạn. Sau khi dừng, thuộc tính sẽ được đặt thành giá trị ở cuối sóng.
* **delay count** - độ trễ tính bằng phách trước khi oscillator bắt đầu chạy. Trước khi bắt đầu chạy, thuộc tính sẽ được đặt thành giá trị ở đầu sóng.

{% hint style="info" %}
Nếu dùng _repeat count_ và _delay count_ một cách khéo léo, bạn có thể tạo các hoạt ảnh rất phức tạp, gần giống như một timeline riêng!
{% endhint %}

## Cài đặt chung

* **steps** - chia chuyển động thành một số bước rời rạc. Phù hợp khi bạn muốn thuộc tính “nhảy” đến các giá trị thay vì di chuyển mượt.

{% hint style="info" %}
Lưu ý rằng các bước được chia theo thời gian chứ không theo giá trị. Vì vậy, với một sóng được chia thành 4 steps và có duration là 1 ô nhịp, thuộc tính sẽ thay đổi tức thì sau mỗi phách.
{% endhint %}

* **clamp min / clamp max -** tăng tỷ lệ của sóng vượt ra ngoài giá trị tối thiểu hoặc tối đa, rồi giới hạn kết quả.

{% hint style="info" %}
Khái niệm _clamp_ khá khó giải thích, nhưng hãy hình dung dạng sóng vượt ra khỏi phía trên hoặc phía dưới biểu đồ, rồi bị kẹp lại ở các cạnh. Tôi khuyên bạn nên thử nghiệm với chúng! Chúng rất hữu ích nếu bạn muốn một sóng răng cưa bắt đầu muộn hoặc kết thúc sớm.
{% endhint %}

* **ease function** - sóng Sawtooth và Triangle cũng có ease function, giúp thay đổi nhẹ đường cong hoạt ảnh và có thể làm hoạt ảnh của bạn biểu cảm hơn nhiều!
  * **LINEAR** - mặc định, không có easing, chỉ di chuyển tuyến tính giữa giá trị min và max.
* **EASE OUT** - bắt đầu nhanh rồi chậm dần khi gần đến cuối. Rất phù hợp để mô phỏng vật lý, ví dụ như chậm dần đến khi dừng hẳn.
  * **EASE IN** - bắt đầu chậm rồi tăng tốc dần. Phù hợp để mô phỏng việc tích lũy động lượng.
  * **EASE IN/OUT** - kết hợp cả hai, tạo chuyển động rất tự nhiên.

{% hint style="warning" %}
**Easing -** Tôi khuyên bạn nên tránh hoạt ảnh tuyến tính mặc định khi có thể, trừ khi bạn thật sự muốn hiệu ứng trông như robot. Easing có thể làm hoạt ảnh trở nên trôi chảy và tự nhiên hơn rất nhiều!
{% endhint %}

## <img src="../../.gitbook/assets/sawtooth-wave-icon.png" alt="" data-size="line"> Sóng răng cưa

Đôi khi còn được gọi là _dạng sóng ramp_ vì nó tăng dần lên rồi giảm mạnh ở cuối chu kỳ. Đây có lẽ là wave oscillator phổ biến nhất, vì nó tạo loop để tuần hoàn các thuộc tính như _hue_ hoặc _rotation_.

Xem các phần ở trên để biết về:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

Riêng với Sawtooth:

* **cycle range compensation** - khả dụng khi đã đặt **steps**, phù hợp để tuần hoàn các giá trị, ví dụ rotation từ 0 đến 360. Khi không bật tùy chọn này, giá trị đầu và cuối sẽ giống nhau, có thể gây cảm giác bị kẹt tại điểm bắt đầu (vì 0 và 360 là cùng một góc). Bật tùy chọn này để giảm phạm vi tối đa nhằm hiệu chỉnh vị trí của các bước.

## <img src="../../.gitbook/assets/triangle-wave-icon.png" alt="" data-size="line"> Sóng tam giác

Khác với _sóng răng cưa_ nhảy trở lại điểm bắt đầu ở mỗi chu kỳ, _sóng tam giác_ di chuyển tuyến tính tiến lên rồi lùi lại.

Xem các phần ở trên để biết về:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**
* **ease function**

## <img src="../../.gitbook/assets/sine-wave-icon.png" alt="" data-size="line"> Sóng sin

Dạng sóng mượt nhất! Dao động nhẹ nhàng giữa hai giá trị như con lắc.

Xem các phần ở trên để biết về:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

## <img src="../../.gitbook/assets/square-wave-icon.png" alt="" data-size="line"> Sóng vuông

Dạng sóng đơn giản nhất - nó chỉ chuyển qua lại giữa hai giá trị!

Xem các phần ở trên để biết về:

* **range min / range max**
* **duration**
* **offset**
* **repeat count**
* **delay count**

Riêng với Square wave:

* **pulse width** - khoảng thời gian sóng ở giá trị tối đa so với tổng duration. 50% là mặc định, tức là chia đúng một nửa. Nếu bạn chỉ muốn nó “bật” trong một phần tư thời gian, hãy đặt thành 25%. Bạn có thể điều chỉnh thời điểm pulse này xảy ra bằng giá trị _offset_.

## <img src="../../.gitbook/assets/noise-wave-icon.png" alt="" data-size="line"> Nhiễu

Một trong những điểm mạnh của Liberation là có thể tạo các hiệu ứng ngẫu nhiên nhưng lặp lại được. Oscillator _noise_ có thể dùng để tạo chuyển động ngẫu nhiên dạng loop trông tự nhiên, với mức chi tiết/rung nhiễu tùy ý.

Xem các phần ở trên để biết về:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **clamp min**
* **clamp max**
* **repeat count**
* **delay count**

Riêng với Noise:

* **noise type** - thuật toán dùng để tạo nhiễu.
  * **SIMPLEX** - mặc định, một giá trị uốn lượn lên xuống, lặp lại theo loop.
  * **RANDOM** - dùng thuật toán số ngẫu nhiên truyền thống hơn, hoàn toàn nhiễu và hỗn loạn.

{% hint style="info" %}
**Simplex noise** được Ken Perlin thiết kế vào năm 2001 như một bản cải tiến cho thuật toán “Perlin noise” của ông, thuật toán mà ông phát triển năm 1983 trong quá trình làm việc cho bộ phim _Tron_ (nhờ đó ông đã giành giải Oscar!)

Loại nhiễu “gradient” này ra đời từ sự không hài lòng của ông với hình ảnh do máy tính tạo ra trước đó, vốn trông quá “máy móc”. Trong thế giới CGI, nó đặc biệt hữu ích để render mây, mặt nước, hoặc thậm chí height-map cho địa hình chân thực.

Còn trong Liberation, nó rất phù hợp để tạo chuyển động có vẻ khó đoán nhưng vẫn mượt và tự nhiên.
{% endhint %}

* **seed** - giá trị dùng để tạo nhiễu. Nếu bạn không thích hình dạng của noise wave hiện tại, hãy thử thay đổi giá trị này.

{% hint style="info" %}
Một sự thật thú vị dành cho dân kỹ thuật! Để có simplex noise loop hoàn hảo, tôi lặp quanh một vòng tròn trên mặt phẳng nhiễu 2D. Và việc thay đổi giá trị seed sẽ di chuyển mặt phẳng này qua chiều thứ 3!
{% endhint %}

* **simplex detail** - thay đổi mức độ chi tiết hoặc độ rung nhiễu của noise. Nếu bạn muốn mẫu lặp khó nhận ra hơn, hãy tăng duration và tăng giá trị này.

## <img src="../../.gitbook/assets/custom-osc-icon.png" alt="" data-size="line"> Bộ dao động tùy chỉnh

Tạo một dạng sóng hoàn toàn tùy chỉnh. Điều này rất hữu ích để tạo các hoạt ảnh phức tạp.

Xem các phần ở trên để biết về:

* **range min / range max**
* **duration**
* **offset**
* **steps**
* **repeat count**
* **delay count**

Bên dưới là danh sách các vị trí và giá trị. Duration được chia thành 64 bước và bạn có thể đặt một giá trị tại bất kỳ điểm nào trong số này.

Mỗi bước có các cài đặt sau:

* **Step** - bước thời gian trong duration. 0 là ở đầu và 64 là ở cuối.
* **Level** - mức của sóng tại bước thời gian đó. Level nằm trong khoảng từ 0 đến 1.
* **Animation type** - menu thả xuống cho phép bạn chọn cách di chuyển từ bước trước đến level này.
  * **None** - không chuyển tiếp, chỉ nhảy thẳng đến level này tại thời điểm đã cho.
  * **Linear** - chuyển động hoàn toàn tuyến tính từ level trước đó đến level này.
  * **Ease in / Ease out / Ease in/out** - easing từ level trước đó đến level này. Xem _ease function_ ở trên để biết mô tả về các kiểu hoạt ảnh.

***
