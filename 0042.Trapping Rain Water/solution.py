#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-18
Last_modify:    2016-02-18
******************************************
'''

'''
Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water, minH = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            while l < r and height[l] <= minH:
                    water += minH - height[l]
                    l += 1
            while l < r and height[r] <= minH:
                    water += minH - height[r]
                    r -= 1
            minH = min(height[l], height[r])
        return water
