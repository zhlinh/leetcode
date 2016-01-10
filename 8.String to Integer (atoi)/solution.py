#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-10
Last_modify: 	2016-01-10
******************************************
'''

'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and
ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely
(ie, no given input specs).
You are responsible to gather all the input requirements up front.
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        min, max = ord('0'), ord('9')
        outi = 0
        s = 1
        start = 0
        for i in range(len(str)):
            if i == start:
                if str[i] == ' ':
                    start += 1
                    continue
                if str[i] == '+':
                    continue
                if str[i] == '-':
                    s = -1
                    continue
            num = ord(str[i])
            if num >= min and num <= max:
                num = num - min
                outi = outi * 10 + num
            else:
                break
        if outi >= 2 ** 31:
            if s == 1:
                outi = 2 ** 31 - 1
            else:
                outi = 2 ** 31
        return s * outi
