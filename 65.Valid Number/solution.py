#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-24
Last_modify:    2016-02-24
******************************************
'''

'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            i += 1
        n_dot, n_num = 0, 0
        while i < len(s) and ((s[i] >= '0' and s[i] <= '9') or s[i] == '.'):
            if s[i] == '.':
                n_dot += 1
            else:
                n_num += 1
            i += 1
        if n_dot > 1 or n_num < 1:
            return False
        if i < len(s) and s[i] == 'e':
            i += 1
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            n_num = 0
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                i += 1
                n_num += 1
            if n_num < 1:
                return False
        while i < len(s) and s[i] == ' ':
            i += 1
        return i == len(s)

