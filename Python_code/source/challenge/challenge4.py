#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/13 15:56
# @Author  : 刘宇
# @File    : challenge4.py
from urllib.request import *

code = 12345
for i in range(400):
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={code}'
    content = urlopen(url).read().decode('utf-8')
    print(content)
    code = content.split(" ")[-1]
if __name__ == "__main__":
    run_code = 0
