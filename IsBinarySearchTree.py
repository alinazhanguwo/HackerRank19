# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def isBST(root, value_min, value_max):
    if root==None:
        return True
    elif root.data>value_min and root.data<value_max:
        return isBST(root.left, value_min, root.data) and isBST(root.right, root.data, value_max)
    else:
        return False

def checkBST(root):
    return isBST(root, float('-inf'), float('inf'))
