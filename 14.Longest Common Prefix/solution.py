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
        rstr = ""
        index = 0
        if len(strs) == 0:
            return ""
        minLen = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < minLen:
                minLen = len(strs[i])
        while index < minLen:
            c = strs[0][index]
            for j in range(1, len(strs)):
                if strs[j][index] != c:
                    return rstr
            rstr += c
            index += 1
        return rstr
