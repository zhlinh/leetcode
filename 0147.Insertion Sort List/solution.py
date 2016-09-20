#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-19
Last_modify:    2016-03-19
******************************************
'''

'''
Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        newIter = dummy
        cur = head
        while cur:
            if newIter.next and newIter.next.val > cur.val:
                newIter = dummy
            while newIter.next and newIter.next.val < cur.val:
                newIter = newIter.next
            tmp = cur.next
            cur.next = newIter.next
            newIter.next = cur
            cur = tmp
        return dummy.next
