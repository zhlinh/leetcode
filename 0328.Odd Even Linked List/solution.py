#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-21
Last_modify:    2016-05-21
******************************************
'''

'''
Given a singly linked list, group all odd nodes together followed
by the even nodes. Please note here we are talking about the node
number and not the value in the nodes.

You should try to do it in place. The program should run in O(1)
space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain
as it was in the input.
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and
creating all test cases.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = even = p.next
        while q and q.next:
            p.next = q.next
            p = p.next
            q.next = p.next
            q = q.next
        p.next = even
        return head
