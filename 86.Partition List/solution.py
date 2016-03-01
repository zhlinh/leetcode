#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-01
Last_modify:    2016-03-01
******************************************
'''

'''
Given a linked list and a value x,
partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order
of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

#  Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummyl = l = ListNode(0)
        dummyr = r = ListNode(0)
        p = head
        while p:
            if p.val < x:
                l.next = p
                l = l.next
            else:
                r.next = p
                r = r.next
            p = p.next
        r.next = None
        l.next = dummyr.next
        return dummyl.next
