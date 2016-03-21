#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-20
Last_modify:    2016-03-20
******************************************
'''

'''
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        pMax, nMax = 0, 0
        res = 0
        for n in nums:
            if n < 0:
                pMax, nMax = nMax, pMax
            pMax = max(pMax * n, n)
            nMax = min(nMax * n, n)
            res = max(res, pMax)
        return res
