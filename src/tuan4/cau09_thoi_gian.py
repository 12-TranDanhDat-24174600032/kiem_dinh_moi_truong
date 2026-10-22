from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Bổ sung tính toán khoảng thời gian
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# 25. Giải thích sự khác nhau:
# - datetime: Đối tượng lưu trữ đầy đủ thông tin ngày, tháng, năm, giờ, phút, giây trong hệ thống.
# - str: Chuỗi văn bản thuần túy đại diện cho thời gian sau khi được định dạng để con người dễ đọc.
# - timedelta: Đối tượng thể hiện khoảng thời gian chênh lệch (độ dài thời gian) giữa hai mốc datetime.
