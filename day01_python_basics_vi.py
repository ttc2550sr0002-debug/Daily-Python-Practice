# Day 01: Python Basics & Setup Verification (Bản giải thích Tiếng Việt)
# Ngày học: Ngày 1 - Ôn tập nền tảng Python
# 1. Kiểm tra xuất dữ liệu (print)
# - Hàm print() dùng để in văn bản hoặc kết quả ra màn hình.
print("Hello, Daily Python Practice!")
# Kết quả in ra: Hello, Daily Python Practice!
# 2. Xử lý dữ liệu cơ bản & Tính toán
# [Bước A] Tạo danh sách dữ liệu mẫu (List)
# - Tạo một biến tên là `data` chứa danh sách 5 số nguyên: 10, 20, 30, 40, 50.
data = [10, 20, 30, 40, 50]
# [Bước B] Tính tổng các phần tử trong danh sách (sum)
# - Hàm sum(data) tự động cộng dồn tất cả các con số trong danh sách `data` lại.
# - Phép tính: 10 + 20 + 30 + 40 + 50 = 150.
total_sum = sum(data)
# [Bước C] Hiển thị kết quả (f-string)
# - Cú pháp f"..." giúp chèn trực tiếp giá trị của biến {total_sum} vào chuỗi thông báo.
print(f"合計値 (Tổng giá trị): {total_sum}")
# Kết quả in ra: 合計値 (Tổng giá trị): 150
# 3. Ghi chú bài học tiếp theo
# - Buổi tới: Luyện tập thao tác với mảng và ma trận bằng thư viện NumPy.
