#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-19
Last_modify:    2016-02-19
******************************************
'''

'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        levels = [nums]
        for start in range(len(nums) - 1):
            for row in range(len(levels)):
                for col in range(start + 1, len(nums)):
                    tmp = levels[row][:]
                    tmp[start], tmp[col] = tmp[col], tmp[start]
                    levels.append(tmp)
        return levels
