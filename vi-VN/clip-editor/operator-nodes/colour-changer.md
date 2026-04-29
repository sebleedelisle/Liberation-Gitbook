---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/clip-editor/operator-nodes/colour-changer
---

# 🟩 Thay đổi màu

## <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> Thay đổi màu

Mô tả

* **hue, saturation, brightness** - các giá trị màu, xem [thiết lập màu và HSB](../fundamentals/colour-settings-and-hsb.md)
* **hue mode** -
  * OFF - không thay đổi hue
  * FIXED - hue của các phần tử được đặt theo giá trị hue
  * SHIFT - hue của các phần tử được dịch theo giá trị này, vì vậy các phần tử có màu khác nhau vẫn giữ sự khác biệt, chỉ được dịch chuyển theo giá trị hue.
* **saturation mode** -
  * OFF - không thay đổi saturation
  * FIXED - saturation được cố định ở giá trị đã chỉ định.
* **brightness mode** -
  * OFF - không thay đổi brightness
  * FIXED - brightness của các phần tử được đặt theo giá trị brightness
  * MULTIPLY - brightness của các phần tử được kết hợp với giá trị brightness, vì vậy nếu chúng đang nhấp nháy thì vẫn sẽ nhấp nháy, nhưng chỉ sáng tối đa đến mức brightness được chỉ định tại đây.
* **blend** - mức độ áp dụng colour changer, 0% là không áp dụng, 100% là áp dụng hoàn toàn, và 50% là sự kết hợp giữa màu hiện có và các giá trị mới.
