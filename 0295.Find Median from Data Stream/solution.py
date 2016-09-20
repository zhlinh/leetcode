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
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream
to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.
'''
from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap))
        if len(self.minHeap) < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (self.minHeap[0] - self.maxHeap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
