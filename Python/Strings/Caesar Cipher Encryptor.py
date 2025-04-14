# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:02:04 2022

@author: Avinash Kumar
"""


def caesarCipherEncryptor(string, key):
    key = key % 26
    encrypted = []
    for letter in string:
        encrypted.append(encryptedChar(letter, key))
    return "".join(encrypted)
        
def encryptedChar(letter, key):
    val = ord(letter)
    newVal = val + key
    if newVal <= 122:
        return chr(newVal)
    else:
        return chr(96 + (newVal % 122))
    
string = "xyz"
key = 2
res = caesarCipherEncryptor(string, key)
print(res)