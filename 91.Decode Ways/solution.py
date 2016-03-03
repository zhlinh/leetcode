#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-02
Last_modify:    2016-03-02
******************************************
'''

'''
A message containing letters from A-Z is
being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits,
determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s) + 2)]
        dp[0], dp[1] = 1, 2
        start = 2
        i = 0
        res = 1
        while i < len(s):
            count = 0
            if i > 0 and s[i] == '0' and s[i-1] not in ['1', '2']:
                return 0
            while i < len(s) and (s[i] == '1' or s[i] == '2'):
                count += 1
                i += 1
            if i < len(s) and s[i] == '0':
                count -= 2
            if i == len(s) or (i > 0 and s[i-1] == '2' and s[i] in ['7', '8', '9']):
                count -= 1
            if count > 0:
                res *= self.dpHelper(dp, count, start)
            i += 1
        return res

    def dpHelper(self, dp, n, start):
        if n < start:
            return dp[n]
        for i in range(start, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        start = n
        return dp[n]
