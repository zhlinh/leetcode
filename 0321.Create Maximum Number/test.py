#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  nums1 = [3, 4, 6, 5]
#  nums2 = [9, 1, 2, 5, 8, 3]
#  k = 5

#  nums1 = [6, 7]
#  nums2 = [6, 0, 4]
#  k = 5

#  nums1 = [3, 9]
#  nums2 = [8, 9]
#  k = 3

#  nums1 = [2,2,0,6,8,9,6]
#  nums2 = [5,2,4,5,3,6,2]
#  k = 7

nums1 = [8, 6, 9]
nums2 = [1, 7, 5]
k = 3

#  nums1 = [4, 9, 3, 2, 1, 8, 7, 6]
#  nums2 = [5]
#  k = 8

sol = Solution()
res = sol.maxNumber(nums1, nums2, k)
print(res)
