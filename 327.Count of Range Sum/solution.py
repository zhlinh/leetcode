#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-20
Last_modify:    2016-05-20
******************************************
'''

'''
Given an integer array nums, return the number of range sums
that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements
in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective
sums are: -2, -1, 2.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        self.res = 0
        self.mergeSort(sums, lower, upper)
        return self.res


    def mergeSort(self, sums, lower, upper):
        half = len(sums) // 2
        if half:
            left = self.mergeSort(sums[:half], lower, upper)
            right = self.mergeSort(sums[half:], lower, upper)
            m, n = len(left), len(right)
            i = 0
            b, e = 0, 0
            while i < m:
                while b < n and right[b] - left[i] < lower:
                    b += 1
                while e < n and right[e] - left[i] <= upper:
                    e += 1
                self.res += (e - b)
                i += 1
            i, j = 0, 0
            while i < m or j < n:
                if j >= n or (i < m and left[i] <= right[j]):
                    sums[i+j] = left[i]
                    i += 1
                else:
                    sums[i+j] = right[j]
                    j += 1
        return sums
