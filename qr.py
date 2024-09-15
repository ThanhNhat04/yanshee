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



# Hàm lấy dữ liệu qr từ camera
def sync_do_QR_code_recognition(qr):
    detect_qr = qr.lower()
    # flag = False
    try:
        res = YanAPI.sync_do_QR_code_recognition()        
        for item in res['data']['content']:
            if item['content'] == detect_qr:
                # flag = True
                break
    except:
        # flag = False
        return " "
    # return flag
    return " "


# Tryền dữ liệu từ mảng muons kiểm tra vào trong hàm
result = sync_do_QR_code_recognition()