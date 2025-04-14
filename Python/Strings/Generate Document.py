# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:05:29 2022

@author: Avinash Kumar
"""

def generateDocument(characters, document):
    if document == "":
        return True;
    
    characters = count(characters)
    document = count(document)
    
    for key, value in document.items():
        if characters.get(key, 0) < value:
            return False;
    return True;

def count(string):
    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1
    return d

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
res = generateDocument(characters, document)
print(res)