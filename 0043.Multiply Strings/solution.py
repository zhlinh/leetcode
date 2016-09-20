#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-18
Last_modify:    2016-02-18
******************************************
'''

'''
Given two numbers represented as strings,
return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        prod = [0 for _ in range(len(num1) + len(num2))]
        m, n = len(num1) - 1, len(num2) - 1
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                num = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                num += prod[p2]
                prod[p1] += num // 10
                prod[p2] = num % 10
        res = ''
        for x in prod:
            if len(res) != 0 or x != 0:
                res += chr(x + ord('0'))
        return "0" if len(res) == 0 else res
