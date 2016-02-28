#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-28
Last_modify:    2016-02-28
******************************************
'''

'''
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than
the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 1:
            return False
        il, ir = 0, len(matrix)
        jl, jr = 0, len(matrix[0])
        imid, jmid = 0, 0
        while il < ir:
            imid = (il + ir) // 2
            if matrix[imid][0] == target:
                return True
            elif matrix[imid][0] < target:
                il = imid + 1
            else:
                ir = imid
        imid = il - 1
        while jl < jr:
            jmid = (jl + jr) // 2
            if matrix[imid][jmid] == target:
                return True
            elif matrix[imid][jmid] < target:
                jl = jmid + 1
            else:
                jr = jmid
        return False
