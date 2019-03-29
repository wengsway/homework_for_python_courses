#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/29/2019 2:56 PM 
# File  : Exercise_1_more.py 
# IDE   : PyCharm

# 导入 pandas 和 matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据文件
df = pd.read_csv("C:/Users/Wengs/OneDrive/Documents/HUST/20180926 - Software "
                 "Class/homework_for_python_courses/L4.1_pandas/ticker_data.csv")
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

# 提前写入正确的时间列
temp_dict = {"Date": df['Date'][1:].tolist()}
# 循环获取每只股票在2013年每一天的变动百分比
for ticker in ticker_list:
    change = []
    ticker_name = ticker_list[ticker]
    for i in range(1, len(df)):
        per_change = 100 * (df.loc[df.index[i], ticker] - df.loc[df.index[i-1], ticker]) / df.loc[df.index[i-1], ticker]
        change.append(per_change)
    temp_dict[ticker_name] = change
# 将字典转换为 dataframe
df_change = pd.DataFrame(temp_dict)
# 将 Date 列设为 index
df_change.set_index("Date", inplace=True)

# 画出图形
for i in range(df_change.shape[1]):
    df_change[df_change.columns[i:i+1]].plot(kind='line')
    plt.title("The Percentage Price Change Over 2013 For " + df_change.columns.values[i])
    plt.ylabel("100 * percentage")
    plt.xlabel(df_change.columns.values[i])
    plt.show()
