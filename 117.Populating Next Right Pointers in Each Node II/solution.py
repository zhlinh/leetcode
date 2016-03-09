#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-09
Last_modify:    2016-03-09
******************************************
'''

'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree?
Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
       self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        cur = root
        head = None
        pre = None
        while cur:
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right
                cur = cur.next
            cur = head
            head = None
            pre = None
