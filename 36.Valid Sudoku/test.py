#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

brd = ["....5..1.",".4.3.....",".....3..1", \
       "8......2.","..2.7....",".15......", \
       ".....2...",".2.9.....","..4......"]
sol = Solution()
res = sol.isValidSudoku(brd)
print(res)
