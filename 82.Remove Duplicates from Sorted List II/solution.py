#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-29
Last_modify:    2016-02-29
******************************************
'''

'''
Given a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

#  Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = l = ListNode('*')
        dummy.next = p = head
        pre = l.val
        while p:
            if not p.next:
                if p.val == pre:
                    l.next = None
                else:
                    l.next = p
                p = p.next
            elif p.val != p.next.val and p.val != pre:
                l.next = p
                p = p.next
                l = l.next
            else:
                pre = p.val
                p = p.next
        return dummy.next
