import cv2
import numpy as np

def image_handler():
    image_file='image/galaxy.jpg'
    # 파라미터 인자로 첫째는 이미지 파일의 경로를 주고 두번째 파라미터는 이미지 파일을 읽는 방식을 나타낸다.
    # cv2.IMREAD_COLOR : 이미지를 컬러로 로드하며 투명한 부분은 모두 무시합니다. 
    # cv2.IMREAD_GRAYSCALE : 이미지를 흑백으로 로드합니다.
    # cv2.IMREAD_UNCHANGED : 알파채널을 포함하여 이미지를 원본 그대로 로드하니다.

    img1 = cv2.imread(image_file, 0)
    img2 = cv2.imread(image_file, 1) 
    img3 = cv2.imread(image_file, -1)
    
    # imshow 함수를 사용하는데 첫번째 파라미터는 해당 이미지 윈도우의 타이틀, 두번째는 화면에 나타낼 이미지 객체 입니다.
    cv2.imshow('color 0: Gray Image', img1)
    # cv2.imshow('color 1: Color Image', img2)
    # cv2.imshow('color -1: Unchanged Color Image', img3)
 
    cv2.waitKey(0) & 0xFF

    cv2.destroyAllWindows()

if __name__=='__main__':
    image_handler()
    