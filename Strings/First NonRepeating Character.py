# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:00:23 2022

@author: Avinash Kumar
"""

def firstNonRepeatingCharacter(string):
    nonRepeat = nonRepeating(string)
    for i in range(len(string)):
        if string[i] in nonRepeat:
            return i
    return -1
    
def nonRepeating(string):
    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1
    
    nonRepeat = []
    for key, value in d.items():
        if value == 1:
            nonRepeat.append(key)
    return nonRepeat

string = "abcdcaf"
res = firstNonRepeatingCharacter(string)
print(res)