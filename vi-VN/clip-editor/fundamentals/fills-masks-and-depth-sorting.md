---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/fundamentals/fills-masks-and-depth-sorting
---

# 🟩 Tô đầy, mask và sắp xếp theo chiều sâu

### Nét vẽ, tô đầy và mask

Bạn sẽ thấy một số Creator nodes có tùy chọn _Fill state_; bạn có thể vẽ chúng bằng nét viền, dưới dạng mask (che nội dung bên dưới), hoặc cả hai.

Khi bạn render một hình dưới dạng mask, nó giống như được tô bằng màu đen và mọi thứ nằm bên dưới sẽ bị che đi.

{% hint style="info" %}
Vẽ một đường (hay _stroke_) bằng laser khá đơn giản; bạn quét laser từ điểm đầu đến điểm cuối của đường. Thế là có một đường!

Nhưng các hình được tô đầy thì khó hơn; nếu muốn một hình được tô màu, bạn có thể tự tạo các nét gạch chéo bằng cách vẽ nhiều đường để lấp đầy, nhưng Liberation chưa thể tự động làm việc đó (hiện tại). Và ngay cả khi làm được, bạn vẫn sẽ thấy các đường khác bên dưới hiện xuyên qua.

Điều chúng ta có thể làm là tô các hình bằng _màu đen_. Bên dưới, Liberation thực hiện toàn bộ các phép tính để loại bỏ nội dung nằm dưới hình được tô đen đó. Tin tôi đi, việc này khá rắc rối!

Nhưng nó hoạt động rất tốt và tạo cảm giác như hình đã được tô đầy bằng màu đen.
{% endhint %}

### Sắp xếp theo chiều sâu

Vì một số hình có thể _che_ các hình khác, Liberation phải sắp xếp chúng theo chiều sâu. Theo mặc định, các phần tử được sắp xếp theo chiều sâu dựa trên vị trí z. Nếu chúng ở cùng vị trí z, chúng sẽ được sắp xếp theo vị trí layer; vị trí này có thể thay đổi bằng các nút _MOVE TO FRONT_ và _MOVE TO BACK_ bên trong từng Creator.
