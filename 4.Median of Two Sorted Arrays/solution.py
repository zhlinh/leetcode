#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-06
Last_modify: 	2016-01-06
******************************************
'''

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tlen = len(nums1) + len(nums2)
        if tlen % 2 == 1:
            return self.findKth(nums1, nums2, tlen//2)
        else:
            return (self.findKth(nums1, nums2, tlen//2-1) + \
                    self.findKth(nums1, nums2, tlen//2))/2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            return nums2[k]
        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])
        i = len(nums1) // 2
        j = k - i
        if nums1[i] > nums2[j]:
            # Here assume it is O(1) to get A[:i] and B[j:].
            # In python, it's not but in cpp it is.
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)

