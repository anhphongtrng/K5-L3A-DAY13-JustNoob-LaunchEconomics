# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Võ Sỹ Thái Sơn · Người gắn nhãn 2: anhphongtrng

| Ca | Tóm tắt ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- |
| 1 | Khách nhập số tài khoản thiếu hai chữ số, ngân hàng từ chối lệnh hoàn. | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Kiện nội địa 28 kg bị tra theo giá hàng thường, hoàn thiếu 45.000 đ. | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Tiền về ví LogiX trong 5 phút, nhưng khách chờ tiền về tài khoản ngân hàng. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | LogiX thiếu dữ liệu chặng do hãng nước ngoài giao, trợ lý chuyển ca cho nhân viên. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Kiểm tra cuối tuần phát hiện 14 đơn có mã giảm giá được hoàn thừa trung bình 12.000 đ. | Ngầm | Ngầm | Có | Ngầm |
| 6 | Khách chọn mục giao trễ nhưng mô tả hàng vỡ. Trợ lý từ chối vì đơn giao đúng hạn. | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | API sổ cái lỗi 503 sau 3 lần thử lại, trợ lý vẫn báo đã hoàn tiền. | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Trợ lý viện dẫn điều khoản 7.2 không tồn tại, dù số tiền hoàn đúng. | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Khách nhập mã đơn của sàn thay cho mã vận đơn, trợ lý báo lỗi rồi dừng. | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Đơn trễ do bão bị từ chối hoàn đúng chính sách, nhưng ứng dụng vẫn hiện cam kết giao 24 giờ. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Trợ lý không xử lý được tin nhắn thoại 40 giây và yêu cầu khách nhập chữ. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Tool tra đơn D05 trả thiếu trường. Kết quả vẫn đúng nhưng chi phí token gấp ba suốt ba tuần. | Ngầm | Ngầm | Có | Ngầm |
| 13 | Khách hỏi hoàn phí bảo hiểm ngoài phạm vi, trợ lý trả lời chung chung về phí vận chuyển. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu bị đóng. | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Đơn trễ 26 giờ đáng lẽ hoàn 50%, trợ lý tính 100% và nhân viên phát hiện trước khi gửi. | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng, khách phản ánh bị làm phiền. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Trợ lý dùng bảng giá cũ cho đơn dưới 2 kg, làm lệch 212 đơn trong 9 ngày mà không ai mở lại. | Ngầm | Ngầm | Có | Ngầm |
| 18 | Trợ lý hoàn đúng 15.000 đ nhưng thiếu cách tính, khách tưởng hoàn thiếu và mở lại yêu cầu. | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Đơn đã 14 tháng, vượt phạm vi dữ liệu 12 tháng. Trợ lý chuyển ca kèm tóm tắt. | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Khách gửi lại yêu cầu sau 10 phút, trợ lý hoàn hai lần vì thiếu khóa chống trùng. | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20/20 = 100%, đạt ngưỡng 80%.

## Quy tắc phân biệt cho các ca không trùng

Hai bộ nhãn trùng ở cả 20 ca.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_account_validation_failed` mỗi khi số tài khoản sai định dạng theo ngân hàng nhận. Cảnh báo nếu có bất kỳ lệnh hoàn nào được gửi sau lỗi kiểm tra. | Chặn gửi lệnh, chỉ rõ trường cần sửa và xác thực lại trước khi gửi. | Kỹ sư tích hợp thanh toán |
| 20 | Hệ thống | Đối soát sổ cái theo mã yêu cầu hoàn và mã đơn. Cảnh báo ngay khi cùng một khoản hoàn được ghi thành công từ 2 lần trở lên. | Dùng khóa chống trùng cố định theo khoản hoàn, chặn ghi lặp ở sổ cái và chuyển giao dịch đã ghi trùng cho kế toán đối soát. | Kỹ sư dịch vụ hoàn phí |
| 18 | Ngữ cảnh | Rà hằng tuần các event `ticket_reopened` có lý do hoàn thiếu. Đếm ca số tiền đúng nhưng thông báo thiếu căn cứ tính. | Ghi phí gốc, tỉ lệ hoàn và số tiền trong thông báo, ví dụ hoàn 50% của 30.000 đ là 15.000 đ. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Ghi `handoff_to_staff` với lý do vượt 12 tháng. Cảnh báo nếu yêu cầu vượt mốc này không có event bàn giao. | Nêu giới hạn tra cứu và chuyển cho nhân viên kèm mã đơn, ngày gửi và tóm tắt yêu cầu. | Trưởng nhóm vận hành CSKH |
| 5 | Ngầm | Mỗi tuần lấy mẫu đơn có mã giảm giá. Dùng `audit_sample_checked` để đối chiếu số đã hoàn và số đúng theo chính sách, rà ngay nếu phát hiện ít nhất 1 ca hoàn thừa. | Tính khoản hoàn trên số tiền sau giảm giá, thêm phép thử cho đơn có mã giảm giá và đối soát các khoản đã hoàn sai. | Kế toán đối soát |
