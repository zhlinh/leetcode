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
A linked list is given such that each node contains
an additional random pointer which could point to
any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
   def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        cur = head
        while cur:
            cur_cp = RandomListNode(cur.label)
            cur_cp.next = cur.next
            cur.next = cur_cp
            cur = cur_cp.next
        cur = head
        while cur:
            cur_cp = cur.next
            if cur.random:
                cur_cp.random = cur.random.next
            cur = cur_cp.next
        cur = head
        head_cp = cur.next
        while cur:
            cur_cp = cur.next
            cur.next = cur_cp.next
            cur = cur.next
            if cur:
                cur_cp.next = cur.next
        return head_cp
