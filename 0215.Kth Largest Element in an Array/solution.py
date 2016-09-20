#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-26
Last_modify:    2016-03-26
******************************************
'''

'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution(object):
    maxHeapSize = 0
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.maxHeapSize = len(nums)
        self.buildMaxHeap(nums)
        for i in range(k):
            nums[0], nums[self.maxHeapSize-1] = nums[self.maxHeapSize-1], nums[0]
            self.maxHeapSize -= 1
            self.maxHeapify(nums, 0)
        return nums[self.maxHeapSize]

    def maxHeapify(self, nums, idx):
        largest = idx
        left = (largest  << 1) + 1
        right = (largest  << 1) + 2
        if left < self.maxHeapSize and nums[left] > nums[largest]:
            largest = left
        if right < self.maxHeapSize and nums[right] > nums[largest]:
            largest = right
        if idx != largest:
            nums[idx], nums[largest] = nums[largest], nums[idx]
            self.maxHeapify(nums, largest)

    def buildMaxHeap(self, nums):
        for i in reversed(range(self.maxHeapSize >> 1)):
            self.maxHeapify(nums, i)
