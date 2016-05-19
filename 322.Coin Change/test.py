#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  coins = [1, 2, 5]
#  amount = 11
#  coins = [2]
#  amount = 3
coins = [186,419,83,408]
amount = 6249
sol = Solution()
res = sol.coinChange(coins, amount)
print(res)
