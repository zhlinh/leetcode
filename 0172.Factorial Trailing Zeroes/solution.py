#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-22
Last_modify:    2016-03-22
******************************************
'''

'''
Given an integer n, return the number of trailing zeroes in "n!".

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 5
        res = 0
        while base <= n:
            res += n // base
            base *= 5
        return res
