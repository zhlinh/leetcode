#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-22
Last_modify:    2016-05-22
******************************************
'''

'''
Given an unsorted array return whether an increasing subsequence of length 3
exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small, secondSmall = 2 ** 31 - 1, 2 ** 31 - 1
        for num in nums:
            if num <= small:
                small = num
            elif num <= secondSmall:
                secondSmall = num
            else:
                return True
        return False
