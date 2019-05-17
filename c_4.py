#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# 01
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b[1, 1] = 10
# print(a.shape)
# print(b.shape)
# print(a.dtype)
# print("a = ", a)
# print("b = ", b)
#
# print(a.size)
# print(b.size)

# 02

# person_type = np.dtype({"names": ["name", "age", "chinese", "math", "english"],
#                         "formats": ['S32', 'i', 'i', 'i', 'f']})
#
# persons = np.array([("ZhangFei", 32, 75, 100, 90), ("GuanYu", 24, 85, 96, 88.5),
#                     ("ZhaoYun", 28, 85, 92, 96.5), ("HuangZhong", 29, 65, 85, 100)],
#                    dtype=person_type)
#
# chinese = persons[:]['chinese']
# ages = persons[:]['age']
# math = persons[:]['math']
# english = persons[:]['english']
#
# print("ages = ", ages)
# print("chinese = ", chinese)
# print("math = ", math)
# print("english = ", english)
# print(np.mean(ages))
# print(np.mean(chinese))
# print(np.mean(math))
# print(np.mean(english))


# 03
# x1 = np.arange(0, 11, 2)
# print(x1)
#
# x2 = np.linspace(0, 9, 6)
# print(x2)
#
# x3 = np.mod(x2, x1)
# print('x3 = ', x3)

# 04

b = np.array([[1, 2, 30], [4, 5, 6], [7, 8, 9]])

# print(np.amin(b))
# print(np.amin(b, 1))


# print(np.ptp(b))
# print(np.ptp(b, 1))


print(np.percentile(b, 20))
