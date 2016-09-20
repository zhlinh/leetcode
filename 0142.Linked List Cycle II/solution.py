#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-17
Last_modify:    2016-03-17
******************************************
'''

'''
Given a linked list,
return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow, entry = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while slow != entry:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
