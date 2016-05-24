#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-24
Last_modify:    2016-05-24
******************************************
'''

'''
Write a function that takes a string as input and reverse
only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        strBuilder = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, n - 1
        while i <= j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            strBuilder[i] = s[j]
            strBuilder[j] = s[i]
            i += 1
            j -= 1
        return ''.join(strBuilder)
