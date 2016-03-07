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
Given inorder and postorder traversal of a tree,
construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        n = len(postorder)
        root = TreeNode(postorder[n-1])
        stack = [root]
        inindex = n - 1
        for i in reversed(range(n - 1)):
            if stack and stack[-1].val != inorder[inindex]:
                cur = stack[-1]
                cur.right = TreeNode(postorder[i])
                stack.append(cur.right)
            else:
                while stack and stack[-1].val == inorder[inindex]:
                    cur = stack[-1]
                    stack.pop()
                    inindex -= 1
                if inindex >= 0:
                    cur.left = TreeNode(postorder[i])
                    stack.append(cur.left)
        return root
