# 웹캠으로 사진찍기 (video_cam_take_pic.py)

import cv2

cap = cv2.VideoCapture(0) # 0번 카메라 연결
if cap.isOpended():
    while True:
        ret, frame = cap.read() # 카메라 프레임 읽기
        if ret:
            cv2.imshow('camera', frame) # 프레임 화면에 표시
            if cv2.waitKey(1) != 1: # 아무 키 입력 시
                cv2.imwrite('photo.jpg', frame) # 해당 프레임을 이미지로 저장
                break
        else:
            print('no frame!')
            break
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()




