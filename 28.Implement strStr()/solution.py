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
        j = 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 1
                while i + j < len(haystack) and j < len(needle):
                    if haystack[i+j] != needle[j]:
                        break
                    j += 1
            if j == len(needle):
                return i
        return -1
