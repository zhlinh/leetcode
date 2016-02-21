#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-20
Last_modify:    2016-02-20
******************************************
'''

'''
Implement pow(x, n).
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0:
            x = 1.0 / x
            n = -(n + 1)
            res = res * x
        while n > 0:
            if n & 1 == 1:
                res = res * x
            x *= x
            n >>= 1
        return res
