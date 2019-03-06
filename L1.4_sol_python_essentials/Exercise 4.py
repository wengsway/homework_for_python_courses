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
