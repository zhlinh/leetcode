#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-02
Last_modify:    2016-03-02
******************************************
'''

'''
Given a string s1,
we may represent it as a binary tree by
partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string,
we may choose any non-leaf node and swap its two children.

For example,
if we choose the node "gr" and swap its two children,
it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly,
if we continue to swap the children of nodes "eat" and "at",
it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length,
determine if s2 is a scrambled string of s1.
'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.helper(s1, s2)

    def helper(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        # avoid LTE
        count = [0 for _ in range(26)]
        for i in range(len(s1)):
            count[ord(s1[i])-ord('a')] += 1
            count[ord(s2[i])-ord('a')] -= 1
        for i in range(26):
            if count[i] != 0:
                return False
        for i in range(1, len(s1)):
            if self.helper(s1[:i], s2[:i]) \
               and self.helper(s1[i:], s2[i:]):
                return True
            if self.helper(s1[:i], s2[len(s1)-i:]) \
                    and self.helper(s1[i:], s2[:len(s1)-i]):
                return True
        return False
