#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-25
Last_modify:    2016-03-25
******************************************
'''

'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        minStart, minLen = 0, len(nums) + 1
        i = 0
        while i < len(nums):
            count += nums[i]
            while count >= s:
                minLen = min(minLen, i - minStart + 1)
                count -= nums[minStart]
                minStart += 1
            i += 1
        return 0 if minLen == len(nums) + 1 else minLen
