#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

s = "leetcode"
wordDict = set(["leet", "code"])
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
