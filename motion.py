# sync_play_motion
# YanAPI.sync_play_motion(name: str = ‘reset’, direction: str = ‘’, speed: str = ‘normal’, repeat: int = 1, version: str = ‘v1’)

# name (str) – Motion filename, excluding the hts suffix
# direction (str) - Direction
# repeat (int) - Repeat the number：1-100
# speed (str) - Speed of MOtion execution：very slow/slow/normal/fast/very fast
# timestamp (int) - timestamp, Unix Standard time
# version (str) - Action execution type. ‘v1’- HTS action/ ‘v2’- Layers action that supports the action layering. The default value is ‘v1’
    # name	direction
    # crouch/bow	（don't have to set the direction）
    # raise/stretch/come on/wave	left/right/both
    # bend/turn around	left/right
    # walk	forward/backward/left/right
    # head	forward/left/right
    # Return type bool



# stop_play_motion
# YanAPI.stop_play_motion(timestamp: int = 0, name: str = ‘’, version: str =’v1’)

# timestamp (int) - timestamp, Unix Standard time
# name (str) – Action name, not including hts /layers suffix, name=’’ means to stop all actions
# version (str) - Action execution type. ‘v1’- HTS action/ ‘v2’- Layers action that supports the action layering. The default value is ‘v1’
# Return type dict

# Return instructions

# {
#     code:integer Return code：0 is normal
#     data:
#         {
#             total_time:integer  Time required to complete the operation (unit ms)
#         }
#     msg:string Prompt information
# }






def put_motions(name, direction="", speed="normal", repeat=1):
    try:
        YanAPI.sync_play_motion(name, direction, speed, repeat)
    except:
        print('bad program')

        
 
def start_play_motion(name: str = "reset", direction: str = "", speed: str = "normal", repeat: int = 1, timestamp: int = 0, version: str = "v2"):
    try:
        if name == '':
            return
        if version == 'v1':
            YanAPI.sync_play_motion(name, direction, speed, repeat)
        else:
            YanAPI.start_play_motion(name, direction, speed, repeat, int(time.time() * 1000), version)
    except:
        print('bad program')






def reset_robot():
    global is_on_stop
    is_on_stop = True
    YanAPI.stop_voice_iat()
    YanAPI.stop_voice_tts()



    import YanAPI

YanAPI.yan_api_init("192.168.1.105")

# YanAPI.start_play_motion("tha", "", "normal", 1, version="v2")
# YanAPI.get_motion_list_value()

def put_motions(name, direction="", speed="normal", repeat=1):
    try:
        YanAPI.sync_play_motion(name, direction, speed, repeat)
    except:
        print('bad program')
        
def start_play_motion(name: str = "reset", direction: str = "", speed: str = "normal", repeat: int = 1, timestamp: int = 0, version: str = "v2"):
    try:
        if name == '':
            return
        if version == 'v1':
            YanAPI.sync_play_motion(name, direction, speed, repeat)
        else:
            YanAPI.start_play_motion(name, direction, speed, repeat, int(time.time() * 1000), version)
    except:
        print('bad program')
        
        
        
        
        
put_motions("walk", "forward", "fast", 2)
start_play_motion("gapDemo", "", "fast", 1, version="v1")
 
# moves_walk.
put_motions("walk", "forward", "fast", 2)
start_play_motion("tha", "", "fast", 1, version="v1")