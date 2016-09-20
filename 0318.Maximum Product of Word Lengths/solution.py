#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-18
Last_modify:    2016-05-18
******************************************
'''

'''
Given a string array words, find the maximum value of
length(word[i]) * length(word[j]) where the two words
do not share common letters. You may assume that each
word will contain only lower case letters.
If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len, reverse=True)
        masks = [0] * len(words)
        maxProduct = 0
        for i in range(len(words)):
            for c in words[i]:
                masks[i] |= 1 << (ord(c) - ord('a'))
        for i in range(len(words)):
            # pruning
            if len(words[i]) * len(words[i]) <= maxProduct:
                    break
            for j in range(i+1, len(words)):
                if masks[i] & masks[j] == 0:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
                    break
        return maxProduct

