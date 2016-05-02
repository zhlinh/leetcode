#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  s = "2-1 + 2"
s = " 5 - 2*3 / 6 + 6"
#  s = "14-3/2"
#  s = "0/1"
sol = Solution()
res = sol.calculate(s)
print(res)
