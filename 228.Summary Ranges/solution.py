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
        if not nums:
            return []
        start = 2 ** 31 - 1
        end = -2 ** 31
        res = []
        n = len(nums)
        for i in range(n):
            if start >= nums[i]:
                start = nums[i]
                pre = nums[i]
            elif nums[i] - pre == 1:
                end = nums[i]
            elif nums[i] - pre > 1:
                if end > start:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(start))
                start = nums[i]
                end = -2 ** 31
            pre = nums[i]
        if end > start:
            res.append(str(start) + "->" + str(end))
        else:
            res.append(str(start))
        return res
