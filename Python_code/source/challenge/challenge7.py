#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 8:19
# @Author  : 刘宇
# @File    : challenge7.py
from urllib.request import *
# http://www.pythonchallenge.com/pc/def/oxygen.html
# http://www.pythonchallenge.com/pc/def/oxygen.png
# from urllib.request import urlretrieve
#
# path = './data/oxygen.png'
# url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
# urlretrieve(url, path)
path = './data/oxygen.png'
from PIL import Image

image = Image.open(path)
# RGBA 629 95
print(image.width, image.height)
# for i in range(image.height):
info = []
for j in range(0, image.width - 21, 7):
    r, g, b, a = image.getpixel((j, image.height // 2))
    # print(chr(r),end=' ')
    info.append(chr(r))
    # if not (r==g and g==b):
    #     print(j)
print(''.join(info))
key = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(x) for x in key]))
if __name__ == "__main__":
    run_code = 0
# integrity