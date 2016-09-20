#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-09
Last_modify:    2016-05-09
******************************************
'''

'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n
        mid = 0
        while l < r:
            mid = l + (r - l) // 2
            if citations[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1
        return n - mid
