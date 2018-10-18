'''동영상 플레이'''
import cv2

# vimage=input("Input Video file name :")
# vimage=os.getcwd()+'\\'+vimage

cap = cv2.VideoCapture('./image/01_Command_Stream.ts')
while True:
    ret, frame = cap.read() #ret : 영상이 정상적으로 읽혀지면 True, 그렇지 않은면 False, frame: 불러온 영상저장 버퍼
    if ret:
        GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', GRAY)
        if cv2.waitKey(10)&0xFF == ord('q'):
            break
    else:
        break

#Release
cap.release()
cv2.destroyAllWindows()
