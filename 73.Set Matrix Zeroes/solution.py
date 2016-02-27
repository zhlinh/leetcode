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
        zr, zc = {}, {}
        if len(matrix) > 0:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        zr[i], zc[j] = 1, 1
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i in zr or j in zc:
                        matrix[i][j] = 0
                        continue
