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
Given a binary tree,
return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next
level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q1 = [root]
        q2 = []
        levels = []
        while q1:
            level = []
            while q1:
                cur = q1.pop()
                level.append(cur.val)
                if cur.left:
                    q2.append(cur.left)
                if cur.right:
                    q2.append(cur.right)
            levels.append(level)
            level = []
            while q2:
                cur = q2.pop()
                level.append(cur.val)
                if cur.right:
                    q1.append(cur.right)
                if cur.left:
                    q1.append(cur.left)
            if level:
                levels.append(level)
        return levels
