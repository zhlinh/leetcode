#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-17
Last_modify:    2016-05-17
******************************************
'''

'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of
smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

Subscribe to see which companies asked this question
'''

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        if n < 1:
            return res
        padding = min(nums)
        for i in range(len(nums)):
            # let all the nums[i] >= 0
            nums[i] = nums[i] - padding + 1
        clen = max(nums)
        self.c = [0] * (clen + 1)
        for i in reversed(range(n)):
            res.append(self.getSum(nums[i] - 1))
            self.update(nums[i], 1)
        return res[::-1]

    def update(self, k, val):
        while k < len(self.c):
            self.c[k] += val
            k += (k & -k)

    def getSum(self, k):
        ret = 0
        while k > 0:
            ret += self.c[k]
            k -= (k & -k)
        return ret

