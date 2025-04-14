# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:59:15 2022

@author: Avinash Kumar
"""

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while right > left:
        value = array[left] + array[right]
        if targetSum == value:
            return [array[left], array[right]]
        elif value > targetSum:
            right-=1
        else:
            left+=1
    return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
result = twoNumberSum(array, targetSum)
print(result)