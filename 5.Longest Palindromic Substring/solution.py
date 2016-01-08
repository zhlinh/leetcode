#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-07
Last_modify: 	2016-01-07
******************************************
'''

'''
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return None
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i-maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                maxLen = maxLen + 2
                start = i-maxLen-1
                continue
            if i-maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                maxLen = maxLen + 1
                start = i-maxLen
        return s[start:start+maxLen]
