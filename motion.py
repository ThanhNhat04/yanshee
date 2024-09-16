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