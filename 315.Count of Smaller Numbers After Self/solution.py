#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-17
Last_modify:    2016-05-17
******************************************
'''

'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of
smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

Subscribe to see which companies asked this question
'''

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsWithIndex = [[0 for _ in range(2)] for __ in range(len(nums))]
        for i in range(len(nums)):
            numsWithIndex[i][0] = i
            numsWithIndex[i][1] = nums[i]
        res = [0] * len(nums)
        self.mergeSort(numsWithIndex, res)
        return res


    def mergeSort(self, numsWithIndex, res):
        half = len(numsWithIndex) // 2
        if half:
            left = self.mergeSort(numsWithIndex[:half], res)
            right = self.mergeSort(numsWithIndex[half:], res)
            i, j = 0, 0
            m, n = len(left), len(right)
            while i < m or j < n:
                if j >= n or (i < m and left[i][1] <= right[j][1]):
                    numsWithIndex[i+j] = left[i]
                    # count the num smaller to the right of origin nums[i]
                    # witch means reversed.
                    res[left[i][0]] += j
                    i += 1
                else:
                    numsWithIndex[i+j] = right[j]
                    j += 1
        return numsWithIndex
