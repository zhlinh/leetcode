#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
word = "SEE"
sol = Solution()
res = sol.exist(board, word)
print(res)
