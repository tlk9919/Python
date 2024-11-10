#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/13 16:37
# @Author  : 刘宇
# @File    : challenge5.py
from urllib.request import *
import pickle

# file_name='banner.p'
# url=f'http://www.pythonchallenge.com/pc/def/{file_name}'
path = './date/banner.p'
# urlretrieve(url,path)
with open(path, 'rb') as f:
    data = pickle.load(f)
    print(data)
    for i in data:
        for j in i:
            print(j[0] * j[1], end='')
        print()
if __name__ == "__main__":
    run_code = 0
