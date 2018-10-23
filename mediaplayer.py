'''ffpyplayer를 이용한 비디오 플레이어'''
# from ffpyplayer.player import MediaPlayer
# import time

# # filename = './image/01_Command_Stream.ts'
# filename = './image/SampleVideo_1280x720_1mb.mp4'
# player = MediaPlayer(filename)
# val=''
# while val != 'eof':
#     frame, val = player.get_frame()
#     if val != 'eof' and frame is not None:
#         img, t = frame

from ffpyplayer.player import MediaPlayer
import time

player = MediaPlayer('./image/01_Command_Stream.ts')
while 1:
    player.get_frame()
    # if val == 'eof':
    #     break
    # elif frame is None:
    #     time.sleep(0.01)
    # else:
    #     img, t = frame
    #     print(val, t, img.get_pixel_format(), img.get_buffer_size())
    #     time.sleep(val)