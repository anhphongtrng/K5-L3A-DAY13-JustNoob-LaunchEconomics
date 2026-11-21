# Báo cáo nhóm JustNoob · Lab 13

## 1. Thông tin nhóm

Nhóm **JustNoob**, lớp **L3A**. Xem thành viên và phân công trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm dùng 1.200 yêu cầu hoàn phí giả lập của LogiX-VN để tính chi phí, phân loại lỗi và đề xuất pilot có đối chứng. Khi so với mức 12.000 đ/yêu cầu xử lý thủ công, nhóm tính cả phần nhân viên phải làm thay.

## 3. Giải pháp theo checkpoint

| Phần | Nhóm đã làm | Bằng chứng |
| --- | --- | --- |
| A · Chi phí | Ba phép thử A1 đều đạt. Mô hình cộng token, tool, thời gian xem lại và làm lại. Với 978 ca thành công, chi phí là 4.472 đ/ca. Tính cả nhân viên làm thay cho ra 5.865 đ/yêu cầu (simulated). | [Code](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Kiểm tra 9 kịch bản. Làm lại gấp đôi tăng chi phí 51,8%, xem lại gấp đôi tăng 40,7% và lương tăng 25% làm chi phí tăng 23,1% (simulated). | [Bảng B1–B4](bang_chi_phi.md) |
| C · Lỗi | Hai cột nhãn trùng 20/20. Nhóm chọn một ca cho mỗi loại để ghi cách phát hiện, xử lý và người phụ trách. Ca hoàn trùng dùng khóa chống trùng và đối soát sổ cái. | [Bảng lỗi](bang_loi.md) |
| D · Pilot | Chọn nội địa và hàng nặng. Chia ngẫu nhiên 20 nhân viên dùng trợ lý và 20 đối chứng, cần 299 yêu cầu đủ điều kiện mỗi người để phát hiện chênh 6 điểm phần trăm với power 80%. Có ba luật dừng và phương án quay lui. | [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Mẫu giả lập ghi nhận 82,83% đóng trong 24 giờ và không mở lại trong 7 ngày, 27,12% gợi ý bị sửa hoặc bỏ trong các ca được xem lại, 4,25% yêu cầu mở lại. Nhóm đặc tả 6 sự kiện có trace_id và ghi rủi ro làm lại, xem lại. | [Chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## 4. Kết quả và duyệt chéo

Nhóm đề xuất **Go có điều kiện** cho pilot nội địa và hàng nặng. Xem lại 100% và làm lại mất 15,3 phút có thể đưa chi phí lên **12.415 đ/ca thành công** (simulated). Nếu chi phí vượt **10.000 đ/ca** trong hai tuần đo hoàn chỉnh liên tiếp, PM sẽ thu hẹp về nội địa và giới hạn hai lần chạy. [Hồ sơ launch JustNoob](ho_so_launch_v0.md)

**Câu hỏi hội đồng**

> Một lần chạy rẻ hơn, sao nhóm chọn hai lần?

**Câu trả lời của nhóm**

> Một lần rẻ nhất trên mỗi ca trợ lý làm xong, nhưng còn 319 ca phải để nhân viên xử lý. Hai lần còn 234 ca. Khi cộng phần nhân viên làm thay, hai lần có tổng chi phí thấp nhất trong ba kịch bản.

Đối chiếu B3, mức 1, 2 và 3 lần có tổng chi phí hệ thống lần lượt là **7.449.781 đ**, **6.901.220 đ** và **7.037.585 đ** (simulated). Giới hạn hai lần giảm được 85 ca phải xử lý thủ công so với một lần. [Bảng B3](bang_chi_phi.md#b3--giới-hạn-chạy-lại-có-thật-sự-rẻ-hơn)

Điểm và quyết định hội đồng công bố cho JustNoob chờ xác nhận. Phần JustNoob nhận xét hồ sơ NST nằm trong [phiếu duyệt chéo](phieu_cham.md).

## 5. Khó khăn và cách xử lý

Máy của Sơn thiếu lệnh py, nên Sơn tạo môi trường bằng python -m venv .venv rồi chạy lại CP1 và CP2. Khi so chi phí, nhóm ghi rõ số nào tính trên ca thành công và số nào tính trên toàn bộ yêu cầu.

## 6. Tổng hợp đóng góp

- **Võ Sỹ Thái Sơn (2A202603623)** phụ trách A, B và bộ nhãn Người 1. [Báo cáo cá nhân](2A202603623_VoSyThaiSon.md)
- **Trần Nguyễn Anh Phong (2A202603629)** phụ trách các mục 4, 5 và 6 của hồ sơ launch. Phong viết chỉ số, gắn nhãn Người 2 và hoàn thiện bảng khắc phục, tính cỡ mẫu và lập kế hoạch pilot. [Báo cáo cá nhân](2A202603629_TranNguyenAnhPhong.md)

## 7. Hạn chế và hướng cải thiện

Dữ liệu chạy thử là giả lập và thiếu đối chứng đồng thời. Pilot cần đo lại thời gian xem lại, làm lại và thu đủ 7 ngày theo dõi mở lại. Thiết kế có khoảng 64% power nếu tác động thật chỉ là +5 điểm phần trăm. Nếu thiếu mẫu hoặc thời gian theo dõi, nhóm giữ phạm vi pilot và hẹn mốc đánh giá mới.

## 8. Tài liệu tham khảo

[Đề bài và checkpoint](../../CHECKPOINTS.md) · [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Rubric duyệt chéo](../../RUBRIC.md)
