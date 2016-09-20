#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-21
Last_modify:    2016-05-21
******************************************
'''

'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary
(i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])
        maxLen = 0
        cache = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen, self.helper(matrix, i, j, m, n, cache))
        return maxLen

    def helper(self, matrix, x, y, m, n, cache):
        if cache[x][y] != 0:
            return cache[x][y]
        res = 1
        if x + 1 < m and matrix[x+1][y] > matrix[x][y]:
            res = max(res, 1 + self.helper(matrix, x + 1, y, m, n, cache))
        if x - 1 >= 0 and matrix[x-1][y] > matrix[x][y]:
            res = max(res, 1 + self.helper(matrix, x - 1, y, m, n, cache))
        if y + 1 < n and matrix[x][y+1] > matrix[x][y]:
            res = max(res, 1 + self.helper(matrix, x, y + 1, m, n, cache))
        if y - 1 >= 0 and matrix[x][y-1] > matrix[x][y]:
            res = max(res, 1 + self.helper(matrix, x, y - 1, m, n, cache))
        cache[x][y] = res
        return res

