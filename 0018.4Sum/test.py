#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
inpt = [1, 0, -1, 0, -2, 2]
#  inpt = [-1, 0, 1, 2, -1, -4]
target = 0
sol = Solution()
res = sol.fourSum(inpt, target)
print(res)
