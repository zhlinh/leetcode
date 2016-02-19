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
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        levels = [nums]
        dic = {}
        for start in range(len(nums) - 1):
            for lsi in range(len(levels)):
                dic = {}
                dic[levels[lsi][start]] = 1
                for li in range(start + 1, len(levels[lsi])):
                    if levels[lsi][li] not in dic:
                        dic[levels[lsi][li]] = 1
                        tmp = levels[lsi][:]
                        tmp[start], tmp[li] = tmp[li], tmp[start]
                        levels.append(tmp)
        return levels
