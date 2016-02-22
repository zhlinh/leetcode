#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhsteps_inh
Email:          zhsteps_inhng@gmail.com
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
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        res = [0 for _ in range(m*n)]
        i, j, k = 0, -1, 0
        dir_i, dir_j = 1, 1
        steps_i, steps_j = m, n
        while k < m * n:
            if dir_i * dir_j == 1:
                for _ in range(steps_j):
                    j += dir_j
                    res[k] = matrix[i][j]
                    k += 1
                dir_j = -dir_j
                steps_i -= 1
            else:
                for _ in range(steps_i):
                    i += dir_i
                    res[k] = matrix[i][j]
                    k += 1
                dir_i = -dir_i
                steps_j -= 1
        return res
