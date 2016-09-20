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
Given a binary tree,
check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        l = root.left
        r = root.right
        while stack or (l and r):
            while l and r:
                if l.val != r.val:
                    return False
                stack.append(r)
                stack.append(l)
                l = l.left
                r = r.right
            if l != r:
                return False
            l = stack.pop()
            r = stack.pop()
            l = l.right
            r = r.left
        return l == r
