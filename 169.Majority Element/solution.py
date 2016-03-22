#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-22
Last_modify:    2016-03-22
******************************************
'''

'''
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority
element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        res = 0
        gap = len(nums) // 2
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
            if dic[n] > gap:
                return n
        return
