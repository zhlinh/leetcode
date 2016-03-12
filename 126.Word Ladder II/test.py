#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

#  bw = "hit"
#  ew = "cog"
#  wl = set(["hot","dot","dog","lot","log"])
bw = "hot"
ew = "dog"
wl = set(["hot", "dog"])
sol = Solution()
res = sol.findLadders(bw, ew, wl)
print(res)
