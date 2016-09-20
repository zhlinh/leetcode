#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-03
Last_modify:    2016-05-03
******************************************
'''

'''
Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for
adding this problem and creating all test cases.
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return  (n & (n - 1)) == 0
