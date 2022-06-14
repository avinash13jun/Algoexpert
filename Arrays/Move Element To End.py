# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:48:03 2022

@author: Avinash Kumar
"""

def moveElementToEnd(array, toMove):
    for i in range(len(array)):
        if array[i] == toMove:
            for j in range(i+1, len(array)):
                if array[j] != toMove:
                    array[i], array[j] = array[j], array[i]
                    break
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
res = moveElementToEnd(array, toMove)
print(res)