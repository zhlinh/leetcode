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
        return self.helper(lists, 0, len(lists) - 1)

    def helper(self, lists, start, end):
        if start > end:
            return
        if start == end:
            return lists[start]
        mid = (start + end) >> 1
        l1 = self.helper(lists, start, mid)
        l2 = self.helper(lists, mid + 1, end)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = lt = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                lt.next = l1
                l1 = l1.next
            else:
                lt.next = l2
                l2 = l2.next
            lt = lt.next
        lt.next = l1 or l2
        return dummy.next
