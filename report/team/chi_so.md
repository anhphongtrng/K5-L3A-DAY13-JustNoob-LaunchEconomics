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

Tác động lấy từ [bảng độ nhạy B1](bang_chi_phi.md#b1--đổi-từng-yếu-tố) trên toàn bộ 1.200 yêu cầu, so với mức gốc 4.472 đ/ca thành công (simulated). Mốc theo dõi lấy từ CSV giả lập, lọc `noi_dia` và `hang_nang` theo phạm vi pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Nhân viên phải làm lại nhiều hơn | Chi phí làm lại gấp đôi đưa CPS lên **6.787 đ/ca**, tăng **51,8%** (simulated). | Cảnh báo nếu tỉ lệ làm lại theo tuần **vượt 7%**. Tử số là số yêu cầu phải làm lại, mẫu số là tổng yêu cầu trong phạm vi của nhóm can thiệp. Mốc chạy thử: **48/982 = 4,89%** (`ket_qua = lam_lai`). | Rà tối đa 20 trace phải làm lại trong tuần để tìm nguyên nhân và ưu tiên sửa luồng gây lỗi nhiều nhất. Nếu chi phí vượt luật D3, thu hẹp về `noi_dia` và giới hạn tối đa 2 lần chạy. | PM trợ lý hoàn phí |
| Khối lượng xem lại tăng | Chi phí xem lại gấp đôi đưa CPS lên **6.292 đ/ca**, tăng **40,7%** (simulated). | Cảnh báo nếu tỉ lệ xem lại theo tuần **vượt 20%**. Tử số là số yêu cầu có `staff_review_decision`, mẫu số là tổng yêu cầu trong phạm vi của nhóm can thiệp. Mốc chạy thử: **128/982 = 13,03%** (`duoc_xem_lai = 1`). | Rà các yêu cầu phải xem lại theo loại và nguyên nhân. Sửa luồng gây xem lại nhiều nhất và giữ bước rollout hiện tại cho đến khi chi phí và an toàn đạt điều kiện D3. | Trưởng nhóm CSKH |

Ngưỡng 7% và 20% dùng để cảnh báo sớm, cao hơn mốc chạy thử lần lượt khoảng 2,1 và 7,0 điểm phần trăm. Luật dừng chi phí áp dụng theo [kế hoạch pilot](pilot_plan.yaml).
