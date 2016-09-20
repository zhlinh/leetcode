#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-22
Last_modify:    2016-02-22
******************************************
'''

'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x: x.start)
        prev = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if prev.end >= intervals[i].start:
                prev.end = max(prev.end, intervals[i].end)
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res
