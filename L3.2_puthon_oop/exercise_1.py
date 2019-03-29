#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 3:55 PM 
# File  : Exercise_1.py
# IDE   : PyCharm

from random import uniform


class ECDF:
    """define a class for  empirical cumulative distribution function (ecdf)"""

    def __init__(self, observations):
        self.observations = observations

    def __call__(self, x):
        true_num = []
        for obj in self.observations:
            if obj <= x:
                true_num.append(obj)
        return sum(true_num) / len(self.observations)


samples = [uniform(0, 1) for i in range(10)]
F = ECDF(samples)
print(F(0.5))
