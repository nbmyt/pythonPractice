#!/usr/bin/env python
# coding=utf-8

#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

img = Image.open("1.jpg")
length, width = img.size
red = (255, 0, 0)
imgDraw = ImageDraw.Draw(img)
ft = ImageFont.truetype("font.ttf", 100)
imgDraw.text((width - 100, 0), "2", fill = red, font = ft)
img.show()
# img.save("3.jpg")

