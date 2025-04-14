# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:54:00 2022

@author: Avinash Kumar
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
                
        return self

    def contains(self, value):
        if value < self.value:
            if self.left != None:
                return self.left.contains(value)
        elif value > self.value:
             if self.right != None:
                 return self.right.contains(value)
        else:
            return True;
                
        return False;

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
    
    def print(self, res = []):
        res.append(self.value)
        if self.left != None:
            self.left.print(res)
        if self.right != None:
            self.right.print(res)
        return res

root = BST(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(1)
root.insert(14)
root.insert(12)
print(root.print())
#root.remove(10)
result = root.contains(15)
print(result)
