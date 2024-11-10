#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 8:24
# @Author  : 刘宇
# @File    : zidian1.py
# 步骤1: 初始化两个字典
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}
result_dict = {}
# 步骤2: 创建一个空字典用于存储结果


# 步骤3和4: 遍历第一个字典的键，如果键在第二个字典中也存在，则计算乘积并存储
for key in dict1.keys():
    if key in dict2.keys():
        result_dict = {key: dict1[key] * dict2[key]}
dict1.update(dict2)
dict1.update(result_dict)

# 步骤5: 打印结果字典
print(dict1)
if __name__ == "__main__":
    run_code = 0
