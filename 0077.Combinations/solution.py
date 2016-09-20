#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-28
Last_modify:    2016-02-28
******************************************
'''

'''
Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result, results = [], []
        start = 1
        self.dfs(n, k, start, result, results)
        return results

    def dfs(self, n, k, start, result, results):
        if len(result) >= k:
            results.append(result)
            return
        for i in range(start, n + 1):
            self.dfs(n, k, i + 1, result + [i], results)
