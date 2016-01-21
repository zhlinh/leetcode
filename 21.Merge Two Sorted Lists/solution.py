#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-20
Last_modify:    2016-01-20
******************************************
'''

'''
Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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

