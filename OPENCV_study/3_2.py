#_1.py 에서 이미지를 회색조(GRAYSCALE)로 불러오기

import cv2

img_file = 'img_file/rainbow_2.png'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')