#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

obstacleGrid = [ [0,0,0], [0,1,0], [0,0,0] ]
sol = Solution()
res = sol.uniquePathsWithObstacles(obstacleGrid)
print(res)
