#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  grid = [['1','1','1','1','0'], ['1','1','0','1','0'], \
        #  ['1','1','0','0','0'], ['0','0','0','0','0']]
grid = [['1','1','0','0','0'], ['1','1','0','0','0'], \
        ['0','0','1','0','0'], ['0','0','0','1','1']]
sol = Solution()
res = sol.numIslands(grid)
print(res)
