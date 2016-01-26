#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-26
Last_modify:    2016-01-26
******************************************
'''

'''
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        rLen = 1
        for i in range(1, len(nums)):
            if nums[rLen] == nums[rLen-1]:
                nums.pop(rLen)
            else:
                rLen += 1
        return rLen
