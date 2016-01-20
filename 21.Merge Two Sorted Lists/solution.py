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
        head = lt = ListNode(0)
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                if l1.val < l2.val:
                    lt.next = ListNode(l1.val)
                    lt, l1 = lt.next, l1.next
                else:
                    lt.next = ListNode(l2.val)
                    lt, l2 = lt.next, l2.next
            elif l1 == None:
                lt.next = ListNode(l2.val)
                lt, l2 = lt.next, l2.next
            else:
                lt.next = ListNode(l1.val)
                lt, l1 = lt.next, l1.next
        return head.next

