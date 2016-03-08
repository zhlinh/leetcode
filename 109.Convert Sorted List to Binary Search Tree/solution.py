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
        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        cur = [head]
        return self.helper(cur, n)

    def helper(self, cur, n):
        if n <= 0:
            return None
        root = TreeNode(0)
        root.left = self.helper(cur, n // 2)
        root.val = cur[0].val
        cur[0] = cur[0].next
        root.right = self.helper(cur, n - (n // 2) - 1)
        return root

