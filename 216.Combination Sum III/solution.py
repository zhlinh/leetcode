#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-27
Last_modify:    2016-03-27
******************************************
'''

'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(1, n, [], results, k)
        return results

    def dfs(self, start, curSum, result, results, depth):
        if curSum < 0 or depth < 0:
            return
        if depth == 0 and curSum == 0:
            results.append(result)
        for i in range(start, 10):
            self.dfs(i + 1, curSum - i, result + [i], results, depth - 1)

