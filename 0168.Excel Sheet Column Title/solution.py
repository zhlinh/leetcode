#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-22
Last_modify:    2016-03-22
******************************************
'''

'''
Given a positive integer,
return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n != 0:
            n -= 1
            rem = n % 26
            n //= 26
            res = chr(ord('A') + rem) + res
        return res
