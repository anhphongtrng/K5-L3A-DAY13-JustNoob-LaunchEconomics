# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm **JustNoob** · Lớp **L3A**

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/ca thành công**, với 978 ca thành công trên 1.200 yêu cầu. [A2](bang_chi_phi.md#a2--mô-hình-chi-phí-từ-trace) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% **+23,1%**. [B1–B2](bang_chi_phi.md#b1--đổi-từng-yếu-tố) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Tính cả phần nhân viên làm thay, chi phí hệ thống là **5.865 đ/yêu cầu** so với **12.000 đ** xử lý thủ công. [A2](bang_chi_phi.md#a2--mô-hình-chi-phí-từ-trace) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, sử dụng và an toàn | Chạy thử ghi nhận **82,83%** đóng trong 24 giờ và không mở lại trong 7 ngày, **27,12%** gợi ý bị sửa hoặc bỏ trong số yêu cầu được xem lại, **4,25%** mở lại. [E1](chi_so.md) | Giả lập | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai cột nhãn trùng **20/20 ca**, đã lập bảng khắc phục cho **5 loại lỗi**. [C](bang_loi.md) | Xong, có bằng chứng | Người gắn nhãn 2 |
| 6 · Pilot plan | `noi_dia` và `hang_nang`, chia ngẫu nhiên **20 nhân viên mỗi nhóm**, cần **299 yêu cầu đủ điều kiện/người**. Power **80%** ở mức chênh **6 điểm phần trăm**, khoảng **64%** ở mức **5 điểm**. [D](pilot_plan.yaml) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Theo dõi làm lại trên **7%** và xem lại trên **20%** mỗi tuần. Nếu phải xem lại 100% và làm lại mất 15,3 phút/ca, CPS lên **12.415 đ/ca**, vượt mốc **12.000 đ**. [E2](chi_so.md#e2--rủi-ro-kinh-tế) · [B4](bang_chi_phi.md#b4--nếu-phải-xem-lại-tất-cả) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất Gate 2a — Go có điều kiện cho pilot `noi_dia` và `hang_nang`.** A3 ước tính chi phí **2.696 đ** và **8.221 đ/ca thành công** (simulated). Rủi ro xem lại 100% có thể xóa lợi thế chi phí, và thiết kế chỉ có khoảng **64% power** nếu tác động thật là đúng 5 điểm phần trăm.

- **30/11/2026 · Giám đốc vận hành:** Xác nhận đủ 40 nhân viên và khả năng thu 299 yêu cầu đủ điều kiện/người. Khóa phân nhóm và kiểm tra cơ chế tắt trợ lý, bàn giao thủ công trước ngày bắt đầu dự kiến 01/12/2026.
- **30/11/2026 · PM trợ lý hoàn phí:** Kiểm tra log đo chi phí và ba luật dừng trước rollout. Nếu chi phí vượt **10.000 đ/ca thành công** trong hai tuần đo hoàn chỉnh liên tiếp, thu hẹp về `noi_dia` và giới hạn hai lần chạy.
- **26/01/2027 · Giám đốc vận hành:** Đánh giá khi đủ mẫu và đủ 7 ngày theo dõi. Chỉ đề xuất mở rộng nếu chỉ số chính cao hơn đối chứng ít nhất **5 điểm phần trăm**, kiểm định hai phía **p < 0,05** theo cụm nhân viên và đạt các điều kiện vận hành trong kế hoạch.
