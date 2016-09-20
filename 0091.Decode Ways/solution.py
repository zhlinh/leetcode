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
        dp0, dp1 = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                dp1 = 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6' ):
                dp1 = dp0 + dp1
                dp0 = dp1 - dp0
            else:
                dp0 = dp1
        return dp1
