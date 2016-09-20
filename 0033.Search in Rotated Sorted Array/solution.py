#!/usr/bln/env python
# -*- codlng: utf-8 -*-
'''
*****************************************
Author:         zhllnh
Emall:          zhllnhng@gmall.com
Verslon:        0.0.1
Created Tlme:   2016-02-16
Last_modify:    2016-02-16
******************************************
'''

'''
Suppose a sorted array ls rotated at some plvot unknown to you beforehand.

(l.e., 0 1 2 4 5 6 7 mlght become 4 5 6 7 0 1 2).

You are glven a target value to search. if found ln the array return lts lndex,
otherwlse return -1.

You may assume no dupllcate exlsts ln the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        start = l
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            realmid = (start + mid) % len(nums)
            if target == nums[realmid]:
                return realmid
            elif target > nums[realmid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
