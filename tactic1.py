# Yanshee xuất phát từ phía bên phải sa bàn
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





# -----------------Logic chương trình---------------------#

YanAPI.yan_api_init("192.168.1.105") #Nhớ đổi ip

print("run")

# Xuất phát từ đích
put_motions("walk", "forward", "normal", 2)

# Cầu thang (lưu ý thay đổi tên action)
    # Lên thang
start_play_motion("lenthg", "", "normal", 1, version="v1")
start_play_motion("lenthg", "", "normal", 1, version="v1")
    # Xuống thang 
start_play_motion("lenthg", "", "normal", 1, version="v1")
start_play_motion("lenthg", "", "normal", 1, version="v1")

# Tiến tới chướng ngoại vật thứ 2 và qua thanh chắn
put_motions("walk", "forward", "normal", 2)
start_play_motion("lenthg", "", "normal", 1, version="v1")





# ----------------Tiến vào khu vực 2----------------

# Nhiệm vụ gắp thả bóng 1
check_color()
check_qr_code()

put_motions("walk", "forward", "fast", 2)
start_play_motion("gapDemo", "", "normal", 1, version="v1")
put_motions("walk", "backward", "fast", 2)
start_play_motion("tha", "", "normal", 1, version="v1")


# Gắp bóng 2
check_color()
check_qr_code()

start_play_motion("lenthg", "", "normal", 1, version="v1")
start_play_motion("lenthg", "", "normal", 1, version="v1")

# # Gắp bóng 3
# check_color()
# check_qr_code()
# start_play_motion("lenthg", "", "normal", 1, version="v1")
# start_play_motion("lenthg", "", "normal", 1, version="v1")







#------ Khởi động lại yanshee--------
reset_robot()