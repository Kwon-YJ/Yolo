# 관심영역 표시 (roi.py)

import cv2
import numpy as np 

img = cv2.imread('img_file/sunset.jpg')

# roi 좌표
x = 320
y = 150
w = 50
h = 50

# roi 지정
roi = img[y:y+h, x:x+w] # roi 지정
img2 = roi.copy()       # roi 배열 복제

img[y:y+h, x+w:x+w+w] = roi # 새로운 좌표에 roi 추가
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0)) # 복제된 영역 표시

cv2.imshow("img", img) # 원본 이미지 출력
cv2.imshow("roi", img2) # roi 만 따로 출력


key = cv2.waitKey(0)
cv2.destroyAllWindows()