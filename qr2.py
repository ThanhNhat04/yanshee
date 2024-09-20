import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Khởi tạo camera
cap = cv2.VideoCapture(0)

# Biến để theo dõi dữ liệu trước đó
previous_data = None

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    
    # Kiểm tra nếu khung hình được đọc thành công
    if not ret:
        print("Không thể đọc khung hình từ camera")
        break

    # Giải mã mã vạch
    decoded_objects = decode(frame)

    # Kiểm tra có mã vạch nào được phát hiện hay không
    if decoded_objects:
        # Lấy dữ liệu từ mã vạch đầu tiên
        current_data = decoded_objects[0].data.decode('utf-8')

        # So sánh với dữ liệu trước đó
        if current_data != previous_data:
            print(current_data)  # In ra dữ liệu mới
            previous_data = current_data  # Cập nhật dữ liệu trước đó

    # Hiển thị khung hình
    cv2.imshow('Camera', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()