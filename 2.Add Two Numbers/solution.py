#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-04
Last_modify:    2016-01-04
******************************************
'''

'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        lt = ListNode(0)
        l3 = lt
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            lt.next = ListNode(sum % 10)
            carry = sum // 10
            lt = lt.next
        return l3.next

