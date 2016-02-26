#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-26
Last_modify:    2016-02-26
******************************************
'''

'''
Implement int sqrt(int x).
Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x
        while n * n > x:
            n = (n + x // n) // 2
        return n
