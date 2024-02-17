from PIL import Image
from PIL import ImageFilter
im = Image.open("img_3.png")
print(im.format, im.size, im.mode )
im.show()
filtered_image = im.filter(ImageFilter.BoxBlur(5))
filtered_image.show()
im = Image.open("img_3.png")
im = im.transpose(Image.ROTATE_90)
im.save("rotered.png")
im = im.convert("L")
im.save("black_white.png")