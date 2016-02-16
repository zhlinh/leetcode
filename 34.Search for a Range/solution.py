#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-16
Last_modify:    2016-02-16
******************************************
'''

'''
Given a sorted array of integers,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        # bisect_left
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        l = lo
        if nums[l] != target:
            l = -1
        # bisect_right
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2 + 1
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        r = lo
        if nums[r] != target:
            r = -1
        return [l, r]
