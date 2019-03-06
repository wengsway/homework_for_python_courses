#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 1:31 PM 
# File  : study_numba_3.py 
# IDE   : PyCharm

import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import quantecon as qe

# @jit
def qm(x0, n):
    x = np.empty(n+1)
    x[0] = x0
    for t in range(n):
        x[t+1] = 4 * x[t] * (1 - x[t])
    return x

qe.tic()
x = qm(0.1, int(10**5))
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, 'b-', lw=2, alpha=0.8)
ax.set_xlabel('time', fontsize=16)
plt.show()
qe.toc()

qm_numba = jit(qm)
# If you don’t need a separate name for the “numbafied” version of qm, you can just put @jit before the function.
# This is equivalent to qm = jit(qm)
qe.tic()
qm_numba(0.1, int(10**5))
qe.toc()

