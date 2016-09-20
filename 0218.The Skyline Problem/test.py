#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
sol = Solution()
res = sol.getSkyline(buildings)
print(res)
