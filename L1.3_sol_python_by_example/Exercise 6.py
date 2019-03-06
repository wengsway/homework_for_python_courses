# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:14:49 2018

@author: Wengsway

"""

import numpy as np
import matplotlib.pyplot as plt


def timeseries(α, T):
    x = [0]
    ε = np.random.randn(T)
    for t in range(T):
        x.append(α * x[t - 1] + ε[t])
    return x


T = int(input('Please input the T:'))
for i in range(3):
    α = float(input('Please input the α：'))
    plt.figure(figsize=(10, 5))
    plt.plot(timeseries(α, T + 1), color='r', label='x')
    plt.legend()
    plt.show()
