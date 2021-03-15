# 이미지 저장

import cv2

img_file = 'img_file/rainbow_2.png'
save_file = 'img_file/rainbow_2_gray.png'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)
cv2.waitKey()
cv2.destroyAllWindows()