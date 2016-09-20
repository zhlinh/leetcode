#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-26
Last_modify:    2016-01-26
******************************************
'''

'''
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end
should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = lt = ListNode(0)
        dummy.next = head
        while lt.next:
            tmp = lt.next
            p = []
            for i in range(k):
                if not tmp:
                    return dummy.next
                p.append(tmp)
                tmp = tmp.next
            lt.next = p[-1]
            p[0].next = p[-1].next
            j = k - 1
            while j > 0:
                p[j].next = p[j-1]
                j -= 1
            lt = p[0]
        return dummy.next
