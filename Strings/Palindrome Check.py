# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:51:33 2022

@author: Avinash Kumar
"""

def isPalindrome(string):
    sIdx = 0
    lIdx = len(string) - 1
    while sIdx < lIdx:
        if string[sIdx] != string[lIdx]:
            return False
        sIdx += 1
        lIdx -= 1
    return True

string = "abcdcba"
res = isPalindrome(string)
print(res)