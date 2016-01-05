#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-05
Last_modify: 	2016-01-05
******************************************
'''

'''
Given a string, find the length of the longest substring
without repeating characters.
For example, the longest substring without repeating letters
for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        max = 0
        #substr = None
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            d[s[i]] = i
            if (i - start + 1) > max:
                max = i - start + 1
                #若需要求解substr
                #substr = s[start:i+1]
        return max
