#!/usr/bin/python
# -*- coding: utf-8 -*-
import YanAPI

arrLocal = ['r','l','m']
arrColor = ['red','blue','green']
# Màu sắc để so sánh
colors = ['green', 'blue', 'red']
Locals = ['right', 'left', 'mid']

# Funcion xử lý
# Hàm xử lý màu sắc
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

# List Funcion







# Logic chương trình
YanAPI.yan_api_init("")

while True:
    for color in colors:
        color_result = camera_detect_color(color)
        if color == 'red' and color_result:
            print("red")
        elif color == 'green' and color_result:
            print("green")
        elif color == 'blue' and color_result:
            print("blue")

# while True:
#     for color in colors:
#         qr_result = sync_do_QR_code_recognition()


# YanAPI.sync_play_motion("walk", "forward", "normal", 1)
# reset_robot()


# YanAPI.exit_motion_gait()

# print("Get item {} and put in the box {}")
