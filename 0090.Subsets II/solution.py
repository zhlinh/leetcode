#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-02
Last_modify:    2016-03-02
******************************************
'''

'''
Given a collection of integers that might contain duplicates,
nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        start = 0
        for i in range(len(nums)):
            start = length if i > 0 and nums[i] == nums[i-1] else 0
            length = len(res)
            for j in range(start, length):
                res.append(res[j] + [nums[i]])
        return res
