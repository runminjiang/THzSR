"""
用来裁剪图片并绘制矩形框
"""

from PIL import Image
from PIL import ImageDraw
name = 'unet'
img = Image.open("%s.bmp" % name)

a = ImageDraw.ImageDraw(img)  #用a来表示

print(img.width,img.height)

left = 150
upper = 60
right = 200
lower = 100

area = (left,upper,right,lower)
# img.show()

crop_img = img.crop(area)
# crop_img.show()
crop_img.save("%s_crop.bmp"%name)

# 在边界框的两点（左上角、右下角）画矩形，无填充，边框红色，边框像素为1
a.rectangle(((left, upper),(right, lower)), fill=None, outline='red', width=1)  
# img.show()

img.save("%s_rec.bmp"%name)