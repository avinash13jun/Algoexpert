# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:01:00 2022

@author: Avinash Kumar
"""

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    res = []
    left1 = 0
    left2 = 0
    least = float('inf')
    while left1 < len(arrayOne) and left2 < len(arrayTwo):
        diff = absDiff(arrayOne[left1], arrayTwo[left2])
        if diff < least:
            least = diff
            res = [arrayOne[left1], arrayTwo[left2]]
            
        if arrayOne[left1] >= arrayTwo[left2]:
            left2+=1
        else:
            left1+=1
    return res
        
    
def absDiff(num1, num2):
    return abs(num1 - num2)

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
res = smallestDifference(arrayOne, arrayTwo)
print(res)