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
        res = 0
        for i in range(len(points)):
            dic = {}
            overlap = 0
            diffMax = 0
            for j in range(i + 1, len(points)):
                x = points[i].x - points[j].x
                y = points[i].y - points[j].y
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                gcd = self.getGCD(x, y)
                if gcd:
                    x //= gcd
                    y //= gcd
                key = (x, y)
                if key in dic:
                    dic[key] += 1
                else:
                    dic[key] = 1
                diffMax = max(diffMax, dic[key])
            res = max(res, diffMax + overlap + 1)
        return res

    def getGCD(self, x, y):
        while y:
            x, y = y, x % y
        return x

