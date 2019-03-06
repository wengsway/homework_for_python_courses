#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 2:45 PM 
# File  : ClassConsumer.py
# IDE   : PyCharm


class Consumer:
    """定义关于消费者的一个类"""

    def __init__(self, w):
        """初始化消费者的财富"""
        self.wealth = w

    def earn(self, y):
        """定义消费者赚了y元"""
        self.wealth += y

    def spend(self, x):
        """定义消费者花费了x元"""
        new_wealth = self.wealth - x
        if new_wealth < 0:
            print("Insufficent funds")
        else:
            self.wealth = new_wealth


c1 = Consumer(10)
c1.spend(5)
print(c1.wealth)
c1.earn(15)
print(c1.wealth)
print(c1.__dict__)
print(Consumer.__dict__)