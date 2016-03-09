#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-09
Last_modify:    2016-03-09
******************************************
'''

'''
Given a string S and a string T,
count the number of distinct subsequences of T in S.
[How many distinct subsequences in S that are equal to T]

A subsequence of a string is a new string which is
formed from the original string by deleting some(can be none)
of the characters without disturbing the relative positions
of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

ra*bbit=T
rab*bit=T
ra*bbit=T
so there're totally 3.

'''

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t), len(s)
        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(m)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
