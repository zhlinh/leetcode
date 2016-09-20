#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-24
Last_modify:    2016-03-24
******************************************
'''

'''
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded
by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid
are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, m, n)
                    count += 1
        return count

    def bfs(self, grid, i, j, m, n):
        grid[i][j] = '0'
        q = [(i, j)]
        while q:
            x, y = q.pop(0)
            if x - 1 >= 0 and grid[x-1][y] == '1':
                grid[x-1][y] = '0'
                q.append((x-1, y))
            if x + 1 < m and grid[x+1][y] == '1':
                grid[x+1][y] = '0'
                q.append((x+1, y))
            if y - 1 >= 0 and grid[x][y-1] == '1':
                grid[x][y-1] = '0'
                q.append((x, y-1))
            if y + 1 < n and grid[x][y+1] == '1':
                grid[x][y+1] = '0'
                q.append((x, y+1))
