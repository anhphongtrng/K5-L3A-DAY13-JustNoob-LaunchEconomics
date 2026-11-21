# Báo cáo cá nhân CP1 và CP2

## 1. Thông tin thành viên

- Họ tên: Võ Sỹ Thái Sơn
- MSSV: 2A202603623
- Email: …
- Vai trong nhóm: Người 1, phụ trách phần A ở CP1 và phần B ở CP2.

## 2. Phần việc phụ trách

Ở CP1, em phụ trách tính chi phí cho mỗi yêu cầu hoàn phí mà trợ lý xử lý thành công. Em kiểm tra số lần chạy lại, tính các khoản chi phí, xem kết quả theo từng loại yêu cầu rồi thử cộng thêm chi phí cố định.

Ở CP2, em xem chi phí thay đổi bao nhiêu khi chỉnh từng yếu tố. Em cũng so ba mức giới hạn số lần chạy và tính thử trường hợp nhân viên phải xem lại 100% yêu cầu có kết quả trong phạm vi nội địa và hàng nặng.

## 3. Đóng góp cụ thể

Em tạo môi trường Python trên máy và chạy CP1 bằng Git Bash trong repo của nhóm. Khi thiết lập môi trường lần đầu, máy em thiếu lệnh `py`, nên em dùng `python -m venv .venv` để tạo môi trường. Sau khi cài thư viện, em chạy lại và kiểm tra lần lượt các phần A1 đến A4.

Với CP2, em chạy lại mô hình ở chín kịch bản B1 và so các dòng với bảng chi phí. Khi kiểm tra B3, em đọc cả cột chi phí của trợ lý lẫn cột chi phí cả hệ thống, vì yêu cầu trợ lý xử lý không xong vẫn phải chuyển cho nhân viên.

## 4. Bằng chứng

Em chạy CP1 trong thư mục `src/` bằng lệnh sau:

```bash
./.venv/Scripts/python.exe lab13.py --checkpoint 1
```

| Phần | Kết quả em kiểm tra |
| --- | --- |
| A1 | Cả ba phép thử đều đạt, với các mốc 1,20 · 1,25 · 1,25. |
| A2 | Có 978 ca thành công trên 1.200 yêu cầu. Tổng chi phí là 4.373.585 đ, tính ra khoảng 4.472 đ/ca thành công (simulated). Chi phí làm lại chiếm 51,8% tổng chi phí (simulated). |
| A3 | Kết quả đủ bốn loại yêu cầu. Quốc tế có 27,3% ca thành công và tốn 22.515 đ/ca thành công (simulated). Tỉ lệ lần chạy trả về `ok` giảm từ 30,0% ở lần đầu xuống 2,2% ở lần thứ ba. |
| A4 | Với nội địa và hàng nặng, sau khi cộng 40 triệu đ/tháng, chi phí là 4.599 đ/ca ở mức 45.000 yêu cầu toàn công ty mỗi tháng và 5.784 đ/ca ở mức 22.500 (simulated). |

Em chạy CP2 trong cùng thư mục:

```bash
./.venv/Scripts/python.exe lab13.py --checkpoint 2
```

| Phần | Kết quả em kiểm tra |
| --- | --- |
| B1 | Có đủ 9 kịch bản. Gấp đôi số ca làm lại làm chi phí tăng 51,8%, lên 6.787 đ/ca thành công (simulated). |
| B2 | Gấp đôi giá token và phần xem lại cùng lúc cho ra 6.543 đ/ca, tăng 46,3% (simulated). Ba yếu tố ảnh hưởng nhiều nhất là làm lại, xem lại rồi đến lương nhân viên. |
| B3 | Một lần chạy có chi phí mỗi ca thành công thấp nhất là 4.111 đ. Hai lần chạy có tổng chi phí cả hệ thống thấp nhất là 6.901.220 đ (simulated). |
| B4 | Khi xem lại 100%, chi phí là 11.743 đ/ca nếu làm lại mất 9 phút và 12.415 đ/ca nếu mất 15,3 phút (simulated). Mức thứ hai vượt mốc 12.000 đ của cách làm thủ công. |

[Bảng chi phí của nhóm](bang_chi_phi.md) · [Mã chạy CP1 và CP2](../../src/lab13.py)

## 5. Công cụ AI đã dùng

Em dùng Codex để hỗ trợ viết code và sửa lỗi khi cài môi trường. Claude giúp rà lại phép tính ở CP1, B3 và B4. Em tự chạy hai lệnh trên fork của nhóm rồi so số in ra với bảng chi phí.

## 6. Tự đánh giá

Điều em thấy dễ nhầm nhất là lấy 274,7 đ tiền token và tool trên mỗi yêu cầu để nói về chi phí xử lý. Phép tính của CP1 còn cộng tiền xem lại, làm lại và tính cả chi phí của những lần chạy lỗi. Tổng đó chỉ chia cho 978 ca làm thành công nên kết quả là 4.472 đ/ca (simulated), gấp khoảng 16,28 lần mức 274,7 đ.

Ở CP2, em thấy chọn số lần chạy còn tùy mình nhìn vào cột nào. Giới hạn một lần nhìn rẻ hơn nếu chỉ tính các ca trợ lý làm xong, nhưng lại có thêm 85 ca không thành công so với mức hai lần. Khi cộng khoản nhân viên phải xử lý những ca đó, mức hai lần có tổng chi phí thấp hơn.
