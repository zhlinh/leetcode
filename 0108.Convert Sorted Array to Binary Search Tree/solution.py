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
        if not nums:
            return None
        root = TreeNode(0)
        stack = [root]
        leftStack = [0]
        rightStack = [len(nums) - 1]
        while stack:
            cur = stack.pop()
            l = leftStack.pop()
            r = rightStack.pop()
            mid = l + (r - l) // 2
            cur.val = nums[mid]
            if l <= mid - 1:
                cur.left = TreeNode(0)
                stack.append(cur.left)
                leftStack.append(l)
                rightStack.append(mid - 1)
            if mid + 1 <= r:
                cur.right = TreeNode(0)
                stack.append(cur.right)
                leftStack.append(mid + 1)
                rightStack.append(r)
        return root
