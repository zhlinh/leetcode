#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

matrix = [['1', '0', '1', '0', '0'],
          ['1', '0', '1', '1', '1'],
          ['1', '1', '1', '1', '1'],
          ['1', '0', '0', '1', '0']]
sol = Solution()
res = sol.maximalSquare(matrix)
print(res)
