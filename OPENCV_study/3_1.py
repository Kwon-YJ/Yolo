# 이미지를 읽고 출력하기
# 키 입력시 모든 창 종료

import cv2

img_file = 'img_file/rainbow_2.png'
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file')