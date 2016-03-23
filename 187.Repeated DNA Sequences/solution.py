#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-23
Last_modify:    2016-03-23
******************************************
'''

'''
All DNA is composed of a series of nucleotides abbreviated
as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA,
it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
Subscribe to see which companies asked this question
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        key = 0
        res = []
        for i in range(len(s)):
            key = ((key << 3) & 0x3FFFFFFF) | (ord(s[i]) & 7)
            if key in dic:
                if dic[key] == 1:
                    dic[key] += 1
                    res.append(s[i-9:i+1])
            else:
                dic[key] = 1
        return res
