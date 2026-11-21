# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Tóm tắt ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Khách nhập số tài khoản thiếu hai chữ số, ngân hàng từ chối lệnh hoàn. | Do người dùng | Do người dùng | ... | ... |
| 2 | Kiện nội địa 28 kg bị tra theo giá hàng thường, hoàn thiếu 45.000 đ. | Hệ thống | Hệ thống | ... | ... |
| 3 | Tiền về ví LogiX trong 5 phút, nhưng khách chờ tiền về tài khoản ngân hàng. | Ngữ cảnh | Ngữ cảnh | ... | ... |
| 4 | LogiX thiếu dữ liệu chặng do hãng nước ngoài giao, trợ lý chuyển ca cho nhân viên. | Giới hạn hệ thống | Giới hạn hệ thống | ... | ... |
| 5 | Kiểm tra cuối tuần phát hiện 14 đơn có mã giảm giá được hoàn thừa trung bình 12.000 đ. | Ngầm | Ngầm | ... | ... |
| 6 | Khách chọn mục giao trễ nhưng mô tả hàng vỡ. Trợ lý từ chối vì đơn giao đúng hạn. | Do người dùng | Do người dùng | ... | ... |
| 7 | API sổ cái lỗi 503 sau 3 lần thử lại, trợ lý vẫn báo đã hoàn tiền. | Hệ thống | Hệ thống | ... | ... |
| 8 | Trợ lý viện dẫn điều khoản 7.2 không tồn tại, dù số tiền hoàn đúng. | Hệ thống | Hệ thống | ... | ... |
| 9 | Khách nhập mã đơn của sàn thay cho mã vận đơn, trợ lý báo lỗi rồi dừng. | Do người dùng | Do người dùng | ... | ... |
| 10 | Đơn trễ do bão bị từ chối hoàn đúng chính sách, nhưng ứng dụng vẫn hiện cam kết giao 24 giờ. | Ngữ cảnh | Ngữ cảnh | ... | ... |
| 11 | Trợ lý không xử lý được tin nhắn thoại 40 giây và yêu cầu khách nhập chữ. | Giới hạn hệ thống | Giới hạn hệ thống | ... | ... |
| 12 | Tool tra đơn D05 trả thiếu trường. Kết quả vẫn đúng nhưng chi phí token gấp ba suốt ba tuần. | Ngầm | Ngầm | ... | ... |
| 13 | Khách hỏi hoàn phí bảo hiểm ngoài phạm vi, trợ lý trả lời chung chung về phí vận chuyển. | Giới hạn hệ thống | Giới hạn hệ thống | ... | ... |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu bị đóng. | Do người dùng | Do người dùng | ... | ... |
| 15 | Đơn trễ 26 giờ đáng lẽ hoàn 50%, trợ lý tính 100% và nhân viên phát hiện trước khi gửi. | Hệ thống | Hệ thống | ... | ... |
| 16 | Trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng, khách phản ánh bị làm phiền. | Ngữ cảnh | Ngữ cảnh | ... | ... |
| 17 | Trợ lý dùng bảng giá cũ cho đơn dưới 2 kg, làm lệch 212 đơn trong 9 ngày mà không ai mở lại. | Ngầm | Ngầm | ... | ... |
| 18 | Trợ lý hoàn đúng 15.000 đ nhưng thiếu cách tính, khách tưởng hoàn thiếu và mở lại yêu cầu. | Ngữ cảnh | Ngữ cảnh | ... | ... |
| 19 | Đơn đã 14 tháng, vượt phạm vi dữ liệu 12 tháng. Trợ lý chuyển ca kèm tóm tắt. | Giới hạn hệ thống | Giới hạn hệ thống | ... | ... |
| 20 | Khách gửi lại yêu cầu sau 10 phút, trợ lý hoàn hai lần vì thiếu khóa chống trùng. | Hệ thống | Hệ thống | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
