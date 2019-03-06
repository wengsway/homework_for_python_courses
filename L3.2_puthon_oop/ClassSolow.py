#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 2:54 PM 
# File  : ClassSolow.py 
# IDE   : PyCharm


class Solow:
    """
    Implements the Solow growth model with update rule
    k_{t+1} = [(s z k^α_t) + (1 - δ)k_t] /(1 + n)
    """

    def __init__(self,
                 n=0.05,        # population growth rate
                 s=0.25,        # saving rate
                 δ=0.1,        # depreciation rate
                 α=0.3,        # share of labor
                 z=2.0,         # productivity
                 k=1.0):        # current capital stock
        self.n, self.s, self.δ = n, s, δ
        self.α, self.z, self.k = α, z, k

    def h(self):
        """Evaluate the h function"""
        # Unpack parameters (get rid of self to simplify notation)
        n, s, δ, α, z = self.n, self.s, self.δ, self.α, self.z
        # Apply the update rule
        return (s * z * self.k**α + (1 - δ) * self.k) / (1 + n)

    def update(self):
        """Update the current state"""
        self.k = self.h()

    def steady_state(self):
        """Compute the steady state value of capital"""
        # Unpack parameters (get rid of self to simplify notation)
        n, s, δ, α, z = self.n, self.s, self.δ, self.α, self.z
        # Compute and return steady state
        return ((s * z) / (n + δ)) ** (1 / (1 - α))

    def generate_sequence(self, t):
        """Generate and return a time series of lenght t"""
        path = []
        for i in range(t):
            path.append(self.k)
            self.update()
        return path
