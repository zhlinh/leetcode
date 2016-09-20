#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-19
Last_modify:    2016-05-19
******************************************
'''

'''
Given an unsorted array nums, reorder it such that
nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def T(i, n):
            return (i * 2 + 1) % (n | 1)
        n = len(nums)
        nums.sort()
        mid = nums[n // 2]
        left, cur, right = 0, 0, n - 1
        while cur <= right:
            if nums[T(cur, n)] > mid:
                nums[T(cur, n)], nums[T(left, n)] = nums[T(left, n)], \
                        nums[T(cur, n)]
                left += 1
                cur += 1
            elif nums[T(cur, n)] < mid:
                nums[T(cur, n)], nums[T(right, n)] = nums[T(right, n)], \
                        nums[T(cur, n)]
                right -= 1
            else:
                cur += 1
