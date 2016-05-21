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
        return self.mergeSort(sums, 0, len(sums), lower, upper)

    def mergeSort(self, sums, start, end, lower, upper):
        if end - start <= 1:
            return 0
        half = start + (end - start) // 2
        res = self.mergeSort(sums, start, half, lower, upper) \
                + self.mergeSort(sums, half, end, lower, upper)
        b, e = half, half
        k, j = 0 , half
        mergeList = [0] * (end - start)
        for i in range(start, half):
            while b < end and sums[b] - sums[i] < lower:
                b += 1
            while e < end and sums[e] - sums[i] <= upper:
                e += 1
            res += (e - b)
            while j < end and sums[j] < sums[i]:
                mergeList[k] = sums[j]
                k += 1
                j += 1
            mergeList[k] = sums[i]
            k += 1
        for i in range(k):
            sums[start+i] = mergeList[i]
        return res

