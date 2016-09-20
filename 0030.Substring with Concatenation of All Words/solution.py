#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-01-29
Last_modify:    2016-01-29
******************************************
'''

'''
You are given a string, s, and a list of words, words,
that are all of the same length.
Find all starting indices of substring(s) in s
that is a concatenation of each word in words exactly once
and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        m, n, k = len(s), len(words), len(words[0])
        rList = []
        dic = {}
        for w in words:
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1
        for i in range(k):
            count = 0
            tmpdic = {}
            left = i
            for j in range(i, m - k + 1, k):
                word = s[j:j+k]
                if word in dic:
                    if word in tmpdic:
                        tmpdic[word] += 1
                    else:
                        tmpdic[word] = 1
                    count += 1
                    while tmpdic[word] > dic[word]:
                        tmpdic[s[left:left+k]] -= 1
                        left += k
                        count -= 1
                    if count == n:
                        rList.append(left)
                else:
                    tmpdic = {}
                    count = 0
                    left = j + k
        return rList

