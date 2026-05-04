---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/MdbbIbIwHdJwkEREnJyv/midi-control/midi-control-overview
---

# 🟩 Tổng quan về điều khiển MIDI

Liberation sử dụng MIDI theo một số cách:

* Làm bộ điều khiển live. APC40 Mk1/Mk2, APC Mini và MIDI Fighter Twister có thể tự động kết nối khi có thiết bị tương ứng. Xem [Bộ điều khiển MIDI live](live-control-with-the-apc40.md "mention").
* Làm nguồn đồng bộ nhịp bằng MIDI clock và thông điệp vị trí bài hát MIDI. Xem [MIDI clock](../tempo-synchronisation.md#midi-clock "mention")
* Làm đầu vào tương tác trên node MIDI notes để tạo hiệu ứng kiểu “đàn hạc laser”. Xem [MIDI notes](../clip-editor/operator-nodes/midi-notes.md "mention")
* Làm hệ thống đầu vào/đầu ra tổng quát hơn bằng hệ thống MIDI Send/Receive. Xem [MIDI Send/Receive](midi-send-receive.md "mention")

Các bộ điều khiển live được hỗ trợ sẽ theo trạng thái hiển thị trên màn hình của Liberation: các nút Clip sáng theo màu của group, các nút zone hiển thị trạng thái zone, và các knob hoặc encoder đã map sẽ theo hiệu ứng hiện tại hoặc các điều khiển trong panel Parameters.
