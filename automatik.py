import os
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFilter
file_list = os.listdir("photos/")
for photo_name in file_list:
    photo = Image.open("photos/"+photo_name)
    photo = photo.filter(ImageFilter.EMBOSS)
    photo.save("edited_photo/"+photo_name)
    photo.close()
print(file_list)
im = Image.open("img.png")
I1 = ImageDraw.Draw(im)
myFont = ImageFont.truetype('Deutsch Gothic.ttf', 65)
I1.text((10, 10), "spongebob", font=myFont, fill =(255, 238, 0))
im.show()
im.save("img_5.png")