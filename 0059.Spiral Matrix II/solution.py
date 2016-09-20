#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-22
Last_modify:    2016-02-22
******************************************
'''

'''
Given an integer n, generate a square matrix
filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for __ in range(n)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step = [n, n]
        iDir = 0
        ir, ic = 0, -1
        k = 0
        while k < n * n:
            for _ in range(step[iDir%2]):
                ir += dirs[iDir][0]
                ic += dirs[iDir][1]
                k += 1
                res[ir][ic] = k
            iDir = (iDir+1) % 4
            step[iDir%2] -= 1
        return res
