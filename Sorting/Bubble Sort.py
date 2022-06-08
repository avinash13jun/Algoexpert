# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:20:22 2022

@author: Avinash Kumar
"""

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array
                
                
                
def swap(sIdx, tIdx, array):
    temp = array[sIdx]
    array[sIdx] = array[tIdx]
    array[tIdx] = temp
    
array = [8, 5, 2, 9, 5, 6, 3]
res = bubbleSort(array)
print(res)
