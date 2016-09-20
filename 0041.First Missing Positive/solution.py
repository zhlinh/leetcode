#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-18
Last_modify:    2016-02-18
******************************************
'''

'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i]-1 < len(nums) and \
                    nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
        i = 0
        while i < len(nums) and nums[i]-1 == i:
            i += 1
        return i + 1
