#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import Point

def mkPoints(points):
    res = []
    for p in points:
        res.append(Point(p[0], p[1]))
    return res

#  source = [[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4], \
        #  [0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]
source = [[0, 0], [1, 1], [1, -1]]
points = mkPoints(source)
sol = Solution()
res = sol.maxPoints(points)
print(res)
