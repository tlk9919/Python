#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 9:21
# @Author  : 刘宇
# @File    : challenge1.py
def change(i):
    if ord(i)>=97 and ord(i)<=120:
        return chr(ord(i)+2)
    elif ord(i)==121 or ord(i)==122:
        return chr(ord(i)+2-26)
    else:
        return i
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb"


print(''.join(map(change, 'map')))
if __name__ == "__main__":
    run_code = 0
