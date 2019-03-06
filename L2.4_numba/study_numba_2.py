#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 12:15 PM 
# File  : study_numba_2.py 
# IDE   : PyCharm

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import quantecon as qe


def f(x, y):
    return np.cos(x ** 2 + y ** 2) / (1 + x ** 2 + y ** 2)


# xgrid 和 ygrid 的值
xgrid = np.linspace(-3, 3, 1000)  # 如果调高50，图形将变得更“细腻”
ygrid = xgrid
# 用于生成x-y平面的网格
x, y = np.meshgrid(xgrid, ygrid)

fig = plt.figure(figsize=(10, 6))
ax = Axes3D(fig)
# 也可以采用下面的方式生成
# ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,                      # 横轴的值
                y,                      # 纵轴的值
                f(x, y),                # Z 轴的值
                rstride=2, cstride=2,   # rstride 和 cstride 分别代表 row 和 column 的夸大；越小越密，越大越粗。
                cmap=cm.jet,            # 填充颜色，可以尝试改为'rainbow'
                alpha=0.7,              # 用于设置3D图形的透明度，值越小越透明。
                linewidth=0.25)         # 用于设置图形中曲线的粗细
ax.contour(x,                           # 横轴的值
           y,                           # 纵轴的值
           f(x, y),                     # Z 轴的值
           zdir='z',                    # 'z'将图形投影到 X-Y 平面
           offset=-0.5,                 # 投影的结果放在 Z=-0.5 这个平面上
           cmap=cm.jet)                 # 投影的颜色，一般与图形的颜色相同。
"""
其他颜色可参考以下网址的信息：
https://matplotlib.org/examples/color/colormaps_reference.html
"""
ax.set_zlim(-0.5, 1.0)                  # 用于设置Z轴的坐标范围，不设置时，将在图形上自动生成适当的范围。
plt.show()

# compare Python loops and vectorized method
grid = np.linspace(-3, 3, 1000)
m = -np.inf
qe.tic()
for x in grid:
    for y in grid:
        z = f(x, y)
        if z > m:
            m = z
qe.toc()

qe.tic()
np.max(f(x, y))
qe.toc()
