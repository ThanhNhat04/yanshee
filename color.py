#!/usr/bin/python
# -*- coding: utf-8 -*-
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