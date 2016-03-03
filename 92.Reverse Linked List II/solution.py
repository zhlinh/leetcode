#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-03
Last_modify:    2016-03-03
******************************************
'''

'''
Reverse a linked list from position m to n.
Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        for i in range(m-1):
            pre = pre.next
        start = pre.next
        then = start.next
        for i in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        return dummy.next
