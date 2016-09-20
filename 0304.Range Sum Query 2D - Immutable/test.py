#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import NumMatrix

matrix =  [[3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))

