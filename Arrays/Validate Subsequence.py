# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:05:31 2022

@author: Avinash Kumar
"""

def isValidSubsequence(array, sequence):
    seqCheck = 0
    lenSeq = len(sequence)
    for value in array:
        if seqCheck == lenSeq:
            break
        if sequence[seqCheck] == value:
            seqCheck += 1
    return seqCheck == lenSeq

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
result = isValidSubsequence(array, sequence)
print(result)