#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-19
Last_modify:    2016-02-19
******************************************
'''

'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):
            return False
        dp = [[False for _ in range(len(s)+1)] for __ in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            dp[i][0] = dp[i-1][0] and p[i-1] == '*'
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and \
                            (p[i-1] == s[j-1] or p[i-1] == '?')
        return dp[-1][-1]
