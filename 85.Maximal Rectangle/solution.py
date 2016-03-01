#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-01
Last_modify:    2016-03-01
******************************************
'''

'''
Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing all ones and return its area.
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        height = [0 for _ in range(n)]
        maxA = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            # height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j], cur_left = 0, j + 1
            # right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j], cur_right = n, j
            for j in range(n):
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        return maxA
