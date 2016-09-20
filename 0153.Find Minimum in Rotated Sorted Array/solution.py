#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-21
Last_modify:    2016-03-21
******************************************
'''

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] <= nums[-1]:
                j = mid
            else:
                i = mid + 1
        return nums[i]

