#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-22
Last_modify:    2016-02-22
******************************************
'''

'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k == 0:
            return head
        p = head
        n = 0
        while p:
            n += 1
            end = p
            p = p.next
        # notice k may greater than n
        k = k % n
        if k == 0:
            return head
        p = head
        for i in range(n-k-1):
            p = p.next
        rotate_end = p
        rotate_start = p.next
        end.next = head
        rotate_end.next = None
        return rotate_start
