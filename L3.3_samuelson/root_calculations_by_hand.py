#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/7/2019 3:57 PM 
# File  : root_calculations_by_hand.py 
# IDE   : PyCharm

from cmath import sqrt
import matplotlib.pyplot as plt


# Part 1: "plot_y" can plot what we  passed arguments - any function
def plot_y(function=None):
    """function plots path of Y_t"""
    plt.subplots(figsize=(10, 6))
    plt.plot(function)
    plt.xlabel('Time $t$')
    plt.ylabel('$Y_t$', rotation=0)
    plt.grid()
    plt.show()


# Part 2: This is a 'manual' method to calculating root
# You can find another version called "Uses numpy to calculate roots" in study_samuelson_2.py


def y_nonstochastic(y_0=100, y_1=80, α=.92, β=.5, γ=10, n=80):
    """
    Takes values of parameters and computes roots of characteristic polynomial.
    It tells whether they are real or complex and whether they are less than unity in absolute value.
    It also computes a simulation of length n starting from the two given initial conditions for national income
    """

    roots = []

    ρ1 = α + β
    ρ2 = -β

    print(f'ρ_1 is {ρ1}')
    print(f'ρ_2 is {ρ2}')

    discriminant = ρ1 ** 2 + 4 * ρ2

    if discriminant == 0:
        roots.append(-ρ1 / 2)
        print('Single real root: ')
        print(''.join(str(roots)))
    elif discriminant > 0:
        roots.append((-ρ1 + sqrt(discriminant).real) / 2)
        roots.append((-ρ1 - sqrt(discriminant).real) / 2)
        print('Two real roots: ')
        print(''.join(str(roots)))
    else:
        roots.append((-ρ1 + sqrt(discriminant)) / 2)
        roots.append((-ρ1 - sqrt(discriminant)) / 2)
        print('Two complex roots: ')
        print(''.join(str(roots)))

    if all(abs(root) < 1 for root in roots):
        print('Absolute values of roots are less than one')
    else:
        print('Absolute values of roots are not less than one')

    def transition(x, t): return ρ1 * x[t - 1] + ρ2 * x[t - 2] + γ

    y_t = [y_0, y_1]

    for t in range(2, n):
        y_t.append(transition(y_t, t))

    return y_t


plot_y(y_nonstochastic())
