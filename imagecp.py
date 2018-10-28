import cv2
import numpy as np

def copy_image(filename):
    image=filename.split('/')[-1].split('.')[-2] #/로 split한 리스트의 마지막 element를 다시 . 으로 split 한 마직막에서 2번째
    source_img=cv2.imread(filename, -1)
    cv2.imshow(filename, source_img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27: #esc 키를 입력하면
        cv2.destroyAllWindows()
    elif k == ord('s'): #이미지를 Save 하기 위해 's' 입력을 대기한다.
        cv2.imwrite('./image/'+image+'_copied.jpg', source_img)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    copy_image('./image/galaxy.jpg')