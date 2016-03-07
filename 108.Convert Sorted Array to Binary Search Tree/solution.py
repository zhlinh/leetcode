#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-07
Last_modify:    2016-03-07
******************************************
'''

'''
Given an array where elements are sorted in
ascending order, convert it to a height balanced BST.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, start, end, nums):
        if start > end:
            return None
        index = (start + end) // 2
        root = TreeNode(nums[index])
        root.left = self.helper(start, index - 1, nums)
        root.right = self.helper(index + 1, end, nums)
        return root
