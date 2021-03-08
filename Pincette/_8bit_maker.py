# import the image module

from PIL import Image

 

# Read a color image

colorImage = Image.open("img_file/sample.jpeg")

colorImage.show()



# Convert the color image to grey scale image

greyScaleImage = colorImage.convert("L")

 

# display the grey scale image

greyScaleImage.show()

 

# convert the color image to black and white image

blackAndWhiteImage = colorImage.convert("1")

blackAndWhiteImage.show()

 

# Convert using adaptive palette of color depth 8

imageWithColorPalette = colorImage.convert("P", palette=Image.ADAPTIVE, colors=8)

imageWithColorPalette.show()