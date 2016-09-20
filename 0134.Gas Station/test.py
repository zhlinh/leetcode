#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

gas = [4, 2, 1, 3]
cost = [2, 0, 2, 4]
sol = Solution()
res = sol.canCompleteCircuit(gas, cost)
print(res)
