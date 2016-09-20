#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-03
Last_modify:    2016-05-03
******************************************
'''

'''
Given an integer n, count the total number of digit 1
appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        m, res = 1, 0
        while m <= n:
            a, b = n // m, n % m
            res += ((a + 8) // 10) * m + (a % 10 == 1) * (b + 1)
            m *= 10
        return res

