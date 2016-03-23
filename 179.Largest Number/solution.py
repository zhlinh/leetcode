#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-23
Last_modify:    2016-03-23
******************************************
'''

'''
Given a list of non negative integers,
arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9],
the largest formed number is 9534330.

Note: The result may be very large,
so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

from functools import cmp_to_key

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        strs = []
        for n in nums:
            strs.append(str(n))
        def myCmp(x, y):
            return (y + x) - int(x + y)
        strs.sort(key=cmp_to_key(myCmp))
        start = False
        res = ""
        for s in strs:
            if start or s != "0":
                start = True
                res += s
        return res or "0"
