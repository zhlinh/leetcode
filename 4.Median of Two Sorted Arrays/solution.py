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
        rnum = None
        sumLen = len(nums1) + len(nums2)
        if sumLen == 0:
            return rnum
        med = sumLen//2 + 1
        lst = []
        i = j = 0
        for r in range(med):
            if i > len(nums1)-1:
                if j > len(nums2)-1:
                    break
                else:
                    lst.append(nums2[j])
                    j = j + 1
                    continue
            if j > len(nums2)-1:
                if i > len(nums1)-1:
                    break
                else:
                    lst.append(nums1[i])
                    i = i + 1
                    continue
            if nums1[i] > nums2[j]:
                lst.append(nums2[j])
                j = j + 1
            else:
                lst.append(nums1[i])
                i = i + 1
        if sumLen % 2 == 0:
            return (lst[med-1]+lst[med-2])/float(2)
        else:
            return float(lst[med-1])
