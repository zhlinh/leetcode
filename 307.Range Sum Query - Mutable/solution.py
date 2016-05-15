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

class SegmentTree(object):
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.sum = 0


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.buildSegmentTree(nums, 0, len(nums) - 1)

    def buildSegmentTree(self, nums, start, end):
        if start > end:
            return None
        node = SegmentTree(start, end)
        if start == end:
            node.sum = nums[start]
        else:
            mid = start + (end - start) // 2
            node.left = self.buildSegmentTree(nums, start, mid)
            node.right = self.buildSegmentTree(nums, mid + 1, end)
            node.sum = node.left.sum + node.right.sum
        #  print(node.start, node.end, node.sum)
        return node

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.updateHelper(self.root, i, val)

    def updateHelper(self, node, i, val):
        if not node or i > node.end or i < node.start:
            return
        if node.start == i and node.end == i:
            node.sum = val
        else:
            mid = node.start + (node.end - node.start) // 2
            if i <= mid:
                self.updateHelper(node.left, i, val)
            else:
                self.updateHelper(node.right, i, val)
            node.sum = node.left.sum + node.right.sum

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeHelper(self.root, i, j)

    def sumRangeHelper(self, node, i, j):
        if not node or i > node.end or j < node.start:
            return 0
        if node.start == i and node.end == j:
            return node.sum
        else:
            mid = node.start + (node.end - node.start) // 2
            if j <= mid:
                return self.sumRangeHelper(node.left, i, j)
            elif i > mid:
                return self.sumRangeHelper(node.right, i, j)
            else:
                return self.sumRangeHelper(node.left, i, mid) + \
                        self.sumRangeHelper(node.right, mid + 1, j)
        return node.sum


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)       return self.from0Sum[j+1] - self.from0Sum[i]
