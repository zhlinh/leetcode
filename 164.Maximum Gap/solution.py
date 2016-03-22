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
        maxNum = nums[0]
        for n in nums:
            maxNum = max(maxNum, n)
        exp = 1  # exp can be 1, 10, 100...
        sortedNums = [0] * length
        while maxNum // exp > 0:
            countDit = [0] * 10 # count quantity of 0~9
            for n in nums:
                countDit[(n//exp)%10] += 1
            for i in range(1, 10):
                countDit[i] += countDit[i-1]
            for i in reversed(range(length)):
                countDit[(nums[i]//exp)%10] -= 1
                index = countDit[(nums[i]//exp)%10]
                sortedNums[index] = nums[i]
            for i in range(length):
                nums[i] = sortedNums[i]
            exp *= 10
        for i in range(1, length):
            res = max(res, sortedNums[i] - sortedNums[i-1])
        return res
