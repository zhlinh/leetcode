#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

**Each number in C may only be used once in the combination.**

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order.
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        result = []
        candidates.sort()
        self.dfs(candidates, target, results, result, 0)
        return results

    def dfs(self, nums, target, results, result, index):
        if target == 0:
            results.append(result)
            return
        i = index
        while i < len(nums):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], results, result+[nums[i]], i+1)
            # avoid duplicate, this depth is already got the same value
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
