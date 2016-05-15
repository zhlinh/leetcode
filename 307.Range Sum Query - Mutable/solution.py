#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-13
Last_modify:    2016-05-13
******************************************
'''

'''
Given an integer array nums, find the sum of the elements between
indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at
index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function
is distributed evenly.
'''

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.c = [0] * (self.n + 1)
        self.f = nums
        for i in range(self.n):
            k = i + 1
            while k < self.n + 1:
                self.c[k] += self.f[i]
                k += (k & -k)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.f[i]
        self.f[i] = val
        k = i + 1
        while k < self.n + 1:
            self.c[k] += diff
            k += (k & -k)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        j = j + 1
        while j > 0:
            res += self.c[j]
            j -= (j & -j)
        while i > 0:
            res -= self.c[i]
            i -= (i & -i)
        return res


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)       return self.from0Sum[j+1] - self.from0Sum[i]
