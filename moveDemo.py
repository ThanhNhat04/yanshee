#!/usr/bin/python
# -*- coding: utf-8 -*-
import YanAPI
import socket
import re

HOST = '192.168.10.39'
PORT = 8888

YanAPI.yan_api_init(HOST)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

# ------wait connect
print(HOST, PORT)
print('...waiting for Yanshee message..')

# ---function reset action
def reset_robot():
    YanAPI.sync_play_motion("reset")
while True:
    data, address = s.recvfrom(1024)
    temp = data.decode('utf-8')

    # Duyệt từ khóa
    keywords = ["forward", "backward", "left", "right", "dance", "di", "lui", "trai", "phai","nhay"]
    found_keyword = None
    for keyword in keywords:
        if keyword in temp:
            found_keyword = keyword
            break

    # Tìm và lọc số từ đoạn văn bản
    numbers = re.findall(r'\d+', temp)
    value = None
    if numbers:
        value = int(numbers[0])  # Lấy số đầu tiên trong danh sách

    # So sánh từ khóa và số với các điều kiện
    if found_keyword is not None:
        if found_keyword == "forward" or found_keyword == "di" :
            if value is not None:
                YanAPI.sync_do_tts("Move forward {} steps".format(value))
                YanAPI.sync_play_motion("walk", "forward", "normal", value)
                reset_robot()
            else:
                YanAPI.sync_do_tts("Move forward")
                YanAPI.sync_play_motion("walk", "forward", "normal", 1)
                reset_robot()
        elif found_keyword == "backward" or found_keyword == "lui":
            if value is not None:
                YanAPI.sync_do_tts("Move backward {} steps".format(value))
                YanAPI.sync_play_motion("walk", "backward", "normal", value)
                reset_robot()
            else:
                YanAPI.sync_do_tts("Move backward")
                YanAPI.sync_play_motion("walk", "backward", "normal", 1)
                reset_robot()
        elif found_keyword == "left" or found_keyword == "trai":
            if value is not None:
                YanAPI.sync_do_tts("Go left {} steps".format(value))
                YanAPI.sync_play_motion("walk", "left", "normal", value)
                reset_robot()
            else:
                YanAPI.sync_do_tts("Go left")
                YanAPI.sync_play_motion("walk", "left", "normal", 1)
                reset_robot()
        elif found_keyword == "right" or found_keyword == "phai":
            if value is not None:
                YanAPI.sync_do_tts("Go right {} steps".format(value))
                YanAPI.sync_play_motion("walk", "right", "normal", value)
                reset_robot()
            else:
                YanAPI.sync_do_tts("Go right")
                YanAPI.sync_play_motion("walk", "right", "normal", 1)
                reset_robot()
        elif found_keyword == "dance" or found_keyword == "nhay":
            if value is not None:
                YanAPI.sync_do_tts("Let's dance")
                YanAPI.start_play_motion("raise", "left", "normal", value)
                YanAPI.sync_play_motion("raise", "right", "normal", value)
                reset_robot()
            else:
                YanAPI.sync_do_tts("Let's dance")
                YanAPI.start_play_motion("raise", "left", "normal", 1)
                YanAPI.sync_play_motion("raise", "right", "normal", 1)
                reset_robot()
    else:
        YanAPI.sync_do_tts("I do not understand{}".format(temp))

s.close()
