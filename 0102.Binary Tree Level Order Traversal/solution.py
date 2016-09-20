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
return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        self.helper(root, 0, results)
        return results

    def helper(self, node, depth, results):
        if not node:
            return
        if depth >= len(results):
            results.append([])
        results[depth] += [node.val]
        if node.left:
            self.helper(node.left, depth + 1, results)
        if node.right:
            self.helper(node.right, depth + 1, results)

