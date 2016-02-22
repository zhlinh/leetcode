#!/usr/bin/env python
# -*- coding: utf-8 -*-

from solution import Solution
from solution import Interval

intervals = [Interval(1, 3), Interval(2, 6), \
        Interval(8, 10), Interval(15, 18)]
sol = Solution()
res = sol.merge(intervals)
res_list = []
for i in range(len(res)):
    res_list.append([res[i].start, res[i].end])
print(res_list)
