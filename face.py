# sync_do_object_recognition
# YanAPI.sync_do_object_recognition()

# Begin object recognition and return when recognition is complete
# Return type dict

# Return instructions

# {
#     code: integer Return code：0 is normal
#     type:string Message type that returns only one type of data at a time.
#     data:
#         {
#             recognition:
#                     {
#                         name:string Identified objects
#                     }
#         }
#     timestamp:integer timestamp，Unix Standard time
#     status: string state
#     msg: string Prompt information
# }


# YanAPI.sync_do_object_recognition()


# Thư viện ngoài


# https://pypi.org/project/face-recognition/



def compare_face_by_name(name):
    result = False
    try:
        res = YanAPI.sync_do_face_recognition('recognition')
        __validation_response(res)
        if res is not None:
            recognition = res['data']['recognition']
            if recognition:
                result_name = recognition["name"]
                if result_name and result_name != 'none':
                    if result_name and result_name == name:
                        return True
    except:
        print('bad program')
    return result


compare_face_by_name('demo')
