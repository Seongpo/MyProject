import numpy
import math
import cv2

original = cv2.imread('image/LSC_OFF.bmp', cv2.IMREAD_COLOR)
contrast = cv2.imread('image/LSC_ON.bmp', cv2.IMREAD_COLOR)
def lsc(imgs, imgc):
    img1=gray(imgs)
    img2=gray(imgc)
    sourcemean=numpy.mean(img1)    
    print(sourcemean)
    mse=numpy.mean((img2-sourcemean)**2)
    #for i in range(len(img2)):
    #    print(img2[i])
    print('MSE = ', math.sqrt(mse))
    return

def gray(image_color):
    image_gray=[]
    for i in range(len(image_color)):
        for j in range(len(image_color[i])):
            image_gray.append(0.299*image_color[i][j][0]+0.5870*image_color[i][j][1]+0.114*image_color[i][j][2])
    #print(len(image_gray))
    return image_gray

lsc(original, contrast)