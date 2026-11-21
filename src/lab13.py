"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import argparse
import math

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return float('inf') if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    xac_suat = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / xac_suat if xac_suat else float('inf')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] * (gia_vao / 1000) + runs['tokens_out'] * (gia_ra / 1000)
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=token,
        tool=tool,
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('inf'),
        hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else 0,
    )



PHAM_VI_PILOT = ('noi_dia', 'hang_nang')
CHI_PHI_CO_DINH = 40_000_000
YEU_CAU_MOI_THANG = 45_000


def in_cp1(runs, reqs, goc):
    print('\nA2 · Chi phí từ trace (đ)')
    khoan_simulated = {'xem_lai', 'lam_lai', 'tong', 'cps'}
    for ten, gia_tri in goc.items():
        nhan = ' [simulated]' if ten in khoan_simulated else ''
        so_le = 1 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:17s} {gia_tri:>14,.{so_le}f}{nhan}')
    print(f"CPS / hóa đơn mỗi yêu cầu: {goc['cps'] / goc['hoa_don_moi_yc']:.2f}× [simulated]")
    print(f"Làm lại / tổng chi phí: {goc['lam_lai'] / goc['tong']:.1%} [simulated]")
    he_thong = goc['tong'] + (len(reqs) - goc['thanh_cong']) * BASELINE
    print(f'Chi phí hệ thống mỗi yêu cầu: {he_thong / len(reqs):,.0f} đ [simulated]')

    print('\nA3 · Theo loại (yêu cầu | thành công | lần chạy/yêu cầu | đ/ca thành công | so baseline)')
    for loai, nhom in reqs.groupby('loai', sort=False):
        kq = mo_hinh(runs, nhom)
        print(f"{loai:12s} {len(nhom):>4} | {kq['thanh_cong'] / len(nhom):6.1%} | "
              f"{nhom['so_lan_chay'].mean():.2f} | {kq['cps']:>7,.0f} | "
              f"{kq['cps'] / BASELINE:.2f}× [simulated]")

    quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'] == 'quoc_te', 'request_id'])]
    print('Tỉ lệ lần chạy ok của quốc tế theo attempt:')
    for attempt, nhom in quoc_te.groupby('attempt'):
        print(f"  Lần {attempt}: {nhom['status'].eq('ok').mean():.1%}")

    print('\nA4 · Chi phí cố định (yêu cầu/tháng | ca thành công | cố định/ca | tổng/ca | so baseline)')
    pham_vi = mo_hinh(runs, reqs[reqs['loai'].isin(PHAM_VI_PILOT)])
    for khoi_luong in (YEU_CAU_MOI_THANG, YEU_CAU_MOI_THANG // 2):
        # 45.000 là lượng yêu cầu toàn công ty, còn ca thành công chỉ tính trong phạm vi pilot.
        thanh_cong = khoi_luong * pham_vi['thanh_cong'] / len(reqs)
        co_dinh_moi_ca = CHI_PHI_CO_DINH / thanh_cong
        cps = pham_vi['cps'] + co_dinh_moi_ca
        print(f'{khoi_luong:6,} | {thanh_cong:6,.0f} | {co_dinh_moi_ca:5,.0f} | '
              f'{cps:5,.0f} | {cps / BASELINE:.2f}× [simulated]')


def in_cp2(runs, reqs, goc):
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=1.25 * LUONG_PHUT),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    ket_qua = {ten: mo_hinh(runs, reqs, **tham_so) for ten, tham_so in kich_ban.items()}
    print('\nB1 · Độ nhạy (đ/ca thành công | thay đổi)')
    for ten, kq in ket_qua.items():
        print(f"{ten:25s} {kq['cps']:>7,.0f} | {kq['cps'] / goc['cps'] - 1:+6.1%} [simulated]")

    doi_cap = mo_hinh(runs, reqs, **kich_ban['Giá token gấp đôi'], **kich_ban['Xem lại gấp đôi'])
    xep_hang = {
        'giá token': ket_qua['Giá token gấp đôi']['cps'] - goc['cps'],
        'làm lại': ket_qua['Làm lại gấp đôi']['cps'] - goc['cps'],
        'xem lại': ket_qua['Xem lại gấp đôi']['cps'] - goc['cps'],
        'lương nhân viên': ket_qua['Lương tăng 25%']['cps'] - goc['cps'],
    }
    print(f"\nB2 · Token và xem lại gấp đôi: {doi_cap['cps']:,.0f} đ | "
          f"{doi_cap['cps'] / goc['cps'] - 1:+.1%} [simulated]")
    ba_yeu_to = sorted(xep_hang, key=xep_hang.get, reverse=True)[:3]
    print('Ba yếu tố nhạy nhất: ' + ' → '.join(ba_yeu_to))

    print('\nB3 · Giới hạn (lần | đ trợ lý | số không thành công | đ hệ thống | đ/ca thành công)')
    for gioi_han, kq in enumerate((ket_qua['Chỉ 1 lần chạy'], ket_qua['Tối đa 2 lần chạy'], goc), 1):
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_thanh_cong * BASELINE
        print(f"{gioi_han} | {kq['tong']:>9,.0f} | {khong_thanh_cong} | "
              f"{he_thong:>9,.0f} | {kq['cps']:>5,.0f} [simulated]")

    pham_vi = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    runs_ok = runs[runs['status'].eq('ok') & runs['request_id'].isin(pham_vi['request_id'])]
    ca_xem_lai = runs_ok['request_id'].nunique()
    ca_lam_lai = pham_vi['ket_qua'].eq('lam_lai').sum()
    so_phut_lam_lai = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    kq = mo_hinh(runs, pham_vi)
    print(f'\nB4 · Xem lại 100%: {ca_xem_lai} ca xem lại, {ca_lam_lai} ca làm lại')
    for phut_lam_lai in (9, round(so_phut_lam_lai, 1)):
        tong = kq['token'] + kq['tool'] + LUONG_PHUT * (ca_xem_lai * 5 + ca_lam_lai * phut_lam_lai)
        cps = tong / kq['thanh_cong']
        print(f'{phut_lam_lai:g} phút làm lại: {cps:,.0f} đ/ca | {cps / BASELINE:.2f}× [simulated]')


def in_cp4():
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lab 13 · Chi phí, độ nhạy và cỡ mẫu pilot')
    parser.add_argument('--checkpoint', choices=('1', '2', '4'), help='Chỉ in bảng của checkpoint đã chọn')
    args = parser.parse_args()

    kiem_tra_dap_an_biet_truoc()
    if args.checkpoint != '4':
        runs = pd.read_csv('logix_runs.csv')
        reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
        ket_qua = mo_hinh(runs, reqs)
        if args.checkpoint in (None, '1'):
            in_cp1(runs, reqs, ket_qua)
        if args.checkpoint in (None, '2'):
            in_cp2(runs, reqs, ket_qua)
    if args.checkpoint in (None, '4'):
        in_cp4()
