#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-19
Last_modify:    2016-02-19
******************************************
'''

'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, results = [], []
        self.dfs(nums, result, results)
        return results

    def dfs(self, nums, result, results):
        if len(result) == len(nums):
            results.append(result)
            return
        for i in range(len(nums)):
            if nums[i] not in result:
                self.dfs(nums, result+[nums[i]], results)
