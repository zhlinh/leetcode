#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-25
Last_modify:    2016-02-25
******************************************
'''

'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        if i < 0:
            return b
        if j < 0:
            return a
        carry = 0
        sum_str = ""
        while i >= 0 or j >= 0 or carry:
            rem = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1') + carry
            carry = rem // 2
            rem %= 2
            sum_str = str(rem) + sum_str
            i -= 1
            j -= 1
        return sum_str
