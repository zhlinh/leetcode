#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-15
Last_modify: 	2016-01-15
******************************************
'''

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList = []
        if len(nums) < 3:
            return []
        for i in range(len(nums) - 2):
            d = {}
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in d:
                    tmpList= sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                    if tmpList not in rList:
                        rList.append(tmpList)
                d[nums[j]] = j
        return rList
