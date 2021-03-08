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
img = cv2.imread('img_file/blank_500.jpg')

cv2.line(img, (50, 50), (150, 50), (250,0,0)) # 


