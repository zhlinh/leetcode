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
Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.
'''

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        q = [root]
        data = [root.val]
        while q:
            cur = q.pop(0)
            if cur.left:
                q.append(cur.left)
                data.append(cur.left.val)
            else:
                data.append(None)
            if cur.right:
                q.append(cur.right)
                data.append(cur.right.val)
            else:
                data.append(None)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = self.createNode(data[0])
        if not root:
            return None
        q = [root]
        idx = 1
        while q:
            cur = q.pop(0)
            if idx == len(data):
                break
            cur.left = self.createNode(data[idx])
            if cur.left:
                q.append(cur.left)
            idx += 1
            if idx == len(data):
                break
            cur.right = self.createNode(data[idx])
            if cur.right:
                q.append(cur.right)
            idx += 1
        return root

    def createNode(self, num):
        if num == None:
            return None
        return TreeNode(num)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
