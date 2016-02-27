#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-27
Last_modify:    2016-02-27
******************************************
'''

'''
Given a m x n matrix,
if an element is 0, set its entire row and column to 0.
Do it in place.
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        if len(matrix) > 0:
            for i in range(len(matrix)):
                if matrix[i][0] == 0:
                    col0 = 0
                for j in range(1, len(matrix[0])):
                    if matrix[i][j] == 0:
                        matrix[i][0] = matrix[0][j] = 0
            # reverse to not change matrix[0][0]
            for i in range(len(matrix) - 1, -1, -1):
                for j in range(len(matrix[0]) - 1, 0, -1):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
                if col0 == 0:
                    matrix[i][0] = 0
