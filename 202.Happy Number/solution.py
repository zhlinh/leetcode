#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-24
Last_modify:    2016-03-24
******************************************
'''

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and
creating all test cases.
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        magic = 4
        while True:
            m = 0
            while n != 0:
                m += (n % 10) ** 2
                n //= 10
            n = m
            if n == 1:
                return True
            if n == magic:
                return False
