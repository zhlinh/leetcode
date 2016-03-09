#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-09
Last_modify:    2016-03-09
******************************************
'''

'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0 for _ in range(rowIndex + 1)]
        res[0] = 1
        for n in range(1, rowIndex + 2):
            pre = 0
            for i in range(n):
                tmp = res[i]
                res[i] += pre
                pre = tmp
        return res
