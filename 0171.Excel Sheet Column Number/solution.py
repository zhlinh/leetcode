#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-22
Last_modify:    2016-03-22
******************************************
'''

'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet,
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for ch in s:
            n = ord(ch) - ord('A') + 1
            res = res * 26 + n
        return res
