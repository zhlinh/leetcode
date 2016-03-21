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
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums) + 1)]
        res = -2 ** 31
        count, start = 0, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                count, start = 0, -1
                res = max(res, 0)
                continue
            if nums[i] < 0:
                count += 1
                if start == -1:
                    start = i + 1
            dp[i+1] = dp[i] * nums[i]
            if count % 2 == 1 and start != i + 1 and start != -1:
                res = max(res, dp[i+1]//dp[start])
            else:
                res = max(res, dp[i+1])
        return res
