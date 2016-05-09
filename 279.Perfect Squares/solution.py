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

class Solution(object):
    dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        m = len(self.dp)
        while m <= n:
            cur = 2 ** 31 - 1
            i = 1
            while i * i <= m:
                cur = min(cur, self.dp[m-i*i] + 1)
                i += 1
            self.dp.append(cur)
            m += 1
        return self.dp[n]
