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
        i, j = 0, x + 1
        while i < j:
            mid = (i + j) // 2
            if mid * mid > x:
                j = mid
            else:
                i = mid + 1
        return i - 1
