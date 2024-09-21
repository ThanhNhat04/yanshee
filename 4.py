#!/usr/bin/python
# -*- coding: utf-8 -*-
import YanAPI
import sys
import os
import time 
import cv2
import numpy as np

isCanGaitControl = False
is_need_reset_gait_control = False
is_on_stop = False

# Funcion xử lý chương trình
# Reset robot
def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()
    # Since Reset and exit motion are pretty much the same, so if
    # have gait we only need exit, if not, use hts reset
    if is_need_reset_gait_control:
        YanAPI.exit_motion_gait()
    else:
        YanAPI.start_play_motion(name = "Reset", repeat = 1)
    YanAPI.set_robot_led("button", "white", "reset")

# Hàm kiểm tra camera
def __validation_response(res=None):
    if res:
        if res['code'] == 7 or res['code'] == 20001:
            sys.stdout.write("\r")
            sys.stdout.write("message:CAMERA_BUSY")
            sys.stdout.flush()
            os._exit(0)

# Hàm xử lý màu sắc 
def camera_detect_color(color):
    detect_color = color.lower()
    flag = False
    try:
        res = YanAPI.sync_do_color_recognition()
        __validation_response(res)
        for item in res['data']['color']:
            if item['name'] == detect_color:
                flag = True
                break
    except:
        flag = False
    return flag

# Hàm xử lý QR
def camera_detect_qr_code(qr):
    detect_qr = qr.lower()
    flag = False
    try:
        res = YanAPI.sync_do_QR_code_recognition(4)
        print(res)
        __validation_response(res)
        for item in res['data']['contents']:
            if item == detect_qr:
                flag = True
                break
    except :
        flag = False
    return flag

# Hàm xử lý motion
def put_motions(name, direction="", speed="normal", repeat=1):
    try:
        YanAPI.sync_play_motion(name, direction, speed, repeat)
    except:
        print('bad program')
        
def start_play_motion(name: str = "reset", direction: str = "", speed: str = "normal", repeat: int = 1, timestamp: int = 0, version: str = "v2"):
    try:
        if name == '':
            return
        if version == 'v1':
            YanAPI.sync_play_motion(name, direction, speed, repeat)
        else:
            YanAPI.start_play_motion(name, direction, speed, repeat, int(time.time() * 1000), version)
    except:
        print('bad program')

def put_gait_motions(speed_v: int = 0, steps: int = 0): # Chuyển động ổn định
    try:
        YanAPI.sync_do_motion_gait(speed_v=speed_v, steps=steps, period=6-abs(speed_v))
    except:
        #result = False
        print('bad program')

# List Funcion
def delay(delay): # Hàm delay
    time.sleep(delay)

def check_color(): # Check color
    colors = ["red", "green", "cyan"]
    for color in colors:
        if camera_detect_color(color):
            print(color)
            break 

def check_qr_code(): # Check qr
    key_qr = ["l", "m", "r"]
    for qr in key_qr:
        if camera_detect_qr_code(qr):
            print(qr)
            break
            
# def check_color_and_qr():
#     colors = ["red", "green", "cyan"]
#     key_qr = ["l", "m", "r"]
    
#     for color in colors:# Kiểm tra màu sắc
#         if camera_detect_color(color):
#             detected_color = color
#             print(detected_color)
#             break
#     else:
#         detected_color = None
        
#     for qr in key_qr: #Kiểm tra mã QR
#         if camera_detect_qr_code(qr):
#             detected_qr = qr
#             print(detected_qr)
#             break
#     else:
#         detected_qr = None
        
#     if detected_color and detected_qr:
#         print("Lấy vật phẩm 1 màu {} và đặt vào khung hộp bên ở {}.".format(detected_color, detected_qr))
#     elif detected_color:
#         print("Lấy vật phẩm 1 màu {}.".format(detected_color))
#     elif detected_qr:
#         print("Đã phát hiện mã QR: {}.".format(detected_qr))
#     else:
#         print("Không phát hiện màu sắc hoặc mã QR.")

def check_color_and_qr():
    colors = ["red", "green", "cyan"]
    key_qr = ["l", "m", "r"]
    position_map = {
        "l": "trái",
        "m": "giữa",
        "r": "phải"
    }

    detected_color = None
    detected_qr = None

    for color in colors:  # Kiểm tra màu sắc
        if camera_detect_color(color):
            detected_color = color
            break
            
    for qr in key_qr:  # Kiểm tra mã QR
        if camera_detect_qr_code(qr):
            detected_qr = qr
            break

    if detected_color and detected_qr:
        position = position_map[detected_qr]
        print("Lấy vật phẩm 1 màu {} và đặt vào khung hộp bên ở {}.".format(detected_color, position))
    elif detected_color:
        print("Lấy vật phẩm 1 màu {}.".format(detected_color))
    elif detected_qr:
        position = position_map[detected_qr]
        print("Đã phát hiện mã QR: {} (tương ứng với vị trí: {}).".format(detected_qr, position))
#     else:
#         print("Không phát hiện màu sắc hoặc mã QR.")
        

# Code check cân bằng
def check_gyro_status():
    response = YanAPI.get_sensors_gyro()
    
    if response['code'] != 0:
        print("Error fetching sensor data.")
        return
    
    gyro_data = response['data']['gyro'][0]
    
    # Lấy giá trị góc Euler x
    euler_x = gyro_data['euler-x']
    
    # Kiểm tra trạng thái
    if euler_x >= 45 and euler_x < 135:
        print("Đứng yên")
    elif euler_x < 45 and euler_x > -45:
        print("Té về trước")
        start_play_motion("GetupFront", "", "slow", 1, version="v1")
    elif euler_x < -45 or euler_x > 45:
        print("Té về sau")
        start_play_motion("GetupRear", "", "normal", 1, version="v1")
    else:
        print("Trạng thái không xác định")

# Check color 2

# Tạo các danh sách để lưu màu đã nhận diện
color_red = []
color_blue = []
color_green = []

def add_to_list(color_list, color_name): # Hàm thêm màu vào danh sách và in thông báo
    if color_name not in color_list:
        color_list.append(color_name)
        print("Lấy được vật phẩm màu {}".format(color_name))

def detect_red(hsv): # Hàm nhận diện màu đỏ
    lower_red = np.array([170, 126, 50])
    upper_red = np.array([180, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    if np.any(mask_red):
        add_to_list(color_red, "đỏ")
        return True
    return False

def detect_green(hsv): # Hàm nhận diện màu xanh lá cây
    lower_green = np.array([40, 180, 55])
    upper_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    if np.any(mask_green):
        add_to_list(color_green, "xanh")
        return True
    return False

def detect_blue(hsv): # Hàm nhận diện màu xanh biển
    lower_blue = np.array([90, 150, 87])
    upper_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    if np.any(mask_blue):
        add_to_list(color_blue, "lam")
        return True
    return False

def detect_color_in_frame():
    cap = cv2.VideoCapture(0)  # Ensure the camera is initialized
    try:
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
            x, y, w, h = 100, 350, 500, 300
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 250), 2)
            cropped_frame = frame[y:y + h, x:x + w]
            hsv = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2HSV)
            if detect_red(hsv):
                break
            if detect_green(hsv):
                break
            if detect_blue(hsv):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

# Xoay người
#put_motions("turn around", "right", "normal", 1)

# Di chuyển sang ngang
    # put_motions("walk", "left", "fast", 2)
    # put_motions("walk", "right", "fast", 2)

# -----------------Logic chương trình---------------------#

YanAPI.yan_api_init("10.0.7.248") #Nhớ đổi ip
print("Yanshee ready running")

# Tiến tới cầu thang
# put_motions("walk", "forward", "normal", 2)
# put_motions("turn around", "right", "slow", 1)

# Cầu thang (lưu ý thay đổi tên action)
start_play_motion("T1", "", "normal", 1, version="v1")
start_play_motion("T2", "", "normal", 1, version="v1")
start_play_motion("T3", "", "normal", 1, version="v1")
check_gyro_status()
start_play_motion("T4", "", "normal", 1, version="v1")
check_gyro_status()


put_gait_motions(2,5)
put_motions("turn around", "right", "slow", 1)
put_motions("walk", "forward", "slow", 3)
put_motions("walk", "right", "fast", 4)

# # Tiến tới chướng ngoại vật thứ 2 và qua thanh chắn
start_play_motion("thurao", "", "normal", 1, version="v1")



#----------------Tiến vào khu vực 2----------------#

# Nhiệm vụ gắp thả bóng 1

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("turn around", "right", "slow", 1)
# put_motions("walk", "forward", "slow", 6)
# put_motions("turn around", "left", "slow", 1)
# # put_motions("walk", "forward", "very slow", 1)
# start_play_motion("gap", "", "normal", 1, version="v1")
# put_motions("walk", "backward", "very slow", 7)
# put_motions("turn around", "right", "very slow", 3)
# put_motions("walk", "forward", "very slow", 2)
# start_play_motion("tha", "", "normal", 1, version="v1")


# Nhiệm vụ gắp thả bóng 2

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("walk", "forward", "very slow", 5)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "very slow", 3)
# start_play_motion("gap", "", "normal", 1, version="v1")
# put_motions("walk", "backward", "very slow", 6)


# Chuỗi nhiệm vụ 1,2 gần
    #1
# put_motions("walk", "forward", "slow", 6)
# put_motions("turn around", "left", "slow", 1)
# put_motions("walk", "forward", "slow", 6)

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("walk", "forward", "slow", 6)

# start_play_motion("gap", "", "normal", 1, version="v1")
# put_motions("walk", "backward", "very slow", 7)

# put_motions("turn around", "right", "very slow", 3)
# put_motions("walk", "forward", "very slow", 2)
# start_play_motion("tha", "", "normal", 1, version="v1")

# put_motions("turn around", "right", "very slow", 3)
# put_motions("turn around", "right", "very slow", 2)

    #2
# put_motions("walk", "forward", "slow", 6)
# put_motions("turn around", "right", "slow", 1)

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("walk", "forward", "slow", 6)

# start_play_motion("gap", "", "normal", 1, version="v1")
# put_motions("walk", "backward", "very slow", 7)
# put_motions("turn around", "right", "very slow", 3)
# put_motions("walk", "forward", "very slow", 2)
# start_play_motion("tha", "", "normal", 1, version="v1")

    #3
# put_motions("turn around", "right", "very slow", 3)
# put_motions("turn around", "right", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)
# put_motions("turn around", "right", "very slow", 2)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)


# Chuỗi nhiệm vụ 1,2 xa
    #1
# put_motions("walk", "forward", "slow", 6)
# put_motions("turn around", "left", "slow", 1)
# put_motions("walk", "forward", "slow", 6)

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("walk", "forward", "slow", 6)

# start_play_motion("gap", "", "normal", 1, version="v1")
# put_motions("walk", "backward", "very slow", 7)

# put_motions("turn around", "right", "very slow", 3)
# put_motions("walk", "forward", "very slow", 2)
# start_play_motion("tha", "", "normal", 1, version="v1")

# put_motions("turn around", "right", "very slow", 3)
# put_motions("turn around", "right", "very slow", 2)

    #2.1 đi ngang
# put_motions("walk", "left", "fast", 2)
# put_motions("turn around", "right", "slow", 5)
# put_motions("walk", "forward", "very slow", 2)

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("walk", "forward", "slow", 6)

# start_play_motion("gap", "", "normal", 1, version="v1")
# put_motions("walk", "backward", "very slow", 7)
# put_motions("turn around", "right", "very slow", 3)
# put_motions("walk", "forward", "very slow", 2)
# start_play_motion("tha", "", "normal", 1, version="v1")

    #2.2 đi dọc
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)

# start_play_motion("ha", "", "normal", 1, version="v1")
# detect_color_in_frame()
# check_color_and_qr()

# put_motions("turn around", "left", "very slow", 2)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)

    #3
# put_motions("turn around", "right", "very slow", 3)
# put_motions("turn around", "right", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("turn around", "right", "very slow", 2)
# put_motions("walk", "forward", "very slow", 2)























# Nhiệm vụ dectect khuôn mặt
# put_motions("walk", "left", "fast", 2)


# Nhiệm vụ đi thẳng phá 
# put_motions("walk", "forward", "normal", 6)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "normal", 6)


# Nhiệm vụ về đích luôn
# put_motions("walk", "forward", "fast", 6)
# put_motions("turn around", "left", "very slow", 2)
# put_motions("walk", "forward", "fast", 6)

# #------ Khởi động lại yanshee--------
reset_robot()