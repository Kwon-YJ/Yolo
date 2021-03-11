'''
RGB(x) BRG(o)

원
cv2.circle(img, center, radius, color, thickness, lineType) 
타원
cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness, lineType)


center: 타원의 중심 좌표 (x, y)
axes: 타원의 중심에서 가장 긴 축의 길이와 가장 짧은 축의 길이
angle: 타원의 기준 축 회전 각도
startAngle: 타원의 호가 시작하는 각도
endAngle: 타원의 호가 끝나는 각도

'''

import cv2


img = cv2.imread('img_file/blank_500.jpeg')

# 원점(150,150), 반지름 100
cv2.circle(img, (150,150), 100, (0,255,0), 5)
# 원점(300,150), 반지름 70
cv2.circle(img, (300, 150), 70, (0,255,0), 5)
# 원점(400,150), 반지름 50, 채우기
cv2.circle(img, (400,150), 50, (0,0,255), -1)

# 원점(325, 300), 반지름(75, 50) 납작한 타원 그리기
cv2.ellipse(img, (325, 300), (75,50), 0,0,360, (0,255,0))
# 원점(450,300), 반지름(50,75) 홀쭉한 타원 그리기
cv2.ellipse(img, (450, 300), (50,75), 0,0,360, (255,0,255))

# 원점(350, 425), 홀쭉한 타원 45도 회전 후 아랫 반원 그리기
cv2.ellipse(img, (350, 425), (50,75), 45, 0, 180, (0,0,255))
# 원점(400, 425), 홀쭉한 타원 45도 회전 후 윗 반원 그리기
cv2.ellipse(img, (400,425), (50,75), 45, 181, 360, (255,0,0))



cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()