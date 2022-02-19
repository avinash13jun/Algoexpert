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
        
def nodeDepths(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    nodeSum = getNodeSum(root, 0, 0)
    return nodeSum

def getNodeSum(root, nodeSum, nodeLevel):
    if root.left is not None:
        nodeSum = getNodeSum(root.left, nodeSum, nodeLevel + 1)
    if root.right is not None:
        nodeSum = getNodeSum(root.right, nodeSum, nodeLevel + 1)
        
    return nodeSum + nodeLevel

root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

result = nodeDepths(root)
print(result)
    