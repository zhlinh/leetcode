#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

s = "abefcdgiescdfimde"
p = "ab*cd?i*de"
sol = Solution()
res = sol.isMatch(s, p)
print(res)
