'''Trackbar 함수를 windows에 묶음'''
import cv2
import numpy as np

def nothing(x):
    pass

#Create a black image, a window
img = np.zeros((512,512, 3), np.uint8)
cv2.namedWindow('image')

R = 'Red  '
G = 'Green'
B = 'Blue '

#Create trackbars for color change
#cv.CreateTrackbar(trackbarName, windowName, value:초기값, count:최대값, onChange)
cv2.createTrackbar(R, 'image', 0, 255, nothing)
cv2.createTrackbar(G, 'image', 0, 255, nothing)
cv2.createTrackbar(B, 'image', 0, 255, nothing)

# Create switch for ON/OFF functionality. createTrackbar 함수를 이용하여 스위치 만들기
switch = '0:OFF'+'\n'+'1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    #get current positions of four trackbars
    r = cv2.getTrackbarPos(R, 'image')
    g = cv2.getTrackbarPos(G, 'image')
    b = cv2.getTrackbarPos(B, 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    
    # if s == 0:
    #     img[:] = 0
    # else:
    #     img[:] = [b, g, r]

    img = cv2.line(img, (0, 0), (511, 511), (b, g, r), 5)
       
cv2.destroyAllWindows()