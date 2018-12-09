'''Color Space convert 방법을 연습한다. 
'''

import numpy as np
import cv2

def play_video(filename):
    cap = cv2.VideoCapture(filename)

    cnt=1
    while(cap.isOpened()):
        ret, frame = cap.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        # cv2.imwrite('./image/test_'+str(cnt)+'.png', frame)
        cnt+=1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    play_video('./image/SampleVideo_1280x720_1mb.mp4')