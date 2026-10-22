# 5 & 6. Tạo biến theo quy tắc snake_case và chọn kiểu dữ liệu phù hợp
ma_phien = "LAB026"          # str
ma_may = "PC12"              # str
cong_suat_w = 250.0          # float
thoi_gian_phut = 90          # int
trang_thai_hoat_dong = True  # bool
ghi_chu = None               # NoneType

# 7. In giá trị và kiểm tra kiểu dữ liệu
print("Mã phiên:", ma_phien, "-", type(ma_phien))
print("Mã máy:", ma_may, "-", type(ma_may))
print("Công suất (W):", cong_suat_w, "-", type(cong_suat_w))
print("Thời gian (phút):", thoi_gian_phut, "-", type(thoi_gian_phut))
print("Trạng thái:", trang_thai_hoat_dong, "-", type(trang_thai_hoat_dong))
print("Ghi chú:", ghi_chu, "-", type(ghi_chu))

# 8. Gán lại giá trị thời gian và in ra
thoi_gian_phut = 120
print("Thời gian sau khi cập nhật (phút):", thoi_gian_phut)
