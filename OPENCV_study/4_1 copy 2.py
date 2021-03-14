
import cv2
import os

# path = 'data/img/'

path = 'save_/'



def make_img(class_):
    for i in range(1200):
        num = str(i)

        if len(num) == 1:
            num = '000' + num
        elif len(num) == 2:
            num = '00' + num
        elif len(num) == 3:
            num = '0' + num

        name = class_ + num + '.jpg'
        if os.path.isfile(path + name):
            continue

        name = class_ + num + '.jpeg'
        if os.path.isfile(path + name):
            continue

        name = class_ + num + '.JPG'
        if os.path.isfile(path + name):
            continue

        name = class_ + num + '.JPEG'
        if os.path.isfile(path + name):
            continue

        print(name)










make_img('apis')

make_img('ggoma')

make_img('simil')

make_img('crabro')

make_img('jangsu')

make_img('black')






#for i in range(0, img.shape[0], 2):
#    cv2.line(img, (0,i), (img.shape[1],i), (255,255,255))

