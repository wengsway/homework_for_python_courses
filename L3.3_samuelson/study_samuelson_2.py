#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 10:38 PM 
# File  : study_samuelson_2.py
# IDE   : PyCharm

import matplotlib.pyplot as plt
from cmath import sqrt
import numpy as np
import math
import cmath


# Part 1: Function to describe implications of characteristic polynomial
def categorize_solution(ρ1, ρ2):
    """this function takes values of ρ1 and ρ2 and uses them to classify the type of solution"""

    discriminant = ρ1 ** 2 + 4 * ρ2
    if ρ2 > 1 + ρ1 or ρ2 < -1:
        print('Explosive oscillations')
    elif ρ1 + ρ2 > 1:
        print('Explosive growth')
    elif discriminant < 0:
        print('Roots are complex with modulus less than one; therefore damped oscillations')
    else:
        print('Roots are real and absolute values are less than zero; therefore get smooth convergence to a steady '
              'state')


# Part 2: Function for plotting  𝑌𝑡  paths
# "plot_y" can plot what we  passed arguments - any function
def plot_y(function=None):
    """function plots path of Y_t"""
    plt.subplots(figsize=(10, 6))
    plt.plot(function)
    plt.xlabel('Time $t$')
    plt.ylabel('$Y_t$', rotation=0)
    plt.grid()
    plt.show()


# Part 3: Uses numpy to calculate roots under conditions:nonstochastic
def y_nonstochastic(y_0=100, y_1=80, α=.9, β=.8, γ=10, n=80):
    """ Rather than computing the roots of the characteristic polynomial by hand as we did earlier, this function
    enlists numpy to do the work for us """

    # Useful constants
    ρ1 = α + β
    ρ2 = -β

    categorize_solution(ρ1, ρ2)

    # Find roots of polynomial
    roots = np.roots([1, -ρ1, -ρ2])
    print(f'Roots are {roots}')

    # Check if real or complex
    if all(isinstance(root, complex) for root in roots):
        print('Roots are complex')
    else:
        print('Roots are real')

    # Check if roots are less than one
    if all(abs(root) < 1 for root in roots):
        print('Roots are less than one')
    else:
        print('Roots are not less than one')

    # Define transition equation
    def transition(x, t):
        return ρ1 * x[t - 1] + ρ2 * x[t - 2] + γ

    # Set initial conditions
    y_t = [y_0, y_1]

    # Generate y_t series
    for t in range(2, n):
        y_t.append(transition(y_t, t))

    return y_t


plot_y(y_nonstochastic())
print("\n")

# Part 4: code to reverse engineer a  cycle
# y_t = r^t (c_1 cos(ϕ t) + c2 sin(ϕ t))
# 给定极坐标系下的半径r和角度ϕ，计算出笛卡尔坐标系下的ρ1, ρ2, a, b

import cmath


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


# Part 5: Under conditons:stochastic
def y_stochastic(y_0=0, y_1=0, α=0.8, β=0.2, γ=10, n=100, σ=5):
    """This function takes parameters of a stochastic version of the model and proceeds to analyze
    the roots of the characteristic polynomial and also generate a simulation"""

    # Useful constants
    ρ1 = α + β
    ρ2 = -β

    # Categorize solution
    categorize_solution(ρ1, ρ2)

    # Find roots of polynomial
    roots = np.roots([1, -ρ1, -ρ2])
    print(roots)

    # Check if real or complex
    if all(isinstance(root, complex) for root in roots):
        print('Roots are complex')
    else:
        print('Roots are real')

    # Check if roots are less than one
    if all(abs(root) < 1 for root in roots):
        print('Roots are less than one')
    else:
        print('Roots are not less than one')

    # Generate shocks
    ϵ = np.random.normal(0, 1, n)

    # Define transition equation
    def transition(x, t):
        return ρ1 * \
               x[t - 1] + ρ2 * x[t - 2] + γ + σ * ϵ[t]

    # Set initial conditions
    y_t = [y_0, y_1]

    # Generate y_t series
    for t in range(2, n):
        y_t.append(transition(y_t, t))

    return y_t


plot_y(y_stochastic())
print("\n")

# Part 6: Let’s do a simulation in which there are shocks and the characteristic polynomial has complex roots

r = .97
#  length of cycle in units of time
period = 10
ϕ = 2 * math.pi / period
# apply the  reverse engineering function f
ρ1, ρ2, a, b = f(r, ϕ)
a = a.real  # drop the imaginary part so that it is a valid input into y_nonstochastic
b = b.real
print(f"a, b = {a}, {b}")
plot_y(y_stochastic(y_0=40, y_1=42, α=a, β=b, σ=2, n=100))


# Part 7: computes a response to either a permanent or one-off increase in government expenditures
def y_stochastic_g(y_0=20,
                   y_1=20,
                   α=0.8,
                   β=0.2,
                   γ=10,
                   n=100,
                   σ=2,
                   g=0,
                   g_t=0,
                   duration='permanent'):
    """This program computes a response to a permanent increase in government expenditures that occurs
       at time 20"""

    # Useful constants
    ρ1 = α + β
    ρ2 = -β

    # Categorize solution
    categorize_solution(ρ1, ρ2)

    # Find roots of polynomial
    roots = np.roots([1, -ρ1, -ρ2])
    print(roots)

    # Check if real or complex
    if all(isinstance(root, complex) for root in roots):
        print('Roots are complex')
    else:
        print('Roots are real')

    # Check if roots are less than one
    if all(abs(root) < 1 for root in roots):
        print('Roots are less than one')
    else:
        print('Roots are not less than one')

    # Generate shocks
    ϵ = np.random.normal(0, 1, n)

    def transition(x, t, g):

        # Non-stochastic - separated to avoid generating random series when not needed
        if σ == 0:
            return ρ1 * x[t - 1] + ρ2 * x[t - 2] + γ + g

        # Stochastic
        else:
            ϵ = np.random.normal(0, 1, n)
            return ρ1 * x[t - 1] + ρ2 * x[t - 2] + γ + g + σ * ϵ[t]

    # Create list and set initial conditions
    y_t = [y_0, y_1]

    # Generate y_t series
    for t in range(2, n):

        # No government spending
        if g == 0:
            y_t.append(transition(y_t, t))

        # Government spending (no shock)
        elif g != 0 and duration == None:
            y_t.append(transition(y_t, t))

        # Permanent government spending shock
        elif duration == 'permanent':
            if t < g_t:
                y_t.append(transition(y_t, t, g=0))
            else:
                y_t.append(transition(y_t, t, g=g))

        # One-off government spending shock
        elif duration == 'one-off':
            if t == g_t:
                y_t.append(transition(y_t, t, g=g))
            else:
                y_t.append(transition(y_t, t, g=0))
    return y_t


plot_y(y_stochastic_g(g=10, g_t=20, duration='permanent'))
print("\n")
plot_y(y_stochastic_g(g=500, g_t=50, duration='one-off'))
print("\n")
