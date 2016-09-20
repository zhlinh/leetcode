#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-10
Last_modify:    2016-01-10
******************************************
'''

'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x
        r = 0
        if x < 0:
            return False
        while y != 0:
            r = r * 10 + y % 10
            y = y // 10
        return r == x
