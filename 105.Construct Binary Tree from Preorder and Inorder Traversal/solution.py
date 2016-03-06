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
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)

    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart >= len(preorder) or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inIndex = 0
        for i in range(inStart, inEnd + 1):
            if inorder[i] == root.val:
                inIndex = i
                break
        root.left = self.helper(preStart + 1, inStart, inIndex - 1, \
                preorder, inorder)
        root.right = self.helper(preStart + inIndex - inStart + 1, \
                inIndex + 1, inEnd, preorder, inorder)
        return root
