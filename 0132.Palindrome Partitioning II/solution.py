#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-14
Last_modify:    2016-03-14
******************************************
'''

'''
Given a string s, partition s such that every substring
of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning
["aa","b"] could be produced using 1 cut.
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [i - 1 for i in range(n + 1)]
        for i in range(n):
            j = 0
            # odd palindrome
            while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j] + 1)
                j += 1
            j = 1
            # even palindrome
            while i - j + 1 >= 0 and i + j < n and s[i-j+1] == s[i+j]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j+1] + 1)
                j += 1
        return dp[n]

