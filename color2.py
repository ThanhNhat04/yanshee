import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Khởi tạo camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    rs = decode(frame)
    print(rs)
    # Chuyển đổi khung hình sang không gian màu HSV
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Định nghĩa các khoảng màu
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])
    
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])
    
    # Tạo mặt nạ cho các màu
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Kết hợp các mặt nạ
    mask = cv2.bitwise_or(mask_red, mask_green)
    mask = cv2.bitwise_or(mask, mask_blue)
    
    # Áp dụng mặt nạ lên khung hình gốc
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Kiểm tra xem màu nào được phát hiện
    if np.sum(mask_red) > 1000:  # Thay đổi ngưỡng nếu cần
        color_name = "Red"
    elif np.sum(mask_green) > 1000:
        color_name = "Green"
    elif np.sum(mask_blue) > 1000:
        color_name = "Blue"
    else:
        color_name = "No Color Detected"
    
    # In tên màu ra màn hình
#     print(color_name)
    
#     # Hiển thị kết quả
#     cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
#     cv2.imshow('Result', result)
    
    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()