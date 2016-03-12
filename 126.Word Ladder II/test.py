#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

beginWord = "hit"
endWord = "cog"
wordlist = set(["hot","dot","dog","lot","log"])
#  bw = "hot"
#  ew = "dog"
#  wl = set(["hot", "dog"])
sol = Solution()
res = sol.findLadders(beginWord, endWord, wordlist)
print(res)
