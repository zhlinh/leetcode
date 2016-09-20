#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-17
Last_modify:    2016-03-17
******************************************
'''

'''
Given a string s and a dictionary of words dict,
add spaces in s to construct a sentence where
each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        cache = {}
        return self.helper(s, wordDict, cache)

    def helper(self, s, wordDict, cache):
        if s in cache:
            return cache[s]
        res = []
        if len(s) == 0:
            res.append("")
            return res
        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                subList = self.helper(s[n:], wordDict, cache)
                for subStr in subList:
                    conn = " " if subStr else ""
                    res.append(word + conn + subStr)
        cache[s] = res
        return res
