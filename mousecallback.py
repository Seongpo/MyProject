'''마우스이용한 그림그리기'''
import cv2
import numpy as np

#mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
    if event == cv2.EVENT_RBUTTONUP:
        cv2.circle(img, (x, y), 25, (0, 255, 0), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)
    if event == cv2.EVENT_MOUSEMOVE:
        print('x, y = (%s, %s)'%(x,y), end='\r' )
    

# create a black image, a window and bind the function to window
# 배경이미지를 만들고
img = np.zeros((512, 512, 3), np.uint8) 
# image라는 이름의 윈도우를 만들고
cv2.namedWindow('image')
# 마우스 동작이 발생하면 image라는 윈도우에 draw_circle을 호출한다. 
cv2.setMouseCallback('image', draw_circle)


# image 라는 윈도우에 img를 그린다. 20msecond 동안 키 입력을 기다려서 esc 가 나오면
# 루프를 나오고 그렇지 않은면 다시 루프를 돈다.
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(2000) & 0xFF == 27:
        break
cv2.destroyAllWindows()

