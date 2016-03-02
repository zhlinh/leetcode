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
        for i in reversed(range(m)):
            nums1[i+n] = nums1[i]
        p, p1, p2 = 0, n, 0
        while p2 < n:
            if p1 >= n + m:
                nums1[p] = nums2[p2]
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                nums1[p] = nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
