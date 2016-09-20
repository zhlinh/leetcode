#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  nums = [0, 1, 2, 3, 4, 1, 5, 2]
#  k = 5
#  t = 4
nums = [1, 3, 1]
k = 2
t = 1
sol = Solution()
res = sol.containsNearbyAlmostDuplicate(nums, k, t)
print(res)
