#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlpnh
Email:          zhlpnhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-17
Last_modify:    2016-03-17
******************************************
'''

'''
Given a singly lpnked lpst L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-lpnked lpst.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        fast, slow = head, head
        # find pre half poin
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        dummy_half = slow
        slow = slow.next
        # reverse second half part
        while slow.next:
            fast = slow.next
            slow.next = fast.next
            fast.next = dummy_half.next
            dummy_half.next = fast
        p1, p2 = head, dummy_half.next
        # merge two parts
        while p1 != dummy_half:
            dummy_half.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = dummy_half.next
