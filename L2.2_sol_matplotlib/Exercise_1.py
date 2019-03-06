# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:00:33 2018

@author: Wengsway

"""

import matplotlib.pyplot as plt
import numpy as np
import math


fig, ax = plt.subplots()
theta = np.linspace(0, 2, 10)
for i in range(len(theta)):
    x = np.linspace(0,5,50)
    y = np.cos(math.pi*theta[i]*x)*np.exp(-x)
    current_label = f'$theta = {theta[i]:.2}$'
    ax.plot(x, y, linewidth=2, alpha=0.6, label=current_label)
ax.legend()
plt.show()
