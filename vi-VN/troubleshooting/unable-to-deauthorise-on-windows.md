---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/unable-to-deauthorise-on-windows
---

# ✅ Không thể hủy ủy quyền trên Windows?

#### Không thể hủy ủy quyền trên Windows?

Nếu bạn không thể hủy ủy quyền một máy tính trên Windows, trước tiên hãy đảm bảo bạn hủy ủy quyền giấy phép bằng đúng phiên bản Liberation đã dùng để ủy quyền ban đầu, trước khi ủy quyền lại giấy phép đó trong một phiên bản khác.

Nếu cách này không hiệu quả và bạn đang dùng phiên bản cũ hơn 1.0, nguyên nhân có thể là do cách các bản Liberation cũ trên Windows nhận dạng máy tính. Trong các phiên bản đó, hệ thống dùng để tạo machine ID kém ổn định hơn, và trong một số trường hợp ID có thể thay đổi giữa các lần khởi động lại, ngay cả khi phần cứng không có thay đổi rõ ràng.

Nếu bạn đang bị kẹt khi cố hủy ủy quyền và chưa chuyển phiên bản, vui lòng liên hệ support@liberationlaser.com để chúng tôi có thể hủy ủy quyền máy theo cách thủ công cho bạn.

**Vì sao điều này xảy ra**

Trong các bản Liberation đầu tiên trên Windows (trước 1.0), chúng tôi sử dụng phương thức hệ thống do Windows khuyến nghị để tạo machine ID. Tuy nhiên, phương thức này tỏ ra không nhất quán trong một số tình huống. Vì vậy, hệ thống cấp phép đã được viết lại cho phiên bản 1.0 để dùng một tổ hợp phương thức ổn định hơn, hiện hoạt động đáng tin cậy.

Do đó, ID máy tính mà các phiên bản Liberation cũ sử dụng có thể khác với ID mà các phiên bản hiện tại sử dụng. Nếu ID đã thay đổi, bộ phận hỗ trợ cần xử lý việc hủy ủy quyền theo cách thủ công.

***
