#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-04-07
Last_modify:    2016-04-07
******************************************
'''

'''
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k < 1:
            return False
        visited = set()
        start = 0
        for i in range(len(nums)):
            if i - start > k:
                visited.remove(nums[start])
                start += 1
            if nums[i] not in visited:
                visited.add(nums[i])
            else:
                return True
        return False
