import cv2
import numpy as np

def image_copy():
    img_file ='image/galaxy.jpg'
    img=cv2.imread(img_file, cv2.IMREAD_COLOR)
    
    cv2.imshow('title',img)

    key=cv2.waitKey(0) & 0xFF
    if key ==27:
        cv2.destroyAllWindows()
        return
    elif key==ord('c'):
        cv2.imwrite('image/galaxy2.jpg', img)
        cv2.destroyAllWindows()
        return
if __name__=='__main__':
    image_copy()