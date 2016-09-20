#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-10
Last_modify:    2016-05-10
******************************************
'''

'''
Given an array nums containing n + 1 integers where each integer
is between 1 and n (inclusive), prove that at least one duplicate
number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be
repeated more than once.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and
creating all test cases.
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return -1
        fast, slow, entry = nums[0], nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                while entry != slow:
                    entry = nums[entry]
                    slow = nums[slow]
                return entry
        return -1
