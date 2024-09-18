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
