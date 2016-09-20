#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-20
Last_modify:    2016-05-20
******************************************
'''

'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and math.pow(3, math.log(0x7fffffff) // math.log(3)) % n == 0
