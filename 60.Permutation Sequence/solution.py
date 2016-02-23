#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-22
Last_modify:    2016-02-22
******************************************
'''

'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i+1) for i in range(n)]
        # make k start from 0
        k -= 1
        factor = 1
        res = ""
        for i in range(1, n):
            factor *= i
        if k > n * factor - 1:
            return ""
        for i in reversed(range(n)):
            res += nums[k // factor]
            nums.remove(nums[k // factor])
            if i != 0:
                k %= factor
                factor //= i
        return res
