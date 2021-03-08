# 카메라(웹캠) 프레임 읽어오기
# cv2.waitKey()는 지정된 시간 내에 입력이 없을 경우 -1을 리턴


import cv2

cap = cv2.VideoCapture(0) # 0번 카메라 연결

if cap.isOpened():
    while True:
        ret, frame = cap.read() # 카메라 프레임 읽기
        if ret:
            cv2.imshow('camera', frame) # 프레임 화면에 표시
            if cv2.waitKey(1) != -1: # 아무 키 입력 시
                break
        else:
            print('no frame')
            break
else:
    print('cant open camera.')
cap.release()
cv2.destroyAllWindows()

