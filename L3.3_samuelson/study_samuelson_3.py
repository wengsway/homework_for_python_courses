#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 10:52 PM 
# File  : study_samuelson_3.py 
# IDE   : PyCharm

import sympy
from sympy import Symbol

r1 = Symbol("ρ_1")
r2 = Symbol("ρ_2")
z = Symbol("z")

print(sympy.solve(z**2 - r1*z - r2, z))

a = Symbol("α")
b = Symbol("β")
r1 = a + b
r2 = -b

print(sympy.solve(z**2 - r1*z - r2, z))