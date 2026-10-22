cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tính điện năng tiêu thụ và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In giá trị và kiểu dữ liệu
print("Điện năng (kWh):", dien_nang_kwh, "-", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "-", type(chi_phi))

# 16. Thay so_phut bằng 60 và tính lại để so sánh
# Nhận xét: Khi thời gian giảm từ 90 xuống 60 phút, điện năng và chi phí giảm đi 1.5 lần.
