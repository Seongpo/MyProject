'''동영상 플레이'''
import numpy as np
import cv2

def play_video(filename):
    cap = cv2.VideoCapture(filename)
    cap.set(3,3840)
    cap.set(4,2160)
    print(cap.get(1), cap.get(2), cap.get(3), cap.get(4))

    cnt=1
    while(cap.isOpened()):
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if cnt<10 :
            cv2.imwrite('./image/comart'+str(cnt)+'.png', frame)
            cnt+=1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    devicename = 0
    # devicename = './image/SampleVideo_1280x720_1mb.mp4'
    play_video(devicename)