---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/troubleshooting/intermittent-flashing-output
---

# ✅ Đầu ra chập chờn / nhấp nháy

Mở panel _Laser Overview_ và nhìn đèn kết nối bên cạnh laser đang gặp sự cố.

**Nếu đèn kết nối KHÔNG luôn sáng màu xanh lá:**\
Có thể bạn đang gặp sự cố về mạng hoặc hiệu năng CPU:

**Hiệu năng mạng -**

* Đảm bảo bạn không kết nối với mạng Wi-Fi. Bạn nên luôn dùng kết nối có dây. Hãy chắc chắn hệ điều hành đang ưu tiên mạng có dây hơn Wi-Fi, hoặc tắt Wi-Fi nếu bạn không chắc.
* Kiểm tra bộ chuyển đổi mạng - và thử một bộ chuyển đổi USB-C khác.
* Người dùng Windows - kiểm tra / nâng cấp driver mạng, chạy các công cụ kiểm tra mạng phù hợp.
* Kiểm tra toàn bộ dây cáp, switch và router. Thay thế và kiểm tra từng dây cáp một cách có hệ thống.
* Khởi động lại toàn bộ thiết bị mạng, bao gồm switch, router và từng Ether Dream.

**Hiệu năng CPU**

Nếu máy tính của bạn cũ hoặc cấu hình thấp, máy có thể quá chậm để chạy Liberation. Hãy kiểm tra chỉ báo tốc độ khung hình ở phía bên phải của thanh biểu tượng.

Ở đó có hai con số - tốc độ khung hình thực tế và tốc độ khung hình mục tiêu. Nếu tốc độ khung hình thực tế giảm xuống dưới 30, bạn có thể gặp sự cố.

Các thao tác sau có thể hữu ích:

* Gỡ bỏ các laser không dùng đến, ví dụ nếu bạn chỉ có một laser được kết nối, hãy xóa các laser còn lại.
* Chuyển sang Output view hoặc Canvas view.
* Đóng tất cả chương trình khác, kiểm tra cài đặt tường lửa mạng, tắt phần mềm diệt virus, Dropbox, v.v.
* Giảm độ phân giải màn hình và thu nhỏ cửa sổ Liberation.

Nếu các cách trên không hiệu quả, hãy cân nhắc nâng cấp máy tính.

***

**Nếu đèn kết nối luôn sáng màu xanh lá:**

Khi đó nhiều khả năng đây là sự cố phần cứng. Nội dung này nằm ngoài phạm vi của tài liệu hướng dẫn này, nhưng bạn có thể thử các thao tác sau:

* Tắt hệ thống SFS (Scan Fail Safety). Một số laser có chức năng tắt đầu ra nếu bộ quét ngừng di chuyển, tức là tạo ra một tia tĩnh mạnh. Các hệ thống này đôi khi hơi quá nhạy / không ổn định.

{% hint style="danger" %}
Hãy cực kỳ thận trọng khi tắt hệ thống scan fail safety. Tia tĩnh mạnh có thể gây cháy! Đảm bảo bạn có sẵn nút dừng khẩn cấp và bình chữa cháy.
{% endhint %}

* Kiểm tra cáp và hệ thống khóa liên động.
* Kiểm tra toàn bộ cáp giữa controller và laser.

[ILDA Gem](https://shop.stanwaxlaser.co.uk/ilda-gem-pocket-2020-718-p.asp) có thể là một công cụ rất hữu ích để khắc phục sự cố laser.
