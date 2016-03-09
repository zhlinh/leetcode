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
Given numRows, generate the
first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for n in range(1, numRows + 1):
            level = []
            for i in range(n):
                if i == 0 or i == n - 1:
                    level.append(1)
                else:
                    level.append(res[n-2][i-1] + res[n-2][i])
            res.append(level)
        return res
