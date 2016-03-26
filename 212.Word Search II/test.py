#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

board = [['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']]
words = ["oath","pea","eat","rain"]
sol = Solution()
res = sol.findWords(board, words)
print(res)
