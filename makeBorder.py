'''Image border'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [0, 0, 255]

img = cv2.imread('./image/opencv.png')
img1 = img[:, :, ::-1]

# 사진 테두리를 그릴때 -> copyMakeBorder(sorce, top, bottom, left, right, bordertype)
replicate = cv2.copyMakeBorder(img1, 30, 30, 30, 30, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 30, 30, 30, 30, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 30, 30, 30, 30, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 30, 30, 30, 30, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 30, 30, 30, 30, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('1. ORIGINAL'),plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('2. REPLICATE'),plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('3. REFLECT'),plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('4. REFLECT_101'),plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('5. WRAP'),plt.xticks([]),plt.yticks([])
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('6. CONSTANT'),plt.xticks([]),plt.yticks([])


plt.show()
