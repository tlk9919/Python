#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 10:05
# @Author  : 刘宇
# @File    : a.py
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2,2)
y = x**2 -2*x + 9
plt.plot(x,y) # 绘制x-y的折线图
plt.show()  # 显示绘制的图。请注意，如果使用save保存图片，需要在show前面保存
if __name__ == "__main__":
    run_code = 0
