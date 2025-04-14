# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:11:05 2022

@author: Avinash Kumar
"""

def threeNumberSum(array, targetSum):
    array.sort()
    res = []
    for i in range(len(array) - 2):
        sIdx = i+1
        lIdx = len(array) - 1
        while lIdx > sIdx:
            value = array[i] + array[sIdx] + array[lIdx]
            if value > targetSum:
                lIdx-=1
            elif value < targetSum:
                sIdx+=1
            else:
                res.append([array[i], array[sIdx], array[lIdx]])
                sIdx+=1
                lIdx-=1
    return res

array = [12, 3, 1, 2, -6, 5, -8, 6]
#array = [-8, -6, 1, 2, 3, 5, 6, 12] --------
targetSum = 0
res = threeNumberSum(array, targetSum)
print(res)