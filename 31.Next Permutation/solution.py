#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-29
Last_modify:    2016-01-29
******************************************
'''

'''
Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the
lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and
its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = k = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            while j > i:
                nums[j], nums[i] = nums[i], nums[j]
                i, j =  i + 1, j - 1
            return
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r =  l + 1, r - 1
