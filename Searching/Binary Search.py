# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 12:03:18 2022

@author: Avinash Kumar
"""
import math

def binarySearch(array, target):
    array.sort()
    sIdx = 0
    lIdx = len(array) - 1
    mid = math.floor(len(array) / 2)
    while sIdx <= lIdx:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            lIdx = mid - 1
            mid = math.floor((sIdx + lIdx) / 2)
        else:
            sIdx = mid + 1
            mid = math.floor((sIdx + lIdx) / 2)
    return -1
    
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
res = binarySearch(array, target)
print(res)