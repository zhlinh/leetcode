#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  n = 4
#  edges = [[1, 0], [1, 2], [1, 3]]
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
sol = Solution()
res = sol.findMinHeightTrees(n, edges)
print(res)
