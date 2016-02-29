#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-29
Last_modify:    2016-02-29
******************************************
'''

'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 1
        while start < len(nums) and nums[start] >= nums[start-1]:
            start += 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            realmid = (start + mid) % len(nums)
            if nums[realmid] == target:
                return True
            elif nums[realmid] > target:
                r -= 1
            else:
                l += 1
        return False

