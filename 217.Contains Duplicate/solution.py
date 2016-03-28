#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-28
Last_modify:    2016-03-28
******************************************
'''

'''
Given an array of integers,
find if the array contains any duplicates.
Your function should return true if any value
appears at least twice in the array,
and it should return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
