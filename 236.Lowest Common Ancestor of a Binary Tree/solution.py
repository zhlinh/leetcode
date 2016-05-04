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
Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between
two nodes v and w as the lowest node in T
that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Frame(object):
    def __init__(self, node, parent):
        # TreeNode: node
        self.node = node
        # Frame: parent
        self.parent = parent
        # TreeNode list: sub
        self.sub = []

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        answer = Frame(None, None)
        stack.append(Frame(root, answer))
        while stack:
            top = stack[-1]
            node = top.node
            parent = top.parent
            if not node or node == p or node == q:
                parent.sub.append(node)
                stack.pop()
            elif not top.sub:
                stack.append(Frame(node.right, top))
                stack.append(Frame(node.left, top))
            else:
                left = top.sub[0]
                right = top.sub[1]
                parent.sub.append(node if left and right else left or right)
                stack.pop()
        return answer.sub[0]
