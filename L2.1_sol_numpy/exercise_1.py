# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:00:33 2018

@author: Wengsway

"""

import numpy as np


N = int(input("请输入一个正整数作为 N："))
X = int(input("请输入一个值作为X："))
X_ARRAY = np.full(N, X, dtype=int)
X_ARRAY = np.insert(X_ARRAY, 0, 1)
A = input("请以空格为间隔连续输入一个数组:")
A_ARRAY = np.array(list(map(int, A.strip().split())))
B = np.array([A_ARRAY, np.cumprod(X_ARRAY)])
C = np.cumprod(B, axis=0)
print("\n", "最终的结果为：", sum(C[1]))
