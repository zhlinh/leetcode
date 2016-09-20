#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-05-23
Last_modify:    2016-05-23
******************************************
'''

'''
Given a list of unique words. Find all pairs of distinct indices (i, j)
in the given list, so that the concatenation of the two words,
i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

import collections

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        if n < 2:
            return []
        dic = collections.defaultdict(int)
        res = []
        for i in range(n):
            dic[words[i]] = i
        for i in range(n):
            # it must be (len(words[i]) + 1) for the case empty str ""
            # which len("") == 0
            for j in range(len(words[i]) + 1):
                left = words[i][:j]
                right = words[i][j:]
                if self.isPalindrome(left):
                    rev_right = right[::-1]
                    if rev_right in dic and dic[rev_right] != i:
                        res.append([dic[rev_right], i])
                # len(right) > 0 to avoid duplicates, for example ["ab", "ba"]
                # only left can be empty str ""
                # and then match the full reversed str
                if len(right) > 0 and self.isPalindrome(right):
                    rev_left = left[::-1]
                    if rev_left in dic and dic[rev_left] != i:
                        res.append([i, dic[rev_left]])
        return res

    def isPalindrome(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
