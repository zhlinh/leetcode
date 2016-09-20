#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-11
Last_modify:    2016-05-11
******************************************
'''

'''
Given an unsorted array of integers,
find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101],
therefore the length is 4. Note that there may be more
than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        res = 0
        lists = [nums[0]]
        for i in range(1, n):
            # new smallest value
            if nums[i] < lists[0]:
                lists[0] = nums[i]
            # new largest subsequence
            elif nums[i] > lists[-1]:
                lists.append(nums[i])
            # replace end of one existing subsequence
            else:
                lists[self.findPosValue(lists, nums[i])] = nums[i]
        return len(lists)

    def findPosValue(self, lists, val):
        left, right = 0, len(lists)
        while left < right:
            mid = left + (right - left) // 2
            if lists[mid] >= val:
                right = mid
            else:
                left = mid + 1
        return left
