#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

pattern = "abba"
s = "dog dog dog dog"
pattern = "ab"
s = "b c"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
