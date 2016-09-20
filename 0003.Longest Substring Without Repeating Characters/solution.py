#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-05
Last_modify:    2016-01-05
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
        chList = [-1] * 256
        maxLen = 0
        start = 0
        for i in range(len(s)):
            asc = ord(s[i])
            if chList[asc] !=-1 and chList[asc] >= start:
                if (i - start) > maxLen:
                    maxLen = i - start
                start = chList[asc] + 1
            chList[asc] = i
        return max(maxLen, len(s)-start)
