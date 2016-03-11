#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-03-11
Last_modify:    2016-03-11
******************************************
'''

'''
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem, we define empty
string as valid palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not self.isAlpha(s[i]) and not self.isNumeric(s[i]):
                i += 1
            while i < j and not self.isAlpha(s[j]) and not self.isNumeric(s[j]):
                j -= 1
            if i < j and not self.isSame(s[i], s[j]):
                return False
            i += 1
            j -= 1
        return True

    def isAlpha(self, c):
        if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
            return True
        return False

    def isNumeric(self, c):
        if c >= '0' and c <= '9':
            return True
        return False

    def isSame(self, c1, c2):
        diff = ord('a') - ord('A')
        ordC1, ordC2 = ord(c1), ord(c2)
        if ordC1 == ordC2:
            return True
        if self.isAlpha(c1) and self.isAlpha(c2) and \
                (ordC1 == ordC2 + diff or ordC1 == ordC2 - diff):
            return True
        return False
