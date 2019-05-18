#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import pandas as pd

from pandas import Series, DataFrame


# x1 = Series([1, 2, 3, 4, "x1"])
# print(x1)
#
# x2 = Series(data=[11, 22, 33, 44], index=['a', 'b', 'c', 'd'])
# print(x2)

# d = pd.read_csv('data.txt')
# # print(d.dtypes)
#
# data = DataFrame(d)
#
# print(data)
# df2 = DataFrame(d)
# print(df2)

def power(x):
    return x * x


#
#
# data = {'Chinese': [66, 99, 93, 90, 80,95], 'English': [65, 85, 92, 88, 90,85], 'Math': [30, 98, 96, 77, 90,100]}
#
# df = DataFrame(data)
# print(df)
# df2 = DataFrame(data, index=["xumeng", "hanqing", "fuck", 'love', 'bibi', "x1"])
# print(df2)
# df2.to_csv('d.txt')
# df2 = df2.drop(columns=['English'],index=['fuck'])
# df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace = True)
# df2 = df2.drop_duplicates()
# df2['Chinese'].astype('str')
# df2['Chinese'] = df2['Chinese'].str.strip('x')
# print(df2)

# print(df2.columns)
# 全部大写
# df2.columns = df2.columns.str.upper()
# 全部小写
# df2.columns = df2.columns.str.lower()
# 首字母大写
# df2.columns = df2.columns.str.title()
# df2['Chinese'] = df2['Chinese'].apply(str.upper)
# print(df2.apply(power))

# print(df2.describe())

# print(df2.count())

# print(df2.idxmin())


# df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# df2 = DataFrame({'name':['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2':range(5)})
#
# # print(df1)
# # print(df2)
#
# # df3 = pd.merge(df1, df2, on="name")
# df3 = pd.merge(df1, df2, how='outer' )
# print(df3)

# from pandasql import sqldf, load_births, load_meat
# df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
# pysqldf = lambda sql: sqldf(sql, globals())
# sql = "select * from df1 where name ='ZhangFei'"
# print(pysqldf(sql))
def sum(df: DataFrame):
    df['总分'] = df["中文"] + df["英语"] + df["数学"]
    return df


df = DataFrame(pd.read_csv("data.txt"))

df.rename(columns={"Chinese": "中文", "English": "英语", "Math": "数学"}, inplace=True)
df = df.drop_duplicates()
print(df)
df = df.apply(sum, axis=1)
print("--------")
print(df)
