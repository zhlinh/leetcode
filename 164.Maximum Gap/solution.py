#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-21
Last_modify:    2016-03-21
******************************************
'''

'''
Given an unsorted array,
find the maximum difference between
the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are
non-negative integers and fit in the 32-bit signed integer range.

Credits:
Special thanks to @porker2008 for adding
this problem and creating all test cases.
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        res = 0
        minNum = nums[0]
        maxNum = nums[0]
        for n in nums:
            minNum = min(minNum, n)
            maxNum = max(maxNum, n)
        gap = 1 + (maxNum - minNum - 1) // (length - 1)
        minValues = [2 ** 31 - 1] * (length - 1)
        maxValues = [-2 ** 31] * (length - 1)
        for n in nums:
            if n == minNum or n == maxNum:
                continue
            i = (n - minNum) // gap
            minValues[i] = min(minValues[i], n)
            maxValues[i] = max(maxValues[i], n)
        pre = minNum
        for i in range(length - 1):
            if minValues[i] == 2 ** 31 - 1 and maxValues[i] == -2 ** 31:
                continue
            res = max(res, minValues[i] - pre)
            pre = maxValues[i]
        res = max(res, maxNum - pre)
        return res
