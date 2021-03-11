# BGR, BGRA, Ahlpha 채널 (rgba.py)

import cv2
import numpy as np

img = cv2.imread('img_file/black1430.jpg')

img2 = img.astype(np.uint16) # dtype 변경
b, g, r = cv2.split(img2)    # 채널 별로 분리

gray1 = ((b + g + r)/ 3).astype(np.uint8) # 평균 값 연산 후 dtype 변경

gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR을 그레이 스케일로 변경
cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()
