#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-20
Last_modify:    2016-03-20
******************************************
'''

'''
Given n points on a 2D plane,
find the maximum number of points that lie on the same straight line.
'''

# Definition for a point.
class Point(object):
   def __init__(self, a=0, b=0):
       self.x = a
       self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n < 2:
            return n
        dic = {}
        res = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[i].x == points[j].x:
                    a = 1
                    b = 0
                    c = -points[i].x
                elif points[i].y == points[j].y:
                    a = 0
                    b = 1
                    c = -points[i].y
                else:
                    a = float((points[i].y - points[j]. y)) / \
                            (points[i].x - points[j].x)
                    b = -1
                    c = points[i].y - a * points[i].x
                key = (a, b, c)
                if key in dic:
                    dic[key].add(i)
                    dic[key].add(j)
                    res = max(res, len(dic[key]))
                else:
                    dic[key] = set([i, j])
                    res = max(res, 2)
        return res
