#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-17
Last_modify:    2016-03-17
******************************************
'''

'''
A linked list is given such that each node contains
an additional random pointer which could point to
any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
   def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        return self.helper(head, dic)

    def helper(self, node, dic):
        if not node:
            return None
        if node.label in dic:
            return dic[node.label]
        root = RandomListNode(node.label)
        dic[node.label] = root
        root.next = self.helper(node.next, dic)
        root.random = self.helper(node.random, dic)
        return root
