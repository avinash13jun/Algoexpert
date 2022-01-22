# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 06:21:15 2022

@author: Avinash Kumar
"""

def sortedSquaredArray(array):
    newArray = []
    for x in array:
        newArray.append(x * x)
    newArray.sort()
    return newArray

array = [1, 2, 3, 5, 6, 8, 9]
result = sortedSquaredArray(array)
print(result)