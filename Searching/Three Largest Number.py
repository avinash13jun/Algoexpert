# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 12:03:18 2022

@author: Avinash Kumar
"""

def findThreeLargestNumbers(array):
    res = [None, None, None]
    for num in array:
        if res[2] is None or num >= res[2]:
            adjustArray(2, num, res)
        elif res[1] is None or num >= res[1]:
            adjustArray(1, num, res)
        elif res[0] is None or num >= res[0]:
            adjustArray(0, num, res)
        else:
            continue
    return res

def adjustArray(pos, num, res):
    if res[pos] == None:
        res[pos] = num
        return
    
    prevNum = None
    for i in reversed(range(pos + 1)):
        if i == pos:
            prevNum = res[pos]
            res[pos] = num
            continue
        
        temp = res[i]
        res[i] = prevNum
        prevNum = temp 
        
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
res = findThreeLargestNumbers(array)
print(res)
        