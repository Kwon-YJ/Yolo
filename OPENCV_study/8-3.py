# 오츠의 알고리즘을 적용한 스레시 홀딩

import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지를 그레이 스케일로 읽기
img = cv2.imread('img_file/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

# 경계 값을 130으로 지정
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

# 경계 