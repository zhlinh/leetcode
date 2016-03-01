#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-01
Last_modify:    2016-03-01
******************************************
'''

'''
Given n non-negative integers representing the
histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1,
given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area,
which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                h = heights[stack.pop()]
                l = (i - stack[-1] - 1) if stack else i
                res = max(res, h * l)
            stack.append(i)
        return res
