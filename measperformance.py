'''measuring performance with OpenCV'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.setUseOptimized(True)

img1 = cv2.imread('./image/galaxy.jpg', 1)
# try:
#     img1 = cv2.imread('./image/galaxy.jpg', 1)
#     # if img1 == None:
#     #     print(img1)
#     #     raise Exception('그림 파일이 없습니다.')
# except Exception as e:
#     print("error occured.", e)
#     exit()

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
img2=img1[:, :, ::-1]
plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()

e2 = cv2.getTickCount()
time = (e2 - e1)/cv2.getTickFrequency()
print(time)