#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
sol = Solution()
res = sol.solve(board)
print(board)
