# Đã sửa các lỗi cú pháp và ngữ nghĩa để chương trình chạy được ổn định
ma_may = input("Nhập mã máy: ")
# Lỗi 1 sửa đổi: Phải ép kiểu sang float/int ngay để tính toán ở dưới, không để str
cong_suat_w = float(input("Nhập công suất W: ")) 
so_phut = int(input("Nhập số phút: "))

# Lỗi 2 sửa đổi: Phép tính toán trước đó bị lỗi TypeError do nhân chuỗi (str) với int
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
# Lỗi 3 & 4 sửa đổi: Gọi sai tên biến (dien_nang đổi thành dien_nang_kwh) và thiếu dấu đóng ngoặc ")" ở cuối hàm print
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# 23. Comment mô tả các lỗi đã phát hiện:
# - Lỗi 'TypeError': Do cong_suat_w nhận vào từ input() là kiểu str, không thể thực hiện phép toán số học (*, /). Biện pháp: Ép kiểu sang float.
# - Lỗi 'NameError': Sử dụng sai tên biến 'dien_nang' trong khi biến định nghĩa là 'dien_nang_kwh'.
# - Lỗi 'SyntaxError': Thiếu dấu đóng ngoặc đơn ")" ở cuối câu lệnh print cuối cùng.
