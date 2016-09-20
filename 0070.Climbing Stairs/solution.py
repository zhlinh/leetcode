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
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1, n2, nc = 1, 2, 0
        for i in range(3, n + 1):
            nc = n1 + n2
            n1, n2 = n2, nc
        return nc
