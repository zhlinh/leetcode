#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-11
Last_modify:    2016-03-11
******************************************
'''

'''
Given a string s, partition s such that every substring
of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = []
        n = len(s)
        results = []
        for i in range(n):
            tmp = [i]
            for j in range(i + 1, n):
                if self.isPalindrome(s[i:j+1]):
                    tmp.append(j)
            dp.append(tmp)
        self.dfs(s, n, dp, 0, [], results)
        return results

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True

    def dfs(self, s, n, dp, start, result, results):
        if start >= n:
            results.append(result)
            return
        for i in dp[start]:
            self.dfs(s, n, dp, i + 1, result + [s[start:i+1]], results)
