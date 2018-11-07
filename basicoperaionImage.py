'''Basic Operation'''
import cv2
import numpy as np


img=cv2.imread('./image/galaxy.jpg', 1)

centerX, centerY = img.shape[0:2]
centerX = int(centerX/2)
centerY = int(centerY/2)

part = img[centerY : centerY + 100, centerX : centerX + 100]
img[centerY -100 : centerY, centerX - 100 : centerX] = part

while(1):
    cv2.imshow('galxy', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
