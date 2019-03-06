#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 9:18 AM 
# File  : study_scipy.py 
# IDE   : PyCharm


import numpy as np
import timeit
from scipy.stats import beta, linregress
from scipy.optimize import bisect, newton, brentq
from scipy.integrate import quad
import matplotlib.pyplot as plt

'''
# Part 1: Random Variables and Distributions
q = beta(5, 5)      # beta(a, b) with a = b = 5
obs = q.rvs(2000)   # rvs means random variates and it is a method of beta
grid = np.linspace(0.01, 0.99, 100)

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(obs, bins=40, normed=True)
ax.plot(grid, q.pdf(grid), 'k-', linewidth=2)
plt.show()
'''
'''
# Part 2: Linregress
x = np.random.randn(200)    # 从标准正太分布中返回200个值
y = 2 * x + 0.1 * np.random.randn(200)
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print("斜率：", slope)
print("截距：", intercept)
print("相关系数：", r_value)
print("P 值：", p_value)
print("标准差：", std_err)
'''
'''
# Part 3: Roots and Fixed Points
f = lambda x: np.sin(4 * (x - 1 / 4)) + x + x ** 20 - 1
x = np.linspace(0, 1, 100)

plt.figure(figsize=(10, 8))
plt.plot(x, f(x))
plt.axhline(ls='--', c='k')
plt.show()
'''
'''
# Part 4: Bisection （对分）
# Compare the time two methods need
# bisect method is convenient
start = timeit.default_timer()
print(bisect(f, 0, 1))
end = timeit.default_timer()
print(str(end - start))

# newton method is not robust
start = timeit.default_timer()
print(newton(f, 0))  # Start the search at initial condition x = 0 or another one
end = timeit.default_timer()
print(str(end - start))

# brentq combines fast and robust
start = timeit.default_timer()
print(brentq(f, 0, 1))
end = timeit.default_timer()
print(str(end - start))
'''
# Part 5: Intergration
integral, error = quad(lambda x: x**2, 0, 1)
print(integral, error)
