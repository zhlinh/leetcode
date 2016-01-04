#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-04
Last_modify: 	2016-01-04
******************************************
'''

'''
Given an array of integers,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.

Please note that your returned answers (both index1 and index2)
are not zero-based.

You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(nums):
            if target-v in d:
                return [d[target-v], i+1]
            d[v] = i + 1

