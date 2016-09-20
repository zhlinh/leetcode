#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-24
Last_modify:    2016-02-24
******************************************
'''

'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
