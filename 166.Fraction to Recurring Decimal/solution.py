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
Given two integers representing the numerator
and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge.
Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious.
Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as
you can think of and test your code thoroughly.
Credits:
Special thanks to @Shangrila for adding this problem
and creating all test cases.
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = []
        if numerator == 0:
            return "0"
        sign = (numerator > 0) ^ (denominator > 0)
        if sign:
            res.append('-')
        n = abs(numerator)
        d = abs(denominator)
        res.append(str(n // d))
        n %= d
        if n == 0:
            return ''.join(res)
        res.append('.')
        dic = {}
        while n != 0:
            if n in dic:
                res.insert(dic[n], '(')
                res.append(')')
                break
            dic[n] = len(res)
            n *= 10
            res.append(str(n // d))
            n %= d
        return ''.join(res)
