tong_phut = 135
cong_suat_w = 250

# 9. Tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"Thời gian: {so_gio} giờ và {so_phut_con_lai} phút")

# 10. Biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Sử dụng lâu (>60 phút):", su_dung_lau)

# 11. Biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# 12. Kiểm chứng hai biểu thức (Dự đoán: 160 và 360)
print("Kết quả 100 + 20 * 3 =", 100 + 20 * 3)
print("Kết quả (100 + 20) * 3 =", (100 + 20) * 3)
