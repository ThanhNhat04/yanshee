#!/usr/bin/python
# -*- coding: utf-8 -*-
import YanAPI
import sys
import os
import time 

isCanGaitControl = False
is_need_reset_gait_control = False
is_on_stop = False

# Mảng lưu trữ giá trị trả về data di chuyển
arrLocal = ['r','l','m']
Locals = ['right', 'left', 'mid']

# Funcion xử lý chương trình
# Reset robot
def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()

# Hàm delay
def delay(delay):
    time.sleep(delay)

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
def sync_do_QR_code_recognition(qr):
    detect_qr = qr.lower()
    flag = False
    try:
        res = YanAPI.sync_do_QR_code_recognition()        
        for item in res['data']['content']:
            if item['content'] == detect_qr:
                flag = True
                break
    except:
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




# Logic chương trình

YanAPI.yan_api_init("192.168.1.105") #Nhớ đổi ip

print("run")

while True:
    if (camera_detect_color("red")):
        print("red")
    elif (camera_detect_color("green")):     
        print("green")
    elif (camera_detect_color("cyan")):
        print("cyan")
        


# print("Get item {} and put in the box {}")

# YanAPI.sync_play_motion("walk", "forward", "normal", 1)
reset_robot()
