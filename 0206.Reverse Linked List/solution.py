#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-24
Last_modify:    2016-03-24
******************************************
'''

'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively.
Could you implement both?
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(None, head)

    def helper(self, pre, head):
        if not head:
            return pre
        nextNode = head.next
        head.next = pre
        return self.helper(head, nextNode)
