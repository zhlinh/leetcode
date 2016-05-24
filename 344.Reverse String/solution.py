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
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        strBuilder = []
        for i in reversed(range(len(s))):
            strBuilder.append(s[i])
        return ''.join(strBuilder)
