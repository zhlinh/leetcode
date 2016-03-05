#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-05
Last_modify:    2016-03-05
******************************************
'''

'''
Given two binary trees,
write a function to check if they are equal or not.

Two binary trees are considered equal if they are
structurally identical and the nodes have the same value.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.inorder(p, q)

    def inorder(self, p, q):
        if not p or not q:
            return p == q
        if not self.inorder(p.left, q.left):
            return False
        if p.val != q.val:
            return False
        return self.inorder(p.right, q.right)
