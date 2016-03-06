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
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder, dic)

    def helper(self, preStart, inStart, inEnd, preorder, inorder, dic):
        if preStart >= len(preorder) or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inIndex = dic[root.val]
        root.left = self.helper(preStart + 1, inStart, inIndex - 1, \
                preorder, inorder, dic)
        root.right = self.helper(preStart + inIndex - inStart + 1, \
                inIndex + 1, inEnd, preorder, inorder, dic)
        return root
