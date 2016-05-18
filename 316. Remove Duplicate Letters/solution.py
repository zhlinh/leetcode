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
Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order
among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        letters = [[] for i in range(26)]
        countChar = 0
        res = ""
        for i in range(n):
            index = ord(s[i]) - ord('a')
            if not letters[index]:
                countChar += 1
            letters[index].append(i)
        while countChar > 0:
            minLargest = 2 ** 31 - 1
            chosenPos = 0
            for li in letters:
                if li and li[-1] < minLargest:
                    minLargest = li[-1]
            for i in range(len(letters)):
                if letters[i] and letters[i][0] <= minLargest:
                    #  print(i)
                    res += chr(i + ord('a'))
                    chosenPos = letters[i][0]
                    letters[i] = []
                    break
            if countChar > 0:
                for li in letters:
                    while li and li[0] < chosenPos:
                        li.pop(0)
            countChar -= 1
        return res

