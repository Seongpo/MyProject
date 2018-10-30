'''나중에 다시 보기로 하고 남겨둠'''

import cv2
import numpy as np

class VideoCaptureYUV:
    def __init__(self, filename, size):
        self.height, self.width = size
        self.frame_len = self.width * self.height * 3 / 2
        self.f = open(filename, 'rb')
        self.shape = (int(self.height*1.5), self.width)

    def read_raw(self):
        try:
            raw = self.f.read(int(self.frame_len))
            yuv = np.frombuffer(raw, dtype=np.uint8)
            yuv = yuv.reshape(self.shape)
        except Exception as e:
            print(str(e))
            return False, None
        return True, yuv

    def read(self):
        ret, yuv = self.read_raw()
        if not ret:
            return ret, yuv
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV420P2RGB)
        
        return ret, bgr


if __name__ == "__main__":
    filename = "./image/galaxy.yuv"
    size = (640, 480)
    cap = VideoCaptureYUV(filename, size)
 
    while 1:
        ret, frame = cap.read()
        if ret:
            print(np.shape(frame))
            cv2.imshow("frame", frame)
            cv2.waitKey(0)
        else:
            break