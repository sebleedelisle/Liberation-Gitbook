---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/stylisation
---

# 🟩 Các node Stylisation

## &#x20;Randomise

Tạo các bản sao rải rác của những phần tử đầu vào bằng một trường nhiễu mạch lạc. Nói cách khác, node này sao chép và di chuyển các hình dạng và điểm của bạn theo một cách có kiểm soát nhưng vẫn “nhiễu”. Thay vì mọi thứ nằm gọn ở một vị trí, bạn sẽ có nhiều phiên bản dịch chuyển và tỏa ra, giống như các hạt đang chuyển động trong một dòng chảy.

* **count** – số bản sao cho mỗi phần tử đầu vào (1–20). Với giá trị 1, bạn nhận được một phiên bản bị lệch nhẹ của mỗi phần tử. Giá trị cao hơn tạo nhiều bản sao rải rác hơn.
* **noise offset** – di chuyển tuần hoàn qua trường nhiễu (0–100%). Vòng lặp liền mạch, vì vậy khi animate tham số này bằng Oscillator Node, tất cả bản sao sẽ chuyển động mượt và liên tục cùng nhau.
* **noise jitter** – điều khiển thang kết cấu của nhiễu. Giá trị thấp tạo biến thiên rộng và mượt. Giá trị cao tạo vị trí chặt hơn, thất thường hơn. Tham số này thay đổi mẫu nhiễu, không phải cường độ.
* **change between points** – điều khiển mức độ khác nhau giữa mỗi bản sao và bản sao trước đó. Giá trị thấp giữ các bản sao tụ gần nhau và tương tự nhau. Giá trị cao làm chúng tỏa rộng hơn với nhiều biến thiên hơn.
* **face direction** – xoay từng bản sao để nó hướng theo chiều di chuyển trong trường nhiễu, tạo ra các mũi tên/hạt thẳng hàng với dòng chảy.
* **amount** – cường độ tổng thể của hiệu ứng (0–100%). Tham số này nhân cả độ dịch chuyển và độ xoay từ Face direction.

{% hint style="info" %}
node Randomise là phần cốt lõi của hiệu ứng Randomise!
{% endhint %}

## &#x20;Trails

Tạo các “tiếng vọng” của nội dung, để lại các bản sao mờ dần hoặc thay đổi tỉ lệ phía sau bản gốc khi nó di chuyển.

* **change render profile for trail** – nếu bật, tất cả bản sao trail sẽ dùng **render profile** đã chọn. _Xem_ [render profile](../fundamentals/render-profile.md).
* **render profile** – profile dùng cho các bản sao trail khi công tắc ở trên được bật. Thường dùng khi nội dung chính được đặt thành **DETAIL** nhưng các tiếng vọng được render dưới dạng **FAST**, giúp giữ chi tiết rõ trên các hình dạng chính trong khi render trail hiệu quả hơn.
* **delay** – đặt khoảng cách giữa các bản sao trail theo thời gian âm nhạc, đo bằng **bước nốt 1/64**.\
  Để tham khảo:
  * 16 = 1/16 ô nhịp (nốt 1/16)
  * 32 = 1/8 ô nhịp (nốt 1/8)
  * 64 = 1/4 ô nhịp (nốt 1/4)
  * 128 = 1/2 ô nhịp (nốt 1/2)
  * 256 = 1 ô nhịp
* **trail size** – số bản sao trail được vẽ phía sau nội dung đang chạy.
* **freeze trails** – biến các trail đang chảy mượt thành một chuỗi ảnh chụp đóng băng. Hữu ích để tạo hiệu ứng trail kiểu ngắt nhịp, đồng bộ theo beat.
* **brightness start / brightness end** – áp dụng độ sáng dọc theo trail, từ bản sao mới nhất (**start**) đến bản sao cũ nhất (**end**). Thông thường đặt **brightness start** ở 100% và **brightness end** ở 0% để các tiếng vọng mờ dần.
* **scale start / scale end** – áp dụng tỉ lệ dọc theo trail, từ bản sao mới nhất (start) đến bản sao cũ nhất (end). Với trail thu nhỏ dần về 0, đặt **scale start** thành 100% và **scale end** thành 0%.

## &#x20;Shimmer

Thêm biến thiên độ sáng lấp lánh vào nội dung, từ ánh nhấp nháy nhẹ đến strobe mạnh.

* **speed** – shimmer thay đổi nhanh đến mức nào theo thời gian. Giá trị cao hơn nhấp nháy nhanh hơn; 0 tạm dừng hiệu ứng.
* **separation** – mức độ khác nhau giữa các điểm/phần tử lân cận.
  * 0: mọi thứ shimmer cùng nhau.
  * \>0: các điểm gần nhau dần có pha khác nhau, nên shimmer biến thiên trên toàn hình dạng.
  * <0: giống như trên, nhưng chiều tiến pha chạy theo hướng ngược lại.
* **threshold** – thay vì mờ dần mượt mà, các điểm sẽ bật sáng hoàn toàn hoặc tắt hoàn toàn tùy theo độ sáng của chúng. Phần tử sáng hơn sẽ sáng lên thường xuyên hơn, nhưng lưu ý rằng phần tử ở độ sáng 100% luôn bật, còn phần tử ở độ sáng 0% luôn tắt. Hữu ích cho hiệu ứng lấp lánh sắc nét hoặc ánh sao.

{% hint style="info" %}
Bật **threshold** là một trong những tính năng ẩn rất hay, có thể thật sự làm cho các hạt hoặc nội dung của bạn sống động hơn. Thay vì mờ dần, các điểm được bật/tắt nhanh dựa trên độ sáng của chúng. Vì tại mỗi thời điểm có ít điểm được vẽ hơn, kết quả là Output sáng hơn và animation mượt hơn.

Nhưng hãy lưu ý rằng nếu nội dung của bạn đã ở độ sáng 100% thì tham số này sẽ không tạo ra thay đổi!
{% endhint %}

* **use whole shape** – áp dụng một giá trị shimmer đồng nhất cho toàn bộ hình dạng. Khi tắt, node chia nhỏ các hình dạng để những phần khác nhau có thể lấp lánh độc lập, tạo cảm giác hạt lốm đốm.

## &#x20;Particles

Đây là một hiệu ứng thử nghiệm, tạo và animate các hạt dựa trên nội dung của bạn. Mọi phần tử dạng điểm đi vào đều được xem là vị trí emitter. Vì đường đi của hạt được tính trước, nếu nội dung đầu vào thay đổi, bạn có thể cần làm mới/tính toán lại để cập nhật các hạt (chỉ cần thay đổi bất kỳ setting nào).

**General**

* **keep original** – nếu bật, nội dung gốc được giữ lại và các hạt được thêm lên trên. Hữu ích khi bạn muốn các điểm emitter vẫn hiển thị.
* **number of particles** – số hạt được tạo cho mỗi lần phát. Giá trị cao hơn tạo hiệu ứng dày hơn, giá trị thấp hơn tạo hiệu ứng tối giản hơn.
* **emission period** – khoảng thời gian của vòng lặp (tính theo ô nhịp) mà trong đó các hạt được phát ra. Ở 100%, chúng được trải đều trên toàn vòng lặp; giá trị nhỏ hơn gom chúng lại để tạo các đợt bùng phát.
* **loop length** – thời lượng của vòng lặp hạt, đo bằng ô nhịp âm nhạc.
* **loop count** – số lần vòng lặp lặp lại trước khi reset. Nếu đặt là 1, các hạt sẽ luôn đi theo đúng cùng một mô phỏng mỗi lần, giúp lặp lại hoàn toàn chính xác. Giá trị cao hơn tạo thêm biến thiên trước khi chu kỳ reset.
* **delay** – dịch thời điểm bắt đầu phát theo số lượng nốt 1/64, dùng cho các hiệu ứng căn thời gian.

**Motion**

* **speed** – tốc độ các hạt di chuyển ra xa emitter.
* **speed variation** – thêm độ ngẫu nhiên để các hạt không di chuyển cùng một tốc độ. Tạo độ tỏa tự nhiên hơn.
* **direction** – đặt hướng cơ bản mà các hạt được bắn ra, được xác định bằng **góc x, y, z**. Các góc này xoay vector bắn trong không gian 3D, vì vậy bạn có thể hướng các hạt thẳng lên, sang ngang hoặc theo bất kỳ đường chéo nào. Kết hợp với **spread** để tạo hình nón rộng hơn hoặc các đợt bùng phát hỗn loạn hơn.

{% hint style="info" %}
**Góc Euler**\
Liberation dùng **góc Euler** để mô tả hướng trong không gian 3D. Đây đơn giản là các phép xoay quanh ba trục chính:

* **X** – nghiêng tới/lùi (giống như gật đầu)
* **Y** – quay trái/phải (giống như lắc đầu “không”)
* **Z** – lăn theo chiều kim đồng hồ/ngược chiều kim đồng hồ (giống như nghiêng đầu sang bên)

Bằng cách điều chỉnh ba giá trị này, bạn có thể hướng các hạt theo bất kỳ hướng nào.
{% endhint %}

* **direction variation** – thêm độ tỏa ngẫu nhiên quanh hướng đó. Hữu ích để tạo hình nón, tia phun hoặc vụ nổ.
* **drag** – làm các hạt chậm dần theo thời gian. Giá trị cao hơn khiến chúng có cảm giác nặng hơn và ì hơn.
* **gravity** – kéo các hạt xuống (giá trị dương) hoặc đẩy chúng lên (giá trị âm).
* **gravity variation** – thêm biến thiên trọng lực cho từng hạt, làm chuyển động hỗn loạn hơn.

**Life**

* **life duration** – thời gian các hạt tồn tại (đo bằng đơn vị nốt 1/64). Với giá trị ngắn hơn, hạt biến mất nhanh; với giá trị dài hơn, chúng vẫn hiển thị trong thời gian dài hơn.
* **life variation** – thêm độ ngẫu nhiên cho thời lượng tồn tại của hạt để chúng không biến mất cùng lúc.
* **start delay / start delay variation** – trì hoãn thời điểm từng hạt trở nên hiển thị (theo bước nốt 1/64). Hạt đã được tạo và đang di chuyển trong khoảng thời gian này, nhưng độ sáng của nó được giữ ở 0, nên nó vẫn vô hình cho đến khi hết thời gian trễ. Hữu ích nếu bạn muốn các “tia lấp lánh” pháo hoa xuất hiện trễ.

**Colour & brightness**

* **hue start** – màu ban đầu của hạt.
* **hue variation** – thêm độ ngẫu nhiên để các hạt không bắt đầu với cùng một màu.
* **hue change** – dịch chuyển hue trong suốt vòng đời của hạt, tạo các trail đổi màu.
* **brightness start / brightness end** – áp dụng độ sáng trong suốt vòng đời của hạt. Thông thường đặt brightness start cao và brightness end thấp để hạt mờ dần tự nhiên.
* **brightness variation** – ngẫu nhiên hóa độ sáng ban đầu để tạo cảm giác động hơn.
* **saturation start / saturation end** – đặt độ rực của màu ở thời điểm bắt đầu và kết thúc.
* **saturation variation** – ngẫu nhiên hóa saturation để tạo biến thiên giữa các hạt.

**Simulation**

* **time adjustment** – tăng tốc hoặc làm chậm toàn bộ mô phỏng hạt. Hữu ích để đồng bộ với các tempo khác nhau hoặc phóng đại chuyển động.
