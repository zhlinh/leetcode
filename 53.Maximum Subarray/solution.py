#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-22
Last_modify:    2016-02-22
******************************************
'''

'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        res = dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            res = max(res, dp[i])
        return res
