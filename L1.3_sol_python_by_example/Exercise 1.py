# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 23:01:45 2018

@author: Wengsway

"""


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('please input any positive integer:'))
print(factorial(n))
