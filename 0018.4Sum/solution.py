#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-18
Last_modify:    2016-01-18
******************************************
'''

'''
Given an array S of n integers, are there elements a, b, c, and d in S
such that a + b + c + d = target? Find all unique quadruplets in the array
which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order.
(ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rList = []
        nums.sort()
        self.findNum(nums, 0, target, 4, [], rList)
        return rList

    def findNum(self, nums, start, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        if nums[start] * N > target or nums[-1] * N < target:
            return
        if N == 2:
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    results.append(result + [nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    r -= 1
                    l += 1
        else:
            for i in range(start, len(nums) - N + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                self.findNum(nums, i + 1, target - nums[i], \
                        N - 1, result + [nums[i]], results)
