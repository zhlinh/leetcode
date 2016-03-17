#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

s = "catsanddog"
wordDict = set(["cat", "cats", "and", "sand", "dog"])
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
