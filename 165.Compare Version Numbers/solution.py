#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-21
Last_modify:    2016-03-21
******************************************
'''

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty
and contain only digits and the . character.
The . character does not represent a decimal point and
is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way
to version three", it is the fifth second-level revision
of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n1, n2 = len(version1), len(version2)
        start1, start2 = 0, 0
        i1, i2 = 0, 0
        while i1 < n1 or i2 < n2:
            while i1 < n1 and version1[i1] != '.':
                i1 += 1
            while i2 < n2 and version2[i2] != '.':
                i2 += 1
            cmp1 = int(version1[start1:i1]) if i1 > start1 else 0
            cmp2 = int(version2[start2:i2]) if i2 > start2 else 0
            i1 += 1
            i2 += 1
            start1, start2 = i1, i2
            if cmp1 == cmp2:
                continue
            return 1 if cmp1 > cmp2 else -1
        return 0
