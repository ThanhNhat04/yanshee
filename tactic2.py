#!/usr/bin/python
# -*- coding: utf-8 -*-
import YanAPI
import sys
import os
import time 

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
            
def check_color_and_qr():
    colors = ["red", "green", "cyan"]
    key_qr = ["l", "m", "r"]
    
    for color in colors:# Kiểm tra màu sắc
        print("runc")
        if camera_detect_color(color):
            detected_color = color
            print(detected_color)
            break
    else:
        detected_color = None
        
    for qr in key_qr: #Kiểm tra mã QR
        print("qr")
        if camera_detect_qr_code(qr):
            detected_qr = qr
            print(detected_qr)
            break
    else:
        detected_qr = None
        
    if detected_color and detected_qr:
        print("Lấy vật phẩm 1 màu {} và đặt vào khung hộp bên ở {}.".format(detected_color, detected_qr))
    elif detected_color:
        print("Lấy vật phẩm 1 màu {}.".format(detected_color))
    elif detected_qr:
        print("Đã phát hiện mã QR: {}.".format(detected_qr))
    else:
        print("Không phát hiện màu sắc hoặc mã QR.")

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


# Xoay người
#put_motions("turn around", "right", "normal", 1)

# Di chuyển chữ U
def movement_u():
    put_motions("walk", "forward", "fast", 2)
    put_motions("turn around", "left", "normal", 1)
    put_motions("walk", "forward", "fast", 2)
    put_motions("turn around", "left", "normal", 1)
    put_motions("walk", "forward", "fast", 2)


# Di chuyển chữ L
def movement_L():
    put_motions("walk", "forward", "fast", 2)
    put_motions("turn around", "left", "normal", 1)
    put_motions("walk", "forward", "fast", 2)


# Di chuyển sang ngang
    # put_motions("walk", "left", "fast", 2)
    # put_motions("walk", "right", "fast", 2)

# Di chuyển lùi


# -----------------Logic chương trình---------------------#

YanAPI.yan_api_init("10.0.9.10") #Nhớ đổi ip
print("Yanshee ready running")

# put_motions("walk", "forward", "normal", 2)

# # Cầu thang (lưu ý thay đổi tên action)
# start_play_motion("T1", "", "normal", 1, version="v1")
# start_play_motion("T2", "", "normal", 1, version="v1")
# check_gyro_status()
# start_play_motion("T3", "", "normal", 1, version="v1")
# start_play_motion("T4", "", "normal", 1, version="v1")


# put_motions("walk", "forward", "normal", 2)

# # Tiến tới chướng ngoại vật thứ 2 và qua thanh chắn
# start_play_motion("rc", "", "normal", 1, version="v1")



#----------------Tiến vào khu vực 2----------------#


# Nhiệm vụ gắp thả bóng 1

put_motions("walk", "forward", "very slow", 5)
put_motions("turn around", "left", "very slow", 2)
put_motions("walk", "forward", "very slow", 3)
start_play_motion("gapB", "", "normal", 1, version="v1")
put_motions("walk", "backward", "very slow", 6)


# Nhiệm vụ gắp thả bóng 2






# #------ Khởi động lại yanshee--------
reset_robot()