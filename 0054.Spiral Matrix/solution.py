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
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: steps_ist[steps_ist[int]]
        :rtype: steps_ist[int]
        """
        res = []
        nr = len(matrix)
        if nr == 0:
            return res
        nc = len(matrix[0])
        if nc == 0:
            return res
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step = [nc, nr]
        iDir, ir, ic = 0, 0, -1
        while step[iDir%2] > 0 :
            for _ in range(step[iDir%2]):
                ir += dirs[iDir][0]
                ic += dirs[iDir][1]
                res.append(matrix[ir][ic])
            iDir = (iDir + 1) % 4
            step[iDir%2] -= 1
        return res
