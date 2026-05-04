---
metaLinks:
  alternates:
    - https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/dmx-control/dmx-zones
---

# 🟩 DMX zones

DMX zone là các zone Output của Liberation gửi Art-Net/DMX thay vì các điểm laser. Chúng xuất hiện cùng với beam zone và canvas zone, nên có thể gán Clip cho chúng theo cùng quy trình chọn zone.

Mở **DMX Zones** từ menu, hoặc dùng phần DMX trong Laser Overview để quản lý chúng.

* **ADD DMX ZONE** - tạo một DMX zone mới.
* **ARM** - bật đầu ra DMX cho zone đó. DMX zone chưa được kích hoạt sẽ xóa các kênh đã ánh xạ về 0.
* **Node** - chọn số node Art-Net.
* **Universe** - chọn universe Art-Net. Giá trị hiển thị bắt đầu từ 1, nên Universe 1 là universe đầu tiên.
* **Address** - đặt địa chỉ bắt đầu của fixture. Giá trị hiển thị cũng bắt đầu từ 1.
* **Preset** - chọn DMX preset dùng để ánh xạ nội dung Clip sang các kênh DMX.
* **Edit DMX zone settings** (biểu tượng bút chì) - mở các cài đặt zone như chuyển tiếp zone thủ công và hướng của fixture.
* **Edit DMX profile/channel mapping** (biểu tượng thanh trượt) - mở trình chỉnh sửa DMX preset/kênh.
* **Delete** - xóa DMX zone.

### Giới hạn kích hoạt

Số lượng DMX zone có thể được kích hoạt cùng lúc phụ thuộc vào cấp giấy phép của bạn. Nếu cấp giấy phép không cho phép đầu ra DMX, hoặc bạn đã kích hoạt số lượng DMX zone tối đa, nút **ARM** cho các zone bổ sung sẽ bị vô hiệu hóa và hiển thị biểu tượng cấm vào khi di chuột lên.

Hãy tắt kích hoạt một DMX zone khác, hoặc dùng cấp giấy phép có giới hạn DMX cao hơn, trước khi kích hoạt thêm zone.
