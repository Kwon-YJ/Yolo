# 웹캠 녹화
# cv2.VideoWriter(file_path, fourcc, fps, (width, height)) // 여러 프레임 동영상 저장
# (경로, 코덱, 프레임, (사이즈))

import cv2

cap = cv2.VideoCapture(0) # 0번 카메라 연결
if cap.isOpened:
    file_path = './record.avi' # 저장할 파일 경로 이름
    fps = 30.0                 # FPS, 초당 프레임 수
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))  # 프레임 사이즈
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # VideoWriter 객체 생성
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording', frame)
            out.write(frame)
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            print("no frame!")
            break
    out.release()
else:
    print("cant open camera!")
cap.release()
cv2.destroyAllWindows()





