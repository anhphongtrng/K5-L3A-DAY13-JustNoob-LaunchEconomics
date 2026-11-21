# Báo cáo cá nhân · Trần Nguyễn Anh Phong

## 1. Thông tin thành viên

| Thông tin | Nội dung |
| --- | --- |
| Họ tên | Trần Nguyễn Anh Phong |
| MSSV | 2A202603629 |
| Nhóm, lớp | JustNoob, L3A |
| Phần phụ trách | Các mục 4, 5 và 6 của hồ sơ launch. Người gắn nhãn 2 ở CP3. |

## 2. Phần việc phụ trách

Tôi phụ trách mục 4, 5 và 6 của hồ sơ launch. Tôi viết phần đo chỉ số, làm bảng lỗi cùng nhóm và lên kế hoạch pilot để trình bày ở Gate 2a. [Hồ sơ launch](ho_so_launch_v0.md)

## 3. Đóng góp cụ thể

- **Mục 4 · Chỉ số và cách đo.** Tôi viết cách tính cho ba chỉ số trên mẫu giả lập. Có 994/1.200 yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (**82,83%**), 48/177 gợi ý bị sửa hoặc bỏ trong số ca được xem lại (**27,12%**) và 51/1.200 yêu cầu mở lại (**4,25%**). Tôi ghi sáu sự kiện có trace_id, chỉ rõ sự kiện dùng cho từng chỉ số và bổ sung dấu hiệu theo dõi rủi ro làm lại, xem lại. [Bảng E1–E2](chi_so.md)
- **Mục 5 · Bảng lỗi.** Tôi điền 20 nhãn Người 2. Sau khi ghép hai cột, kết quả trùng 20/20. Nhóm chọn năm ca, mỗi loại một ca, rồi ghi cách phát hiện, xử lý và người phụ trách. Với ca 20, nhóm đề xuất dùng chung một khóa cho cùng khoản hoàn và đối soát sổ cái để chặn hoàn trùng. [Bảng lỗi CP3](bang_loi.md)
- **Mục 6 · Pilot.** Tôi tính D1 và chọn chia ngẫu nhiên theo nhân viên, phân tầng theo depot. Pilot gồm nội địa và hàng nặng, với 20 người dùng trợ lý và 20 người đối chứng. Để có khoảng 859 mẫu hiệu dụng mỗi nhóm và phát hiện chênh 6 điểm phần trăm, cần ít nhất 299 yêu cầu đủ điều kiện mỗi người. Tôi ghi ba luật dừng về an toàn, chi phí, sử dụng và cách chuyển về xử lý thủ công khi phải quay lui. [Kế hoạch D1–D3](pilot_plan.yaml)

## 4. Bằng chứng

| Phần | Commit |
| --- | --- |
| Chỉ số, sự kiện và rủi ro kinh tế | 6d94b59, 38341d9 |
| Nhãn Người 2, đối chiếu và bảng khắc phục | 9ef0427, 40c2139 |
| Cỡ mẫu, cách chia và kế hoạch pilot | 926e935, 808e798, ca7e630 |
| Tổng hợp hồ sơ Gate 2a | 616172a |

## 5. Tự đánh giá

Phần dễ nhầm trong kế hoạch của tôi là hai mốc 5 và 6 điểm phần trăm. Nhóm dùng mốc 6 điểm để tính cỡ mẫu và mốc 5 điểm để cân nhắc mở rộng. Với cỡ mẫu đã chọn, power khoảng 80% ở mức 6 điểm và 64% ở mức 5 điểm. Đến ngày đánh giá, tôi cần xem đã đủ mẫu và đủ thời gian theo dõi chưa rồi mới đề xuất mở rộng.
