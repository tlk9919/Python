#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/13 17:24
# @Author  : 刘宇
# @File    : challenge6.py
from urllib.request import *

# file_name = 'channel.zip'
# url = f'http://www.pythonchallenge.com/pc/def/{file_name}'
# path = './data/channel.zip'
# urlretrieve(url, path)
code = 90052
my_code = ['90052']
for i in range(910):
    url = f'./data/channel/{code}.txt'
    with open(url, 'r') as f:
        content = f.read()
        # print(content)
        code = content.split()[-1]
        my_code.append(code)
        if code == '46145':
            break

path = './data/channel.zip'
import zipfile

print(zipfile.ZipFile(path))
file = zipfile.ZipFile(path)
print(file.namelist())
# for i in resourse.namelist():
#     print(resourse.getinfo(i).comment)
for i in my_code:
    print(file.getinfo(i + '.txt').comment.decode('utf-8'), end='')
    if __name__ == "__main__":
     run_code = 0
