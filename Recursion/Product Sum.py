# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 12:03:18 2022

@author: Avinash Kumar
"""

def productSum(array, level = 1):
    sumVal = 0
    for elem in array:
        if type(elem) is list:
            sumVal += (level + 1) * productSum(elem, level + 1)
        else:
            sumVal += elem
    return sumVal

test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
res = productSum(test)
print(res)