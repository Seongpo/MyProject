'''Video 저장'''
import numpy as np
import cv2

def save_Video(filename):
    cap = cv2.VideoCapture(filename)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #아래 라인의 영상 사이즈 적용하는 것이 중요.(int(cap.get(3)), int(cap.get(4)))
    video_width = int(cap.get(3))
    video_height = int(cap.get(4))

    out = cv2.VideoWriter('./image/output3.avi', fourcc, 20.0, (video_width, video_height))
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)

            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    save_Video('./image/01_Command_Stream.ts')