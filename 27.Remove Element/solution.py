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
Given an array and a value,
remove all instances of that value in place and return the new length.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = -1, 0
        for r in range(len(nums)):
            if nums[r] != val:
                l += 1
                nums[l] = nums[r]
        return l + 1


