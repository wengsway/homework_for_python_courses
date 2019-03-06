# Python Class homework 2

### Exercise 1

Part 1: Given two numeric lists or tuples `x_vals` and `y_vals` of equal length, compute their inner product using `zip()`

Part 2: In one line, count the number of even numbers in 0,…,99

- Hint: `x % 2` returns 0 if `x` is even, 1 otherwise

Part 3: Given `pairs = ((2, 5), (4, 2), (9, 8), (12, 10))`, count the number of pairs `(a, b)` such that both `a` and `b` are even

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:15:44 2018

@author: Wengsway

"""

# Part 1
x_vals , y_vals = (1,2,3),(4,5,6)
sum = 0
for x,y in zip(x_vals,y_vals):
      sum = sum + x*y
print("The inner product is:", sum)

# Part 2
print(len([n for n in range(0,100) if n%2==0]))

# Part 3
pairs = ((2,5),(4,2),(9,8),(12,10))
count = 0
for i in pairs:
      if i[0]%2 == 0 and i[1]%2 == 0:
            count = count + 1
print(count)
```

### Exercise 2

Consider the polynomial
$$
p(x)
= a_0 + a_1 x + a_2 x^2 + \cdots a_n x^n
= \sum_{i=0}^n a_i x^i
$$
Write a function `p` such that `p(x, coeff)` that computes the value in [(1)](http://localhost:8888/notebooks/Lec%201.4%20-%20python_essentials.ipynb#equation-polynom0) given a point `x` and a list of coefficients `coeff`

Try to use `enumerate()` in your loop

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:41:28 2018

@author: Wengsway

"""

def p(x,coeff):
      sum = 0
      for index,coeffvalue in enumerate(coeff):
            sum = sum + coeffvalue * (x**index)
      return sum
print(p(2,[1,2,3]))
```

### Exercise 3

Write a function that takes a string as an argument and returns the number of capital letters in the string

Hint: `'foo'.upper()` returns `'FOO'`

略

### Exercise 4

Write a function that takes two sequences `seq_a` and `seq_b` as arguments and returns `True` if every element in `seq_a` is also an element of `seq_b`, else `False`

- By “sequence” we mean a list, a tuple or a string
- Do the exercise without using [sets](https://docs.python.org/3/tutorial/datastructures.html#sets) and set methods

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:50:43 2018

@author: Wengsway

"""


def sequence(seq_a, seq_b):
    counts = 0
    for i in range(len(seq_a)):
        if seq_a[i] in seq_b:
            counts = counts + 1
    if counts == len(seq_a):
        return True
    else:
        return False


print(sequence([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]))

```

### Exercise 5

When we cover the numerical libraries, we will see they include many alternatives for interpolation and function approximation

Nevertheless, let’s write our own function approximation routine as an exercise

In particular, without using any imports, write a function `linapprox` that takes as arguments

- A function `f` mapping some interval [a,b][a,b] into ℝR
- two scalars `a` and `b` providing the limits of this interval
- An integer `n` determining the number of grid points
- A number `x` satisfying `a <= x <= b`

and returns the [piecewise linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) of `f` at `x`, based on `n` evenly spaced grid points `a = point[0] < point[1] < ... < point[n-1] = b`

Aim for clarity, not efficiency

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:57:41 2018

@author: Wengsway

"""


def linapprox(a, b, n, x):
    f = lambda x: 1 / (x ** 2 + 1)
    point = [a]
    for i in range(1, n):
        point.append(point[0] + (i * (b - a)) / (n - 1))
    for j in range(n - 1):
        if x >= point[j] and x < point[j + 1]:
            y = f(point[j]) * (1 - (x - point[j]) / (point[j + 1] - point[j])) + f(point[j + 1]) * (x - point[j]) / (
                        point[j + 1] - point[j])
    return y


fit = round(linapprox(0, 1, 11, 0.55), 4)
print(fit)

```
