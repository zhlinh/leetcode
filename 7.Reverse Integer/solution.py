#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-09
Last_modify: 	2016-01-09
******************************************
'''

'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 1 if x >=0 else -1
        x = abs(x)
        rs, num = 0, 0
        while x != 0:
            num = x % 10
            x = x // 10
            rs = rs * 10 + num
        return s * rs * (rs < 2 ** 31)
