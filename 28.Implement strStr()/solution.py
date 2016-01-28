#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-26
Last_modify:    2016-01-26
******************************************
'''

'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        # prefix for next[]
        while j < n - 1:
            if i == -1 or needle[j] == needle[i]:
                i += 1
                j += 1
                next[j] = i
            else:
                i = next[i]
        # start checking
        i = j = 0
        while i < m and j < n:
            if j == -1 or needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1
