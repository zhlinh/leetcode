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
        if len(nums) < 4:
            return []
        nums.sort()
        for i in range(len(nums) - 3):
            f = nums[i]
            if i > 0 and f == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                s = nums[j]
                if j > i + 1 and s == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if f + s + nums[l] + nums[r] > target:
                        r -= 1
                    elif f + s + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        rList.append([f, s, nums[l], nums[r]])
                        while l < r and nums[l+1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        r -= 1
                        l += 1
        return rList
