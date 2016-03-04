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
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        visted = {}
        q = [(0, 0)]
        while q:
            x, y = q.pop(0)
            if x + y == l3:
                return True
            hash_down = (x + 1) * l3 + y
            hash_right = x * l3 + (y + 1)
            if x < l1 and s1[x] == s3[x+y] and hash_down not in visted:
                q.append((x + 1, y))
                visted[hash_down] = 1
            if y < l2 and s2[y] == s3[x+y] and hash_right not in visted:
                q.append((x, y + 1))
                visted[hash_right] = 1
        return False
