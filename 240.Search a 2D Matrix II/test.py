#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

m = [[1,   4,  7, 11, 15],
     [2,   5,  8, 12, 19],
     [3,   6,  9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]
t = 2
sol = Solution()
res = sol.searchMatrix(m, t)
print(res)
