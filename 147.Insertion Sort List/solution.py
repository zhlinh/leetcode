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
        newLinkIter = dummy
        cur = head
        while cur:
            tmp = cur.next
            if newLinkIter.next and newLinkIter.next.val > cur.val:
                newLinkIter = dummy
            while newLinkIter.next and newLinkIter.next.val < cur.val:
                newLinkIter = newLinkIter.next
            cur.next = newLinkIter.next
            newLinkIter.next = cur
            #  newLinkIter = dummy
            cur = tmp
        return dummy.next
