#! python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter

im = Image.open('Chapter05_3rd_pillow-tj.jpg')  # 打开当前目录下的图片
w, h = im.size  # 获得图像尺寸:
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w // 2, h // 2))  # 缩放到50%:
print('Resize image to: %sx%s' % (w // 2, h // 2))
im.show()  # 显示图片
# im.save('Chapter05_3rd_pillow-tj.jpg', 'jpeg')  # 把缩放后的图像用jpeg格式保存

im2 = im.filter(ImageFilter.BLUR)  # 应用模糊滤镜
im2.show()

# ### Pillow(PIL, Python Imaging Library)
# Python Imaging Library (Fork)
# PYPI: https://pypi.python.org/pypi/Pillow/
# Home Page: https://python-pillow.org
# Documentation: https://pillow.readthedocs.io/en/latest/
