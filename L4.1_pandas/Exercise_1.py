#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/29/2019 1:46 PM 
# File  : Exercise_1.py 
# IDE   : PyCharm

# 导入 pandas 和 matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# 读取数据文件
df = pd.read_csv("C:/Users/Wengs/OneDrive/Documents/HUST/20180926 - Software "
                 "Class/homework_for_python_courses/L4.1_pandas/ticker_data.csv")
# 将 Date 设置为 index
df.set_index("Date", inplace=True)
# 将股票代码和全称设置为 dict
ticker_list = {'INTC': 'Intel',
               'MSFT': 'Microsoft',
               'IBM': 'IBM',
               'BHP': 'BHP',
               'TM': 'Toyota',
               'AAPL': 'Apple',
               'AMZN': 'Amazon',
               'BA': 'Boeing',
               'QCOM': 'Qualcomm',
               'KO': 'Coca-Cola',
               'GOOG': 'Google',
               'SNE': 'Sony',
               'PTR': 'PetroChina'}
# 生成一个 pd.Series 用于存储计算后的数据
percentage_price_change_list = pd.Series()
# 循环计算每只股票在2013年笼统的涨跌幅
for ticker in ticker_list:
    change = 100 * (df.loc[df.index[-1], ticker] - df.loc[df.index[0], ticker]) / df.loc[df.index[0], ticker]
    ticker_name = ticker_list[ticker]
    percentage_price_change_list[ticker_name] = change
# 按照涨跌幅进行排序，若为降序，则增加条件 ascending=False
percentage_price_change_list.sort_values(inplace=True)
# 画出图形
plt.title("The Percentage Price Change Over 2013 For Some Stocks")
plt.ylabel("100 * percentage")
percentage_price_change_list.plot(kind='bar')
# 设置横坐标旋转角度的语句应放在导入了横纵坐标的语句之后
plt.xticks(rotation=45)
plt.show()
