#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  nums = [1,3,-1,-3,5,3,6,7]
#  k = 3
#  nums = [1, -1]
#  k = 1
#  nums = [-7,-8,7,5,7,1,6,0]
#  k = 4
nums = [1, 3, 1, 2, 0, 5]
k = 3
sol = Solution()
res = sol.maxSlidingWindow(nums, k)
print(res)
