#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-20
Last_modify:    2016-02-20
******************************************
'''

'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow
the lexicographic order.
All inputs will be in lower-case.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in sorted(strs):
            if s != "":
                key = ''.join(sorted(s))
                dic[key] = dic.get(key, []) + [s]
            else:
                dic["null"] = dic.get("null", []) + [""]
        return list(dic.values())
