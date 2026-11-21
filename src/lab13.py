"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    raise NotImplementedError('VIẾT Ở ĐÂY')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # CP4 · D1: cỡ mẫu theo yêu cầu, nhân viên và depot.
    from statistics import NormalDist

    ty_le_goc = 0.70
    ty_le_muc_tieu = 0.75
    alpha = 0.05
    power = 0.80
    icc = 0.02
    phan_phoi_chuan = NormalDist()
    z_alpha = phan_phoi_chuan.inv_cdf(1 - alpha / 2)
    z_power = phan_phoi_chuan.inv_cdf(power)
    ty_le_trung_binh = (ty_le_goc + ty_le_muc_tieu) / 2
    phuong_sai_gop = 2 * ty_le_trung_binh * (1 - ty_le_trung_binh)
    phuong_sai_rieng = ty_le_goc * (1 - ty_le_goc) + ty_le_muc_tieu * (1 - ty_le_muc_tieu)
    chenhlech = ty_le_muc_tieu - ty_le_goc
    mau_moi_nhom = math.ceil(
        ((z_alpha * math.sqrt(phuong_sai_gop) + z_power * math.sqrt(phuong_sai_rieng)) / chenhlech) ** 2
    )

    yeu_cau_moi_nhan_vien = 75
    he_so_thiet_ke = 1 + (yeu_cau_moi_nhan_vien - 1) * icc
    mau_theo_nhan_vien = math.ceil(mau_moi_nhom * he_so_thiet_ke)
    nhan_vien_can_moi_nhom = math.ceil(mau_theo_nhan_vien / yeu_cau_moi_nhan_vien)

    nhan_vien_moi_nhom = 20
    depot_moi_nhom = 6
    gioi_han_theo_nhan_vien = nhan_vien_moi_nhom / icc
    gioi_han_theo_depot = depot_moi_nhom / icc

    # Đề bài cho sẵn mục tiêu 859 mẫu hiệu dụng mỗi nhóm ở mức chênh 6 điểm.
    mau_hieu_dung_muc_tieu = 859
    yeu_cau_toi_thieu = math.ceil(
        mau_hieu_dung_muc_tieu * (1 - icc)
        / (nhan_vien_moi_nhom - mau_hieu_dung_muc_tieu * icc)
    )
    he_so_thiet_ke_6_diem = 1 + (yeu_cau_toi_thieu - 1) * icc

    print('\nD1 · Cỡ mẫu pilot')
    print(f'a) Theo yêu cầu: {mau_moi_nhom} yêu cầu/nhóm.')
    print(
        f'b) DE = {he_so_thiet_ke:.2f}, {mau_theo_nhan_vien} yêu cầu/nhóm, '
        f'{nhan_vien_can_moi_nhom} nhân viên/nhóm, '
        f'tổng {2 * nhan_vien_can_moi_nhom} > 40 nên không đủ nhân viên.'
    )
    print(
        f'c) 20 nhân viên/nhóm: mẫu hiệu dụng < {gioi_han_theo_nhan_vien:.0f}, '
        f'không đạt {mau_moi_nhom}.'
    )
    print(
        f'd) 6 depot/nhóm: mẫu hiệu dụng < {gioi_han_theo_depot:.0f}, '
        f'không đạt {mau_moi_nhom}.'
    )
    print(f'e) Mức chênh 6 điểm: {yeu_cau_toi_thieu} yêu cầu/nhân viên, DE = {he_so_thiet_ke_6_diem:.2f}.')
