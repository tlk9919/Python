#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 10:32
# @Author  : 刘宇
# @File    : heart.py
import numpy as np
import turtle

t = np.arange(-20, 20, 0.1)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
# 整体坐标放大15倍
x = x * 15
y = y * 15

turtle.setup(800, 700)
# 从中心位置移动到起始位置
turtle.penup()
print(x[0], y[0])
#正式绘制
turtle.goto(x[0], y[0])
turtle.pendown()
for i, j in zip(x, y):
    turtle.goto(i, j)
turtle.done()

if __name__ == "__main__":
    run_code = 0
