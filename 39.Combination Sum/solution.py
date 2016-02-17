#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-17
Last_modify:    2016-02-17
******************************************
'''

'''
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order.
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        result = []
        self.dfs(candidates, target, results, result, 0)
        return results

    def dfs(self, nums, target, results, result, index):
        #if target < 0:
        #    return
        if target == 0:
            results.append(result)
            return
        for i in range(index, len(nums)):
            # add here, for candidates sorted.
            if nums[i] > target:
                break
            self.dfs(nums, target - nums[i], results, result + [nums[i]], i)
