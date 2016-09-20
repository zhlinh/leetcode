#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-02
Last_modify:    2016-03-02
******************************************
'''

'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space
(size that is greater or equal to m + n)
to hold additional elements from nums2.
The number of elements initialized in
nums1 and nums2 are m and n respectively.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, p1, p2 = m + n - 1, m - 1, n - 1
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
