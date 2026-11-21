# Báo cáo cá nhân CP1 đến CP3

## 1. Thông tin thành viên

- Họ tên: Võ Sỹ Thái Sơn
- MSSV: 2A202603623
- Email: …
- Vai trong nhóm: Người 1, phụ trách phần A, phần B và bộ nhãn Người 1 ở CP3.

## 2. Phần việc phụ trách

Ở CP1, tôi tính chi phí cho mỗi ca hoàn phí trợ lý xử lý thành công. Tôi kiểm tra các phép tính về số lần chạy lại, sau đó tách chi phí theo loại yêu cầu và tính thêm phần chi phí cố định.

Ở CP2, tôi xem chi phí thay đổi bao nhiêu khi chỉnh từng yếu tố. Tôi cũng so ba mức giới hạn số lần chạy và tính thử trường hợp nhân viên phải xem lại 100% yêu cầu có kết quả trong phạm vi nội địa và hàng nặng.

Ở CP3, tôi phụ trách cột nhãn Người 1 cho 20 tình huống hoàn phí trong đề. Mỗi ca có một nhãn theo nguyên nhân chính.

## 3. Đóng góp cụ thể

Tôi tạo môi trường Python trên máy và chạy CP1 bằng Git Bash trong repo của nhóm. Khi thiết lập môi trường lần đầu, máy tôi thiếu lệnh `py`, nên tôi dùng `python -m venv .venv` để tạo môi trường. Sau khi cài thư viện, tôi chạy lại và kiểm tra lần lượt các phần A1 đến A4.

Với CP2, tôi chạy lại mô hình ở chín kịch bản B1 và so các dòng với bảng chi phí. Khi kiểm tra B3, tôi đọc cả cột chi phí của trợ lý lẫn cột chi phí cả hệ thống, vì yêu cầu trợ lý xử lý không xong vẫn phải chuyển cho nhân viên.

Phần CP3 đã có đủ 20 nhãn trong cột Người 1. Ví dụ ca 18 được xếp vào lỗi ngữ cảnh vì số tiền hoàn đúng nhưng tin nhắn thiếu cách tính, nên khách tưởng bị hoàn thiếu.

## 4. Bằng chứng

Tôi chạy CP1 trong thư mục `src/` bằng lệnh sau:

```bash
./.venv/Scripts/python.exe lab13.py --checkpoint 1
```

| Phần | Kết quả tôi kiểm tra |
| --- | --- |
| A1 | Cả ba phép thử đều đạt, với các mốc 1,20 · 1,25 · 1,25. |
| A2 | Có 978 ca thành công trên 1.200 yêu cầu. Tổng chi phí là 4.373.585 đ, tính ra khoảng 4.472 đ/ca thành công (simulated). Chi phí làm lại chiếm 51,8% tổng chi phí (simulated). |
| A3 | Kết quả đủ bốn loại yêu cầu. Quốc tế có 27,3% ca thành công và tốn 22.515 đ/ca thành công (simulated). Tỉ lệ lần chạy trả về `ok` giảm từ 30,0% ở lần đầu xuống 2,2% ở lần thứ ba. |
| A4 | Với nội địa và hàng nặng, sau khi cộng 40 triệu đ/tháng, chi phí là 4.599 đ/ca ở mức 45.000 yêu cầu toàn công ty mỗi tháng và 5.784 đ/ca ở mức 22.500 (simulated). |

Tôi chạy CP2 trong cùng thư mục:

```bash
./.venv/Scripts/python.exe lab13.py --checkpoint 2
```

| Phần | Kết quả tôi kiểm tra |
| --- | --- |
| B1 | Có đủ 9 kịch bản. Gấp đôi số ca làm lại làm chi phí tăng 51,8%, lên 6.787 đ/ca thành công (simulated). |
| B2 | Gấp đôi giá token và phần xem lại cùng lúc cho ra 6.543 đ/ca, tăng 46,3% (simulated). Ba yếu tố ảnh hưởng nhiều nhất là làm lại, xem lại rồi đến lương nhân viên. |
| B3 | Một lần chạy có chi phí mỗi ca thành công thấp nhất là 4.111 đ. Hai lần chạy có tổng chi phí cả hệ thống thấp nhất là 6.901.220 đ (simulated). |
| B4 | Khi xem lại 100%, chi phí là 11.743 đ/ca nếu làm lại mất 9 phút và 12.415 đ/ca nếu mất 15,3 phút (simulated). Mức thứ hai vượt mốc 12.000 đ của cách làm thủ công. |

[Bảng chi phí của nhóm](bang_chi_phi.md) · [Mã chạy CP1 và CP2](../../src/lab13.py)

Ở CP3, cột Người 1 có 4 ca do người dùng, 5 ca hệ thống, 4 ca ngữ cảnh, 4 ca giới hạn hệ thống và 3 ca lỗi ngầm. [Bảng nhãn CP3](bang_loi.md)

Trong buổi duyệt chéo, nhóm tôi được hỏi vì sao chọn hai lần chạy. Nhóm trả lời rằng một lần rẻ nhất trên mỗi ca trợ lý làm xong, nhưng để lại 319 ca cho nhân viên. Hai lần còn 234 ca và có tổng chi phí hệ thống thấp nhất là 6.901.220 đ (simulated). [Kết quả duyệt chéo của nhóm](group_report.md#4-kết-quả-và-duyệt-chéo)

## 5. Công cụ AI đã dùng

Tôi dùng Codex để hỗ trợ viết code và sửa lỗi khi cài môi trường. Claude giúp rà lại phép tính ở CP1, B3 và B4.

## 6. Tự đánh giá

Ở CP1, chỗ tôi thấy dễ nhầm nhất là con số 274,7 đ trên mỗi yêu cầu. Số này chỉ tính tiền token và tool. Phép tính của CP1 còn cộng tiền xem lại, làm lại và tính cả chi phí của những lần chạy lỗi. Tổng đó chỉ chia cho 978 ca làm thành công nên kết quả là 4.472 đ/ca (simulated), gấp khoảng 16,28 lần mức 274,7 đ.

Ở CP2, tôi thấy chọn số lần chạy còn tùy mình nhìn vào cột nào. Giới hạn một lần nhìn rẻ hơn nếu chỉ tính các ca trợ lý làm xong, nhưng lại có thêm 85 ca không thành công so với mức hai lần. Khi cộng khoản nhân viên phải xử lý những ca đó, mức hai lần có tổng chi phí thấp hơn.

Ở CP3, tôi thấy lỗi hệ thống và lỗi ngầm dễ lẫn. Ví dụ ca 17 cũng có lỗi dùng bảng giá cũ, nhưng được xếp vào lỗi ngầm vì sai lệch kéo dài mà không ai mở lại yêu cầu.
