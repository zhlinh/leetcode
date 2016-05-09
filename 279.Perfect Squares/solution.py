#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-09
Last_modify:    2016-05-09
******************************************
'''

'''
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem
and creating all test cases.
'''

import math

class Solution(object):
    dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.isSquare(n):
            return 1
        # if it's the form of (4^a)*(8b+7), return 4
        # n % 4 == 0
        while n & 3 == 0:
            # n = n // 4
            n >>= 2
        # n % 8 == 7
        if n & 7 == 7:
            return 4
        m = int(math.sqrt(n))
        for i in range(1, m + 1):
            if self.isSquare(n - i * i):
                return 2
        return 3

    def isSquare(self, n):
        m = int(math.sqrt(n))
        return m * m == n
