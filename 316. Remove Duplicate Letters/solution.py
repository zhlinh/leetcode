#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-18
Last_modify:    2016-05-18
******************************************
'''

'''
Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order
among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        count = [0] * 26
        pos = 0
        for c in s:
            count[ord(c) - ord('a')] += 1
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            index = ord(s[i]) - ord('a')
            count[index] -= 1
            if count[index] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))

