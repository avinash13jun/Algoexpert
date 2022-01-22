# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 07:50:37 2022

@author: Avinash Kumar
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self



def branchSums(root):
    if root is not None:
        newArray = []
        branchArraySum(root, 0, newArray)
        return newArray
    return [0]

def branchArraySum(root, currentSum, newArray):
    if root is None:
        return
    
    newSum = currentSum + root.value
    if root.left is None and root.right is None:
        newArray.append(newSum)
        return
    
    branchArraySum(root.left, newSum, newArray)
    branchArraySum(root.right, newSum, newArray)
    

tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
result = branchSums(tree)
print(result)
