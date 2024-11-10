#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 9:44
# @Author  : 刘宇
# @File    : b.py
from operator import itemgetter

tuples = [(1, 2,4), (3, 1,5), (2, 3,6)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

if __name__ == "__main__":
    run_code = 0
