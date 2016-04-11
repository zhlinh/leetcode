#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-04-11
Last_modify:    2016-04-11
******************************************
'''

'''
Given an array of integers, find out whether there are two distinct
indices i and j in the array such that the difference between
nums[i] and nums[j] is at most t and the difference between
i and j is at most k.
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        n = len(nums)
        dic = {}
        for i in range(n):
            if i > k:
                del dic[nums[i-k-1]//(t + 1)]
            m = nums[i] // (t + 1)
            if m in dic:
                return True
            if m - 1 in dic and abs(dic[m-1] - nums[i]) <= t:
                return True
            if m + 1 in dic and abs(dic[m+1] - nums[i]) <= t:
                return True
            dic[m] = nums[i]
        return False

