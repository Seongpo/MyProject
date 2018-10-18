'''PSNR을 계산'''
import math
import numpy
import cv2

ORIGINAL = cv2.imread('image/DNR_GTc.bmp', cv2.IMREAD_COLOR)
CONTRAST = cv2.imread('image/DNR_ON.bmp', cv2.IMREAD_COLOR)

def psnr(img1, img2):
    '''psnr 계산'''
    mse = numpy.mean((img1-img2)**2)
    if mse == 0:
        return 100
    pixel_max = 255.0
    return 20*math.log10(pixel_max/math.sqrt(mse))

print(psnr(ORIGINAL, CONTRAST))
