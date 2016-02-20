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
        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / (x * self.myPow(x, -(n+1)))
        elif n % 2:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)
