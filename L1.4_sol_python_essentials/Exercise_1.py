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
