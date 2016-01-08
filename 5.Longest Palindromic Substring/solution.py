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
        ll = lmax = len(s)
        substr = None
        while lmax > 0:
            offset = 0
            while (lmax + offset) <= ll:
                substr = s[offset:(lmax+offset)]
                if substr == substr[::-1]:
                    return substr
                else:
                    offset = offset + 1
            lmax = lmax - 1
