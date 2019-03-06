# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:41:28 2018

@author: Wengsway

"""


def p(x, coeff):
    sum = 0
    for index, coeffvalue in enumerate(coeff):
        sum = sum + coeffvalue * (x ** index)
    return sum


print(p(2, [1, 2, 3]))
