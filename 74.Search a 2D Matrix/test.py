#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
#  m = [[1]]
t = 11
sol = Solution()
res = sol.searchMatrix(m, t)
print(res)
