---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/what-if-liberation-wont-open
---

# ✅ Nếu Liberation không mở được thì sao?

Trường hợp này hiếm gặp, nhưng đôi khi Liberation có thể không khởi chạy được hoặc bị crash ngay sau khi mở. Nguyên nhân gần như luôn là do một trong các tệp cấu hình cục bộ bị hỏng - thường xảy ra sau khi hệ thống bị crash hoặc có sự cố bất thường trên máy tính của bạn.

Rất may là bạn có thể khắc phục dễ dàng bằng cách đặt lại các thiết lập cục bộ. Dưới đây là cách thực hiện trên macOS và Windows.

> **Quan trọng**
>
> * Đóng Liberation trước khi làm bất kỳ thao tác nào.
> * Các bước này chỉ ảnh hưởng đến thiết lập cục bộ, log và cache. Giấy phép và tài khoản của bạn vẫn an toàn.

***

#### Tìm thư mục làm việc ở đâu

Mỗi phiên bản Liberation có thư mục làm việc riêng. Ví dụ, nếu bạn đang chạy phiên bản 1.0.0, tên thư mục sẽ là 1.0.0.

* **macOS**: `~/Library/Application Support/Liberation/1.0.0`
* **Windows**: `AppData\Local\Liberation\1.0.0`

**Cách mở nhanh thư mục**

**macOS**

1. Trong Finder, nhấn **Shift + Cmd + G**.
2.  Dán đường dẫn này rồi nhấn **Enter**:

    ```
    ~/Library/Application Support/Liberation
    ```
3. Mở thư mục khớp với số phiên bản của bạn, ví dụ `1.0.0`.

**Windows**

1.  Nhấn **Win + R**, dán nội dung này rồi nhấn **Enter**:

    ```
    %LOCALAPPDATA%\Liberation
    ```
2. Mở thư mục khớp với số phiên bản của bạn, ví dụ `1.0.0`.

> **Mẹo cho Windows**: Nếu bạn duyệt bằng Trình quản lý tệp, hãy bật hiển thị mục ẩn: **Xem > Hiển thị > Mục ẩn**.

***

#### Bước 1 – Đặt lại tệp thiết lập một cách an toàn

Trong thư mục phiên bản của bạn, mở:

```
data/liberation/
```

Trong thư mục liberation, bạn sẽ thấy một tệp có tên `settings.json`. Hãy xóa tệp này.

* **Ví dụ trên macOS**: `~/Library/Application Support/Liberation/1.0.0/data/liberation/settings.json`
* **Ví dụ trên Windows**: `%LOCALAPPDATA%\Liberation\1.0.0\data\liberation\settings.json`

Bây giờ hãy thử khởi chạy Liberation. Nếu ứng dụng mở được, bạn đã hoàn tất.

***

#### Bước 2 – Kiểm tra Clip có vấn đề

Nếu Liberation bị crash khi bạn đang chỉnh sửa một Clip, có thể tệp Clip đó đang gây ra sự cố.

Trong cùng thư mục với tệp settings.json, bạn sẽ thấy một tệp có tên `clipEdit.json`

Hãy sao lưu tệp này vào nơi an toàn (ví dụ: Desktop), sau đó xóa tệp đó khỏi thư mục làm việc của Liberation.

Thử khởi chạy Liberation lại. Nếu ứng dụng mở bình thường, vui lòng gửi tệp đã sao lưu qua email đến [**info@liberationlaser.com**](mailto:info@liberationlaser.com) để chúng tôi có thể kiểm tra nguyên nhân gây ra sự cố.

***

#### Bước 3 - Sao lưu, rồi xóa toàn bộ thư mục làm việc

Nếu Bước 1 và Bước 2 không giúp khắc phục:

1. **Sao lưu** toàn bộ thư mục phiên bản:
   * macOS: Nhấp chuột phải vào thư mục `1.0.0` và chọn **Compress** để tạo tệp zip, hoặc sao chép thư mục đó đến nơi an toàn như Desktop.
   * Windows: Nhấp chuột phải vào thư mục `1.0.0` và chọn **Send to > Compressed (zipped) folder**, hoặc sao chép thư mục đó đến nơi an toàn như Desktop.
2. Sau khi sao lưu, **xóa** thư mục `1.0.0` gốc khỏi vị trí thư mục làm việc của Liberation.
3. Khởi chạy Liberation lại. Ứng dụng sẽ tạo lại một thư mục làm việc mới.

Nếu Liberation mở được, hãy chuyển sang Bước 4.

***

#### Bước 4 - Gửi bản sao lưu cho chúng tôi

Việc này giúp chúng tôi xác định nguyên nhân gây ra sự cố để có thể ngăn lỗi này trong các phiên bản sau.

Nén **bản sao lưu** từ Bước 3 thành tệp zip nếu bạn chưa làm, rồi gửi email cho chúng tôi để chẩn đoán nguyên nhân.

* **To**: [info@liberationlaser.com](mailto:info@liberationlaser.com)
* **Subject**: Sửa lỗi khởi động Liberation - bản sao lưu thư mục làm việc
* **Body**: Vui lòng bao gồm:
  * Hệ điều hành và phiên bản (ví dụ: macOS 14.6 hoặc Windows 11 23H2)
  * Phiên bản Liberation (ví dụ: 1.0.0)
  * Bước nào đã khắc phục được lỗi, nếu có (Bước 1, Bước 2 hoặc Bước 3)
  * Mô tả ngắn gọn về việc đã xảy ra trước khi sự cố bắt đầu
* **Attachment**: bản sao lưu đã nén của thư mục làm việc `1.0.0`.

> Nếu tệp zip quá lớn để gửi qua email, hãy tải lên dịch vụ lưu trữ đám mây và chia sẻ liên kết.

***

#### Vẫn không khởi chạy được sau Bước 3?

Nếu Liberation vẫn không mở được sau khi xóa thư mục làm việc:

* Khởi động lại máy tính rồi thử lại.
* Tạm thời tắt phần mềm diệt virus hoặc công cụ bảo mật có thể chặn việc tạo thư mục mới, rồi thử khởi chạy lại.
* Cài đặt đè bản build Liberation mới nhất lên bản cài hiện có.
* Nếu không cách nào ở trên hiệu quả, hãy liên hệ bộ phận hỗ trợ tại [**info@liberationlaser.com**](mailto:info@liberationlaser.com) kèm thông tin chi tiết và mọi log crash trong thư mục con `logs` nếu có.

***

#### Tóm tắt

1. Xóa `data/liberation/settings.json` trong thư mục làm việc theo phiên bản của bạn.
2. Nếu bạn đang chỉnh sửa một Clip, hãy sao lưu rồi xóa `data/liberation/clipEdit.json`.
3. Nếu vẫn không mở được, hãy sao lưu rồi xóa toàn bộ thư mục `1.0.0` (hoặc phiên bản của bạn).
4. Nếu Bước 3 khắc phục được lỗi (hoặc nếu không), hãy nén bản sao lưu thành tệp zip và gửi đến [**info@liberationlaser.com**](mailto:info@liberationlaser.com) kèm hệ điều hành và phiên bản Liberation của bạn.
