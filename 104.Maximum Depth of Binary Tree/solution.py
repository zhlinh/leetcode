#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-06
Last_modify:    2016-03-06
******************************************
'''

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxdepth = [1]
        self.dfs(root, 1, maxdepth)
        return maxdepth[0]

    def dfs(self, node, depth, maxdepth):
        if depth > maxdepth[0]:
            maxdepth[0] = depth
        if node.left:
            self.dfs(node.left, depth + 1, maxdepth)
        if node.right:
            self.dfs(node.right, depth + 1, maxdepth)
