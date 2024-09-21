def check_gyro_status():
    response = YanAPI.get_sensors_gyro()
    
    if response['code'] != 0:
        print("Error fetching sensor data.")
        return
    
    gyro_data = response['data']['gyro'][0]
    
    # Lấy giá trị góc Euler x
    euler_x = gyro_data['euler-x']
    
    # Kiểm tra trạng thái
    if euler_x >= 45 and euler_x < 135:
        print("Đứng yên")
    elif euler_x < 45 and euler_x > -45:
        print("Té về trước")
        start_play_motion("GetupFront", "", "slow", 1, version="v1")
    elif euler_x < -45 or euler_x > 45:
        print("Té về sau")
        start_play_motion("GetupRear", "", "normal", 1, version="v1")
    else:
        print("Trạng thái không xác định")

        
# Gọi hàm để kiểm tra
check_gyro_status()







# Check hướng

def put_motions(name, direction="", speed="normal", repeat=1):
    try:
        YanAPI.sync_play_motion(name, direction, speed, repeat)
    except:
        print('bad program')

def check_gyro_status():
    # Ngưỡng lệch hợp lý dựa trên ba bộ dữ liệu đã cho
    thresholds = {
        'euler-y': (-0.1087493896484375, 0.340545654296875),  # Ngưỡng cho euler-y
    }

    response = YanAPI.get_sensors_gyro()
    
    if response['code'] != 0:
        print("Error fetching sensor data.")
        return
    
    gyro_data = response['data']['gyro'][0]
    
    # Lấy giá trị euler-y
    euler_y = gyro_data['euler-y']
    
    # Kiểm tra lệch
    if euler_y < thresholds['euler-y'][0]:
        print("Lệch qua phải: {:.6f}".format(euler_y))  # Lệch qua trái
        put_motions("turn around", "left", "slow", 1)
    elif euler_y > thresholds['euler-y'][1]:
        print("Lệch qua trái: {:.6f}".format(euler_y))  # Lệch qua phải
        put_motions("turn around", "right", "slow", 1)
    else:
        print("Ổn định: {:.6f}".format(euler_y))
        
        


# Gọi hàm để kiểm tra
check_gyro_status()

# Hàm xử lý với con quay hồi chuyển
# start_play_motion("GetupFront", "", "normal", 1, version="v1")
# start_play_motion("GetupRear", "", "normal", 1, version="v1")
# start_play_motion("Base_GetupF", "", "normal", 1, version="v1")
# start_play_motion("Base_GetupB", "", "normal", 1, version="v1")
# start_play_motion("Stop", "", "normal", 1, version="v1")
# start_play_motion("Base_GetupB", "", "normal", 1, version="v1")
# start_play_motion("calibration", "", "normal", 1, version="v1")
# start_play_motion("Shutdown", "", "normal", 1, version="v1")
# start_play_motion("Reset", "", "normal", 1, version="v1")
# start_play_motion("H_RBox", "", "normal", 1, version="v1")
















#  ver 4
# import time

# def check_gyro_status():
#     # Ngưỡng lệch hợp lý dựa trên ba bộ dữ liệu đã cho
#     thresholds = {
#         'euler-y': (-0.1087493896484375, 0.340545654296875),  # Ngưỡng cho euler-y
#     }

#     while True:
#         response = YanAPI.get_sensors_gyro()
        
#         if response['code'] != 0:
#             print("Error fetching sensor data.")
#             return
        
#         gyro_data = response['data']['gyro'][0]
        
#         # Lấy giá trị euler-y
#         euler_y = gyro_data['euler-y']
        
#         # Kiểm tra lệch
#         if euler_y < thresholds['euler-y'][0]:
#             print("Lệch qua phải: {:.6f}".format(euler_y))  # Lệch qua trái
#             put_motions("turn around", "left", "slow", 1)
#         elif euler_y > thresholds['euler-y'][1]:
#             print("Lệch qua trái: {:.6f}".format(euler_y))  # Lệch qua phải
#             put_motions("turn around", "right", "slow", 1)
#         else:
#             print("Ổn định: {:.6f}".format(euler_y))
# #             break  # Ngắt vòng lặp khi ổn định

# #         time.sleep(1)  # Dừng 1 giây trước khi kiểm tra lại

# # Gọi hàm để kiểm tra
# check_gyro_status()
