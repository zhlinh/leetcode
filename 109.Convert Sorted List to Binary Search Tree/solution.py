#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-07
Last_modify:    2016-03-07
******************************************
'''

'''
Given a **singly linked list** where elements are
sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

#  Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        slow = head
        fast = head
        pre = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        root = TreeNode(slow.val)
        if pre == None:
            head = None
        else:
            pre.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
