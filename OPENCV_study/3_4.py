# 동영상 파일 읽기

import cv2

video_file = 'img_file/dog.mp4' # 영상 경로

cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성
if cap.isOpened():            # 캡쳐 객체 초기화 확인
    while True:
        ret, img = cap.read() # 다음 프레임 읽기
        if ret:               # 프레임 읽기 유효
            cv2.imshow(video_file, img) # 화면 송출
            cv2.waitKey(25)   # 25ms 지연 (== 40fps 기준 1배속)
        else:                 # 다음 프레임 읽기 실패
            break             # 재생 종료
else:
    print('cant open video.') # 동영상 캡쳐 초기화 실패
cap.release()                 # 캡쳐 자원 반납
cv2.destroyAllWindows()
