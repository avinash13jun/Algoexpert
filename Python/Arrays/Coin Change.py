# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 06:36:14 2022

@author: Avinash Kumar
"""

def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1
    
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    
    return change + 1
        
        

coins = [5, 7, 1, 1, 2, 3, 22]
result = nonConstructibleChange(coins)
print(result)