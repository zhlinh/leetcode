#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:  		zhlinh
Email: 			zhlinhng@gmail.com
Version: 		0.0.1
Created Time: 	2016-01-14
Last_modify: 	2016-01-14
******************************************
'''

'''
Write a function to find the longest common prefix string amongst an array of
strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        end = 0
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if strs[0] == "":
            return ""
        while True:
            for i in range(1, len(strs)):
                if strs[i] == "":
                    return ""
                if end >= len(strs[0]) or end >= len(strs[i]):
                    return strs[0][:end]
                if strs[i][end] != strs[0][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end + 1]
