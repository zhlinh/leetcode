#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30,-5]]
dungeon = [[0, -3]]
sol = Solution()
res = sol.calculateMinimumHP(dungeon)
print(res)
