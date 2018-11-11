'''Bitwise Operation 
'''

import cv2
import numpy as np

#Load Image

img1 = cv2.imread('image/galaxy.jpg', 1)
img2 = cv2.imread('image/opencv.png', 1)

# 로고를 왼쪽위로 두려고, ROI를 만든다. 
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

#로고 마스크를 만들고, 반전 마스크도 만든다. 
#컬러를 변화(cv2.cvtColor())하는데, BGR에서 Gray로(cv2.COLOR_BGR2GRAY)
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) 

# cv2.threshold(대상영상, 임계치, 픽셀최대값, 출력 모양)
# img2gray 영상에서 200 보다 큰값은 255, 작은 값은 0 가지는 바인너리 영상을 INV 한다. 
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

#ROI의 로고 검은색 부분을 mask와 ROI를 AND 하여 없앰
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

#로고영상에서 로고만 뽑아냄
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

#로고를 ROI에 놓고 주영상을 변경
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

# cv2.imshow('img2gray', img2gray)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
