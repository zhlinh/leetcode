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
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return self.helper(len(postorder) - 1, 0, len(inorder) - 1, \
                inorder, postorder, dic)

    def helper(self, postEnd, inStart, inEnd, inorder, postorder, dic):
        if postEnd < 0 or inStart > inEnd:
            return
        root = TreeNode(postorder[postEnd])
        inIndex = dic[root.val]
        rightLen = inEnd - inIndex
        root .right = self.helper(postEnd - 1, inIndex + 1, inEnd, \
                inorder, postorder, dic)
        root.left = self.helper(postEnd - rightLen - 1, inStart, inIndex - 1, \
                inorder, postorder, dic)
        return root
