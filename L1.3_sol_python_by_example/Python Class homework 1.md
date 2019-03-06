# Python Class homework 1

### Exercise 1

Recall that n!n! is read as “nn factorial” and defined as n!=n×(n−1)×⋯×2×1n!=n×(n−1)×⋯×2×1

There are functions to compute this in various modules, but let’s write our own version as an exercise

In particular, write a function `factorial` such that `factorial(n)` returns n!n! for any positive integer n

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 23:01:45 2018

@author: Wengsway

"""

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input('please input any positive integer:'))
print(factorial(n))

```

### Exercise 2

The [binomial random variable](https://en.wikipedia.org/wiki/Binomial_distribution) Y∼Bin(n,p)Y∼Bin(n,p) represents the number of successes in nn binary trials, where each trial succeeds with probability pp

Without any import besides `from numpy.random import uniform`, write a function `binomial_rv` such that `binomial_rv(n, p)` generates one draw of YY

Hint: If UU is uniform on (0,1)(0,1) and p∈(0,1)p∈(0,1), then the expression `U < p` evaluates to `True` with probability p

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:26:42 2018

@author: Wengsway

"""

import numpy as np


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


u = np.random.normal(0, 1)
N = int(input("Please input the N value："))


def binomial_rv(n, p):
    y = p ** n * (1 - p) ** (N - n) * factorial(N) / (factorial(n) * factorial(N - n))
    return y


n = int(input("Please input the n value:"))
p = float(input("Please input the p value:"))
print(binomial_rv(n, p))

```

### Exercise 3

Compute an approximation to ππ using Monte Carlo. Use no imports besides

```
import numpy as np
```

Your hints are as follows:

- If $U$ is a bivariate uniform random variable on the unit square $(0,1)^2$, then the probability that $U$ lies in a subset $B$ of $(0,1)^2$ is equal to the area of $B$
- If U1,…,Un are iid copies of $U$, then, as $n$ gets large, the fraction that fall in $B$ converges to the probability of landing in $B$
- For a circle, area = pi * radius^2

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:23:25 2018

@author: Wengsway

"""

import numpy as np

frequency = 0
numbers = int(input("Please input the number of times:"))
for i in range(1, numbers):
    x, y = np.random.uniform(0,1), np.random.uniform(0,1)
    area = np.sqrt(x**2 + y**2)
    if area <= 1.0:
        frequency = frequency + 1
pi = 4 * (frequency/numbers)
print(pi)

```

### Exercise 4

Write a program that prints one realization of the following random device:

- Flip an unbiased coin 10 times
- If 3 consecutive heads occur one or more times within this sequence, pay one dollar
- If not, pay nothing

Use no import besides `from numpy.random import uniform`

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:25:01 2018

@author: Wengsway

"""

from numpy.random import randint

x = randint(0, 2, 10).tolist()
j = 0
for i in range(len(x) - 2):
    if x[i] == 1 and x[i + 1] == 1 and x[i + 2] == 1:
        j = j + 1
if j >= 1:
    print("You pay one dollar!")
else:
    print("You pay nothing!")

```

### Exercise 5

Your next task is to simulate and plot the correlated time series
$$
x_{t+1} = \alpha \, x_t + \epsilon_{t+1}
\quad \text{where} \quad
x_0 = 0
\quad \text{and} \quad t = 0,\ldots,T
$$
The sequence of shocks {$ϵ_t$} is assumed to be iid and standard normal

In your solution, restrict your import statements to

```python
import numpy as np
import matplotlib.pyplot as plt
```

Set T=200 and α=0.9

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:50:23 2018

@author: Wengsway

"""

import numpy as np
import matplotlib.pyplot as plt


def timeseries(α, T):
    x = [0]
    ε = np.random.randn(T)
    for t in range(T):
        x.append(α * x[t - 1] + ε[t])
    return x


T = int(input('Please input the T:'))
α = float(input('Please input the α：'))
plt.figure(figsize=(10, 5))
plt.plot(timeseries(α, T + 1), color='Hotpink', label='x')
plt.legend()

```

### Exercise 6

To do the next exercise, you will need to know how to produce a plot legend

The following example should be sufficient to convey the idea

```python
import numpy as np
import matplotlib.pyplot as plt

x = [np.random.randn() for i in range(100)]
plt.plot(x, label="white noise")
plt.legend()
plt.show()
```

Now, starting with your solution to exercise 5, plot three simulated time series, one for each of the cases α=0, α=0.8 and α=0.98

In particular, you should produce (modulo randomness) a figure that looks as follows

`not found`

(The figure nicely illustrates how time series with the same one-step-ahead conditional volatilities, as these three processes have, can have very different unconditional volatilities.)

Use a `for` loop to step through the αα values

Important hints:

- If you call the `plot()` function multiple times before calling `show()`, all of the lines you produce will end up on the same figure
  - And if you omit the argument `'b-'` to the plot function, Matplotlib will automatically select different colors for each line
- The expression `'foo' + str(42)` evaluates to `'foo42'`

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:14:49 2018

@author: Wengsway

"""

import numpy as np
import matplotlib.pyplot as plt


def timeseries(α, T):
    x = [0]
    ε = np.random.randn(T)
    for t in range(T):
        x.append(α * x[t - 1] + ε[t])
    return x


T = int(input('Please input the T:'))
for i in range(3):
    α = float(input('Please input the α：'))
    plt.figure(figsize=(10, 5))
    plt.plot(timeseries(α, T + 1), color='r', label='x')
    plt.legend()
    plt.show()

```

