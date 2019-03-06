# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:57:41 2018

@author: Wengsway

"""


def linapprox(a, b, n, x):
    f = lambda x: 1 / (x ** 2 + 1)
    point = [a]
    for i in range(1, n):
        point.append(point[0] + (i * (b - a)) / (n - 1))
    for j in range(n - 1):
        if x >= point[j] and x < point[j + 1]:
            y = f(point[j]) * (1 - (x - point[j]) / (point[j + 1] - point[j])) + f(point[j + 1]) * (x - point[j]) / (
                        point[j + 1] - point[j])
    return y


fit = round(linapprox(0, 1, 11, 0.55), 4)
print(fit)
