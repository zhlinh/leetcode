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
        if not head:
            return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        h2 = slow.next
        while h2 and h2.next:
            tmp = h2.next
            h2.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp
        h2 = slow.next
        #  slow.next = None
        h1 = head
        while h2:
            print(h2.val)
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True


