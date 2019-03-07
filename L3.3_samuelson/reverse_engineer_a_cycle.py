#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/7/2019 4:01 PM 
# File  : reverse_engineer_a_cycle.py 
# IDE   : PyCharm

# code to reverse engineer a  cycle
# y_t = r^t (c_1 cos(ϕ t) + c2 sin(ϕ t))
# 给定极坐标系下的半径r和角度ϕ，计算出笛卡尔坐标系下的ρ1, ρ2, a, b

import cmath
import math


def f(r, ϕ):
    """
    Takes modulus r and angle ϕ of complex number r exp(j ϕ)
    and creates ρ1 and ρ2 of characteristic polynomial for which
    r exp(j ϕ) and r exp(- j ϕ) are complex roots.

    Returns the multiplier coefficient a and the accelerator coefficient b
    that verifies those roots.
    """
    g1 = cmath.rect(r, ϕ)  # Generate two complex roots
    g2 = cmath.rect(r, -ϕ)
    ρ1 = g1 + g2  # Implied ρ1, ρ2
    ρ2 = -g1 * g2
    b = -ρ2  # Reverse engineer a and b that validate these
    a = ρ1 - b
    return ρ1, ρ2, a, b


# Now let's use the function in an example
# Here are the example paramters


r = .95
period = 10  # Length of cycle in units of time
ϕ = 2 * math.pi / period

# Apply the function
ρ1, ρ2, a, b = f(r, ϕ)
print(f"a, b = {a}, {b}")
print(f"ρ1, ρ2 = {ρ1}, {ρ2}")

# Print the real components of ρ1 and ρ2
ρ1 = ρ1.real
ρ2 = ρ2.real
print(ρ1, ρ2)
