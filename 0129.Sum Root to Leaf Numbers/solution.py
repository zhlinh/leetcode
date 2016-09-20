#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-11
Last_modify:    2016-03-11
******************************************
'''

'''
Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3
which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    totalSum = 0
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, 0)
        return self.totalSum


    def helper(self, root, num):
        num = num * 10 + root.val
        if not root.left and not root.right:
            self.totalSum += num
            return
        if root.left:
            self.helper(root.left, num)
        if root.right:
            self.helper(root.right, num)
