#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-05
Last_modify:    2016-05-05
******************************************
'''

'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for
adding this problem and creating all test cases.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        results = []
        if root:
            self.helper(root, "", results)
        return results

    def helper(self, node, result, results):
        if not node.left and not node.right:
            results.append(result + str(node.val))
            return
        if node.left:
            self.helper(node.left, result + str(node.val) + "->", results)
        if node.right:
            self.helper(node.right, result + str(node.val) + "->", results)
