#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-16
Last_modify:    2016-02-16
******************************************
'''

'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()",
which has length = 2.

Another example is ")()())",
where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for x in range(len(s))]
        cmax = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                # case 1: ()()()
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                # case 2: ((()))
                elif i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(' and dp[i-1] > 0:
                    dp[i] = 2 + dp[i-1] + dp[i-2-dp[i-1]]
                cmax = max(dp[i], cmax)
        return cmax


