#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-24
Last_modify:    2016-05-24
******************************************
'''

'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
'''

import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.defaultdict(int)
        freqs = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in nums:
            dic[num] += 1
        for key in dic:
            freqs[dic[key]].append(key)
        i = len(nums)
        while i >= 1 and len(res) < k:
            if freqs[i]:
                res += freqs[i]
            i -= 1
        return res[:k]
