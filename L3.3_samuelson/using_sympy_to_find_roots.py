#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/7/2019 4:15 PM 
# File  : using_sympy_to_find_roots.py 
# IDE   : PyCharm

import sympy
from sympy import Symbol, init_printing
init_printing()

r1 = Symbol("ρ_1")
r2 = Symbol("ρ_2")
z = Symbol("z")

result = sympy.solve(z**2 - r1*z - r2, z)
print(result)