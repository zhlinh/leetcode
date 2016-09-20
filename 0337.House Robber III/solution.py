#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-23
Last_modify:    2016-05-23
******************************************
'''

'''
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this
place forms a binary tree". It will automatically contact the police
if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight
without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        # res[0] means include, res[1] means exclude
        # and bottom - up
        return max(res[0], res[1])

    def helper(self, node):
        if not node:
            return [0] * 2
        left = self.helper(node.left)
        right = self.helper(node.right)
        # bottom - up
        return [node.val + left[1] + right[1],
                max(left[0], left[1]) + max(right[0], right[1])]

