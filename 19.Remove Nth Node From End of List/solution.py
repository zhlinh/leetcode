#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-19
Last_modify:    2016-01-19
******************************************
'''

'''
Given a linked list, remove the nth node from the end of list
and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list
   becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listp = head
        listLen = 0
        while listp != None:
            listLen += 1
            listp=listp.next
        if listLen - n == 0:
            head = head.next
            return head
        listp = head
        for i in range(listLen - n - 1):
            listp = listp.next
        listp.next = listp.next.next
        return head
