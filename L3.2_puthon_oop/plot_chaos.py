#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 3:38 PM 
# File  : plot_chaos.py 
# IDE   : PyCharm

from ClassChaos import Chaos
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ch = Chaos(0.1, 4.0)
"""
# Part 1
ts_length = 250
ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$x_t$', fontsize=14)
x = ch.generate_sequence(ts_length)
ax.plot(range(ts_length), x, 'bo-', alpha=0.5, lw=2, label='$x_t$')
plt.show()
"""
# Part 2
r = 2.5
while r < 4.0:
    ch.r = r
    t = ch.generate_sequence(1000)[950:]
    ax.plot([r] * len(t), t, 'b.', ms=0.6)
    r = r + 0.005

ax.set_xlabel('$r$', fontsize=16)
plt.show()