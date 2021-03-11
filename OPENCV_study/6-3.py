# 마우스로 관심영역 지정 및 표시, 저장 (roi_crop_mouse.py)

import cv2
import numpy as np

img = cv2.imread('img_file/sunset.jpg')


x,y,w,h = cv2.selectROI('img', img, False)

if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped', roi) # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow('cropped', 0, 0) # 새창을 화면 좌측 상단에 이동
    cv2.imwrite('img_file/cropped2.jpg', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()