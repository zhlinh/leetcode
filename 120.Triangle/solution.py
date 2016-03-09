#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-09
Last_modify:    2016-03-09
******************************************
'''

'''
Given a triangle, find the minimum path
sum from top to bottom. Each step you may
move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11
(i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using
only O(n) extra space, where n is the total number
of rows in the triangle.
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp = [0 for _ in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            for j in reversed(range(n)):
                if j == 0:
                    dp[j] = triangle[i][0] + dp[0]
                elif j == n - 1:
                    dp[j] = triangle[i][j] + dp[j-1]
                else:
                    dp[j] = triangle[i][j] + min(dp[j], dp[j-1])
        return min(dp)
