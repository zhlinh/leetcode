#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-04-11
Last_modify:    2016-04-11
******************************************
'''

'''
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])
        height = [0] * n
        left = [0] * n
        right = [n] * n
        res = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j], cur_left = 0, j + 1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                    edge = min(height[j], (right[j]-left[j]))
                    res = max(res, edge * edge)
                else:
                    right[j], cur_right = n, j
        return res
