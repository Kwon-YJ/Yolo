from PIL import Image



im = Image.open("sample.png")

im.save("sample_bmp.bmp")

im.save("sample_png.png")

im.save("sample_gif.gif")

