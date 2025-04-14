# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 07:11:28 2022

@author: Avinash Kumar
"""

def findClosestValueInBst(tree, target):
    diff_main = abs(tree.value - target)
    return nearest(tree, target, tree.value, diff_main)
        
def nearest(tree, target, closest, diff):
    diff_main = abs(tree.value - target)
    if diff > diff_main:
        closest = tree.value
        diff = diff_main
    if tree.left is not None and target < tree.value:
        return nearest(tree.left, target, closest, diff)
    elif tree.right is not None and target > tree.value:
        return nearest(tree.right, target, closest, diff)
    else:
        return closest
    

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

target = 12
result = findClosestValueInBst(root, target)
print(result)