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
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        step = 1
        dummy = ListNode(0)
        dummy.next = head
        while step < n:
            cur = dummy.next
            tail = dummy
            while cur:
                left = cur
                right = self.split(left, step)
                cur = self.split(right, step)
                tail = self.merge(left, right, tail)
            step <<= 1
        return dummy.next

    def split(self, h, step):
        i = 1
        while h and i < step:
            h = h.next
            i += 1
        if not h:
            return None
        second = h.next
        h.next = None
        return second

    def merge(self, h1, h2, tail):
        h = tail
        while h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next
        h.next = h1 or h2
        while h.next:
            h = h.next
        return h
