#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-06
Last_modify:    2016-03-06
******************************************
'''

'''
Given preorder and inorder traversal of a tree,
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inindex = 0
        for i in range(1, len(preorder)):
            if stack and stack[-1].val != inorder[inindex]:
                cur = stack[-1]
                cur.left = TreeNode(preorder[i])
                stack.append(cur.left)
            else:
                while stack and stack[-1].val == inorder[inindex]:
                    cur = stack[-1]
                    stack.pop()
                    inindex += 1
                if inindex < len(inorder):
                    cur.right = TreeNode(preorder[i])
                    stack.append(cur.right)
        return root

