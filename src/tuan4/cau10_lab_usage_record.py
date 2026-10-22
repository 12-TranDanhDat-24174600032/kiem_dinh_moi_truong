from datetime import datetime

# Nhập dữ liệu đầu vào
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút sử dụng: "))
don_gia_kwh = float(input("Nhập đơn giá điện: "))

# Tính toán các giá trị kỹ thuật (Tuyệt đối không dùng cấu trúc IF)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60
thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Xuất dữ liệu định dạng chuẩn đầu ra
print("\n" + "="*30)
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_gian_hien_tai}")
print("="*30)
