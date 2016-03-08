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
find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

#  Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.helper(root, sum, [], results)
        return results

    def helper(self, root, sum, result, results):
        if not root:
            return
        if not root.left and not root.right:
            if sum == root.val:
                results.append(result + [root.val])
            return
        if root.left:
            self.helper(root.left, sum - root.val, result + [root.val], results)
        if root.right:
            self.helper(root.right, sum - root.val, result + [root.val], results)
