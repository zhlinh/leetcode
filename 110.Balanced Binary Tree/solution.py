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
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
'''

#  Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.helper(root.left) - self.helper(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def helper(self, root):
        if not root:
            return 0
        ld = self.helper(root.left)
        rd = self.helper(root.right)
        return 1 + max(ld, rd)
