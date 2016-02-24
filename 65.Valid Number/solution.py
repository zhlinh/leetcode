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
        s = s.strip()
        numberSeen, dotSeen, eSeen, numberAfterE = False, False, False, False
        for i in range(len(s)):
            c = s[i]
            if c <= '9' and c >= '0':
                numberSeen = True
                numberAfterE = True
            elif c == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif c == 'e':
                if eSeen or (not numberSeen):
                    return False
                eSeen = True
                numberAfterE = False
            elif c == '+' or c == '-':
                if i != 0 and s[i-1] != 'e':
                    return False
            else:
                return False
        return numberSeen and numberAfterE
