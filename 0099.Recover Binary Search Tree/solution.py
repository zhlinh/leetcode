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
Two elements of a binary search tree (BST) are swapped by err.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        pre = None
        err = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre != None and cur.val <= pre.val:
                err.append(pre)
                err.append(cur)
            pre = cur
            cur = cur.right
        err[0].val, err[-1].val = err[-1].val, err[0].val
