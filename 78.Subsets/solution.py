#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-29
Last_modify:    2016-02-29
******************************************
'''

'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, results = [], [[]]
        nums.sort()
        self.dfs(nums, 0, result, results)
        return results

    def dfs(self, nums, start, result, results):
        if start > len(nums) - 1:
            return
        for i in range(start, len(nums)):
            results.append(result + [nums[i]])
            self.dfs(nums, i + 1, result + [nums[i]], results)
