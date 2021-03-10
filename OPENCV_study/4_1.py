'''
RGB(x) BRG(o)

다양한 직선 그리기
cv2.line(img, start, end, color, thickness, lineType)

img: 그림을 그릴 이미지 파일
start: 선 시작 좌표(ex; (0,0))
end: 선 종료 좌표(ex; (500. 500))
color: BGR형태의 선 색상 (ex; (255, 0, 0) -> Blue)
thickness (int): 선의 두께. pixel (default=1)
lineType: 선 그리기 형식 (cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA)
'''

import cv2
img = cv2.imread('img_file/blank_500.jpeg')

cv2.line(img, (50, 50), (150, 50), (255,0,0))   # 파란색 1픽셀 선
cv2.line(img, (200,50), (300,50), (0,255,0)) # 초록색 1픽셀 선
cv2.line(img, (350, 50), (450, 50), (0,0,255)) # 빨간색 1픽셀 선

# 하늘색(파랑+초록) 10픽셀 선
cv2.line(img, (100, 100), (400, 100), (255,255,0), 10)
# 분홍(파랑+빨강) 10픽셀 선
cv2.line(img, (100,150), (400, 150), (255,0,255), 10)
# 노랑(초록+빨강) 10픽셀 선



cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()