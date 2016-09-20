#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-25
Last_modify:    2016-01-25
******************************************
'''

'''
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
'''

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = lt = ListNode(0)
        h = [(i.val, i) for i in lists if i]
        heapq.heapify(h)
        while h:
            lt.next = heapq.heappop(h)[1]
            lt = lt.next
            if lt.next:
                heapq.heappush(h, (lt.next.val, lt.next))
        return dummy.next

