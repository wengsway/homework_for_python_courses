#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 3:10 PM 
# File  : plot_solow_steady.py 
# IDE   : PyCharm

from ClassSolow import Solow
import matplotlib.pyplot as plt

s1 = Solow()
s2 = Solow(k=8.0)

T = 60
fig,ax = plt.subplots(figsize=(10, 6))

# Plot the common steady state value of capital
ax.plot([s1.steady_state()] * T, 'k-', label='steady state')

# Plot time series for each economy
for s in s1, s2:
    lb = f'capital series from initial state {s.k}'
    ax.plot(s.generate_sequence(T), 'o-', lw=2, alpha=0.6, label=lb)

ax.legend()
plt.show()
