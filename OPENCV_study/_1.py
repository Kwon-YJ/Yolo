



'''
    for i in range(0, img.shape[1], 2):
        cv2.line(img, (i,0), (i,img.shape[1]), (0,0,0))
    return img

'''

import cv2
img = cv2.imread('img_file/____.jpg')

# 분홍(파랑+빨강) 10픽셀 선
# cv2.line(img, (100,150), (400, 150), (255,0,255), 2)

for i in range(0, img.shape[1], 32):
    cv2.line(img, (i,0), (i,img.shape[1]), (255,0,255), 1)

    cv2.line(img, (0,i), (img.shape[1],i), (255,0,255), 1)



cv2.imshow('lines', img)
cv2.imwrite('img_file/result____.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()