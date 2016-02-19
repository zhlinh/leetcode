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
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(0, nums, results)
        return results

    def dfs(self, start, nums, results):
        if start >= len(nums) - 1:
            results.append(nums[:])
            return
        dic = {}
        for i in range(start, len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
                nums[start], nums[i] = nums[i], nums[start]
                self.dfs(start + 1, nums, results)
                nums[start], nums[i] = nums[i], nums[start]
