'''Matplotlib 를 이용한 이미지 디스플레이 '''
import numpy as np
import cv2
from matplotlib import pyplot as plt

def matplot_display(filename):
    img = cv2.imread(filename, 1)
    #openCV에서 컬러영상을 BGR로 읽어들이기 때문에 matplot에서는 RGB로 변경해야 정상적으로 Display 됨
    #img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 방법 1
    img2 = img[:, :, ::-1]  #방법 2 : 컬러 순서 뒤집기

    plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    matplot_display('./image/galaxy.jpg')