#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-12
Last_modify:    2016-05-12
******************************************
'''

'''
Given a 2D matrix matrix, find the sum of the elements inside
the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by
(row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
Subscribe to see which companies asked this question
'''

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.from00Sum = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.from00Sum[i+1][j+1] = self.from00Sum[i+1][j] + \
                    self.from00Sum[i][j+1] - self.from00Sum[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.from00Sum[row2+1][col2+1] - self.from00Sum[row2+1][col1] - \
                self.from00Sum[row1][col2+1] + self.from00Sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
