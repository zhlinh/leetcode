#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-04
Last_modify:    2016-05-04
******************************************
'''

'''
Given an array of n integers where n > 1,
nums, return an array output such that output[i] is
equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for
the purpose of space complexity analysis.)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        tmp = 1
        for i in range(n):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in reversed(range(n)):
            res[i] *= tmp
            tmp *= nums[i]
        return res
