#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-13
Last_modify:    2016-03-13
******************************************
'''

'''
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence
is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        res = 0
        for n in nums:
            if n not in dict:
                left = dict.get(n - 1, 0)
                right = dict.get(n + 1, 0)
                length = left + right + 1
                dict[n] = length
                dict[n - left] = length
                dict[n + right] = length
                res = max(res, length)
        return res
