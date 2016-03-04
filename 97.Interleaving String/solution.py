#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-04
Last_modify:    2016-03-04
******************************************
'''

'''
Given s1, s2, s3,
find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        visted = {}
        return self.helper(visted, s1, s2, s3, 0, 0, 0)

    def helper(self, visted, s1, s2, s3, p1, p2, p3):
        hashcode = p1 * len(s3) + p2
        if hashcode in visted:
            return False
        if p1 >= len(s1):
            return s2[p2:] == s3[p3:]
        if p2 >= len(s2):
            return s1[p1:] == s3[p3:]
        res = (s1[p1] == s3[p3] and self.helper(visted, s1, s2, s3, p1 + 1, p2, p3 + 1)) or \
              (s2[p2] == s3[p3] and self.helper(visted, s1, s2, s3, p1, p2 + 1, p3 + 1))
        visted[hashcode] = 1
        return res
