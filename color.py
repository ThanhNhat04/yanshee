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