# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:56:51 2020

@author: wuchengxi
"""


import pandas as pd
# df={"姓名":"张飞","语文":68}
# print(df)
inputfile='E:\Data Analysis SVW\Data_Engine_with_Python-master\score.xlsx'
df=pd.read_excel(inputfile)
print(df)
temp=df[['语文','数学','英语']]
print('平均成绩----------------')
print(temp.mean())

print('最大成绩----------------')
print(temp.max())

print('最小成绩----------------')
print(temp.min())

df['总成绩']=temp.sum(axis=1)
print(df)
df['名次']=df['总成绩'].rank(ascending=False)
print(df)