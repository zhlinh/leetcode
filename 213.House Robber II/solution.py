#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-26
Last_modify:    2016-03-26
******************************************
'''

'''
Note: This is an extension of House Robber.

After robbing those houses on that street,
the thief has found himself a new place for his thievery
so that he will not get too much attention.
This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses remain
the same as for those in the previous street.

Given a list of non-negative integers representing the amount
of money of each house, determine the maximum amount of money
you can rob tonight without alerting the police.

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        a, b, c, d = 0, 0, 0, 0
        for i in range(n):
            if i > 0:
                if i % 2 == 1:
                    a = max(a + nums[i], b)
                else:
                    b = max(b + nums[i], a)
            if i < n - 1:
                if i % 2 == 1:
                    c = max(c + nums[i], d)
                else:
                    d = max(d + nums[i], c)
        return max(a, b, c, d)
