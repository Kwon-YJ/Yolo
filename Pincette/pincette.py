import cv2
import os


# src = cv2.imread('123.png')
src = cv2.imread('img_file/8bit.png')


if src is None:
    print('Image load failed!')
    #sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
# dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))


# dst1 = cv2.inRange(src, (75.6, 144.9, 123.3), (92.4, 177.1, 150.7)) # BLUE, RED, GREEN
dst1 = cv2.inRange(src, (0, 0, 0), (92.4, 177.1, 150.7)) # BLUE, RED, GREEN
dst2 = cv2.inRange(src_hsv, (28, 150, 0), (34, 255, 255))


img_result = cv2.bitwise_and(src, src, mask = dst1) 
cv2.imshow('img_color', img_result)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()