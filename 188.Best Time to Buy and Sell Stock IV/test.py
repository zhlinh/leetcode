#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  stock = [3, 4, 2, 5, 6, 7, 2]
#  stock = [2, 1, 2, 1, 0, 1, 2]
#  stock = [1,2,4,2,5,7,2,4,9,0]
stock = [1,2,4,2,5,7,2,4,9,0]
k = 4
sol = Solution()
res = sol.maxProfit(k, stock)
print(res)
