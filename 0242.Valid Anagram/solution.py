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
Given two strings s and t,
write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters?
How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in t:
            if c not in dic or dic[c] == 0:
                return False
            else:
                dic[c] -= 1
        return True
