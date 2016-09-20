#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-28
Last_modify:    2016-02-28
******************************************
'''

'''
Given a string S and a string T,
find the minimum window in S which
will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T,
return the empty string "".

If there are multiple such windows,
you are guaranteed that there will
always be only one unique minimum window in S.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chmap = [0 for _ in range(256)]
        for ch in t:
            chmap[ord(ch)] += 1
        minLen, minStart, start, end = 2 ** 31 - 1, 0, 0, 0
        count = len(t)
        while end < len(s):
            if chmap[ord(s[end])] > 0:
                count -= 1
            chmap[ord(s[end])] -= 1
            end += 1
            while count == 0:
                if end - start < minLen:
                    minLen = end - start
                    minStart = start
                if chmap[ord(s[start])] == 0:
                    count += 1
                chmap[ord(s[start])] += 1
                start += 1
        if minLen == 2 ** 31 - 1:
            return ""
        return s[minStart:minStart + minLen]
