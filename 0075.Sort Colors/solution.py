#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-28
Last_modify:    2016-02-28
******************************************
'''

'''
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n0, n01, n012 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[n012] = 2
                nums[n01] = 1
                nums[n0] = 0
                n0, n01, n012 = n0 + 1, n01 + 1, n012 + 1
            elif nums[i] == 1:
                nums[n012] = 2
                nums[n01] = 1
                n01, n012 = n01 + 1, n012 + 1
            else:
                nums[n012] = 2
                n012 = n012 + 1
