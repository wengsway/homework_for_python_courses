#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 3:34 PM 
# File  : ClassChaos.py 
# IDE   : PyCharm


class Chaos:
    """
    Models the dynamical system with :math:`x_{t+1} = r x_t (1 - x_t)`
    0 <= x0 <= 1, 0 <= r <= 4
    """

    def __init__(self, x0, r):
        """Initialize with state x0 and parameter r"""
        self.x, self.r = x0, r

    def update(self):
        "Apply the map to update state."
        self.x = self.r * self.x * (1 - self.x)

    def generate_sequence(self, n):
        "Generate and return a sequence of length n."
        path = []
        for i in range(n):
            path.append(self.x)
            self.update()
        return path
