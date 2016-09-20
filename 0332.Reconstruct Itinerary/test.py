#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
sol = Solution()
res = sol.findItinerary(tickets)
print(res)
