# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:09:42 2020

@author: wuchengxi
"""

import pandas as pd
inputfile='E:\Data Analysis SVW\Data_Engine_with_Python-master\Data_Engine_with_Python-master\L1\car_data_analyze\car_complain_data.xlsx'
df=pd.read_excel(inputfile)

c_brand=df.groupby('brand')['id'].count()
print('品牌投诉总数---------------------------------------------------')
print(c_brand.sort_values(ascending=False))

print ('\n' )
print('车型投诉总数---------------------------------------------------')
c_model=df.groupby('car_model')['id'].count()
print(c_model.sort_values(ascending=False))


df1=df.groupby(['brand'],as_index=False)['id'].agg({'投诉总数':'count'})
df2=df.groupby(['brand'],as_index=False)['car_model'].agg({'车型总数':'nunique'})

df3=pd.merge(df1,df2,how='left',on='brand')
df3['平均车型投诉']=df3['投诉总数']/df3['车型总数']
data=df3.sort_values(ascending=False,by='平均车型投诉')

print ('\n' )
print('平均车型投诉数最多的品牌')
print(data.head(1))