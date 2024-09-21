import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)


cv2.namedWindow('Color Detection')


cv2.createTrackbar('Lower_H', 'Color Detection', 0, 179, nothing)
cv2.createTrackbar('Lower_S', 'Color Detection', 108, 255, nothing)
cv2.createTrackbar('Lower_V', 'Color Detection', 143, 255, nothing)
cv2.createTrackbar('Upper_H', 'Color Detection', 179, 179, nothing)
cv2.createTrackbar('Upper_S', 'Color Detection', 255, 255, nothing)
cv2.createTrackbar('Upper_V', 'Color Detection', 255, 255, nothing)

while True:
   
    ret, frame = cap.read()
    
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos('Lower_H', 'Color Detection')
    lower_s = cv2.getTrackbarPos('Lower_S', 'Color Detection')
    lower_v = cv2.getTrackbarPos('Lower_V', 'Color Detection')
    upper_h = cv2.getTrackbarPos('Upper_H', 'Color Detection')
    upper_s = cv2.getTrackbarPos('Upper_S', 'Color Detection')
    upper_v = cv2.getTrackbarPos('Upper_V', 'Color Detection')
    
    # Ngưỡng màu đỏ
    lower_red = np.array([lower_h, lower_s, lower_v])
    upper_red = np.array([upper_h, upper_s, upper_v])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    

    res = cv2.bitwise_and(frame, frame, mask=mask)
    

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Color Detection', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
