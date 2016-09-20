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
        if k == 0:
            return []
        if k == 1:
            if k >= 1 and k <= 9:
                return [k]
            else:
                return []
        results = []
        self.helper(k, 1, n, [], results)
        return results

    def helper(self, k, start, target, result, results):
        if k == 2:
            l, r = start, 9
            while l < r:
                if l + r > target:
                    r -= 1
                elif l + r < target:
                    l += 1
                else:
                    results.append(result + [l, r])
                    l += 1
                    r -= 1
        else:
            for i in range(start, 10):
                self.helper(k - 1, i + 1, target - i, result + [i], results)
