# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():  # 随机字母
    return chr(random.randint(65, 90))


def rndColor():  # 随机颜色
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def rndColor2():  # 随机颜色
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)  # 创建Font对象（使用字体文件绝对路径）
draw = ImageDraw.Draw(image)  # 创建Draw对象
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())  # 填充像素
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())  # 输出文字
image = image.filter(ImageFilter.BLUR)  # 应用模糊滤镜
image.show()

# ### Pillow示例
# 生成字母验证码图片：利用ImageDraw提供的绘图方法可以直接绘图；
