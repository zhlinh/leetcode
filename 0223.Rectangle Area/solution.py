#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-01
Last_modify:    2016-05-01
******************************************
'''

'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner
as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

Credits:
Special thanks to @mithmatt for adding this problem,
creating the above image and all test cases.
'''

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        area1 = (C - A) * (D - B)
        area2 = (H - F) * (G - E)
        if y2 - y1 < 0 or x2 - x1 < 0:
            return area1 + area2
        else:
            overlap = (y2 - y1) * (x2 - x1)
            return area1 + area2 - overlap
