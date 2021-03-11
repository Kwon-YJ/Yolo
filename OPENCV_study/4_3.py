'''
RGB(x) BRG(o)

다각형
cv2.polylines(img, pts, isClosed, color, thickness, lineType)

pts: 연결할 꼭짓점 좌표, Numpy array
isClosed: 닫힌 도형 여부, True/False

'''

import cv2
import numpy as np

img = cv2.imread('img_file/blank_500.jpeg')

# Numpy array로 좌표 생성
# 번개 모양 선 좌표
pts1 = np.array([[50,50],[150,150],[100,140],[200,240]], dtype = np.int32)
# 삼각형 좌표
pts2 = np.array([[350,50],[250,200],[450,200]], dtype = np.int32)
# 삼각형 좌표
pts3 = np.array([[150,300],[50,450],[250,450]], dtype = np.int32)
# 5각형 좌표
pts4 = np.array([[350,250],[450,350],[400,450],[250,350]], dtype = np.int32)



# 다각형 그리기
cv2.polylines(img, [pts1], False, (255, 0, 0))
cv2.polylines(img, [pts2], False, (0, 0, 0), 10)
cv2.polylines(img, [pts3], True, (0, 0, 255), 10)
cv2.polylines(img, [pts4], True, (0, 0, 0))


cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()