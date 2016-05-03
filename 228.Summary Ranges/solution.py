#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-02
Last_modify:    2016-05-02
******************************************
'''

'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for
adding this problem and creating all test cases.
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        i = 0
        while i < n:
            start = nums[i]
            while i < n - 1 and nums[i+1] - nums[i] == 1:
                i += 1
            if nums[i] != start:
                res.append(str(start) + "->" + str(nums[i]))
            else:
                res.append(str(start))
            i += 1
        return res
