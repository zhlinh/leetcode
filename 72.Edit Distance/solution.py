#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-27
Last_modify:    2016-02-27
******************************************
'''

'''
Given two words word1 and word2,
find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1, n2 = len(word1), len(word2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        dp = [i for i in range(n2 + 1)]
        for i in range(1, n1 + 1):
            pre, dp[0] = i-1, i
            for j in range(1, len(word2) + 1):
                # important to save dp[j], so that pre = tmp = dp[i-1][j-1]
                # if dp[j] changed, it just could dp[i][j-1]
                tmp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = pre
                else:
                    # dp[j] means dp[i-1][j], dp[j-1] means dp[i][j-1],
                    # pre means dp[i-1][j-1]
                    dp[j] = min(dp[j-1], dp[j], pre) + 1
                pre = tmp
        return dp[n2]
