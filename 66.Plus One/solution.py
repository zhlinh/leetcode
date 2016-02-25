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
Given a non-negative number represented as an array of digits,
plus one to the number.

The digits are stored such that the most significant digit
is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        digits[i] += 1
        carry = digits[i] // 10
        digits[i] %= 10
        while i > 0 and carry:
            i -= 1
            digits[i] = digits[i] + carry
            carry = digits[i] // 10
            digits[i] %= 10
        if i == 0 and carry:
            digits.insert(0, carry)
        return digits
