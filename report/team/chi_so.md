# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Tỉ lệ yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` chia tổng số yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu được xem lại có `quyet_dinh_xem_lai` là `sua` hoặc `bo` chia số yêu cầu có `duoc_xem_lai = 1` | 48/177 = **27,12%** |
| An toàn | Tỉ lệ lỗi lọt đến khách, đo qua yêu cầu mở lại | Số yêu cầu có `mo_lai_trong_7_ngay = 1` chia tổng số yêu cầu | 51/1.200 = **4,25%** |
| Dùng | Tỉ lệ yêu cầu trong nhóm can thiệp được mở bằng trợ lý | Số yêu cầu có ít nhất một lượt mở trợ lý chia tổng số yêu cầu đủ điều kiện trong nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ yêu cầu hoàn sai số tiền trong mẫu kiểm tra hằng tuần | Số yêu cầu đã kiểm tra có số tiền thực hoàn khác số tiền đúng theo chính sách chia tổng số yêu cầu đã kiểm tra | Không cần tính |

Ba kết quả tính thử lấy từ [logix_requests.csv](../../src/logix_requests.csv), dữ liệu giả lập của đợt chạy thử. Chỉ số chính trong đợt chạy thử là **82,83%**. Đợt này thiếu nhóm đối chứng đồng thời nên chưa ước lượng được tác động của trợ lý.

## Danh sách event

Mỗi event có `trace_id` để nối với trace và `request_id` để đếm mỗi yêu cầu một lần. Hệ thống cấp `trace_id` từ lúc tạo yêu cầu ở cả hai nhóm.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `trace_id`, `request_id`, `created_at`, `arm`, `eligible`, `loai` | Khi ghi nhận yêu cầu và xác định nhóm pilot |
| `agent_opened` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `opened_at` | Khi nhân viên mở trợ lý cho yêu cầu |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `decision` (`giu`, `sua`, `bo`), `decided_at` | Khi nhân viên xác nhận quyết định xem lại |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `closed_at` | Mỗi lần yêu cầu được đóng |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` | Mỗi lần yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | `trace_id`, `request_id`, `audit_week`, `checked_at`, `so_tien_da_hoan_vnd`, `so_tien_dung_vnd` | Khi hoàn tất kiểm tra một yêu cầu trong mẫu tuần |

### Đối chiếu chỉ số với event

- **Chỉ số chính:** `refund_request_created` cho mẫu số và mốc bắt đầu. Ghép `ticket_closed` và `ticket_reopened` để đếm yêu cầu đóng lần đầu trong 24 giờ và không mở lại trong 7 ngày kể từ lần đóng đầu.
- **Bỏ qua gợi ý:** dùng quyết định cuối trong `staff_review_decision` của mỗi yêu cầu đã xem lại. Đếm quyết định `sua` hoặc `bo` ở tử số và cả ba loại quyết định ở mẫu số.
- **Mở lại trong 7 ngày:** `refund_request_created` cho mẫu số. Ghép `ticket_closed` và `ticket_reopened` để đếm yêu cầu mở lại trong 7 ngày kể từ lần đóng đầu. Chỉ báo cáo hai chỉ số có cửa sổ 7 ngày khi đã đủ thời gian theo dõi cho kỳ đo.
- **Mở trợ lý:** lọc `refund_request_created` theo `arm` can thiệp và `eligible = true`. Đếm số yêu cầu trong tập đó có ít nhất một `agent_opened`.
- **Hoàn sai số tiền qua kiểm tra mẫu:** dùng `audit_sample_checked`, giữ bản kiểm tra cuối của mỗi yêu cầu trong tuần. So sánh hai trường số tiền để tính tử số, dùng số yêu cầu đã kiểm tra làm mẫu số.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
