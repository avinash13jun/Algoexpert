# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 12:03:18 2022

@author: Avinash Kumar
"""

def getNthFib(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n - 1) + getNthFib(n - 2)
    
res = getNthFib(6)
print(res)