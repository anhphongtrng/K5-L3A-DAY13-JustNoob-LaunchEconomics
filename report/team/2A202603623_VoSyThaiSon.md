# Báo cáo cá nhân CP1

## 1. Thông tin thành viên

- Họ tên: Võ Sỹ Thái Sơn
- MSSV: 2A202603623
- Email: …
- Vai trong nhóm: Người 1, phụ trách phần A ở CP1.

## 2. Phần việc phụ trách

Ở CP1, em phụ trách tính chi phí cho mỗi yêu cầu hoàn phí mà trợ lý xử lý thành công. Em kiểm tra số lần chạy lại, tính các khoản chi phí, xem kết quả theo từng loại yêu cầu rồi thử cộng thêm chi phí cố định.

## 3. Đóng góp cụ thể

Em tạo môi trường Python trên máy và chạy CP1 bằng Git Bash trong repo của nhóm. Khi thiết lập môi trường lần đầu, máy em thiếu lệnh `py`, nên em dùng `python -m venv .venv` để tạo môi trường. Sau khi cài thư viện, em chạy lại và kiểm tra lần lượt các phần A1 đến A4.

## 4. Bằng chứng

Em chạy lệnh sau trong thư mục `src/`:

```bash
./.venv/Scripts/python.exe lab13.py --checkpoint 1
```

| Phần | Kết quả em kiểm tra |
| --- | --- |
| A1 | Cả ba phép thử đều đạt, với các mốc 1,20 · 1,25 · 1,25. |
| A2 | Có 978 ca thành công trên 1.200 yêu cầu. Tổng chi phí là 4.373.585 đ, tính ra khoảng 4.472 đ/ca thành công (simulated). Chi phí làm lại chiếm 51,8% tổng chi phí (simulated). |
| A3 | Kết quả đủ bốn loại yêu cầu. Quốc tế có 27,3% ca thành công và tốn 22.515 đ/ca thành công (simulated). Tỉ lệ lần chạy trả về `ok` giảm từ 30,0% ở lần đầu xuống 2,2% ở lần thứ ba. |
| A4 | Với nội địa và hàng nặng, sau khi cộng 40 triệu đ/tháng, chi phí là 4.599 đ/ca ở mức 45.000 yêu cầu toàn công ty mỗi tháng và 5.784 đ/ca ở mức 22.500 (simulated). |

[Bảng chi phí của nhóm](bang_chi_phi.md) · [Mã chạy CP1](../../src/lab13.py)

## 5. Công cụ AI đã dùng

Em dùng Codex để hỗ trợ viết code và sửa lỗi khi cài môi trường. Claude hỗ trợ kiểm tra lại phép tính chi phí mỗi ca thành công. Em tự chạy lệnh CP1 trên fork của nhóm rồi so số in ra với bảng chi phí.

## 6. Tự đánh giá

Điều em thấy dễ nhầm nhất là lấy 274,7 đ tiền token và tool trên mỗi yêu cầu để nói về chi phí xử lý. Phép tính của CP1 còn cộng tiền xem lại, làm lại và tính cả chi phí của những lần chạy lỗi. Tổng đó chỉ chia cho 978 ca làm thành công nên kết quả là 4.472 đ/ca (simulated), gấp khoảng 16,28 lần mức 274,7 đ.
