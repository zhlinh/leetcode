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
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)
        while nums[j-1] == nums[i] and i < j - 1:
            j -= 1
        end = j - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] <= nums[end]:
                j = mid
            else:
                i = mid + 1
        return nums[i]
