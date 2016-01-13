#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-13
Last_modify: 	2016-01-13
******************************************
'''

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA, i, j = 0, 0, len(height) - 1
        while i != j:
            if height[i] < height[j]:
                tmpA = (j - i) * height[i]
                i += 1
            else:
                tmpA = (j - i) * height[j]
                j -= 1
            if tmpA > maxA:
                maxA = tmpA
        return maxA


