import PIL.Image as Image


im = Image.open('sample.jpeg')
im1 = im.point(lambda x: int(x/17)*17)
im2 = im.point(lambda x: int(x/17))
#im2.save('test.png')

import png
import numpy as np
png.fromarray(np.asarray(im1, np.uint8),'L;4').save('test4bit_pypng.png')