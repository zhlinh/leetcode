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
        dummyl = l = ListNode(0)
        dummyl.next = p = head
        i = 1
        while p and i <= n:
            if i == m - 1:
                l = p
                p = p.next
            elif i == m:
                dummyr = r = p
                p = p.next
            elif m < i < n:
                tmp = p
                p = p.next
                tmp.next = r
                r = tmp
            elif i == n:
                tmp = p
                p = p.next
                dummyr.next = p
                tmp.next = r
                l.next = tmp
            else:
                p = p.next
            i += 1
        return dummyl.next
