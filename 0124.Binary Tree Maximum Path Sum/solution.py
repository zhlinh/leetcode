#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-08
Last_modify:    2016-03-08
******************************************
'''

'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence
of nodes from some starting node to any node in the
tree along the parent-child connections.
The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    maxValue = 0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = -2 ** 31
        self.helper(root)
        return self.maxValue

    def helper(self, root):
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.maxValue = max(self.maxValue, left + right + root.val)
        return max(left, right) + root.val
