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
Given a set of non-overlapping intervals,
insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted
according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16],
insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        res = []
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].start:
            i += 1
        intervals.insert(i, newInterval)
        if i == 0:
            last = intervals[0]
        else:
            last = intervals[i-1]
            res += intervals[:i-1]
        while i < len(intervals):
            if last.end >= intervals[i].start:
                last.end = max(last.end, intervals[i].end)
            else:
                res.append(last)
                last = intervals[i]
            i += 1
        res.append(last)
        return res
