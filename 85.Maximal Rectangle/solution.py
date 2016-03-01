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
        height = [0 for _ in range(n + 1)]
        stack = []
        maxA = 0
        for i in range(m):
            # height, n + 1
            stack = []
            for j in range(n + 1):
                if j < n:
                    if matrix[i][j] == '1':
                        height[j] += 1
                    else:
                        height[j] = 0
                while stack and height[stack[-1]] >= height[j]:
                    h = height[stack.pop()]
                    l = (j - stack[-1] - 1) if stack else j
                    maxA = max(maxA, (h * l))
                stack.append(j)
        return maxA
