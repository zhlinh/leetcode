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
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = self.sortList(slow.next)
        slow.next = None
        h1 = self.sortList(head)
        res = self.merge(h1, h2)
        return res

    def merge(self, h1, h2):
        dummy = p = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                p.next = h1
                h1 = h1.next
            else:
                p.next = h2
                h2 = h2.next
            p = p.next
        p.next = h1 or h2
        return dummy.next
