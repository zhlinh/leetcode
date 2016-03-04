#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
#  s3 = "aadbbbaccc"
sol = Solution()
res = sol.isInterleave(s1, s2, s3)
print(res)
