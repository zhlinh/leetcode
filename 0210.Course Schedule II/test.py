#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  n = 4
#  p = [[1,0],[2,0],[3,1],[3,2]]
#  n = 6
#  p = [[1, 0], [3, 2], [2, 1], [3, 2], [5, 4], [3, 5]]
n = 3
p = [[0,1],[0,2],[1,2]]
sol = Solution()
res = sol.findOrder(n, p)
print(res)
