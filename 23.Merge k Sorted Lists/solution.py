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
        dummy = lt = ListNode(0)
        if not lists:
            return []
        num = len(lists)
        while num > 1:
            start = 0
            end = num - 1
            tmpList = []
            while start < end:
                tmpList.append(self.mergeTwoLists(lists[start], lists[end]))
                start += 1
                end -= 1
            if start == end:
                tmpList.append(lists[start])
            lists = tmpList
            num = len(lists)
        return lists[0]

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
