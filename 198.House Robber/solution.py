#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-24
Last_modify:    2016-03-24
******************************************
'''

'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount
of money of each house, determine the maximum amount of money you
can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
Also thanks to @ts for adding additional test cases.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        for i in range(n):
            if i < 2:
                dp[i+1] = nums[i]
            else:
                dp[i+1] = max(dp[i-1], dp[i-2]) + nums[i]
        return max(dp[n], dp[n-1])
