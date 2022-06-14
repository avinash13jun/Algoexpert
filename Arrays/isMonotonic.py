# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:02:41 2022

@author: Avinash Kumar
"""

"""
def isMonotonic(array):
    if len(array) <= 1:
        return True
    
    dec = True
    
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            dec = False
            break
        elif array[i] < array[i - 1]:
            dec = True
            break
        else:
            continue
            
    trend = dec
    
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            dec = False
        elif array[i] < array[i - 1]:
            dec = True
        else:
            continue
        
        if dec != trend:
            return False
    return True
"""

def isMonotonic(array):
    dec = 0
    inc = 0
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            dec+=1
        elif array[i] < array[i+1]:
            inc+=1
        else:
            continue
        
        if inc > 0 and dec > 0:
            return False
    return True


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
res = isMonotonic(array)
print(res)