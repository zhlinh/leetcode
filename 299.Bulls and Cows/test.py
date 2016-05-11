#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  secret = "1807"
#  guess = "7810"
secret = "1123"
guess = "0111"
sol = Solution()
res = sol.getHint(secret, guess)
print(res)
