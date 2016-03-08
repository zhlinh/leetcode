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
Given a binary tree and a sum,
determine if the tree has a root-to-leaf path
such that adding up all the values along the
path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path
5->4->11->2 which sum is 22.
'''

#  Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = []
        cur = root
        pre = None
        cursum = 0
        while stack or cur:
            while cur:
                cursum += cur.val
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            if not cur.left and not cur.right and cursum == sum:
                return True
            if cur.right and pre != cur.right:
                cur = cur.right
            else:
                pre = cur
                stack.pop()
                cursum -= cur.val
                cur = None
        return False
