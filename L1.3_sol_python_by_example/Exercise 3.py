# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:23:25 2018

@author: Wengsway

"""

import numpy as np

frequency = 0
numbers = int(input("Please input the number of times:"))
for i in range(1, numbers):
    x, y = np.random.uniform(0,1), np.random.uniform(0,1)
    area = np.sqrt(x**2 + y**2)
    if area <= 1.0:
        frequency = frequency + 1
pi = 4 * (frequency/numbers)
print(pi)
