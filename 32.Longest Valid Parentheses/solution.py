#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
*****************************************
Author:         zhlinh
Email:          zhlinhng@gmail.com
Version:        0.0.1
Created Time:   2016-02-16
Last_modify:    2016-02-16
******************************************
'''

'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()",
which has length = 2.

Another example is ")()())",
where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for x in s:
            if x == '(':
                stack.append(1)
            elif stack[-1] & 1:
                a = stack.pop()
                stack[-1] += a + 1
            else:
                stack.append(0)
        r = max(stack)
        # if r is even then return r, else return r - 1
        return r - (r % 2)
