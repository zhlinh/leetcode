#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-26
Last_modify:    2016-03-26
******************************************
'''

'''
Given a string S, you are allowed to convert it to a palindrome
by adding characters in front of it.
Find and return the shortest palindrome you can find by performing
this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

Credits:
Special thanks to @ifanchu for adding this problem and creating
all test cases. Thanks to @Freezen for additional test cases.
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        rev_s = s[::-1]
        kmp_s = s + "#" + rev_s
        i, j = 0, -1
        next = [-1] * len(kmp_s)
        while i < len(kmp_s) - 1:
            if j == -1 or kmp_s[j] == kmp_s[i]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return rev_s[:n - (next[-1]+1)] + s
