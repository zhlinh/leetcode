#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
auther:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-06
Last_modify: 	2016-01-07
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
        m, n = len(nums1), len(nums2)
        if m > n:
            # make sure m < n
            nums1, nums2, m, n = nums2, nums1, n, m
        # i in (imin, imax)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            # binary search
            i = (imin + imax) // 2
            # i+j = m-i+n-j[or actually (m+n+1)-i-j], so j = (m+n+1)/2-i.
            j = half_len - i
            # move imin to right
            if j > 0 and i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            # move imax to left
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                imax = i - 1
            # when meeting both two conditions, we get the answer here
            else:
                # just incase two inputs are both None.
                if i == 0 and j == 0:
                    return None
                elif i == 0:
                    num1 = nums2[j-1]
                elif j == 0:
                    num1 = nums1[i-1]
                else:
                    num1 = max(nums1[i-1], nums2[j-1])
                # if m+n is odd
                if (m + n) % 2 == 1:
                    return num1
                # in this case nums1[i] is None
                if i == m:
                    num2 = nums2[j]
                # in this case nums2[j] is None
                elif j == n:
                    num2 = nums1[i]
                else:
                    num2 = min(nums1[i], nums2[j])
                # if m+n is even
                return (num1 + num2) / 2.0
