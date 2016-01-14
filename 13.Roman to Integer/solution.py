#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-14
Last_modify: 	2016-01-14
******************************************
'''

'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rint = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                rint -= d[s[i]]
            else:
                rint += d[s[i]]
        rint += d[s[-1]]
        return rint
