# color req 
# {
#     code: integer Return code：0 is normal
#     type:string Message type that returns only one type of data at a time.
#     data:
#         {
#             color:
#                 [
#                     {
#                         name:string The recognized color
#                     }
#                 ]
#         }
#     timestamp:integer timestamp，Unix Standard time
#     status: string state
#     msg: string Prompt information
# }

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Code 1
import YanAPI

job1= "red"
job2 = "blue"
job3 = "green"

local1= "l"
local2 = "r"
local3 = "m"


arrlocal = [ local1 , local2 , local3]

arrjob = [ job1 , job2 , job3]



print("Get item {} and put in the box {}")



def camera_detect_color(color):
    detect_color = color.lower()
    flag = False
    try:
        res = YanAPI.sync_do_color_recognition()
        
        for item in res['data']['color']:
            if item['name'] == detect_color:
                flag = True
                break
    except:
        flag = False
    return flag

colors = ['green', 'cyan', 'yellow', 'red']


while True:
    for color in colors:
        result = camera_detect_color(color)
        if color == 'red' and result:
            print("red")
        elif color == 'green' and result:
            print("green")
        elif color == 'cyan' :
            print("cyan")


# Code 2

import YanAPI
import sys
import os

YanAPI.yan_api_init("192.168.1.105")

def __validation_response(res=None):
    if res:
        if res['code'] == 7 or res['code'] == 20001:
            sys.stdout.write("\r")
            sys.stdout.write("message:CAMERA_BUSY")
            sys.stdout.flush()
            os._exit(0)
 
 
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
 

while True:
    if (camera_detect_color("red")):
        print("red")
    elif (camera_detect_color("green")):     
        print("green")
    elif (camera_detect_color("cyan")):
        print("cyan")
        



# 3
import YanAPI
import sys
import os


isCanGaitControl = False
is_need_reset_gait_control = False
is_on_stop = False

def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()

def __validation_response(res=None):
    if res:
        if res['code'] == 7 or res['code'] == 20001:
            sys.stdout.write("\r")
            sys.stdout.write("message:CAMERA_BUSY")
            sys.stdout.flush()
            os._exit(0)


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

print("run")

YanAPI.yan_api_init("192.168.1.106") #Nhớ đổi ip

while True:
    if (camera_detect_color("red")):
        print("red")   
    elif (camera_detect_color("green")):
        print("green")
    elif (camera_detect_color("cyan")):
        print("cyan")
    else:
        print("err")




colors = ["red", "green", "cyan"]

while True:
    for color in colors:
        if camera_detect_color(color):
            print(color)
            break  


if (camera_detect_color("red")):
    print("red")
elif (camera_detect_color("green")):     
    print("green")
elif (camera_detect_color("cyan")):
    print("cyan")


def check_color():
    colors = ["red", "green", "cyan"]
    for color in colors:
        if camera_detect_color(color):
            print(color)
            break 





import YanAPI
import sys
import os
import time

isCanGaitControl = False
is_need_reset_gait_control = False
is_on_stop = False


YanAPI.yan_api_init("10.0.1.193")

def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()

def __validation_response(res=None):
    if res:
        if res['code'] == 7 or res['code'] == 20001:
            sys.stdout.write("\r")
            sys.stdout.write("message:CAMERA_BUSY")
            sys.stdout.flush()
            os._exit(0)


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


def check_color_and_qr():
    colors = ["red", "green", "cyan"]
    key_qr = ["l", "m", "r"]
    
    for color in colors:
        print("runc")
        if camera_detect_color(color):
            detected_color = color
            break
    else:
        detected_color = None

    for qr in key_qr:
        print("qr")
        if camera_detect_qr_code(qr):
            detected_qr = qr
            break
    else:
        detected_qr = None

    # In kết quả
    if detected_color and detected_qr:
        print("Lấy vật phẩm 1 màu {} và đặt vào khung hộp bên ở {}.".format(detected_color, detected_qr))
    elif detected_color:
        print("Lấy vật phẩm 1 màu {}.".format(detected_color))
    elif detected_qr:
        print("Đã phát hiện mã QR: {}.".format(detected_qr))
    else:
        print("Không phát hiện màu sắc hoặc mã QR.")

        
        
        
        
check_color_and_qr()        

# def check_color(): # Check color
#     colors = ["red", "green", "cyan"]
#     for color in colors:
#         print("run")
#         if camera_detect_color(color):
#             print(color)
#             break 

# def check_qr_code(): # Check qr
#     key_qr = ["l", "m", "r"]
#     for qr in key_qr:
#         if camera_detect_qr_code(qr):
#             print(qr)
#             break

# YanAPI.yan_api_init("10.0.1.193")
 
# check_color()
# check_color()
# check_qr_code()


