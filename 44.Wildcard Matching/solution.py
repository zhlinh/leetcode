#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-19
Last_modify:    2016-02-19
******************************************
'''

'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn, pn = len(s), len(p)
        save_si, save_pi = 0, -1
        pi, si = 0, 0
        while si < sn:
            if si < sn and pi < pn and (s[si] == p[pi] or p[pi] == '?'):
                si, pi = si + 1, pi + 1
            elif pi < pn and p[pi] == '*':
                save_si, save_pi = si, pi + 1
                pi += 1
            elif save_pi != -1:
                pi = save_pi
                save_si += 1
                si = save_si
            else:
                return False
        while pi < pn and p[pi] == '*':
            pi += 1
        return pi == pn
