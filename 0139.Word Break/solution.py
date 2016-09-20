#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-17
Last_modify:    2016-03-17
******************************************
'''

'''
Given a string s and a dictionary of words dict,
determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s)):
            for word in wordDict:
                n = len(word)
                if dp[i] and s[i:i+n] == word:
                    dp[i+n] = True
        return dp[-1]
