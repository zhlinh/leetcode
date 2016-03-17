#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-16
Last_modify:    2016-03-16
******************************************
'''

'''
Given an array of integers,
every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x0, x1, mask = 0, 0, 0
        for n in nums:
            x1 ^= (x0 & n)
            x0 ^= n
            mask = ~(x0 & x1)
            x0 &= mask
            x1 &= mask
        return x0
