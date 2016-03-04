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
        trees = self.helper(1, n)
        return trees

    def helper(self, start, end):
        trees = []
        if start > end:
            trees.append(None)
            return trees
        if start == end:
            trees.append(TreeNode(start))
            return trees
        left = []
        right = []
        for i in range(start, end + 1):
            left = self.helper(start, i - 1)
            right = self.helper(i + 1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    trees.append(root)
        return trees
