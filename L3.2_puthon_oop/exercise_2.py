#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 4:02 PM 
# File  : exercise_2.py 
# IDE   : PyCharm


class Polynomial:
    """define a class to describe "evaluating polynomials"""

    def __init__(self, coeff):
        """initialize the class"""
        self.coeff = coeff

    def __call__(self, x):
        """evaluate the polynomial and return the result"""
        sum = 0
        for index, a in enumerate(self.coeff):
            sum += a * (x**index)
        return sum

    def derivative_evaluate(self, x):
        """evaluate the derivative polynomial and return the result"""
        # 我的理解是a0变为0，a1还是a1，a2变为2*a2...aN变为N*aN，然后x的次幂不变
        sum = 0
        for index, a in enumerate(self.coeff):
            sum += a * index * (x**(index))
        # 如果是整个求导，即不仅系数改变，x的次幂也都改变，那就使用下面的代码块。
        '''
        for index, a in enumerate(self.coeff):
            sum += a * index * (x**(index - 1))
        '''
        return sum


coeff = [1, 2, 3]
p = Polynomial(coeff)
print(p(2))
print(p.derivative_evaluate(2))


