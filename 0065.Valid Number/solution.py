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
        state = [{'b':0, 's':1, 'd':2, '.':3},
                 {'d':2, '.':3},
                 {'d':2, '.':4, 'e':5, 'b':8},
                 {'d':4},
                 {'d':4, 'e':5, 'b':8},
                 {'s':6, 'd':7},
                 {'d':7},
                 {'d':7, 'b':8},
                 {'b':8} ]
        curState = 0
        for c in s:
            if c >= '0' and c <= '9':
                c = 'd'
            if c == '+' or c == '-':
                c = 's'
            if c == ' ':
                c = 'b'
            if c not in state[curState]:
                return False
            curState = state[curState][c]
        if curState not in [2, 4, 7, 8]:
            return False
        return True
