#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 1:51 PM 
# File  : study_numba_4.py 
# IDE   : PyCharm

from numba import vectorize
import numpy as np
import quantecon as qe


@vectorize('float64(float64, float64)', target='parallel')
def f_vec(x, y):
    return np.cos(x**2 + y**2) / (1 + x**2 + y**2)


grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)

# run once to compile
np.max(f_vec(x, y))

qe.tic()
np.max(f_vec(x, y))
qe.toc()
