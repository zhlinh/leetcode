#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import Interval

#  intervals = [Interval(1, 2), Interval(3, 5), \
    #  Interval(6, 7), Interval(8, 10), Interval(12, 16)]
#  newInterval = Interval(4, 9)
intervals = [Interval(0, 5), Interval(9, 12)]
newInterval = Interval(7, 16)
sol = Solution()
res = sol.insert(intervals, newInterval)
res_list = []
for i in range(len(res)):
    res_list.append([res[i].start, res[i].end])
print(res_list)
