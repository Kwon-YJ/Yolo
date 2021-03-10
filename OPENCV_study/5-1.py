import cv2

file_path = 'img_file/sample.jepg'
img = cv2.imread(file_path) # 이미지 기본 값으로 읽기
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) # 이미지를 그레이 스케일로 읽기

cv2.namedWindow('origin') # origin 이름으로 창 생성
cv2.namedWindow('gray', cv2.WINDOW_NORMAL) # gray 이름으로 창 생성
cv2.imshow('origin', img) # origin 창에 이미지 표시
cv2.imshow('gray', img_gray) # gray 창에 이미지 표시

cv2.moveWindow('origin', 0, 0) # 창 위치 변경
