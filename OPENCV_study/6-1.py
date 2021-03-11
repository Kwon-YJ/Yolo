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
roi = img[y:y+h, x:x+w]

print(roi.shape) # (50,50,3)
# cv2.rectangle(roi, (x, y), (x+w, y+h), (0,255,0))
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) # roi 전체에 사각형 그리기
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()