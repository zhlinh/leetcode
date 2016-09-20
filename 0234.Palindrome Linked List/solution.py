#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-03
Last_modify:    2016-05-03
******************************************
'''

'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow
            slow = slow.next
            tmp.next = pre
            pre = tmp
        if fast:
            slow = slow.next
        while pre:
            if pre.val != slow.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
