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
        na, nb = len(a), len(b)
        max_len = max(na, nb)
        carry = 0
        sum_str = ""
        for i in range(max_len):
            tmp = 0
            if na - 1 - i >= 0:
                tmp += int(a[na-1-i])
            if nb - 1 - i >= 0:
                tmp += int(b[nb-1-i])
            tmp += carry
            carry = tmp // 2
            sum_str = str(tmp % 2) + sum_str
        if carry:
            sum_str = "1" + sum_str
        return sum_str
