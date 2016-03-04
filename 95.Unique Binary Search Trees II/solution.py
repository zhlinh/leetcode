#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-03
Last_modify:    2016-03-03
******************************************
'''

'''
Given n, generate all structurally unique
BST's (binary search trees) that store values 1...n.

For example,
Given n = 3,
your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means?
read more on how binary tree is serialized on OJ.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        dp = []
        dp.append([None])
        for i in range(1, n + 1):
            trees = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for lnode in left:
                    for rnode in right:
                        root = TreeNode(j + 1)
                        root.left = lnode
                        root.right = self.cloneAfterAddNum(rnode, j + 1)
                        trees.append(root)
            dp.append(trees)
        return dp[n]

    def cloneAfterAddNum(self, node, offset):
        if not node:
            return None
        newNode = TreeNode(node.val + offset)
        newNode.left = self.cloneAfterAddNum(node.left, offset)
        newNode.right = self.cloneAfterAddNum(node.right, offset)
        return newNode
