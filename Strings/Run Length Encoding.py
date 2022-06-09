# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:23:08 2022

@author: Avinash Kumar
"""

def runLengthEncoding(string):
    counter = 1
    encoded = ""
    for i in range(len(string)):
        if i == len(string) - 1:
            encoded += str(counter) + string[i]
            continue
        if string[i] == string[i+1]:
            if counter == 9:
                encoded += str(counter) + string[i]
                counter = 1
            else:
                counter += 1
        else:
            encoded += str(counter) + string[i]
            counter = 1
    return encoded
            
        

string = "AAAAAAAAAAAAABBCCCCDD"
res = runLengthEncoding(string)
print(res)