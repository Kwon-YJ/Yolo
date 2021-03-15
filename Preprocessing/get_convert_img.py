
import cv2
import os

def convert_img(img):
    for i in range(0, img.shape[1], 2):
        cv2.line(img, (i,0), (i,img.shape[1]), (0,0,0))
    return img


# make_img(벌 명칭, 번호 시작, 번호 끝, 읽기 경로, 쓰기 경로)
def make_img(class_, idx_start, idx_end, R_path, W_path):
    for i in range(idx_start, idx_end):
        num = str(i)

        if len(num) == 1:
            num = '000' + num
        elif len(num) == 2:
            num = '00' + num
        elif len(num) == 3:
            num = '0' + num

        name = class_ + num + '.jpg'
        if os.path.isfile(R_path + name):
            img = cv2.imread(R_path + name)
            result = convert_img(img)
            cv2.imwrite(W_path + name, result)
        
        name = class_ + num + '.png'
        if os.path.isfile(R_path + name):
            img = cv2.imread(R_path + name)
            result = convert_img(img)
            cv2.imwrite(W_path + name, result)

        name = class_ + num + '.jpeg'
        if os.path.isfile(R_path + name):
            img = cv2.imread(R_path + name)
            result = convert_img(img)
            cv2.imwrite(W_path + name, result)

        name = class_ + num + '.JPG'
        if os.path.isfile(R_path + name):
            img = cv2.imread(R_path + name)
            result = convert_img(img)
            cv2.imwrite(W_path + name, result)

        name = class_ + num + '.JPEG'
        if os.path.isfile(R_path + name):
            img = cv2.imread(R_path + name)
            result = convert_img(img)
            cv2.imwrite(W_path + name, result)


# path = 'data/img/'

R_path = 'test_/'

W_path = 'result_/'

start_, end = 0, 100

for i, item in enumerate(['apis', 'ggoma', 'simil', 'crabro', 'jangsu', 'black']):
    make_img(item, start_, end, R_path, W_path)
