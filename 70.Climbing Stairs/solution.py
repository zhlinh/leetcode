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
        maxN2 = n // 2
        res = 1
        for n2 in range(1, maxN2 + 1):
            tmp = 1
            n1 = n - 2 * n2
            m = n1 + n2
            k = min(n1, n2)
            for j in range(1, k + 1):
                tmp = tmp * (m - j + 1) // j
            res += tmp
        return res
