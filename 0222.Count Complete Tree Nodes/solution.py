#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-04-11
Last_modify:    2016-04-11
******************************************
'''

'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left
as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''
# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        if h < 0:
            return 0
        elif self.height(root.right) == h - 1:
            return (1 << h) + self.countNodes(root.right)
        else:
            return (1 << (h - 1)) + self.countNodes(root.left)

    def height(self, root):
        return -1 if root == None else 1 + self.height(root.left)
