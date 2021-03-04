# -*- coding: utf-8 -*- 

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from pathlib import Path


file_list = os.listdir(os.getcwd())
# file_list = os.listdir(os.getcwd() + '/test_')
file_list = [file_list[i] for i in range(len(file_list)) if '.jpg' in file_list[i]]

print(file_list)

for i in range(len(file_list)):
    img = cv2.imread(os.getcwd() + "/" + file_list[i], cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread(os.getcwd() + "/test_" + file_list[i], cv2.IMREAD_GRAYSCALE)

    # Adaptive Thresholding 적용
    max_output_value = 255  # 출력 픽셀 강도의 최대값
    neighborhood_size = 99
    subtract_from_mean = 10
    image_binarized = cv2.adaptiveThreshold(img,
                                            max_output_value,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY,
                                            neighborhood_size,
                                            subtract_from_mean)

    cv2.imwrite(os.getcwd() + "/result/" + file_list[i], image_binarized)
