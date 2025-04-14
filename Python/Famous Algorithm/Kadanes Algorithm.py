# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:20:25 2022

@author: Avinash Kumar
"""

def kadanesAlgorithm(array):
    totalSum = array[0]
    currentSum = array[0]
    for i in range(1, len(array)):
        currentSum = max(array[i], currentSum + array[i])
        totalSum = max(totalSum, currentSum)
    return totalSum

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
res = kadanesAlgorithm(array)
print(res)