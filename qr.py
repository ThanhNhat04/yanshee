# function    sync_do_QR_code_recognition
# YanAPI.sync_do_QR_code_recognition(timeout: int)
# Start QR code recognition and return after recognition

# parameter
# timeout (int) - maximum waiting time (unit: second s). ≤0 indicates that it stops until the identification is successful
# return type dict

# return instructions
# {
#     code: integer Return code：0 is normal
#     content: string Identified content
#     status: string State
#     msg: string Prompt information
# }



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
 

 

# Hàm lấy dữ liệu qr từ camera
def sync_do_QR_code_recognition(qr):
    detect_qr = qr.lower()
    flag = False
    try:
        res = YanAPI.sync_do_QR_code_recognition()   
        __validation_response(res)     
        for item in res['data']['content']:
            if item['content'] == detect_qr:
                flag = True
                break
    except:
        flag = False
    return flag


# Tryền dữ liệu từ mảng muons kiểm tra vào trong hàm
result = sync_do_QR_code_recognition()



def get_object_by_ai():
    result = "none"
    try:
        res = YanAPI.sync_do_object_recognition()
        __validation_response(res)
        if res is not None:
            result = res['data']['recognition']['name']
    except:
        result = "none"
        print('bad program')
 
    return result

get_object_by_ai() == "qr_code"

def display_qr_value():
    result = sync_do_QR_code_recognition()
    
    if result == "qr_code":
        print("Giá trị QR code: ", result)
    else:
        print("Không tìm thấy QR code.")





# Hàm 3

def camera_detect_qr_code(timeout):
    flag = False
    content = None
    try:
        res = YanAPI.sync_do_QR_code_recognition(timeout)
        __validation_response(res)
        if res['code'] == 0:
            flag = True
            content = res['content']
    except:
        flag = False
        content = None
    return flag, content



# Hàm 4

def camera_detect_qr_code(t):
    flag = False
    try:
        res = YanAPI.sync_do_QR_code_recognition(t)
        __validation_response(res)
        # for item in res['content']:
        #     if item['content'] == detect_color:
        #         flag = True
        #         break
    except:
        flag = False
    return flag


# 
result = camera_detect_qr_code()



def camera_detect_qr_code(t):
    flag = False
    try:
        res = YanAPI.sync_do_QR_code_recognition(t)
        __validation_response(res)
        # for item in res['content']:
        #     if item['content'] == detect_color:
        #         flag = True
        #         break
    except:
        flag = False
    return flag


# final qr


import YanAPI
import sys
import os

YanAPI.yan_api_init("10.0.9.10")

def __validation_response(res=None):
    if res:
        if res['code'] == 7 or res['code'] == 20001:
            sys.stdout.write("\r")
            sys.stdout.write("message:CAMERA_BUSY")
            sys.stdout.flush()
            os._exit(0)

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

def check_qr_code():
    key_qr = ["l", "m", "r"]
    for qr in key_qr:
        print("ok2")
        if camera_detect_qr_code(qr):
            print("ok")
            break

check_qr_code()


# Loại 2


def check_color():  # Check color
    colors = ["red", "green", "cyan"]
    for color in colors:
        if camera_detect_color(color):
            return color
    return None  

def check_qr_code():  # Check qr
    key_qr = ["l", "m", "r"]
    for qr in key_qr:
        if camera_detect_qr_code(qr):
            return qr
    return None  


color = check_color()

print("Lấy vật phẩm 1 màu {} và đặt vào khung hộp bên ở {}.".format(color))




def check_color_and_qr():
    colors = ["red", "green", "cyan"]
    key_qr = ["l", "m", "r"]
    
    detected_color = None
    detected_qr = None
    
    # Kiểm tra màu sắc
    for color in colors:
        if camera_detect_color(color):
            detected_color = color
            break  
    
    # Kiểm tra mã QR
    for qr in key_qr:
        if camera_detect_qr_code(qr):
            detected_qr = qr
            break 
            
    return detected_color, detected_qr

color, qr_code = check_color_and_qr()

if color and qr_code:
    print("Lấy vật phẩm 1 màu {} và đặt vào khung hộp bên ở {}.".format(color, qr_code))
elif color:
    print("Lấy vật phẩm 1 màu {}.".format(color))
elif qr_code:
    print("Đã phát hiện mã QR: {}.".format(qr_code))
else:
    print("Không phát hiện màu sắc hoặc mã QR.")




# Ver 3



def check_color_and_qr():
    colors = ["red", "green", "cyan"]
    key_qr = ["l", "m", "r"]
    
    # Kiểm tra màu sắc
    for color in colors:
        if camera_detect_color(color):
            detected_color = color
            break
    else:
        detected_color = None

    # Kiểm tra mã QR
    for qr in key_qr:
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











def check_color_and_qr():
    colors = ["red", "green", "cyan"]
    key_qr = ["l", "m", "r"]
    
#     Kiểm tra màu sắc
    for color in colors:
        print("runc")
        if camera_detect_color(color):
            detected_color = color
            print(detected_color)
            break
    else:
        detected_color = None

#     Kiểm tra mã QR
    for qr in key_qr:
        print("qr")
        if camera_detect_qr_code(qr):
            detected_qr = qr
            print(detected_qr)
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