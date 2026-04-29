---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/reference/midi-send-receive-default-mapping
---

# ✅ Ánh xạ mặc định gửi/nhận MIDI

**Clip được bật và tắt bằng MIDI note on / off trên các kênh 1 đến 14**

Clips có vị trí ngang (x) và dọc (y). Nhấp chuột phải vào một Clip để xem vị trí của nó. MIDI có thể kích hoạt Clips bắt đầu từ 0,0.

{% hint style="info" %}
Lưu ý rằng việc điều khiển Clip bằng hệ thống này là tuyệt đối, và vị trí Clip không thay đổi khi bạn cuộn Clip Deck.
{% endhint %}

MIDI channel 1, note 1 là Clip 0,0; note 2 là Clip 0,1; note 3 là Clip 0,2, lần lượt đi xuống theo hàng rồi sang các cột. Khi đến 128, hệ thống chuyển sang kênh tiếp theo và bắt đầu lại. Vì vậy, tổng cộng bạn có 128 x 14 = 1792 Clips có thể truy cập qua MIDI.

MIDI note cho tọa độ Clip:

<table><thead><tr><th></th><th>x : 0</th><th width="124">x : 1</th><th>x : 2</th><th>x : 3</th><th>x : 4</th></tr></thead><tbody><tr><td><strong>y : 0</strong></td><td>Note : 1</td><td>Note : 6</td><td>Note : 11</td><td>Note : 16</td><td>Note : 20</td></tr><tr><td><strong>y : 1</strong></td><td>Note : 2</td><td>Note : 7</td><td>Note : 12</td><td>Note : 17</td><td>...v.v.</td></tr><tr><td><strong>y : 2</strong></td><td>Note : 3</td><td>Note : 8</td><td>Note : 13</td><td>Note : 18</td><td></td></tr><tr><td><strong>y : 3</strong></td><td>Note : 4</td><td>Note : 9</td><td>Note : 14</td><td>Note : 19</td><td></td></tr><tr><td><strong>y : 4</strong></td><td>Note : 5</td><td>Note : 10</td><td>Note : 15</td><td>Note : 20</td><td></td></tr></tbody></table>

Lưu ý rằng sự kiện MIDI note on sẽ bắt đầu Clip, và sự kiện note off tương ứng sẽ dừng Clip. Điều này không phụ thuộc vào trigger mode của group. Hệ thống này ban đầu được thiết kế cho phát lại và ghi, nên việc để các note bật/tắt luân phiên một Clip sẽ không phù hợp.

### **Hiệu ứng**

Thông điệp MIDI control change (CC) trên **channel 15** điều chỉnh các hiệu ứng.\
Hiệu ứng 1 dùng CC 0-3, giá trị 0-127\
Hiệu ứng 2 dùng CC 4-7, giá trị 0-127\
Hiệu ứng 3 dùng CC 8-11, giá trị 0-127\
… và tiếp tục như vậy.

Mỗi nhóm bốn CC điều khiển mức và 3 tham số của hiệu ứng đó:

<table><thead><tr><th width="164">Hiệu ứng:</th><th>1</th><th width="124">2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td><strong>Mức</strong></td><td>CC : 0</td><td>CC : 4</td><td>CC : 8</td><td>CC : 12</td><td>CC : 16</td></tr><tr><td>Tham số 1</td><td>CC : 1</td><td>CC : 5</td><td>CC : 9</td><td>CC : 13</td><td>...v.v.</td></tr><tr><td><strong>Tham số 2</strong></td><td>CC : 2</td><td>CC : 6</td><td>CC : 10</td><td>CC : 14</td><td></td></tr><tr><td><strong>Tham số 3</strong></td><td>CC : 3</td><td>CC : 7</td><td>CC : 11</td><td>CC : 15</td><td></td></tr></tbody></table>

### **Cài đặt toàn cục**

Thông điệp MIDI control change trên **channel 16** thay đổi các cài đặt toàn cục:\
CC 1 : Shift X (ngang) 0 -127, 64 là vị trí giữa\
CC 2 : Shift Y (dọc) 0 -127, 64 là vị trí giữa\
CC 4 : Scale X\
CC 5 : Scale Y\
CC 8 : Rotation 3D (Y)\
CC 9 : Rotation 2D (Z)

Và quan trọng là:\
CC 15 : Global brightness

Xin lưu ý rằng hệ thống này ban đầu được thiết kế cho ghi và phát lại, cho phép bạn dùng Logic, Ableton hoặc DAW khác để tạo hoạt ảnh theo timeline. Dù bạn có thể dùng nó để điều khiển live, hệ thống này chưa được tối ưu cho mục đích đó, và còn thiếu một số chức năng điều khiển live so với thiết lập APC40.
