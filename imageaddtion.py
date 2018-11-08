'''
Image addition 
    res = image1 + image2
Image Blending
    g(x) = (1-a)f0(x)+af1(x)
'''
import numpy as np
import cv2

img1 = cv2.imread('image/galaxy.png', 1)
img2 = cv2.imread('image/opencv.png', 1)
# addimg = img1 + img2
addimg = cv2.add(img1, img2)
dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('image blending', dst)
cv2.imshow('image addition', addimg)
cv2.waitKey(0)
cv2.destroyWindows()
