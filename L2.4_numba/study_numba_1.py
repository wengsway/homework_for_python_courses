#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 12:02 PM 
# File  : study_numba_1.py
# IDE   : PyCharm

import random
import numpy as np
import quantecon as qe

# Operations on Arrays
qe.util.tic()   # start timing
n = 100000
sum = 0
for i in range(n):
    x = random.uniform(0, 1)
    sum += x**2
qe.util.toc()   # end timing

qe.util.tic()
y = np.random.uniform(0, 1, n)
np.sum(x**2)
qe.util.toc()

# Universal Functions
print(np.cos(1.0))
print(np.cos(np.linspace(0, 1, 3)))
