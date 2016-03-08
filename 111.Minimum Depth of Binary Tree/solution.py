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
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along
the shortest path from the root node down to the nearest leaf node.
'''

#  Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        level = 0
        while q:
            width = len(q)
            level += 1
            for i in range(width):
                cur = q.pop(0)
                if not cur.left and not cur.right:
                    return level
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return level

